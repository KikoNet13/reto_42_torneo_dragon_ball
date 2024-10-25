import reflex as rx

from app.models.action import Action, ActionType


def action(action: Action, is_left: bool = True) -> rx.Component:
    return rx.hstack(
        rx.match(
            action.action_type,
            (ActionType.DODGE.value, rx.text("Dodge")),
            (ActionType.ATTACK.value, rx.text("Attack")),
            (ActionType.DEFENSE.value, rx.text("Defense")),
        ),
        spacing="2",
        width="100%",
        justify=rx.cond(is_left, "end", "start"),
        id="action",
    )
