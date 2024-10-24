import reflex as rx

from app.models.fight import Fight

from app.components.fighter import (
    fighter_left,
    fighter_right,
    fighter_tbd_card,
)
from app.components.fighter_in_fight import fighter_health


class FightComponent(rx.ComponentState):
    @classmethod
    def create(cls, fight: Fight = Fight(), **props):
        return super().create(fight=fight, **props)

    @classmethod
    def get_component(cls, **props) -> rx.Component:
        cls.fight = props.pop("fight", Fight())
        return rx.card(
            rx.hstack(
                rx.hstack(
                    rx.cond(
                        cls.fight.left,
                        fighter_left(cls.fight.left.fighter),
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
                        on_click=cls.simulate_fight,
                        disabled=cls.fight.simulated,
                    ),
                    padding_x="2em",
                ),
                rx.hstack(
                    rx.cond(
                        cls.fight.right,
                        fighter_right(cls.fight.right.fighter),
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

    async def simulate_fight(self):
        self.fight.simulated = True


fight = FightComponent.create
