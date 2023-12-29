import reflex as rx
from typing import List
# import reflex_tutorial.components.sidebar as sidebar
from . import styles
from .components import chat, modal, navbar, sidebar
from .state import State

# # Sidebar
# class DrawerState(rx.State):
#     show_right: bool = False
#     show_top: bool = False

#     def top(self):
#         self.show_top = not (self.show_top)

#     def right(self):
#         self.show_right = not (self.show_right)

# def sidebar():
#     return rx.box(
#     rx.button(
#         "Show Right Drawer", on_click=DrawerState.right
#     ),
#     rx.drawer(
#         rx.drawer_overlay(
#             rx.drawer_content(
#                 rx.drawer_header("Confirm"),
#                 rx.drawer_body(
                    
#                 ),
#                 rx.drawer_footer(
#                     rx.button(
#                         "Close", on_click=DrawerState.right
#                     )
#                 ),
#             )
#         ),
#         placement="left",
#         is_open=DrawerState.show_right,
#         color_scheme=styles.BackgroundColor.SIDEBAR
#     )
# )

def other():
    return rx.box(
        sidebar.sidebar(),
        rx.text("Hello World"),
    )
def index() -> rx.Component:
    """The main app."""
    return rx.box(
        sidebar.sidebar(),
        chat.index_chat()
    )
app = rx.App()
app.add_page(index)
app.add_page(other)
app.compile()

