"""
Topologia da Rede da Colônia Lunar.

Este programa modela a infraestrutura física de uma colônia lunar
utilizando um grafo não direcionado e ponderado.

Cada vértice representa um módulo funcional da colônia, enquanto
cada aresta representa uma conexão física entre dois módulos.

Os pesos associados às arestas correspondem às distâncias, em metros,
entre os módulos conectados.

A visualização é produzida com NetworkX e Matplotlib, permitindo
analisar a conectividade, centralidade e redundância da rede.
"""

import matplotlib.pyplot as plt
import networkx as nx


# ==========================================================
# MÓDULOS DA COLÔNIA
# ==========================================================

"""
Lista de vértices do grafo.

Cada elemento representa um módulo operacional da colônia lunar.
"""

VERTICES = [
    "Centro",
    "Agricultura",
    "Comunicacao",
    "Pesquisa",
    "Recursos",
    "Energia",
    "Medico",
    "Habitacao",
    "Transporte",
]


# ==========================================================
# CONEXÕES ENTRE MÓDULOS
# ==========================================================

"""
Lista de arestas ponderadas.

Estrutura:
    (origem, destino, distancia)

Onde:

- origem: módulo de origem.
- destino: módulo de destino.
- distancia: comprimento da conexão em metros.

O grafo é não direcionado, portanto as conexões são
bidirecionais.
"""

ARESTAS = [

    # ------------------------------------------------------
    # Centro de Controle
    # ------------------------------------------------------
    ("Centro", "Agricultura", 250),
    ("Centro", "Comunicacao", 180),
    ("Centro", "Pesquisa", 220),
    ("Centro", "Recursos", 260),
    ("Centro", "Energia", 120),
    ("Centro", "Medico", 200),
    ("Centro", "Habitacao", 170),
    ("Centro", "Transporte", 300),

    # ------------------------------------------------------
    # Sistema Energético
    # ------------------------------------------------------
    ("Energia", "Agricultura", 140),
    ("Energia", "Comunicacao", 150),
    ("Energia", "Pesquisa", 160),
    ("Energia", "Recursos", 190),
    ("Energia", "Medico", 170),
    ("Energia", "Habitacao", 130),
    ("Energia", "Transporte", 210),

    # ------------------------------------------------------
    # Interconexões Secundárias
    # ------------------------------------------------------
    ("Agricultura", "Comunicacao", 110),
    ("Agricultura", "Recursos", 90),

    ("Comunicacao", "Pesquisa", 130),

    ("Pesquisa", "Recursos", 80),

    ("Medico", "Habitacao", 95),

    ("Habitacao", "Transporte", 145),

    ("Recursos", "Transporte", 175),
]


# ==========================================================
# POSIÇÕES DOS MÓDULOS NO MAPA
# ==========================================================

"""
Coordenadas cartesianas utilizadas na renderização.

As posições foram definidas manualmente para destacar:

- Centro de Controle como hub principal.
- Energia como hub estratégico.
- Setores funcionais distribuídos ao redor da rede.
"""

POSICOES = {

    # Hub Principal
    "Centro": (0, 0),

    # Hub Energético
    "Energia": (0, -2),

    # Setor Oeste
    "Agricultura": (-4, -2),
    "Comunicacao": (-4, 1),

    # Setor Norte
    "Pesquisa": (0, 3),

    # Setor Leste
    "Recursos": (4, 1),

    # Setor Sul
    "Medico": (-2, -5),
    "Habitacao": (2, -5),

    # Logística
    "Transporte": (5, -3),
}


# ==========================================================
# CRIAÇÃO DO GRAFO
# ==========================================================

"""
Instanciação do grafo da colônia lunar.

O objeto NetworkX armazena os vértices e as conexões
ponderadas entre os módulos.
"""

grafo = nx.Graph()

grafo.add_nodes_from(VERTICES)

for origem, destino, distancia in ARESTAS:
    grafo.add_edge(
        origem,
        destino,
        weight=distancia
    )


# ==========================================================
# VISUALIZAÇÃO
# ==========================================================

"""
Renderização gráfica da topologia.

A figura apresenta:

- Os módulos da colônia como vértices.
- As conexões físicas como arestas.
- As distâncias entre módulos como rótulos.
"""

plt.figure(figsize=(12, 8))

nx.draw(
    grafo,
    POSICOES,
    with_labels=True,
    node_size=4000,
    font_size=10,
)

pesos = nx.get_edge_attributes(
    grafo,
    "weight"
)

nx.draw_networkx_edge_labels(
    grafo,
    POSICOES,
    edge_labels=pesos
)

plt.title(
    "Topologia da Rede da Colônia Lunar"
)

plt.axis("off")
plt.tight_layout()
plt.show()