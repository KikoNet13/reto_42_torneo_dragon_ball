import reflex as rx

from app.models.action import Action

MIN_DAMAGE_RATIO = 0.1


class Event(rx.Base):
    time: float
    left: Action
    right: Action
    damage: int

    @property
    def time_str(self) -> str:
        return f"{self.time:6.2f}"
