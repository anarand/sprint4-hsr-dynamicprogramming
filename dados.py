
# Nós: 
NOS_CRM = [
    "Lead",
    "Primeiro Contato",
    "Qualificação",
    "Reagendamento",
    "Agendamento",
    "Consulta",
    "Orçamento",
    "Negociação",
    "Confirmação",
]

# ── Arestas direcionadas: (origem, destino, peso_em_horas) ────
#
# O peso representa o tempo médio que a equipe leva para
# avançar de uma etapa para a próxima. Quanto menor, mais
# ágil é aquela transição no processo comercial.
#
ARESTAS_CRM = [
    # Entrada do lead no sistema
    ("Lead",             "Primeiro Contato",  1),
    # Lead chega pré-qualificado via formulário detalhado
    ("Lead",             "Qualificação",      5),

    # Contato bem-sucedido → qualificação do interesse
    ("Primeiro Contato", "Qualificação",      2),
    # Não foi possível contato → entra em fila de reagendamento
    ("Primeiro Contato", "Reagendamento",     7),

    # Após tentativas de contato, finalmente agenda
    ("Reagendamento",    "Agendamento",       9),

    # Lead qualificado → consulta agendada
    ("Qualificação",     "Agendamento",       3),

    # Aguarda a data da consulta
    ("Agendamento",      "Consulta",          2),

    # Médico gera orçamento logo após a consulta
    ("Consulta",         "Orçamento",         1),

    # Paciente solicita ajuste de valores → negocia
    ("Orçamento",        "Negociação",        4),
    # Paciente aceita o orçamento diretamente (sem negociar)
    ("Orçamento",        "Confirmação",       7),

    # Negociação concluída → contrato confirmado
    ("Negociação",       "Confirmação",       2),
]

# ── Pontos de origem e destino do fluxo ───────────────────────
ORIGEM  = "Lead"
DESTINO = "Confirmação"