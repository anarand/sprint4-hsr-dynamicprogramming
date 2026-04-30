# 🏥 CRM Hospital São Rafael — Sprint 4: Grafos e Dijkstra

## Para acessar a documentação técnica, clique aqui no [link da documentação do projeto.](https://docs.google.com/document/d/12iFjDxmj4o4cLB6VeEuLOk47B1eSCFefqIFj37hK0GY/edit?usp=sharing)

**Turma:** 2ESPS  

**Alunos:**
- Ana Luiza Santana RM: 561194  
- Erick Cardoso RM: 560440  
- Gabrielly Candido RM: 560916  
- João Victor Ferreira RM: 560439  
- Luiza Ribeiro RM: 560200
---

## 📋 Sobre o Projeto

Este repositório contém a **Sprint 4** do desafio integrador de desenvolvimento de um **CRM de Vendas e Leads** para o **Hospital São Rafael**.
O foco desta sprint é modelar o **fluxo do CRM como um grafo direcionado** e aplicar o **algoritmo de Dijkstra** para encontrar o caminho mais eficiente — em tempo — para converter um Lead em Confirmação de contrato.

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
git clone https://github.com/anarand/sprint4-hsr-dynamicprogramming.git
cd SPRINT4-HSR-PY

# Executar o projeto completo
python main.py

# Ou executar uma tarefa individualmente
python grafo.py
python dijkstra.py
```

---
