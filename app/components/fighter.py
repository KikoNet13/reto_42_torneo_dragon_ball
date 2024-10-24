import reflex as rx
from enum import Enum

from app.models.fighter import Fighter
from app.models.fighter_in_fight import FighterInFight


class Colors(Enum):
    ATTACK = "red"
    DEFENSE = "green"
    SPEED = "yellow"
    HEALTH = "orange"


def fighter_tbd_card() -> rx.Component:
    return rx.text.strong(
        "TBD",
        size="4",
        padding="2",
    )


def fighter_name(name: str) -> rx.Component:
    return (
        rx.cond(
            name.length() % 2 == 0,
            rx.text.strong(
                name,
                style={"line-height": "1"},
            ),
            rx.text(
                name,
                style={"line-height": "1"},
                color_scheme="gray",
            ),
        ),
    )


def fighter_attributes(speed: int, attack: int, defense: int) -> rx.Component:
    return rx.hstack(
        rx.tooltip(
            rx.badge(
                speed,
                color_scheme=Colors.SPEED.value,
            ),
            content="Velocidad",
        ),
        rx.tooltip(
            rx.badge(
                attack,
                color_scheme=Colors.ATTACK.value,
            ),
            content="Ataque",
        ),
        rx.tooltip(
            rx.badge(
                defense,
                color_scheme=Colors.DEFENSE.value,
            ),
            content="Defensa",
        ),
        spacing="1",
    )


def fighter_left(fighter: Fighter) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            fighter_name(fighter.name),
            fighter_attributes(fighter.speed, fighter.attack, fighter.defense),
            justify="between",
            align="end",
        ),
        rx.avatar(
            fallback=fighter.average.to_string(),
            size="4",
        ),
        align="center",
        justify="start",
    )


def fighter_right(fighter: Fighter) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            fallback=fighter.average.to_string(),
            size="4",
        ),
        rx.vstack(
            fighter_name(fighter.name),
            fighter_attributes(fighter.speed, fighter.attack, fighter.defense),
            justify="between",
            align="start",
        ),
        align="center",
        justify="start",
    )


def fighter_card(fighter: Fighter) -> rx.Component:
    return rx.card(
        fighter_left(fighter),
    )
