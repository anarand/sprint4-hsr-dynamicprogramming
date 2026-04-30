from dados          import ARESTAS_CRM, ORIGEM, DESTINO
from grafo          import construir_grafo, exibir_grafo, info_grafo
from dijkstra       import dijkstra
from utils          import separador, exibir_caminho


def main():
    print("   CRM Hospital São Rafael — Grafos e Dijkstra · Sprint 4")

    # ── Constrói o grafo (usado pelas três tarefas) ────────────
    grafo = construir_grafo(ARESTAS_CRM)

    # TAREFA 1 — Representação do fluxo como grafo
    separador("TAREFA 1 — Fluxo CRM representado como Grafo")

    exibir_grafo(grafo)

    info = info_grafo(grafo)
    print(f"\n  Vértices           : {info['vertices']}")
    print(f"  Arestas            : {info['arestas']}")
    print(f"  Grau médio de saída: {info['grau_medio_saida']}")

    # TAREFA 2 — Dijkstra: menor caminho Lead → Confirmação
    separador("\n TAREFA 2 — Dijkstra: Menor Caminho Lead → Confirmação")

    caminho, custo = dijkstra(grafo, ORIGEM, DESTINO)

    print(f"\n  Origem  : {ORIGEM}")
    print(f"  Destino : {DESTINO}")
    exibir_caminho(caminho, custo)

if __name__ == "__main__":
    main()