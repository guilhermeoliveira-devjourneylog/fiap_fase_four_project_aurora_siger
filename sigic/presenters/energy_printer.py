from algorithms.energy_consumption import (
    EnergyConsumption
)


class EnergyPrinter:
    """
    Apresentação das análises energéticas.
    """

    @staticmethod
    def print_modules(
        graph
    ) -> None:

        print(
            "\nCONSUMO POR MÓDULO\n"
        )

        for (
            module,
            consumption
        ) in (
            EnergyConsumption
            .by_module(graph)
            .items()
        ):

            print(
                f"{module:<20}"
                f"{consumption:>8.2f}"
            )

    @staticmethod
    def print_total(
        graph
    ) -> None:

        print(
            "\nCONSUMO TOTAL\n"
        )

        print(
            EnergyConsumption
            .total(graph)
        )