# SIMULAÇÃO FICTÍCIA — 10 atendimentos

**Atenção:** nenhum dos dados abaixo foi coletado de pessoas reais. Gustavo, Ariane e Thalles são nomes usados exclusivamente em personagens fictícios da simulação. Os tempos, retornos e notas são hipotéticos. Esta simulação **não substitui** o teste obrigatório da Global Solution com 3 pessoas reais de fora da equipe.

| Participante fictício | Atendimento | Pergunta | Confiança | Encontrou | Ajudou | Tempo (s) |
|---|---:|---|---|---|---|---:|
| Gustavo | 1 | Como faço o cartão do SUS? | ALTA (7 pts) | Sim | Sim | 22.4 |
| Gustavo | 2 | Onde encontro minha carteira de trabalho digital? | ALTA (6 pts) | Sim | Sim | 30.8 |
| Gustavo | 3 | Comprei um produto defeituoso, como fazer reclamacao? | ALTA (7 pts) | Sim | Sim | 28.1 |
| Gustavo | 4 | Como faço para emitir segunda via do passaporte? | NÃO ENCONTRADA (0 pts) | Não | Não aplicável | 35.2 |
| Ariane | 5 | Como recebo alerta de enchente no celular? | MÉDIA (3 pts) | Sim | Sim | 21.6 |
| Ariane | 6 | Preciso consultar as vacinas que tomei | MÉDIA (4 pts) | Sim | Sim | 25.9 |
| Ariane | 7 | Quero tirar o RG novo em São Paulo | MÉDIA (4 pts) | Sim | Não | 33.7 |
| Thalles | 8 | Quero saber meus direitos consumidor | MÉDIA (5 pts) | Sim | Sim | 24.2 |
| Thalles | 9 | Onde consigo encontrar UBS perto de casa? | MÉDIA (3 pts) | Sim | Sim | 29.5 |
| Thalles | 10 | Como solicitar a segunda via da conta de luz? | NÃO ENCONTRADA (0 pts) | Não | Não aplicável | 31.4 |

## Indicadores da simulação (NÃO são resultados reais)
- **atendimentos:** 10
- **resposta_encontrada_pct:** 80.0
- **taxa_ajudou_pct:** 87.5
- **tempo_medio_segundos:** 27.0
- **tentativas_por_atendimento:** 1.1
- **facilidade_media:** 4.33
- **duvidas_sem_solucao:** ['Como faço para emitir segunda via do passaporte?', 'Como solicitar a segunda via da conta de luz?']

**Notas fictícias de facilidade:** Gustavo 5/5, Ariane 4/5, Thalles 4/5.

## Como usar
- `historico_simulado.json`: estrutura de registros semelhante ao histórico do programa, com `simulado: true` para identificação.
- `atendimentos_simulados.csv`: tabela detalhada dos personagens fictícios, para visualizar ou abrir em planilha.
- `avaliacoes_simuladas.json`: notas hipotéticas.
- `indicadores_simulados.json`: resultados calculados usando as regras do programa.

Para demonstrar esses indicadores no menu do programa sem misturar dados com testes reais, faça uma **cópia temporária** de `data/historico.json` e `data/avaliacoes.json`, copie os arquivos de simulação para os respectivos nomes em `data/`, execute `python main.py` e escolha a opção `3`. **Depois restaure os arquivos originais.** Não publique essa cópia como evidência de testes reais.

## Para o relatório da FIAP
Use `docs/plano_de_testes.md` com pessoas reais, identificadas apenas como P1, P2 e P3, sem nomes nem informações pessoais. Repita pelo menos 10 atendimentos de verdade e atualize o README com os indicadores obtidos.
