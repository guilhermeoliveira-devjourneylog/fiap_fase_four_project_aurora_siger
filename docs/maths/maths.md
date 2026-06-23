# Modelagem Matemática do Sistema Inteligente de Gerenciamento da Infraestrutura da Colônia (SIGIC)

## 1. Modelagem da Infraestrutura como Grafo

A infraestrutura da colônia é representada por um **grafo ponderado**:

\[
G = (V,E)
\]

onde:

- \(V\) representa o conjunto de vértices (módulos da colônia);
- \(E\) representa o conjunto de arestas (conexões entre módulos).

Cada vértice corresponde a um setor da colônia, como Habitação, Agricultura, Centro Médico ou Armazenamento de Energia.

Cada módulo é modelado pelo conjunto:

\[
v_i=(id,\;nome,\;C_b,\;L,\;G_c)
\]

onde:

| Parâmetro | Descrição |
|------------|------------|
| \(id\) | Identificador do módulo |
| \(nome\) | Nome do módulo |
| \(C_b\) | Consumo energético nominal |
| \(L\) | Fator de carga operacional |
| \(G_c\) | Capacidade de geração |

Essa modelagem permite representar matematicamente a infraestrutura da Aurora Siger como uma rede inteligente de distribuição energética.

---

## 2. Modelo de Consumo Energético

O consumo efetivo de um módulo depende do consumo nominal e da carga operacional aplicada.

\[
C_i=C_{base_i} X L_i
\]

onde:

| Variável | Significado |
|-----------|------------|
| \(C_i\) | Consumo atual do módulo |
| \(C_{base_i}\) | Consumo nominal |
| \(L_i\) | Fator de carga |

O fator de carga representa o nível de utilização do módulo.

### Interpretação

- \(L = 1\) → operação normal;
- \(L > 1\) → sobrecarga;
- \(L < 1\) → operação reduzida.

### Implementação

```python
@property
def consumption(self) -> float:
    return (
        self.base_consumption *
        self.current_load
    )
```

### Exemplo

Se:

\[
C_{base}=100\;kW
\]

e:

\[
L=1.3
\]

então:

\[
C=100 X 1.3
\]

\[
C=130\;kW
\]

---

## 3. Consumo Total da Colônia

A demanda energética global da colônia é obtida pela soma dos consumos individuais:

\[
D=\sum_{i=1}^{n}C_i
\]

onde:

- \(n\) representa o número total de módulos;
- \(C_i\) representa o consumo de cada módulo.

### Implementação

```python
sum(
    vertex.consumption
    for vertex
    in graph.vertices.values()
)
```

### Interpretação

Se os módulos consomem:

| Módulo | Consumo (kW) |
|---------|-------------|
| Habitação | 120 |
| Agricultura | 180 |
| Laboratório | 150 |
| Comunicação | 90 |
| Centro Médico | 60 |

Então:

\[
D=120+180+150+90+60
\]

\[
D=600\;kW
\]

Esse valor representa a demanda total da infraestrutura.

---

## 4. Capacidade de Geração

A energia disponível para a colônia é definida pela capacidade de geração do módulo energético.

\[
G=G_c
\]

onde:

\[
G_c={generation\_capacity}
\]

### Implementação

```python
return (
    graph.vertices[
        EnergyDistribution
        .ENERGY_MODULE_ID
    ]
    .generation_capacity
)
```

### Interpretação

Se:

\[
G=750\;kW
\]

significa que a central energética consegue fornecer até 750 kW para toda a rede.

---

## 5. Índice de Cobertura Energética

O índice de cobertura mede a relação entre energia produzida e energia demandada.

\[
CE={G} / {D}
\]

onde:

| Valor | Interpretação |
|---------|-------------|
| \(CE > 1\) | Sobra energética |
| \(CE = 1\) | Equilíbrio |
| \(CE < 1\) | Déficit |

### Exemplo

\[
CE={900} / {600}
\]

\[
CE=1.5
\]

Existe 50% de capacidade excedente.

### Implementação

```python
return generation / demand
```

---

## 6. Saldo Energético

O saldo energético é calculado pela diferença entre geração e demanda.

\[
S=G-D
\]

onde:

| Resultado | Significado |
|------------|-------------|
| \(S > 0\) | Sobra de energia |
| \(S = 0\) | Equilíbrio |
| \(S < 0\) | Déficit energético |

### Exemplo

\[
S=800-600
\]

\[
S=200\;kW
\]

Há uma reserva operacional de 200 kW.

### Implementação

```python
return generation - demand
```

---

## 7. Modelagem das Perdas de Transmissão

As perdas energéticas são estimadas utilizando os menores caminhos calculados pelo algoritmo de Dijkstra.

Se:

\[
d_i
\]

representa a distância mínima entre o módulo gerador e o módulo \(i\),

então a distância acumulada da rede é:

\[
D_T=\sum_{i=1}^{n}d_i
\]

As perdas energéticas são calculadas por:

\[
P=D_T X f
\]

onde:

| Variável | Significado |
|------------|------------|
| \(D_T\) | Soma das menores distâncias |
| \(f\) | Fator de perda |
| \(P\) | Perda energética total |

No SIGIC:

\[
f=0.01
\]

### Justificativa Física

Quanto maior o comprimento total da rede, maiores tendem a ser as perdas devido à resistência elétrica dos condutores.

### Implementação

```python
return (
    total_distance *
    EnergyDistribution
    .LOSS_FACTOR
)
```

---

## 8. Energia Efetivamente Entregue

Nem toda a energia produzida chega aos módulos consumidores.

A energia efetivamente entregue é calculada por:

\[
E_d=D-P
\]


### Exemplo

Se:

\[
D=600
\]

e:

\[
P=15
\]

então:

\[
E_d=585\;kW
\]

### Implementação

```python
return max(
    demand - losses,
    0
)
```

---

## 9. Índice de Eficiência de Distribuição (EDEI)

O principal indicador de desempenho do SIGIC é:

\[
EDEI={E_d} / {G}
\]

onde:

| Variável | Significado |
|-----------|------------|
| \(E_d\) | Energia entregue |
| \(G\) | Energia gerada |

Esse índice mede a eficiência global da distribuição energética.

### Exemplo

\[
EDEI= {720} / {800}
\]

\[
EDEI=0.90
\]

ou:

\[
90\%
\]

Isso significa que 90% da energia gerada está chegando aos módulos consumidores.

### Implementação

```python
return delivered / generation
```

---

## 10. Classificação da Eficiência

O valor do EDEI é convertido em uma classificação operacional.

| Faixa do EDEI | Classificação |
|---------------|--------------|
| \(EDEI \ge 0.90\) | Excelente |
| \(0.75 \le EDEI < 0.90\) | Boa |
| \(0.60 \le EDEI < 0.75\) | Regular |
| \(EDEI < 0.60\) | Crítica |

### Implementação

```python
if index >= 0.90:
    return "Excelente"

if index >= 0.75:
    return "Boa"

if index >= 0.60:
    return "Regular"

return "Crítica"
```

---

## 11. Modelo de Crescimento da Demanda

Quando a colônia cresce, os módulos passam a exigir mais energia.

O fator de carga é atualizado por:

\[
L_{novo}
=
L_{atual}(
1 + {p} / {100}
)
\]

onde:

- \(p\) representa a taxa percentual de crescimento.

### Exemplo

Para um aumento de 20%:

\[
L_{novo}
=
1.0
(
1+{20}/{100}
)
\]

\[
L_{novo}=1.2
\]

### Implementação

```python
vertex.current_load *= (
    1 + percentage / 100
)
```

---

## 12. Modelo de Expansão do Consumo

A instalação de novos equipamentos aumenta permanentemente a demanda energética do módulo.

\[
C_{base}^{novo}
=
C_{base}^{atual}
+
\Delta C
\]

onde:

- \(\Delta C\) representa a carga adicionada.

### Exemplo

Se:

\[
C_{base}=100\;kW
\]

e:

\[
\Delta C=40\;kW
\]

então:

\[
C_{base}^{novo}
=
100+40
\]

\[
C_{base}^{novo}
=
140\;kW
\]

### Implementação

```python
vertex.base_consumption += amount
```

---

# Formulação Matemática Consolidada

O comportamento energético do SIGIC pode ser resumido pelo conjunto de equações:

\[
C_i=C_{base_i}L_i
\]

\[
D=\sum_{i=1}^{n}C_i
\]

\[
CE=\frac{G}{D}
\]

\[
S=G-D
\]

\[
D_T=\sum_{i=1}^{n}d_i
\]

\[
P=D_Tf
\]

\[
E_d=D-P
\]

\[
EDEI=\frac{E_d}{G}
\]

Essas equações integram conceitos de Teoria dos Grafos, análise de redes, distribuição de energia, modelagem matemática e otimização computacional, permitindo que o SIGIC monitore, avalie e otimize o funcionamento da infraestrutura energética da colônia Aurora Siger.