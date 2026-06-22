from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt


class MenuController:
    """
    Controlador responsável pela exibição e interação com o menu principal do sistema.

    Essa classe utiliza a biblioteca Rich para renderizar o menu no terminal
    e capturar a opção escolhida pelo usuário.
    """

    def __init__(self):
        """
        Inicializa o controlador do menu.

        Cria uma instância do Console do Rich, utilizada para exibição
        formatada no terminal.
        """
        self.console = Console()

    def show(self):
        """
        Exibe o menu principal do sistema no terminal.

        O menu apresenta as opções disponíveis para interação com o sistema,
        como visualização de topologia, análise de energia e execução de algoritmos.
        """
        self.console.print(
            Panel.fit(
                (
                    "[bold cyan]SISTEMA DA COLÔNIA[/bold cyan]\n\n"
                    "[1] Exibir topologia\n"
                    "[2] Energia inicial\n"
                    "[3] Simular crescimento\n"
                    "[4] Energia após crescimento\n"
                    "[5] Rotas mínimas (Dijkstra)\n"
                    "[0] Sair"
                ),
                title="Menu Principal",
                border_style="blue"
            )
        )

    def get_option(self):
        """
        Captura a opção escolhida pelo usuário no menu.

        Returns:
            str: Opção selecionada pelo usuário (como string),
                 com valor padrão "0" caso nenhuma entrada seja fornecida.
        """
        return Prompt.ask(
            "[bold yellow]Escolha uma opção[/bold yellow]",
            default="0"
        )