from abc import ABC, abstractmethod

class GraphRepository(ABC):
    """
    Interface abstrata para repositórios de grafos.

    Define o contrato mínimo que qualquer implementação de repositório de grafo
    deve seguir, garantindo a padronização de carregamento de dados estruturais
    de grafos utilizados no sistema.
    """

    @abstractmethod
    def load(self):
        """
        Carrega a estrutura do grafo a partir de uma fonte de dados.

        Este método deve ser implementado pelas classes concretas para definir
        como o grafo será carregado (ex: arquivo, banco de dados, API, etc.).

        Returns:
            Graph: uma instância do grafo carregado.
        """
        pass