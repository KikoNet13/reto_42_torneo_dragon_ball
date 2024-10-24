import reflex as rx

from app.views.form import form
from app.views.tournament import tournament

from app.state import State, View
from app.states.tournament import TournamentState


class IndexState(rx.State):
    async def reset_all(self) -> None:
        substates = self.get_parent_state().get_substates()
        for substate in substates:
            state = await self.get_state(substate)
            state.reset()
        state = await self.get_state(State)
        state.on_mount()

    async def on_load(self) -> None:
        # substates = self.get_parent_state().get_substates()
        # for substate in substates:
        #     print(substate)
        #     state = await self.get_state(substate)
        #     state.reset()

        print("IndexState.on_load")


@rx.page(route="/", on_load=IndexState.on_load)
def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.icon_button("refresh-ccw", on_click=IndexState.reset_all),
            rx.vstack(
                rx.link(
                    rx.code(
                        "Retos de programación by mouredev",
                        size="4",
                        variant="outline",
                    ),
                    href="https://retosdeprogramacion.com/",
                    is_external=True,
                ),
                rx.heading(
                    rx.code("42", size="8"),
                    " Torneo Dragon Ball",
                    size="8",
                ),
                align="center",
                justify="center",
                margin_y="2em",
            ),
            rx.match(
                State.current_view,
                (
                    View.LOADING,
                    rx.skeleton(
                        rx.box(
                            width="100%",
                            height="100%",
                            align="center",
                            justify="center",
                        ),
                        loading=True,
                    ),
                ),
                (
                    View.FORM,
                    form(),
                ),
                (
                    View.TOURNAMENT,
                    rx.skeleton(
                        tournament(),
                        loading=~TournamentState.tournament,
                    ),
                ),
            ),
            width="100%",
            height="100%",
            align="center",
        ),
        width="100%",
        min_height="100vh",
        align="center",
        justify="center",
        # on_mount=State.on_mount,
    )


app = rx.App(
    title="Torneo Dragon Ball",
)
app.add_page(index)
