# Plano de testes — Citizen Assist AI

## Parte A — Testes de funcionamento do código
1. Entre na pasta `citizen-assist-ai` e execute `python main.py`.
2. Opção 1, pergunta `Como faço o cartão do SUS?`: espera-se `ALTA (7 pontos)`.
3. Digite uma pergunta sem correspondência: o programa deve indicar não encontrada.
4. Digite `meu cpf é 123.456.789-00`: deve recusar e não registrar no histórico.
5. Teste enter vazio, opção fora da faixa, letras no menu e `x` na pergunta `s/n`; não devem encerrar.
6. Opção 2: selecione categoria, orientação, dê retorno e volte com 0.
7. Opção 3: visualize indicadores. Opção 4: gere CSV.
8. Para testar arquivo inválido, faça uma cópia de `data/base_conhecimento.json` antes; remova temporariamente o original e confira a mensagem de erro, depois restaure.

## Parte B — Testes OBRIGATÓRIOS com usuários reais
**Pessoas fora da equipe: pelo menos 3. Atendimentos somados: pelo menos 10.**
Não anote nomes, CPF, telefone, e-mail ou informações identificadoras. Use P1, P2, P3. Cada pessoa escreve sua dúvida espontaneamente — não sugira palavras-chave.
Fale: “Escreva sua dúvida do seu jeito. Não digite nome, CPF, telefone nem e-mail.”

### Situações para apresentar oralmente (não ditar a pergunta)
1. Precisa fazer o cartão do SUS.
2. Quer consultar registros de vacina.
3. Conseguiu o primeiro emprego e precisa da carteira de trabalho.
4. Precisa tirar uma nova identidade em São Paulo.
5. Comprou um produto com problema.
6. Quer saber como receber alertas de enchente.
7. Está procurando uma unidade de saúde.
8. Quer consultar um serviço do governo online.
9. Não sabe onde buscar ajuda com direitos do consumidor.
10. Quer consultar serviços para trabalhadores.
11. Perdeu o acesso ao documento digital.
12. Quer descobrir informações sobre um serviço não cadastrado.

| Pessoa | Atendimento | Pergunta exata sem dados pessoais | Encontrou? | Ajudou? | Tempo (s) | Tentativas |
|---|---:|---|---|---|---:|---:|
| P1 | 1 | | | | | |
| P1 | 2 | | | | | |
| P1 | 3 | | | | | |
| P1 | 4 | | | | | |
| P2 | 5 | | | | | |
| P2 | 6 | | | | | |
| P2 | 7 | | | | | |
| P3 | 8 | | | | | |
| P3 | 9 | | | | | |
| P3 | 10 | | | | | |

Peça que cada pessoa saia com opção 0 e avalie facilidade de 1 a 5.
Depois, registre indicadores da opção 3 no README, dúvidas sem solução e **uma melhoria real** em `palavras_chave`. Reteste a mesma pergunta e registre o antes → mudança → depois. Não invente resultados.
