# Roteiro do vídeo técnico (aprox. 7 minutos)
Todos os integrantes devem falar com a própria voz. Exiba código legível + terminal.
Se houver somente uma pessoa, faça todas as partes. Se houver dupla, use A/B.

1. **0:00–0:30 — A**: identifique equipe, público atendido e problema.
2. **0:30–1:15 — A**: abra `data/base_conhecimento.json`; explique uma orientação, listas e dicionários; mostre a lista de tuplas da busca em `base_conhecimento.py`.
3. **1:15–2:05 — B**: explique `Orientacao`, `BaseConhecimento` e `Assistente`; atributos, métodos, `self` e composição.
4. **2:05–2:55 — A**: mostre `normalizar()` e `pontuar()`. Demonstre `Como faço o cartão do SUS?`: +3 `cartao do sus`, +3 `sus`, +1 `cartao` = 7 (ALTA).
5. **2:55–4:00 — B**: rode o sistema. Mostre pergunta encontrada, sem resultado, opção inválida, texto com `@` bloqueado e navegação por categorias.
6. **4:00–5:10 — A**: faça uma **alteração REAL ao vivo**. Antes: pergunte `Preciso do meu documento de trabalho online` (confirme se não encontrou). Depois: adicione a expressão `documento de trabalho online` às palavras-chave do id 4 no JSON, salve, reinicie e repita: agora encontra. *Não adicione essa expressão antes de gravar.* Se essa pergunta já encontrar, escolha outra expressão inédita e confirme previamente.
7. **5:10–6:10 — B**: abra `data/historico.json`, exporte `data/atendimentos.csv`, mostre opção 3 e explique os **indicadores reais** de >=3 usuários e >=10 atendimentos.
8. **6:10–7:00 — A e B**: explique uma decisão técnica (busca local por regras, sem IA externa) e uma limitação (dependência de palavras-chave/fonte estática).

Conferir áudio, duração de 5 a 8 minutos, vídeo não listado e link acessível antes da entrega.
