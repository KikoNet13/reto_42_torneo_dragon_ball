import reflex as rx
from asyncio import sleep

from app.models.fight import Fight
from app.models.fighter_in_fight import FighterInFight
from app.models.fighter import Fighter
from app.models.event import Event, MIN_DAMAGE_RATIO
from app.models.action import Action, ActionType

from app.states.phase import PhaseState


class FightState(PhaseState):

    def _check_winner(self, fight: Fight) -> None:
        if fight.left.health <= 0:
            fight.winner = fight.right.fighter
        elif fight.right.health <= 0:
            fight.winner = fight.left.fighter

    def _generate_event(
        self,
        time: float,
        attack: Action,
        defender: FighterInFight,
        left_is_attacking: bool,
    ):
        defense = defender.next_defense()
        if defense.action_type == ActionType.DODGE.value:
            damage = 0
        else:
            damage = int(
                max(attack.value - defense.value, attack.value * MIN_DAMAGE_RATIO)
            )

        if left_is_attacking:
            left = attack
            right = defense
        else:
            left = defense
            right = attack

        defender.health = max(defender.health - damage, 0)

        return Event(time=time, left=left, right=right, damage=damage)

    @rx.background
    async def simulate_fight(self, index: int):
        next_phase = None
        if not self.is_last_phase:
            next_phase = self.tournament.phases[self.current_phase_pos + 1]

        fight = self.phase.fights[index]
        fight.simulated = True
        yield

        async def controlled_sleep(pace: float):
            time_elapsed = 0
            default_sleep = 0.1
            while time_elapsed < (self.delay * pace):
                await sleep(default_sleep)
                time_elapsed += default_sleep

        current_time = 0
        left_time = 0
        right_time = 0

        left_attack = fight.left.next_attack()
        left_time += left_attack.pace

        right_attack = fight.right.next_attack()
        right_time += right_attack.pace

        while not fight.winner:
            if left_time < right_time:
                current_time = left_time
                await controlled_sleep(left_attack.pace)
                async with self:
                    fight.events.append(
                        self._generate_event(
                            time=current_time,
                            attack=left_attack,
                            defender=fight.right,
                            left_is_attacking=True,
                        )
                    )
                yield

                left_attack = fight.left.next_attack()
                left_time += left_attack.pace
            else:
                current_time = right_time
                await controlled_sleep(right_attack.pace)
                async with self:
                    fight.events.append(
                        self._generate_event(
                            time=current_time,
                            attack=right_attack,
                            defender=fight.left,
                            left_is_attacking=False,
                        )
                    )
                yield

                right_attack = fight.right.next_attack()
                right_time += right_attack.pace

            print_event(fight.events[-1])

            self._check_winner(fight=fight)

        if next_phase:
            async with self:
                next_phase.fighters.append(fight.winner)
        else:
            self.winner = fight.winner


def print_event(event: Event):
    print(
        f"{event.time:->8.2f}: {event.left.action_type} {event.left.value} vs {event.right.action_type} {event.right.value} - {event.damage}"
    )
