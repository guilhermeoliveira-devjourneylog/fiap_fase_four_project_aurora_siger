## Dijkstra

Tipo de algoritmo: Algoritmo guloso (Greedy) de grafos

O Dijkstra resolve o problema de menor caminho a partir de uma origem em grafos com pesos não negativos.

Funcionamento geral

### 1. Inicialização

```
distances = [inf] * graph.size
distances[source] = 0
previous = [None] * graph.size
visited = [False] * graph.size
```

- distances: guarda a menor distância conhecida até cada nó
- previous: guarda o caminho (predecessores)
- visited: marca nós já processados

### 2. Escolha do próximo nó (passo guloso)

```
for vertex in range(graph.size):
    if not visited[vertex] and distances[vertex] < min_distance:
        current = vertex
```

Sempre escolhe o vértice não visitado com menor distância
Isso caracteriza o comportamento guloso do algoritmo

### 3. Relaxamento das arestas

```
for neighbor, distance in graph.neighbors(current):
```

Para cada vizinho:

```
alternative = distances[current] + distance
```

Se o novo caminho for melhor:

```
if alternative < distances[neighbor]:
    distances[neighbor] = alternative
    previous[neighbor] = current
```

Nome técnico desse processo:

Relaxamento de arestas (edge relaxation)


## 3. Reconstrução de Caminho (reconstruct_path)

```
def reconstruct_path(previous, destination)
```

Funcionamento

1. Parte do destino

current = destination

2. Sobe pelos predecessores

```
while current is not None:
    path.append(current)
    current = previous[current]
```

3. Inverte o caminho

```
path.reverse()
```

O que ele faz na prática

Transforma isso:

previous:
A <- B <- C <- D (destino)

Em isso:

A -> B -> C -> D

4. Resumo do sistema de algoritmos

No conjunto, o sistema funciona assim:

DijkstraAlgorithm

Calcula menores distâncias
Preenche:
distances
previous

ShortestPathResult
Estrutura de retorno padronizada

reconstruct_path
Converte previous em caminho legível