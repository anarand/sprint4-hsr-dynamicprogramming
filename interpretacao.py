"""
interpretacao.py
────────────────
Tarefa 3 — Interpretar o resultado do Dijkstra (2,5 pts)
 
Descrição:
    Analisa o caminho ótimo encontrado pelo Dijkstra e responde:
        • Qual foi o menor caminho encontrado?
        • Qual o custo total?
        • Por que esse fluxo é mais eficiente?
        • Como os demais caminhos se comparam?
"""
 
from dijkstra import todos_os_caminhos
 
 
def interpretar_resultado(
    caminho_otimo: list,
    custo_otimo: int | float,
    grafo: dict,
    origem: str,
    destino: str,
) -> None:
    """
    Exibe a análise completa do caminho ótimo encontrado.
 
    Mostra:
        - O caminho ótimo passo a passo com os custos de cada aresta
        - Todos os caminhos possíveis ordenados por custo
        - Explicação de por que o caminho ótimo é mais eficiente
 
    Args:
        caminho_otimo (list)      : lista de nós do caminho ótimo
        custo_otimo   (int|float) : custo total do caminho ótimo
        grafo         (dict)      : grafo como lista de adjacência
        origem        (str)       : nó de partida
        destino       (str)       : nó de chegada
    """
 
    # ── 1. Caminho ótimo detalhado ─────────────────────────────
    print("\n  ✅ Menor caminho encontrado (Dijkstra):\n")
    _exibir_caminho_detalhado(caminho_otimo, grafo)
    print(f"\n  ⏱  Custo total: {custo_otimo}h")
 
    # ── 2. Comparativo com todos os caminhos ──────────────────
    print("\n  📊 Todos os caminhos possíveis (Lead → Confirmação):\n")
    todos = todos_os_caminhos(grafo, origem, destino)
 
    for i, (caminho, custo) in enumerate(todos, start=1):
        marcador = "  ★" if caminho == caminho_otimo else "   "
        etapas = " → ".join(caminho)
        print(f"{marcador} [{i}] {custo:>3}h  |  {etapas}")
 
    # ── 3. Explicação da eficiência ───────────────────────────
    print("\n  💡 Por que esse caminho é mais eficiente?\n")
    _explicar_eficiencia(caminho_otimo, custo_otimo, todos, grafo)
 
 
def _exibir_caminho_detalhado(caminho: list, grafo: dict) -> None:
    """
    Exibe o caminho ótimo passo a passo, mostrando o peso de cada aresta
    e o custo acumulado após cada transição.
 
    Args:
        caminho (list): nós do caminho na ordem correta
        grafo   (dict): grafo como lista de adjacência
    """
    custo_acumulado = 0
    largura = max(len(no) for no in caminho)
 
    for i in range(len(caminho) - 1):
        origem_etapa  = caminho[i]
        destino_etapa = caminho[i + 1]
        peso          = grafo[origem_etapa][destino_etapa]
        custo_acumulado += peso
 
        print(
            f"    {origem_etapa:<{largura}}  ──({peso:>2}h)──▶"
            f"  {destino_etapa:<{largura}}"
            f"   [acumulado: {custo_acumulado}h]"
        )
 
 
def _explicar_eficiencia(
    caminho_otimo: list,
    custo_otimo: int | float,
    todos_caminhos: list,
    grafo: dict,
) -> None:
    """
    Gera a explicação textual de por que o caminho ótimo é o mais eficiente,
    destacando as etapas que ele evita e o ganho em horas em relação
    às alternativas.
 
    Args:
        caminho_otimo  (list): nós do caminho ótimo
        custo_otimo    (int) : custo total do caminho ótimo
        todos_caminhos (list): lista de (caminho, custo) ordenada por custo
        grafo          (dict): grafo como lista de adjacência
    """
    # Etapas presentes no ótimo
    etapas_otimo = set(caminho_otimo)
 
    # Etapas que existem no grafo mas não aparecem no ótimo
    etapas_evitadas = []
    etapas_custosas = {
        "Reagendamento": "etapa de alta espera (9h só para agendar após tentativas)",
        "Orçamento → Confirmação": "aceitação direta do orçamento, mas sem negociação — leva 7h",
    }
 
    # Segundo pior caminho para calcular o ganho
    if len(todos_caminhos) > 1:
        segundo_caminho, segundo_custo = todos_caminhos[1]
        ganho = segundo_custo - custo_otimo
    else:
        segundo_custo = custo_otimo
        ganho = 0
 
    # Etapas evitadas
    for no in grafo:
        if no not in etapas_otimo and no != "Confirmação":
            etapas_evitadas.append(no)
 
    print(f"    O caminho ótimo percorre {len(caminho_otimo)} etapas em {custo_otimo}h.")
    print()
 
    print("    Etapas evitadas em relação aos caminhos mais longos:")
    for etapa in etapas_evitadas:
        descricao = etapas_custosas.get(etapa, "etapa não alcançada pelo fluxo ótimo")
        print(f"      • {etapa}: {descricao}")
 
    print()
    print("    Vantagens do fluxo ótimo:")
    print("      • Passa por 'Primeiro Contato' (1h) em vez de ir direto")
    print("        à Qualificação pelo formulário (5h) — economiza 4h logo na entrada.")
    print("      • Usa 'Negociação' (2h) para fechar o contrato, evitando")
    print("        a aceitação direta do orçamento (7h) — economiza mais 5h.")
    print("      • Nunca cai em 'Reagendamento', que acrescenta 16h ao processo.")
 
    if ganho > 0:
        print()
        print(f"    Comparado ao segundo melhor caminho ({segundo_custo}h),")
        print(f"    o caminho ótimo chega à Confirmação {ganho}h mais rápido.")
 
 
# ── Demonstração isolada ───────────────────────────────────────
if __name__ == "__main__":
    from dados import ARESTAS_CRM, ORIGEM, DESTINO
    from grafo import construir_grafo
    from dijkstra import dijkstra
    from utils import separador
 
    separador("TAREFA 3 — Interpretação do Resultado")
 
    grafo = construir_grafo(ARESTAS_CRM)
    caminho, custo = dijkstra(grafo, ORIGEM, DESTINO)
 
    interpretar_resultado(caminho, custo, grafo, ORIGEM, DESTINO)