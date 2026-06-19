from abc import ABC
from abc import abstractmethod

class ShortestPathAlgorithm(ABC):
    """
    Interface base para algoritmos de menor caminho em grafos.

    Define o contrato que qualquer algoritmo de caminho mínimo deve implementar.
    """

    @abstractmethod
    def execute(self, graph, source):
        """
        Executa o algoritmo de menor caminho a partir de um vértice de origem.

        Args:
            graph: Estrutura de grafo contendo vértices e arestas.
            source: Índice ou identificador do vértice de origem.

        Returns:
            Resultado do algoritmo, contendo distâncias e/ou predecessores
            conforme a implementação concreta.
        """
        pass