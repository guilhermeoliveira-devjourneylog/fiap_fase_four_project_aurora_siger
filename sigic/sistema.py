from core.system_controller import SystemController


def main():
    """
    Ponto de entrada principal da aplicação.

    Responsável por inicializar e executar o SystemController,
    que coordena o fluxo geral do sistema (simulação, execução
    de algoritmos e interação com o usuário).

    Returns:
        None
    """
    SystemController().run()


if __name__ == "__main__":
    main()