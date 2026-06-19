from dataclasses import dataclass


@dataclass(frozen=True)
class Vertex:
    """
    Representa um módulo da colônia.
    """

    id: int
    name: str