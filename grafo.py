"""
grafo.py
────────
Descrição:
    Transforma o fluxo do CRM em um grafo DIRECIONADO e PONDERADO.

    Cada nó   → etapa do processo (Lead, Qualificação, Consulta...)
    Cada aresta → transição possível entre etapas (com direção)
    Peso      → tempo médio em horas para concluir a transição

Representação escolhida: Lista de Adjacência
    grafo[origem][destino] = peso

    Escolhida por ser eficiente para grafos esparsos — onde cada nó
    tem poucos vizinhos — que é exatamente o caso de um fluxo de CRM.

    Alternativa descartada: Matriz de Adjacência
        Ocupa O(V²) de espaço mesmo quando a maioria das células é zero.
        Ineficiente para o nosso grafo com poucos vértices e arestas.
"""


def construir_grafo(arestas: list) -> dict:
    grafo = {}

    for origem, destino, peso in arestas:
        # Garante que o nó de origem existe no grafo
        if origem not in grafo:
            grafo[origem] = {}

        # Adiciona a aresta direcionada com seu peso
        grafo[origem][destino] = peso

        # Garante que o nó de destino existe no grafo
        # (mesmo que não tenha arestas saindo dele)
        if destino not in grafo:
            grafo[destino] = {}

    return grafo


def exibir_grafo(grafo: dict) -> None:
    print("\n  Fluxo CRM — Grafo Direcionado e Ponderado")
    print("  (peso = tempo médio em horas por transição)\n")

    for no, vizinhos in grafo.items():
        if vizinhos:
            for destino, peso in vizinhos.items():
                print(f"  {no:<22} ──({peso:>2}h)──▶  {destino}")
        else:
            print(f"  {no:<22}  [nó terminal]")


def info_grafo(grafo: dict) -> dict:
    """
    Retorna métricas básicas do grafo.

    Args:
        grafo (dict): grafo representado como lista de adjacência

    Returns:
        dict com número de vértices, arestas e grau médio de saída
    """
    num_vertices = len(grafo)
    num_arestas  = sum(len(vizinhos) for vizinhos in grafo.values())
    grau_medio   = round(num_arestas / num_vertices, 2) if num_vertices else 0

    return {
        "vertices" : num_vertices,
        "arestas"  : num_arestas,
        "grau_medio_saida": grau_medio,
    }


# Demonstração isolada 
if __name__ == "__main__":
    from dados import ARESTAS_CRM
    from utils import separador

    separador("TAREFA 1 — Representação do Fluxo CRM como Grafo")

    grafo = construir_grafo(ARESTAS_CRM)
    exibir_grafo(grafo)

    info = info_grafo(grafo)
    print(f"\n  Vértices : {info['vertices']}")
    print(f"  Arestas  : {info['arestas']}")
    print(f"  Grau médio de saída: {info['grau_medio_saida']}")