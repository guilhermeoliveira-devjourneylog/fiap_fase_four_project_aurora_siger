from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

class MenuController:
    def __init__(self):
        self.console = Console()

    def show(self):
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
        return Prompt.ask(
            "[bold yellow]Escolha uma opção[/bold yellow]",
            default="0"
        )