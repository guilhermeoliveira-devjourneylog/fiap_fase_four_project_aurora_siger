Essas conexões representam a infraestrutura física e lógica da colônia lunar, onde cada aresta indica uma rota de comunicação, transporte de recursos, distribuição de energia ou troca operacional entre dois módulos. O peso associado à conexão pode ser interpretado como a distância em metros, o custo de instalação/manutenção ou o custo de deslocamento entre os módulos.

## Estrutura Geral da Rede

A rede foi projetada com três níveis:

**1. Centro de Controle como Hub Principal**

O módulo Centro de Controle possui ligação direta com todos os demais módulos:

| Conexão              | Distância |
| -------------------- | --------: |
| Centro ↔ Energia     |       120 |
| Centro ↔ Habitação   |       170 |
| Centro ↔ Comunicação |       180 |
| Centro ↔ Médico      |       200 |
| Centro ↔ Pesquisa    |       220 |
| Centro ↔ Agricultura |       250 |
| Centro ↔ Recursos    |       260 |
| Centro ↔ Transporte  |       300 |


**Justificativa**

O Centro de Controle coordena toda a operação da colônia:

- monitora sistemas;
- recebe telemetria;
- envia comandos;
- gerencia emergências;
- supervisiona a distribuição de energia.

Por isso ele possui acesso direto a todos os módulos.

O menor custo ocorre para Energia (120) porque a gestão energética é crítica para a sobrevivência da colônia.

**2. Energia como Hub Secundário**

O módulo Energia também possui ligação direta com todos os módulos operacionais.

| Conexão               | Distância |
| --------------------- | --------: |
| Energia ↔ Habitação   |       130 |
| Energia ↔ Agricultura |       140 |
| Energia ↔ Comunicação |       150 |
| Energia ↔ Pesquisa    |       160 |
| Energia ↔ Médico      |       170 |
| Energia ↔ Recursos    |       190 |
| Energia ↔ Transporte  |       210 |

**Justificativa**

Toda a colônia depende da distribuição elétrica.

A Energia atua como:

- gerador principal;
- distribuidor de potência;
- ponto de monitoramento de carga;
- rota alternativa caso o Centro fique indisponível.

Essa redundância aumenta a resiliência da rede.

**3. Conexões Secundárias**

As conexões secundárias representam interações frequentes entre módulos que trabalham em conjunto.

Agricultura ↔ Recursos (90)

É a menor distância da rede.

Motivo:

- Recursos fornece água, minerais e matéria-prima;
- Agricultura utiliza esses insumos continuamente.

Fluxo intenso de materiais justifica proximidade física.

Pesquisa ↔ Recursos (80)

Menor conexão de toda a colônia.

Motivo:

- amostras minerais extraídas são enviadas para análise;
- laboratórios dependem constantemente de materiais coletados.

Médico ↔ Habitação (95)

Os habitantes precisam de acesso rápido aos serviços médicos.

Em emergências, essa é uma das rotas mais críticas.

Agricultura ↔ Comunicação (110)

Permite:

- transmissão de sensores ambientais;
- controle remoto das estufas;
- monitoramento agrícola em tempo real.

Comunicação ↔ Pesquisa (130)

A Pesquisa gera enormes volumes de dados científicos que precisam ser:

- armazenados;
- compartilhados;
- enviados à Terra.

Habitação ↔ Transporte (145)

Facilita:

- deslocamento diário dos colonos;
- embarque para missões externas;
- logística interna.

