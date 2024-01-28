import reflex as rx
from typing import List
# import reflex_tutorial.components.sidebar as sidebar
from . import styles
from .components import chat, modal, navbar, sidebar
from .state import State
#from .components import upload_files

def index() -> rx.Component:
    """The main app."""
    return rx.box(
        navbar.navbar(),
        rx.flex(
            chat.index_chat(),
            direction="column",
            justify_content="center",
            align_items="center",
            height="100vh",  # This sets the height to the full viewport height
            width="100%",
        )
    )
app = rx.App()
app.add_page(index)
# app.add_page(other)
app.compile()

