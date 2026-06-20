from dataclasses import dataclass


@dataclass
class Vertex:
    """
    Representa um módulo da colônia.

    Attributes:
        id (int): Identificador único do módulo.
        name (str): Nome do módulo.
        base_consumption (float): Consumo energético nominal.
        current_load (float): Fator de carga aplicado ao módulo.
    """

    id: int
    name: str
    base_consumption: float
    current_load: float = 1.0

    @property
    def consumption(self) -> float:
        """
        Retorna o consumo atual do módulo.

        Returns:
            float: Consumo energético atual.
        """
        return self.base_consumption * self.current_load