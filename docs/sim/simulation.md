### Visão geral da simulação

A classe **ColonyGrowthSimulation** modela uma etapa de expansão da colônia, em que um módulo específico sofre aumento de carga energética. Isso simula situações reais do SIGIC, como:

- crescimento populacional em um módulo habitacional;
- aumento de consumo em um centro de processamento;
- sobrecarga temporária em setores críticos da rede.

Componentes envolvidos

### 1. Estrutura de dados base (Graph)

A simulação opera sobre um:

- Graph: representa a infraestrutura da colônia
- cada vertex representa um módulo (habitação, energia, laboratório etc.)
- cada vértice possui atributos como:
- current_load (carga atual)
- base_consumption (consumo base)

### 2. Classe EnergyGrowth (regras de evolução)

Essa classe contém as regras de “crescimento energético” do sistema.

increase_load
```
vertex.current_load *= (1 + percentage / 100)
```

Interpretação:

- aumenta a carga atual de um módulo de forma proporcional
- simula sobrecarga ou aumento de demanda

Exemplo:

- carga = 100
- aumento de 30%
- nova carga = 130

**add_consumption**

```
vertex.base_consumption += amount
```
Interpretação:

- aumenta o consumo base do módulo
- simula crescimento estrutural permanente da demanda energética

### 3. Simulação de crescimento (ColonyGrowthSimulation)
```
EnergyGrowth.increase_load(
    graph,
    vertex_id=7,
    percentage=30
)
```

O que isso faz na prática?

seleciona o módulo de ID 7
aplica um aumento de 30% na carga atual
não altera toda a rede, apenas um nó específico


