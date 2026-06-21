from algorithms.energy_distribution import (
    EnergyDistribution
)


class EnergyDistributionPrinter:
    """
    Apresentação das análises
    de distribuição energética.
    """

    @staticmethod
    def print_report(
        graph
    ) -> None:

        print(
            "\nDISTRIBUIÇÃO ENERGÉTICA\n"
        )

        print(
            f"Geração........: "
            f"{EnergyDistribution.generation_capacity(graph):.2f}"
        )

        print(
            f"Demanda........: "
            f"{EnergyDistribution.total_demand(graph):.2f}"
        )

        print(
            f"Cobertura......: "
            f"{EnergyDistribution.coverage(graph):.2%}"
        )

        print(
            f"Saldo..........: "
            f"{EnergyDistribution.balance(graph):.2f}"
        )

        print(
            f"Perdas.........: "
            f"{EnergyDistribution.transmission_losses(graph):.2f}"
        )

        print(
            f"Energia Entregue: "
            f"{EnergyDistribution.delivered_energy(graph):.2f}"
        )

        print(
            f"EDEI...........: "
            f"{EnergyDistribution.edei(graph):.2%}"
        )

        print(
            f"Classificação..: "
            f"{EnergyDistribution.classification(graph)}"
        )