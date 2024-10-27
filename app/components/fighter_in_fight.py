import reflex as rx


def fighter_health(health: int, is_left: bool = True) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.hstack(
                rx.cond(
                    is_left,
                    rx.fragment(
                        rx.text(health),
                        rx.icon("heart"),
                    ),
                    rx.fragment(
                        rx.icon("heart"),
                        rx.text(health),
                    ),
                ),
            ),
            rx.progress(
                value=health,
                max=100,
                color_scheme="orange",
                width="6em",
            ),
            justify="center",
            align="center",
        ),
        width="100%",
        justify=rx.cond(is_left, "end", "start"),
        align="center",
    )
