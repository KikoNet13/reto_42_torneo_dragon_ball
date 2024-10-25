import reflex as rx

from app.models.action import Action

MIN_DAMAGE_RATIO = 0.1


class Event(rx.Base):
    time: float
    left: Action
    right: Action
    damage: int
