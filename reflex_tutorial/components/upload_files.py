import reflex as rx
from ..state import State
import pandas as pd
from io import StringIO
color = "rgb(107,99,246)"

def data_table():
    return rx.data_table(
        data=State.df,
        search=True,
        pagination=True
    )

    


def upload():
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.button(
                    "Select File",
                    color=color,
                    bg="white",
                    border=f"1px solid {color}",
                    accept={"csv": [".csv"],}
                ),
                rx.text(
                    "Drag and drop files here or click to select files"
                ),
                
            border=f"1px dotted {color}",
            padding="5em",
            )
        ),
        rx.button(
            "Upload",
            on_click=lambda: State.handle_upload(
                rx.upload_files()
            )
        ),
        # rx.text(State.upload_csv[0]),
        data_table()
        )