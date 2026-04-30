"""
dijkstra.py
───────────
Tarefa 2 — Implementar o algoritmo de Dijkstra (2,5 pts)

Descrição:
    Encontra o MENOR CAMINHO (menor custo total) entre dois nós
    de um grafo direcionado e ponderado.

    Aplicado ao CRM: encontra o fluxo mais rápido (em horas)
    para converter um Lead em Confirmação.

Como funciona o algoritmo de Dijkstra:
    1. Define distância 0 para o nó de origem e ∞ para todos os demais.
    2. Insere o nó de origem em uma fila de prioridade (min-heap).
    3. A cada iteração, extrai o nó de menor custo acumulado.
    4. Para cada vizinho desse nó, calcula o custo passando por ele.
       Se for menor que o custo conhecido, atualiza e adiciona ao heap.
    5. Repete até processar o nó de destino ou esvaziar a fila.
    6. Reconstrói o caminho usando o dicionário de predecessores.

Estrutura de dados utilizada:
    heapq (min-heap nativo do Python) — garante que o nó de menor
    custo acumulado seja sempre processado primeiro. Complexidade
    de extração: O(log V).

Complexidade com heap:
    Tempo : O((V + E) · log V) — V vértices, E arestas
    Espaço: O(V) — distâncias, predecessores e heap
"""

import heapq


def dijkstra(grafo: dict, inicio: str, fim: str) -> tuple:
    """
    Executa o algoritmo de Dijkstra e retorna o menor caminho.

    Args:
        grafo  (dict): grafo como lista de adjacência {no: {vizinho: peso}}
        inicio (str) : nó de partida
        fim    (str) : nó de chegada

    Returns:
        tuple(list[str], int | float):
            [0] Caminho ótimo como lista de nós (vazio se não existe caminho)
            [1] Custo total do caminho (float('inf') se não existe caminho)
    """

    # ── Passo 1: inicialização ─────────────────────────────────
    # Todos os nós começam com distância infinita, exceto a origem
    distancias   = {no: float("inf") for no in grafo}
    distancias[inicio] = 0

    # Predecessores: permite reconstruir o caminho ao final
    predecessores = {no: None for no in grafo}

    # Min-heap: (custo_acumulado, nó_atual)
    # Python compara tuplas elemento a elemento → menor custo sai primeiro
    heap = [(0, inicio)]

    # Conjunto de nós já processados (visitados)
    visitados = set()

    # ── Passo 2: exploração ────────────────────────────────────
    while heap:
        custo_atual, no_atual = heapq.heappop(heap)

        # Ignora se já foi processado com custo menor
        if no_atual in visitados:
            continue
        visitados.add(no_atual)

        # Chegou ao destino → não precisa continuar
        if no_atual == fim:
            break

        # ── Passo 3: relaxamento das arestas ──────────────────
        for vizinho, peso in grafo[no_atual].items():
            if vizinho in visitados:
                continue

            novo_custo = custo_atual + peso

            # Atualiza se encontrou caminho mais curto para este vizinho
            if novo_custo < distancias[vizinho]:
                distancias[vizinho]    = novo_custo
                predecessores[vizinho] = no_atual
                heapq.heappush(heap, (novo_custo, vizinho))

    # ── Passo 4: reconstrução do caminho ──────────────────────
    caminho = _reconstruir_caminho(predecessores, inicio, fim)

    custo_total = distancias[fim]
    return caminho, custo_total


def _reconstruir_caminho(
    predecessores: dict,
    inicio: str,
    fim: str,
) -> list:
    """
    Reconstrói o caminho ótimo percorrendo os predecessores de trás para frente.

    Parte do nó de destino e segue os predecessores até chegar à origem.
    Em seguida, inverte a lista para obter a ordem correta.

    Args:
        predecessores (dict): mapeamento nó → nó que veio antes dele
        inicio        (str) : nó de partida
        fim           (str) : nó de chegada

    Returns:
        list[str]: caminho na ordem correta, ou [] se não existe caminho
    """
    caminho = []
    no_atual = fim

    while no_atual is not None:
        caminho.append(no_atual)
        no_atual = predecessores[no_atual]

    caminho.reverse()

    # Verifica se o caminho começa na origem (senão, não existe caminho)
    if not caminho or caminho[0] != inicio:
        return []

    return caminho


def todos_os_caminhos(grafo: dict, origem: str, destino: str) -> list:
    """
    Encontra TODOS os caminhos simples entre origem e destino via DFS.
    Usado para comparar os caminhos e evidenciar por que o Dijkstra
    escolheu o que escolheu.

    Args:
        grafo   (dict): grafo como lista de adjacência
        origem  (str) : nó de partida
        destino (str) : nó de chegada

    Returns:
        list[tuple(list[str], int)]: lista de (caminho, custo_total)
        ordenada do menor para o maior custo
    """
    resultado = []

    def dfs(no_atual, caminho_atual, custo_atual, visitados):
        if no_atual == destino:
            resultado.append((list(caminho_atual), custo_atual))
            return

        for vizinho, peso in grafo.get(no_atual, {}).items():
            if vizinho not in visitados:
                visitados.add(vizinho)
                caminho_atual.append(vizinho)
                dfs(vizinho, caminho_atual, custo_atual + peso, visitados)
                caminho_atual.pop()
                visitados.remove(vizinho)

    dfs(origem, [origem], 0, {origem})
    resultado.sort(key=lambda x: x[1])
    return resultado


# Demonstração isolada 
if __name__ == "__main__":
    from dados import ARESTAS_CRM, ORIGEM, DESTINO
    from grafo import construir_grafo
    from utils import separador, exibir_caminho

    separador("TAREFA 2 — Algoritmo de Dijkstra")

    grafo   = construir_grafo(ARESTAS_CRM)
    caminho, custo = dijkstra(grafo, ORIGEM, DESTINO)

    print(f"\n  Origem  : {ORIGEM}")
    print(f"  Destino : {DESTINO}")
    exibir_caminho(caminho, custo)