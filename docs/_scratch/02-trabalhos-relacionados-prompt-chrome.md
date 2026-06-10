# Prompts para Claude no Chrome — Busca de Trabalhos Relacionados

> **Nota interna (remover na versão final):** Este arquivo contém os prompts operacionais para conduzir a Leva 2 da busca usando o Claude no navegador (Claude for Chrome). Não compõe o corpo do TCC. Após concluída a busca, os resultados extraídos devem ser realocados para [02-trabalhos-relacionados-protocolo.md](02-trabalhos-relacionados-protocolo.md), seção "Tabela de candidatos identificados".

## Antes de começar (passo 0 — manual)

Faça **antes** de invocar o Claude no Chrome:

1. **Logue-se no proxy da UFPE em outra aba** (CAFe / Portal de Periódicos CAPES). Sem isso, ACM, IEEE e Springer retornarão "subscribe to access" e o agente vai parar.
2. **Abra Google Scholar logado com seu e-mail institucional** (`@ufpe.br` ou similar) — isso libera "Acessar via biblioteca" automaticamente em vários papers.
3. **Crie uma pasta de downloads dedicada**: `~/Downloads/tcc-pqc-papers/` — o agente vai baixar PDFs aqui.
4. **Tenha este arquivo aberto numa aba**, com o [protocolo](02-trabalhos-relacionados-protocolo.md) em outra, para colar os resultados ao final de cada sessão.
5. **Reserve 60–90 minutos por sessão.** Não tente tudo de uma vez — divida por string de busca.

---

## Prompt 1 — Kickoff de sessão (cole uma vez por sessão)

Cole este prompt no Claude no Chrome **no início de cada sessão**. Ele estabelece o contexto da pesquisa e os critérios.

```
Você vai me ajudar a executar uma busca sistemática de trabalhos
relacionados para o meu TCC. O tema do TCC é:

  "Avaliação experimental de criptografia pós-quântica (ML-DSA-44 e
   Kyber512/ML-KEM-512) versus criptografia clássica (RSA-2048 com
   JWT RS256) em autenticação de APIs Web, incluindo um modo híbrido
   que combina ambos."

A pergunta de pesquisa norteadora é:

  "Quais estudos empíricos publicados entre 2018 e 2026 avaliam o
   desempenho de algoritmos pós-quânticos baseados em reticulados
   (Dilithium/ML-DSA, CRYSTALS-Kyber/ML-KEM) em autenticação ou
   comunicação segura na Web, comparando com baselines clássicos
   (RSA, ECDSA, ECDH)?"

CRITÉRIOS DE INCLUSÃO (todos devem ser satisfeitos):
- CI1: publicado entre 2018 e 2026
- CI2: reporta medições empíricas (latência, memória ou payload)
- CI3: avalia Dilithium, ML-DSA, CRYSTALS-Kyber ou ML-KEM (Falcon e
       SPHINCS+ também aceitos se comparados aos anteriores)
- CI4: texto completo acessível
- CI5: inglês ou português
- CI6: conferência revisada por pares, periódico, ou pré-print
       IACR/arXiv

CRITÉRIOS DE EXCLUSÃO (qualquer um já elimina):
- CE1: trabalho puramente teórico, sem medições
- CE2: foco exclusivo em hardware (FPGA/ASIC) sem software
- CE3: poster, slide, tutorial, blog post, white paper de empresa
- CE4: survey ou literature review (esses servem para outro
       capítulo do TCC, não para trabalhos relacionados)
- CE5: duplicata — versão antiga de um trabalho que já catalogamos
- CE6: fora do domínio Web (IoT embarcada, redes veiculares, etc.)
       — exceto se comparam diretamente com baseline web

JÁ CATALOGADOS (não me reporte como novidade; só me avise se
encontrar uma versão mais recente):
- Commey et al. (2025), arXiv:2505.02239
- Zheng et al. (2024), arXiv:2404.13544
- Sikeridis; Kampanakis; Devetsikiotis (2020), NDSS
- Paquin; Stebila; Tamvada (2020), PQCrypto
- Schardong (2023), CANS, DOI 10.1007/978-3-031-20974-1_20
- Bindel; Buchmann; Krämer (2017), PQCrypto

REGRA DE OURO: na dúvida, INCLUA na lista preliminar e me deixe
decidir. Não filtre por conta própria além dos critérios acima.

Confirme que entendeu e aguarde meu próximo prompt com a string
de busca.
```

---

## Prompt 2 — Executar uma string de busca (cole uma vez por string)

Depois do kickoff, cole **uma string por vez** com este wrapper. Substitua `<STRING>` pela string da tabela abaixo.

```
Vamos executar a próxima string de busca:

  STRING: <STRING>

PASSOS:
1. Abra https://scholar.google.com em uma nova aba.
2. Cole a STRING acima na barra de busca e pressione Enter.
3. Aplique o filtro de data: "Desde 2018".
4. Liste os primeiros 20 resultados como uma tabela com colunas:
     [posição | título | autores | ano | veículo | link |
      decisão preliminar com base em título+resumo: INCLUIR /
      EXCLUIR / DÚVIDA | justificativa de 1 linha]
5. Para cada resultado marcado INCLUIR ou DÚVIDA, clique em
   "Acessar via biblioteca UFPE" quando disponível; caso
   contrário, clique no título para abrir a página do paper.
6. NÃO baixe PDFs ainda. Apenas liste.

Quando terminar, me apresente a tabela e aguarde minha decisão
sobre quais aprofundar.
```

### Strings de busca a executar (em ordem)

Execute uma por vez. Entre uma e outra, salve a tabela retornada num bloco aqui no arquivo (seção "Saída por string", abaixo).

| # | String | Prioridade |
|---|--------|-----------|
| S5 | `"post-quantum" AND ("JWT" OR "OAuth" OR "OpenID") AND ("authentication" OR "token")` | **Alta** — nicho do TCC, esperam-se poucos mas críticos |
| S4 | `"hybrid" AND ("post-quantum" OR "PQC") AND ("TLS" OR "authentication") AND ("performance" OR "benchmark")` | Alta — modo híbrido é diferencial do TCC |
| S2 | `("Dilithium" OR "ML-DSA") AND ("performance" OR "latency") AND ("benchmark" OR "evaluation") -hardware -FPGA -ASIC` | Média — exclusão de hardware já na query |
| S3 | `("Kyber" OR "ML-KEM") AND ("KEM" OR "key encapsulation") AND ("TLS" OR "QUIC") AND benchmark` | Média |
| S1 | `("post-quantum" OR "PQC") AND ("REST" OR "API" OR "web service") AND ("authentication" OR "token")` | Baixa — caça à lacuna; espera-se quase nada |

---

## Prompt 3 — Aprofundar um candidato (cole uma vez por paper que vale a pena ler)

Quando você quiser que o agente leia um paper completo e preencha a ficha:

```
Aprofunde este candidato:

  URL: <URL_DO_PAPER>

PASSOS:
1. Acesse a URL.
2. Se for paywall, tente "Acessar via biblioteca UFPE" / "Get PDF
   via institution". Se mesmo assim bloquear, me avise — vou
   tentar via outro caminho.
3. Se conseguir o PDF, baixe em ~/Downloads/tcc-pqc-papers/ com
   nome no padrão: AUTORANO_titulo-curto.pdf
   (ex.: SCHARDONG2023_pq-oidc-oauth.pdf)
4. Leia o PDF integralmente e preencha a ficha abaixo:

FICHA DE EXTRAÇÃO:
- Autor(es) e ano (formato ABNT abreviado):
- Veículo completo (conferência/periódico, edição, páginas):
- DOI:
- Algoritmos PQC avaliados:
- Algoritmos clássicos usados como baseline:
- Domínio de aplicação (TLS / SSH / JWT / OIDC / raw benchmark / outro):
- Plataforma (hardware, OS, linguagem, biblioteca usada):
- Métricas reportadas (latência, memória, payload, throughput, energia):
- Tamanho da amostra (N iterações, número de runs):
- Resultado-chave (2-3 frases):
- Relação com o TCC do Gabriel (lacuna preenchida, complementaridade,
  ou competidor direto):
- Decisão final: INCLUIR na tabela comparativa / EXCLUIR /
  REALOCAR para Referencial Teórico — com justificativa.

Devolva apenas a ficha preenchida em markdown, sem comentários
adicionais.
```

---

## Prompt 4 — Fechamento de sessão (cole no final)

```
Encerre a sessão:

1. Liste todos os papers que processamos hoje, com decisão final
   (incluir / excluir / dúvida pendente).
2. Aponte quais ficaram em DÚVIDA e o que falta para decidir.
3. Liste os PDFs salvos em ~/Downloads/tcc-pqc-papers/ e o nome
   exato de cada um.
4. Sugira a próxima string de busca a executar na próxima sessão,
   com base no que ainda não foi coberto.
```

---

## Saída por string (espaço para colar os resultados aqui)

> Cole abaixo, conforme for executando, as tabelas retornadas pelo agente. Mantém a rastreabilidade da Leva 2 e alimenta o registro de execução do protocolo.

### S5 — JWT/OAuth/OIDC

_(colar a tabela retornada pelo agente)_

### S4 — Híbrido

_(colar)_

### S2 — Dilithium/ML-DSA isolado

_(colar)_

### S3 — Kyber/ML-KEM em TLS/QUIC

_(colar)_

### S1 — APIs REST

_(colar)_

---

## Armadilhas comuns (leia uma vez antes de começar)

1. **Google Scholar é ruidoso.** Aceite que ~60% dos resultados serão descartados na triagem. Não tente fazer o agente filtrar mais do que os critérios CI/CE permitem.
2. **PDFs gigantes (>50 páginas) podem estourar o contexto do agente.** Para esses, peça explicitamente: *"leia apenas o abstract, introdução, e seção de resultados/avaliação experimental — pule fundamentação teórica."*
3. **Springer e ACM às vezes pedem captcha** mesmo logado no proxy. Se aparecer, resolva manualmente e devolva o controle ao agente.
4. **O agente pode "alucinar" referências** se encurralado. Quando ele afirmar que um paper diz X, **abra o PDF e confira a página antes de citar no TCC.** Esse passo é inegociável.
5. **Salve incrementalmente.** A cada 2–3 papers processados, copie a saída para este arquivo. Sessões do Chrome caem.

---

## O que devolver para mim quando terminar

Quando você concluir as 5 strings (mesmo que em sessões separadas), me devolva aqui no Claude (CLI):

1. As 5 tabelas brutas (uma por string) — colando o conteúdo acima.
2. As fichas de extração preenchidas dos candidatos marcados INCLUIR.
3. Os PDFs salvos (eu não preciso dos arquivos, só da lista de nomes).

A partir daí eu atualizo o [protocolo](02-trabalhos-relacionados-protocolo.md), consolido a tabela final de 6–10 trabalhos, e começamos a redigir o capítulo.
