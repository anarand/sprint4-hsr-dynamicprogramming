"""
utils.py
────────
Funções auxiliares de exibição compartilhadas entre os módulos.
"""


def separador(titulo: str) -> None:
    """Imprime um separador visual com título."""
    largura = 64
    print(f"  {titulo}")


def exibir_caminho(caminho: list, custo: int | float) -> None:
    """
    Exibe o caminho ótimo e o custo total de forma resumida.

    Args:
        caminho (list)      : lista de nós na ordem correta
        custo   (int|float) : custo total do caminho
    """
    if not caminho:
        print("\n Nenhum caminho encontrado entre os nós informados.")
        return

    print(f"\n  Caminho : {' → '.join(caminho)}")
    print(f"  Custo   : {custo}h")