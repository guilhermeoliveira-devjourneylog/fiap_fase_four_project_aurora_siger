from rich.console import Console
from rich.table import Table

from algorithms.energy_distribution import (
    EnergyDistribution
)

console = Console()


class EnergyDistributionPrinter:
    """
    Apresentação das análises
    de distribuição energética.
    """

    @staticmethod
    def print_report(
        graph
    ) -> None:

        table = Table(
            title="⚡ Distribuição Energética",
            show_header=True,
            header_style="bold cyan"
        )

        table.add_column(
            "Indicador",
            style="bold"
        )

        table.add_column(
            "Valor",
            justify="right"
        )

        table.add_row(
            "Geração",
            f"{EnergyDistribution.generation_capacity(graph):.2f}"
        )

        table.add_row(
            "Demanda",
            f"{EnergyDistribution.total_demand(graph):.2f}"
        )

        table.add_row(
            "Cobertura",
            f"{EnergyDistribution.coverage(graph):.2%}"
        )

        table.add_row(
            "Saldo",
            f"{EnergyDistribution.balance(graph):.2f}"
        )

        table.add_row(
            "Perdas",
            f"{EnergyDistribution.transmission_losses(graph):.2f}"
        )

        table.add_row(
            "Energia Entregue",
            f"{EnergyDistribution.delivered_energy(graph):.2f}"
        )

        table.add_row(
            "EDEI",
            f"{EnergyDistribution.edei(graph):.2%}"
        )

        table.add_row(
            "Classificação",
            EnergyDistribution.classification(graph)
        )

        console.print()
        console.print(table)