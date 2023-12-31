import reflex as rx
def navbar():
    return rx.box(
        rx.text("🏊", style={"font-size": "2rem", "margin-right": "15px"}),
        rx.link("Home", href="http://localhost:3000", style={"padding": "10px", "color": "white", "text-decoration": "none"}),
        rx.link("Other", href="http://localhost:3000/other", style={"padding": "10px", "color": "white", "text-decoration": "none"}),
        position="fixed",
        width="100%",
        top="0px",
        z_index="5",
        style={"background": "#333", "padding": "10px 20px", "box-shadow": "0 2px 4px rgba(0,0,0,.1)", "display": "flex", "align-items": "center", "justify-content": "start"},
    )