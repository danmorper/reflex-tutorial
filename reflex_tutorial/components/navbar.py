import reflex as rx
from .. import state as state_module

# Colors
bg_dark_color = "#222"
bg_light_color = "#fff"
accent_color = "#5535d4"
border_color = "#fff3"

def navbar():
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.icon(
                    tag="hamburger",
                    mr=4,
                    on_click=state_module.State.toggle_drawer,
                    cursor="pointer",
                ),
                rx.link(
                    rx.box(
                        rx.image(src="favicon.ico", width=30, height="auto"),
                        p="1",
                        border_radius="6",
                        bg="#F0F0F0",
                        mr="2",
                    ),
                    href="/",
                ),
                rx.breadcrumb(
                    rx.breadcrumb_item(
                        rx.heading("ReflexGPT", size="sm"),
                    ),
                    rx.breadcrumb_item(
                        rx.text(state_module.State.current_chat, size="sm", font_weight="normal"),
                    ),
                ),
            ),
            rx.hstack(
                rx.button(
                    "+ New chat",
                    bg=accent_color,
                    px="4",
                    py="2",
                    h="auto",
                    on_click=state_module.State.toggle_modal,
                ),
                rx.menu(
                    rx.menu_button(
                        rx.avatar(name="User", size="md"),
                        rx.box(),
                    ),
                    rx.menu_list(
                        rx.menu_item("Help"),
                        rx.menu_divider(),
                        rx.menu_item("Settings"),
                    ),
                ),
                spacing="8",
            ),
            justify="space-between",
        ),
        bg=bg_dark_color,
        backdrop_filter="auto",
        backdrop_blur="lg",
        p="4",
        border_bottom=f"1px solid {border_color}",
        position="sticky",
        top="0",
        z_index="100",
    )