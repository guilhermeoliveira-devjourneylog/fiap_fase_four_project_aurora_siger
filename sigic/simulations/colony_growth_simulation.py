from algorithms.energy_growth import EnergyGrowth


class ColonyGrowthSimulation:
    """
    Responsável pela simulação de crescimento da colônia.
    """

    def simulate(self, graph):
        """
        Aplica expansão energética na colônia.
        """

        EnergyGrowth.increase_load(
            graph,
            vertex_id=7,
            percentage=30
        )