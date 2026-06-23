### Conjunto integrado de estruturas orientadas a objetos e variáveis indexadas, com foco em modelar um grafo ponderado que representa a infraestrutura da colônia

## 1. Estrutura central: Grafo da Colônia

**Graph**

É a estrutura principal de armazenamento.

Tipo de estrutura:
- Grafo ponderado
Implementado com:
- dict[int, Vertex] → armazenamento dos vértices
- list[list[int | None]] → matriz de adjacência

Componentes:

**Vértices**

self.vertices: dict[int, Vertex]

- Chave: id do módulo
- Valor: objeto Vertex

**Arestas**

self.adj_matrix: list[list[None | int]]

Matriz quadrada size x size

Representa o peso (distância/custo) entre nós

None = ausência de conexão

Natureza
Grafo não direcionado
Simétrico:

- adj[i][j] = adj[j][i]

### 2. Estrutura de vértice

Vertex

Representa um módulo da colônia

Tipo:
- Estrutura de dados tipo registro (dataclass)

Campos:
- id: int
- name: str
- base_consumption: float
- current_load: float = 1.0
- generation_capacity: float = 0.0

Propriedade derivada:

consumption = base_consumption * current_load

Isso transforma o vértice em uma estrutura dinâmica, pois o consumo muda conforme carga.

### 3. Estrutura de aresta

**Edge**

source: int
target: int
distance: int

Tipo:
- Registro imutável (frozen=True)
Papel:
- Representa conexão entre módulos
- Guarda o peso da ligação

### 4. Estrutura de resultado do algoritmo

**ShortestPathResult**

- distances: list
- previous: list

Tipo:

Estrutura de retorno de algoritmo

Significado:
- distances

Lista indexada por vértice

Armazena:
- menor distância do nó origem até cada nó
- previous

Lista de predecessores

Permite reconstrução do caminho

É uma estrutura típica de algoritmos de grafos baseada em:

- arrays indexados
- acesso O(1)

### 5. Estrutura auxiliar de reconstrução de caminho

reconstruct_path(previous, destination)

Tipo:

- algoritmo baseado em vetor de predecessores

Estrutura lógica:
- entrada: lista previous[]
- saída: lista path[]

Funcionamento:
- retrocede do destino até a origem

usa encadeamento:
destination → previous → previous → ... → None

### 6. Estruturas energéticas (camada analítica)

**EnergyConsumption**

Estrutura puramente funcional:

- não armazena dados
- opera sobre o grafo

Usa:
- graph.vertices.values() → iteração sobre objetos Vertex

Estrutura base:

- dicionário + objetos + agregação

**EnergyDistribution**

Combina:

- grafos
- algoritmos (Dijkstra)
- agregações

Estruturas internas usadas:
- list (distâncias)
- dict (vértices)

resultados de algoritmo (ShortestPathResult)

Característica importante:

transforma estrutura de grafo em modelo matemático de energia

**EnergyGrowth**

Estrutura de mutação de estado:

- altera atributos de Vertex
- não cria novos dados estruturais
- modifica estados existentes

### 7. Estrutura construtora do sistema

**ColonyGraphBuilder**

Responsável por montar o sistema.

Estruturas criadas:
- Lista de vértices
```
vertices = {
    id: (name, consumption)
}
```
- Lista de arestas
```
edges = [
    (source, target, distance)
]
```

Conversão:
- lista → objetos Vertex
- lista → objetos Edge
- inseridos no Graph

### 8. Classificação geral das estruturas

O sistema combina 4 tipos principais:

1. Vetores (listas Python)
- distances
- previous
- filas implícitas de iteração

2. Matrizes
adj_matrix

estrutura clássica de grafo denso

3. Dicionários
graph.vertices

acesso O(1) por ID

4. Objetos (POO / dataclasses)
Vertex
Edge
ShortestPathResult

encapsulam estado + comportamento

