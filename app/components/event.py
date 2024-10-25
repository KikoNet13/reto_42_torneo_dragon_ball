import reflex as rx

from app.models.event import Event

from app.components.action import action


def event(event: Event) -> rx.Component:
    return rx.hstack(
        action(event.left, is_left=True),
        rx.center(
            rx.text(event.time_str),
            width="10em",
        ),
        action(event.right, is_left=False),
        width="100%",
    )
