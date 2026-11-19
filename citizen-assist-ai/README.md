# Citizen Assist AI
Assistente de orientação ao cidadão no terminal, desenvolvido para a Global Solution de Pensamento Computacional e Automação com Python (FIAP, 2026.2).

## 1. Integrantes
- Nome: [PREENCHER] — RM: [PREENCHER]
- Nome: [PREENCHER] — RM: [PREENCHER]

## 2. Público e problema
Público: cidadãos que precisam descobrir como acessar documentos e serviços públicos em linguagem simples, com foco em serviços nacionais e exemplos do estado de São Paulo.
Problema: informações úteis estão dispersas em muitos sites; o usuário precisa de um ponto inicial para encontrar o canal oficial, sem revelar dados pessoais.

## 3. ODS relacionadas
- ODS 10: redução das desigualdades, pela informação acessível.
- ODS 16: instituições eficazes e acesso à informação pública.

## 4. Como executar
Requer Python 3.9+; sem bibliotecas externas.
```bash
python main.py
```
No Windows, alternativa: `py main.py`. Execute na pasta do projeto.
Menu: 1 perguntar, 2 navegar, 3 indicadores, 4 exportar CSV, 0 sair.
Arquivos com histórico e avaliações são gravados em `data/`. Não publique dados pessoais.

## 5. Orientação a Objetos
- `Orientacao`: representa um registro JSON e exibe sua resposta, documentos, local, fonte e aviso.
- `BaseConhecimento`: carrega o JSON e oferece categorias, pontuação e busca.
- `Assistente`: interage pelo terminal, bloqueia dados pessoais, registra atendimentos, calcula indicadores e exporta CSV.
Composição: Assistente contém BaseConhecimento, que contém objetos Orientacao.
A função `normalizar` retira acentos, pontuação e diferenças entre maiúsculas/minúsculas.

## 6. Pontuação e confiança
- +3 para **cada expressão-chave distinta** encontrada na pergunta inteira.
- +1 para cada palavra distinta da pergunta com pelo menos 4 caracteres encontrada no título.
- Maior pontuação primeiro: tuplas `(pontos, orientacao)`.
- >=6 pontos = ALTA; 3 a 5 = MÉDIA; <3 = não encontrada.
- Apresenta melhor resultado e no máximo 2 alternativas.
Exemplo: `Como faço o cartão do SUS?` → id 1, 7 pontos (expressões `cartao do sus` e `sus`, palavra `cartao` no título).

## 7. Privacidade, limitações e integrações
O assistente não solicita dados pessoais. Mensagens com `@` ou 8 ou mais dígitos são recusadas e não entram no histórico. Não é um órgão oficial. A base é estática, não acessa dados do governo ao vivo e pode ficar desatualizada. Erros de digitação e sinônimos não cadastrados podem deixar uma pergunta sem resposta. A lista de documentos deve ser confirmada na unidade responsável antes do atendimento.
Integrações com outras disciplinas: nenhuma (opcionais no enunciado).

## 8. Fontes consultadas e conferência
**Atenção:** links abaixo são oficiais, mas a equipe ainda precisa abrir e conferir **todos os 12**, comparar cada resposta com a fonte e substituir `PENDENTE` por uma data real de conferência no JSON. A existência de um link não equivale à revisão humana. A conferência dos documentos exigidos pela UBS local e pelo Poupatempo de SP também precisa ser feita pela equipe.

| ID | Tema | Link oficial | Conferência |
|---|---|---|---|
| 1 | Fazer o Cartão Nacional de Saúde (Cartão SUS) | https://www.gov.br/saude/pt-br/acesso-a-informacao/faq/tematicos-e-outros/como-conseguir-o-cartao-sus | [DATA DA CONFERÊNCIA] |
| 2 | Consultar o Cartão SUS digital | https://www.gov.br/saude/pt-br/composicao/seidigi/meususdigital/perguntas-e-respostas/cidadao/9-como-faco-o-cartao | [DATA DA CONFERÊNCIA] |
| 3 | Consultar registros de vacinação | https://www.gov.br/saude/pt-br/composicao/seidigi/meususdigital/perguntas-e-respostas/cidadao | [DATA DA CONFERÊNCIA] |
| 4 | Obter a Carteira de Trabalho Digital | https://www.gov.br/pt-br/servicos/obter-a-carteira-de-trabalho | [DATA DA CONFERÊNCIA] |
| 5 | Solicitar a Carteira de Identidade Nacional (CIN) em São Paulo | https://www.poupatempo.sp.gov.br/carta/D97C3844-A2D9-4C9E-B364-CB4FEB26A1FB | [DATA DA CONFERÊNCIA] |
| 6 | Consultar serviços da conta gov.br | https://www.gov.br/pt-br | [DATA DA CONFERÊNCIA] |
| 7 | Registrar reclamação de compra ou serviço | https://www.gov.br/pt-br/servicos/reclamar-contra-servico-ou-produto-de-empresas-privadas | [DATA DA CONFERÊNCIA] |
| 8 | Conhecer os direitos do consumidor | https://www.gov.br/mj/pt-br/assuntos/seus-direitos/consumidor | [DATA DA CONFERÊNCIA] |
| 9 | Receber alertas da Defesa Civil por SMS | https://www.gov.br/pt-br/servicos/solicitar-cadastro-para-recebimento-de-avisos-e-alertas-de-desastres | [DATA DA CONFERÊNCIA] |
| 10 | Entender o sistema Defesa Civil Alerta | https://www.gov.br/mdr/pt-br/assuntos/protecao-e-defesa-civil/defesa-civil-alerta | [DATA DA CONFERÊNCIA] |
| 11 | Consultar serviços para trabalhadores no Emprega Brasil | https://www.gov.br/pt-br/servicos/acessar-portal-emprega-brasil-2013-trabalhador | [DATA DA CONFERÊNCIA] |
| 12 | Localizar unidades de saúde pelo Meu SUS Digital | https://www.gov.br/saude/pt-br/composicao/seidigi/meususdigital/perguntas-e-respostas/cidadao/2-quais-os-servicos-que | [DATA DA CONFERÊNCIA] |

## 9. Teste com usuários e melhoria
**NÃO REALIZADO:** preencher somente após testes reais com >=3 pessoas de fora da equipe e >=10 atendimentos no total.
- Testadores anônimos: P1, P2, P3
- Total: [PREENCHER]
- Resposta encontrada (%): [PREENCHER]
- Taxa de acerto / ajudou (%): [PREENCHER]
- Tempo médio (s): [PREENCHER]
- Tentativas por atendimento: [PREENCHER]
- Facilidade (1 a 5): [PREENCHER]
- Dúvidas sem solução: [PREENCHER]
- Melhoria comprovada: **Antes** [pergunta sem resposta] → **Mudança** [nova palavra-chave] → **Depois** [resultado do reteste].
Execute opção 3 para coletar indicadores e opção 4 para gerar o CSV.

## Simulação fictícia adicional
Foi criada a pasta `simulacao/` com Gustavo (4 atendimentos), Ariane (3) e Thalles (3), com dados, CSV e indicadores **inteiramente fictícios**. Não são testes com usuários reais e não devem ser utilizados como evidência do requisito da seção 9. Consulte `simulacao/RELATORIO_SIMULADO.md`.

## 10. Vídeo técnico
Link do YouTube não listado: [INSERIR LINK APÓS A GRAVAÇÃO]
Duração permitida: entre 5 e 8 minutos; todos os integrantes devem explicar o código com a própria voz. Ver `docs/roteiro_video.md`.

## 11. Organização
`main.py`, `orientacao.py`, `base_conhecimento.py`, `assistente.py`, `data/`, `docs/`.
