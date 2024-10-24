import reflex as rx

from app.models.action import Action


class Event(rx.Base):
    time: float
    left: Action
    right: Action
