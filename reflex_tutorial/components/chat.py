# chatapp.py
import reflex as rx

from . import style_chat as style
from .. import state as state_module


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="right"),
            style=style.question_style,
        ),
        rx.box(
            rx.text(answer, text_align="left"),
            style=style.answer_style,
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            state_module.State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=state_module.State.question,
            placeholder="Ask a question",
            on_change=state_module.State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=state_module.State.answer,
            style=style.button_style,
        ),
    )


def index_chat() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
    )
