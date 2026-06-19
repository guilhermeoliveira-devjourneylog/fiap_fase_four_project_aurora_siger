from dataclasses import dataclass


@dataclass(frozen=True)
class Edge:
    """
    Representa uma conexão entre módulos.
    """

    source: int
    target: int
    distance: int