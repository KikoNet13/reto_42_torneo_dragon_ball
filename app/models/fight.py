import reflex as rx

from app.models.fighter_in_fight import FighterInFight
from app.models.fighter import Fighter
from app.models.action import Action
from app.models.event import Event


class Fight(rx.Base):
    left: FighterInFight | None = None
    right: FighterInFight | None = None
    winner: Fighter | None = None
    events: list[Event] = []
    simulated: bool = False
    showed: bool = False

    # def do_next_turn(self):
    #     left_action = self.left.next_action()
    #     right_action = self.right.next_action()

    #     if left_action.time < right_action.time:
    #         self._do_next_action(self.left, self.right, left_action)
    #     else:
    #         self._do_next_action(self.right, self.left, right_action)

    # def _do_next_action(
    #     self,
    #     attacker: FighterInFight,
    #     defender: FighterInFight,
    #     action: Action,
    # ):
    #     action.do()
    #     defender.health -= action.damage
    #     if defender.health <= 0:
    #         self.winner = attacker.fighter
