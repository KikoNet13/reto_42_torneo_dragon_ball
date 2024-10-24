import reflex as rx


class Fighter(rx.Base):
    name: str = ""
    speed: int = 0
    attack: int = 0
    defense: int = 0
    eliminated: bool = False

    @property
    def average(self) -> int:
        return (self.speed + self.attack + self.defense) // 3

    def dict(self, **kwargs) -> dict:
        return super().dict() | {"average": self.average}

    def set_column(self, column: int, value: str | int) -> None:
        if column == 0:
            self.name = value
        elif column == 1:
            self.speed = value
        elif column == 2:
            self.attack = value
        elif column == 3:
            self.defense = value
        else:
            raise ValueError("Invalid column index")
