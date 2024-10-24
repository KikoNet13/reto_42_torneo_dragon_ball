import reflex as rx


from app.components.fighter import fighter_card
from app.components.fight import fight

from app.states.phase import PhaseState


def phase() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.foreach(
                PhaseState.phase.fighters,
                fighter_card,
            ),
            justify="center",
            wrap="wrap",
            spacing="2",
        ),
        rx.cond(
            PhaseState.phase.fighters,
            rx.divider(),
        ),
        rx.foreach(PhaseState.phase.fights, lambda f: fight(fight=f)),
        width="inherit",
        align="center",
        spacing="4",
    )
