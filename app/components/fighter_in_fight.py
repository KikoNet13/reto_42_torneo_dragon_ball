import reflex as rx


def fighter_health(health: int) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon("heart"),
            rx.text(health),
        ),
        rx.progress(value=health, max=100),
    )
