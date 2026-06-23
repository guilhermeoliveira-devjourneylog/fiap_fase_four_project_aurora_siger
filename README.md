# fiap_fase_four_project_aurora_siger

Sistema Inteligente de Gerenciamento da Infraestrutura da Colônia (SIGIC)
Arquitetura Computacional para Distribuição Inteligente de Energia na Colônia Aurora Siger

Versão: 1.0
Projeto: Fase 4 – Aurora Siger
Autor: Guilherme Rodrigues Oliveira
Ano: 2026

## Resumo Executivo

A expansão da colônia marciana Aurora Siger trouxe novos desafios relacionados à distribuição de energia, comunicação entre módulos, estabilidade operacional e sustentabilidade da infraestrutura. À medida que novos setores foram adicionados à base, a complexidade da rede aumentou significativamente, exigindo mecanismos computacionais capazes de otimizar recursos e apoiar a tomada de decisão.

O Sistema Inteligente de Gerenciamento da Infraestrutura da Colônia (SIGIC) foi desenvolvido para representar computacionalmente a infraestrutura da colônia utilizando grafos, estruturas de dados e algoritmos clássicos de redes. O sistema permite monitorar módulos críticos, analisar rotas energéticas, identificar caminhos mínimos e simular cenários operacionais visando aumentar a eficiência energética e reduzir desperdícios.

### 1. Introdução

A sobrevivência de uma colônia autossustentável em  depende diretamente da disponibilidade contínua de energia, comunicação e suporte à vida. Conforme a infraestrutura cresce, surgem desafios relacionados à distribuição eficiente de recursos e à manutenção da estabilidade operacional. A proposta do SIGIC é criar uma representação computacional da infraestrutura da Aurora Siger utilizando grafos, onde módulos são modelados como vértices e suas conexões como arestas. Essa abordagem permite aplicar algoritmos clássicos de teoria dos grafos para otimização da rede.

###  2. Problema

A expansão da colônia introduziu diversos desafios:

Desperdício energético;
Rotas ineficientes de distribuição;
Sobrecarga em módulos críticos;
Atrasos de comunicação;
Dificuldade de priorização operacional;
Crescimento da complexidade da rede.

Sem um sistema inteligente de gerenciamento, a infraestrutura corre risco de falhas que podem comprometer a sobrevivência da missão.

### 3. Objetivos

Objetivo Geral

Desenvolver um sistema inteligente capaz de representar, monitorar e otimizar a infraestrutura energética e operacional da colônia Aurora Siger.

Objetivos Específicos
Representar a colônia por meio de grafos.
Implementar algoritmos BFS, DFS e Dijkstra.
Organizar informações utilizando estruturas de dados em Python.
Simular cenários energéticos.
Identificar gargalos operacionais.
Apoiar decisões estratégicas.
Aplicar conceitos de sustentabilidade e governança tecnológica.

### 4. Infraestrutura da Solução

[Infraestrutura](./docs/infraestrutura/infraestrutura.md)

### 5. Estruturas de Dados

[Estrutura de Dados](/docs/data_structure/estrutura_de_dados.md)

### 6. Algoritmos Implementados

[Algoritmos](/docs/algorithms/algorithms.md)

### 7. Modelagem Matemática

[Modelagem Matemática](/docs/maths/maths.md)

### 8. Simulação Energética

[Simulação](/docs/sim/simulation.md)

O SIGIC implementa simulações para:

Crescimento populacional da colônia;
Aumento da demanda energética;
Expansão da infraestrutura;
Redistribuição automática de energia;
Identificação de módulos críticos.

Os resultados permitem avaliar a estabilidade da rede em diferentes cenários operacionais.

### 9. Sustentabilidade e ESG

O projeto incorpora princípios de sustentabilidade e governança tecnológica.

Sustentabilidade
Minimização de perdas energéticas;
Uso eficiente dos recursos;
Planejamento da expansão da infraestrutura;
Redução de desperdícios.
Governança
Priorização de módulos críticos;
Transparência operacional;
Monitoramento contínuo;
Critérios objetivos para tomada de decisão.

### Execução 

## Execução do sistema 
```python
 & [root]/fiap_fase_four_project_aurora_siger/.venv/Scripts/python.exe [root]/fiap_fase_four_project_aurora_siger/sigic/sistema.py
```