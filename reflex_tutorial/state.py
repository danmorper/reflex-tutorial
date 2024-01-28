# state.py
from typing import List
import reflex as rx
import os
import openai
import csv
from load_dotenv import load_dotenv
from io import StringIO
import pandas as pd
load_dotenv()

def string_to_dataframe(string):
    return pd.read_csv(StringIO(string))


client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def get_csv_content(csv_content):
    """Convert the list of lists content into a CSV."""
    final_csv_content = ""
    for row in csv_content:
        final_csv_content += ",".join(row) + "\n"
    return [final_csv_content]
    
class State(rx.State):

    """Controlar mensajes chatgpt analisis de datos"""
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self):
        # Our chatbot has some brains now!
        session = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": self.question}
            ],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        # Add to the answer as the chatbot responds.
        answer = ""
        self.chat_history.append((self.question, answer))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (
                    self.chat_history[-1][0],
                    answer,
                )
                yield

    """Subir archivos"""

    # The cvs
    csv_content: list[str]
    upload_csv: list[str]
    df: pd.DataFrame
    async def handle_upload(self, files : list[rx.UploadFile]):
        """Handle the upload of file(s).

            Args:
                files: The uploaded files.
            """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_asset_path(file.filename)

            # Save the file.
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            # Read the CSV content into memory
            csv_content = []
            with open(outfile, "r", encoding='utf-8') as file_object:
                csv_reader = csv.reader(file_object)
                for row in csv_reader:
                    csv_content.append(row)
            
            # Update the state.
            self.upload_list = csv_content
            self.upload_csv = get_csv_content(csv_content)
            self.df = string_to_dataframe(get_csv_content(csv_content)[0])

    """De pdf a csv"""
    main_prompt = """You will convert text data into a structured CSV format. The text data comes from a swimming competition result sheet and includes columns like 'primer apellido' (first surname), 'segundo apellido' (second surname), 'nombre' (name), 'año' (year), 'género' (gender), 'equipo' (team), 'puntos' (points), 'tiempo' (time), 'estilo' (style), 'distancia' (distance), 'tiempo 50m', and so on. The data is separated by commas.

    Here's an example of the text data:
    'Splash Meet Manager, ... Prueba 13 Masc., 200m Libre Absoluto Masculino 25/02/2023 - 11:15 Resultados Clasificación AN Tiempo Puntos 50m 100m 150m 200m 1.GUTIERREZ RAMOS, R. 04 C.D.N. Ciudad De Algeciras 2:01.35 19,00 27.26 30.06 31.70 32.33 2.GALLARDO MARTIN, J. 04 C.D.N. Inacua Malaga 2:04.57 16,00 28.69 30.89 32.15 32.84...'

    You need to extract and reformat this data into a CSV format like this:
    'primer apellido, segundo apellido, nombre, año, género, equipo, puntos, tiempo, estilo, distancia, tiempo 50m, tiempo 100m, tiempo 150m, tiempo 200m, tiempo 250m, tiempo 300m, tiempo 350m, tiempo 400m, tiempo 800m, tiempo 1500m, fecha, hora, lugar
    GUTIERREZ, RAMOS, R., 04, Masc, C.D.N. Ciudad De Algeciras, 19, 2:01.35, Libre, 200m, 27.26, 30.06, 31.70, 32.33, None, None, None, None, None, None, 25/02/2023, 11:15, Algeciras
    GALLARDO, MARTIN, J., 04, Masc, C.D.N. Inacua Malaga, 16, 2:04.57, Libre, 200m, 28.69, 30.89, 32.15, 32.84, None, None, None, None, None, None, 25/02/2023, 11:15, Algeciras'

    Note: If a swimmer is disqualified, indicated by 'WDR', then the time should be 'None' and the points should be '0'.

    When extracting data, ensure each row has the same number of fields. If the last row or any other row has missing information, fill in those fields with 'None'. Pay special attention to the last row to maintain consistency with the rest of the data.


    """

        # The current question being asked.
    question_pdf_csv: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history_pdf_csv: list[tuple[str, str]]

    def answer_pdf_csv(self):
        try:
            session_pdf_csv = client.chat_completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": self.question_pdf_csv},
                    {"role": "system", "content": self.main_prompt}
                ],
                stop=None,
                temperature=0.7,
                stream=True,
            )

            answer_pdf_csv = ""
            for item in session_pdf_csv:
                # Check if 'content' exists and is not None before concatenating
                if hasattr(item.choices[0].delta, "content") and item.choices[0].delta.content:
                    if item.choices[0].delta.content == None:
                        answer_pdf_csv += ""
                    else:
                        answer_pdf_csv += item.choices[0].delta.content

            # Update the chat history with the new answer
            self.chat_history_pdf_csv.append((self.question_pdf_csv, answer_pdf_csv))

            # Clear the question input after processing
            self.question_pdf_csv = ""

        except Exception as e:
            # If an error occurs, log it or handle it as needed
            print(f"An error occurred: {e}")

        # Finally, return the updated chat history
        return self.chat_history_pdf_csv

