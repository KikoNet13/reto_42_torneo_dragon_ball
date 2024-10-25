import reflex as rx

from app.models.fight import Fight

from app.components.fighter import (
    fighter_left,
    fighter_right,
    fighter_tbd_card,
)
from app.components.fighter_in_fight import fighter_health

from app.states.fight import FightState


def fight_component(fight: Fight, index: int) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.hstack(
                rx.cond(
                    fight.left,
                    fighter_left(
                        fight.left.fighter,
                        # Se compara el contenido porque no hay id
                        fight.left.fighter.to_string() == fight.winner.to_string(),
                    ),
                    fighter_tbd_card(),
                ),
                width="100%",
                justify="end",
            ),
            rx.box(
                rx.button(
                    rx.icon("swords"),
                    variant="ghost",
                    size="2",
                    on_click=FightState.simulate_fight(index),
                    disabled=fight.simulated | ~fight.left | ~fight.right,
                ),
                padding_x="2em",
            ),
            rx.hstack(
                rx.cond(
                    fight.right,
                    fighter_right(
                        fight.right.fighter,
                        # Se compara el contenido porque no hay id
                        fight.right.fighter.to_string() == fight.winner.to_string(),
                    ),
                    fighter_tbd_card(),
                ),
                width="100%",
                justify="start",
            ),
            width="100%",
            justify="center",
            align="center",
            spacing="2",
        ),
        width="100%",
    )
