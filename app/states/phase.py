import reflex as rx
from asyncio import sleep
from random import choice

from app.models.phase import Phase
from app.models.fighter_in_fight import FighterInFight

from app.states.tournament import TournamentState


class PhaseState(TournamentState):
    speed: int = 50
    delay: float = 1

    @rx.var
    def phase(self) -> Phase | None:
        if self.tournament and self.current_phase_pos is not None:
            return self.tournament.phases[self.current_phase_pos].__copy__()
        return None

    @rx.var
    def is_drawable(self) -> bool:
        if self.phase:
            return (
                len(self.phase.fighters) == self.phase.num_fighters
                and not self.phase.drawn
            )
        return False

    def set_delay(self, value: list[int]):
        self.speed = value[0]
        self.delay = 4 + (self.speed - 1) * -0.04

    def _new_fighter_in_fight(self) -> FighterInFight:
        fighter = choice(self.phase.fighters)
        self.phase.fighters.remove(fighter)
        return FighterInFight(fighter=fighter)

    @rx.background
    async def draw(self):
        if not self.is_drawable:
            yield rx.window_alert("No se pueden sortear los luchadores")
            return
        self.phase.drawn = True
        yield

        async def controlled_sleep():
            time_elapsed = 0
            default_sleep = 0.1
            while time_elapsed < self.delay:
                await sleep(default_sleep)
                time_elapsed += default_sleep

        for fight in self.phase.fights:
            await controlled_sleep()
            fight.left = self._new_fighter_in_fight()
            yield

            await controlled_sleep()
            fight.right = self._new_fighter_in_fight()
            yield
