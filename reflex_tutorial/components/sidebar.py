import reflex as rx

class DrawerState(rx.State):
    show_right: bool = False
    show_top: bool = False

    def top(self):
        self.show_top = not (self.show_top)

    def right(self):
        self.show_right = not (self.show_right)

def sidebar():
    return rx.box(
        rx.button(
            rx.icon(tag="hamburger"), on_click=DrawerState.right
        ),
        rx.drawer(
            rx.drawer_overlay(
                rx.drawer_content(
                    rx.drawer_header("Selecciona la opcion deseada"),
                    rx.link(
                        "other",
                        href="http://localhost:3000/other",
                        target="_blank"
                    ),
                    rx.link(
                        "Main",
                        href="http://localhost:3000",
                        target="_blank"
                    ),
                ),
                rx.drawer_footer(
                    rx.button(
                        "Close", on_click=DrawerState.right
                    )
                ),
                bg="rgba(0, 0, 0, 0.3)",
            ),
            is_open=DrawerState.show_right,
            placement="left"
        ),
    )
