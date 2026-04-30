# 🏥 CRM Hospital São Rafael — Sprint 4: Grafos e Dijkstra

> **Matéria:** Dynamic Programming (Python)
> **Instituição:** [Nome da Faculdade]
> **Semestre:** [Semestre/Ano]
> **Equipe:** Ana Luiza Santana · Erick Cardoso · Gabrielly Candido · João Victor Ferreira · Luiza Ribeiro

---

## 📋 Sobre o Projeto

Este repositório contém a **Sprint 4** do desafio integrador de desenvolvimento de um **CRM de Vendas e Leads** para o **Hospital São Rafael**.
O foco desta sprint é modelar o **fluxo do CRM como um grafo direcionado** e aplicar o **algoritmo de Dijkstra** para encontrar o caminho mais eficiente — em tempo — para converter um Lead em Confirmação de contrato.

---

## 🧠 Conceitos Aplicados

| Conceito | Onde é usado |
|---|---|
| **Grafo direcionado e ponderado** | Representação do fluxo CRM em `grafo.py` |
| **Lista de adjacência** | Estrutura de dados escolhida para o grafo |
| **Min-heap (`heapq`)** | Fila de prioridade do Dijkstra em `dijkstra.py` |
| **Algoritmo de Dijkstra** | Menor caminho Lead → Confirmação |
| **DFS (busca em profundidade)** | Enumeração de todos os caminhos possíveis em `interpretacao.py` |
| **Relaxamento de arestas** | Atualização de distâncias no Dijkstra |

---

## 📁 Estrutura do Repositório

```
SPRINT4-HSR-PY/
│
├── main.py            # Ponto de entrada — executa as 3 tarefas em sequência
├── dados.py           # Nós, arestas e pesos do grafo CRM
├── grafo.py           # Tarefa 1 — representação do fluxo como grafo
├── dijkstra.py        # Tarefa 2 — algoritmo de Dijkstra
├── utils.py           # Funções auxiliares de exibição
└── README.md
```

> Cada módulo de tarefa pode ser executado individualmente com `python <arquivo>.py`.

---

## ⚙️ Como Executar

**Pré-requisito:** Python 3.10 ou superior — sem dependências externas.

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/SPRINT4-HSR-PY.git
cd SPRINT4-HSR-PY

# Executar o projeto completo
python main.py

# Ou executar uma tarefa individualmente
python grafo.py
python dijkstra.py
python interpretacao.py
```

---
