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

    # def dict(self, **kwargs) -> dict:
    #     # Obtén el diccionario estándar con super()
    #     result = super().dict(**kwargs)

    #     # Itera sobre los atributos de la clase
    #     for attr_name in dir(self):
    #         # Verifica si es una propiedad
    #         if isinstance(getattr(self.__class__, attr_name, None), property):
    #             # Añade la propiedad al diccionario
    #             result[attr_name] = getattr(self, attr_name)

    #     return result

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
