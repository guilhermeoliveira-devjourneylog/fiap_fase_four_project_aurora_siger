from rich.console import Console
from rich.table import Table

from algorithms.energy_consumption import (
    EnergyConsumption
)


class EnergyPrinter:
    """
    Apresentação rica das análises energéticas.
    """

    console = Console()

    @classmethod
    def print_modules(
        cls,
        graph
    ) -> None:
        """
        Exibe o consumo de energia por módulo.
        """

        table = Table(
            title="Consumo por Módulo"
        )

        table.add_column(
            "Módulo",
            style="cyan"
        )

        table.add_column(
            "Consumo",
            justify="right",
            style="green"
        )

        for (
            module,
            consumption
        ) in (
            EnergyConsumption
            .by_module(graph)
            .items()
        ):
            table.add_row(
                module,
                f"{consumption:.2f}"
            )

        cls.console.print(table)

    @classmethod
    def print_total(
        cls,
        graph
    ) -> None:
        """
        Exibe o consumo total da colônia.
        """

        table = Table(
            title="Consumo Total"
        )

        table.add_column(
            "Métrica",
            style="cyan"
        )

        table.add_column(
            "Valor",
            justify="right",
            style="green"
        )

        table.add_row(
            "Consumo Total",
            f"{EnergyConsumption.total(graph):.2f}"
        )

        cls.console.print(table)