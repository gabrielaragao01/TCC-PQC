# Apêndice A — Protocolo da Revisão de Literatura

> Este apêndice apresenta o protocolo metodológico que orientou a identificação, a filtragem e a classificação dos estudos discutidos no Capítulo 2 (Trabalhos Relacionados). O protocolo foi registrado *previamente* à execução das buscas — característica que distingue um mapeamento sistemático, ainda que leve, de uma revisão narrativa *ad hoc*. As Seções A.1 a A.12 reproduzem o protocolo tal como pré-registrado; a Seção A.13 sintetiza sua execução e o resultado da seleção. A subseção 2.1 do Capítulo 2 ("Metodologia da Revisão") resume, em prosa, o conteúdo deste apêndice.

## A.1 Caracterização e Justificativa

A revisão da literatura adotada neste trabalho caracteriza-se como um **mapeamento sistemático leve** (lightweight systematic mapping), e não como uma revisão sistemática da literatura (SLR) completa nos moldes propostos por Kitchenham e Charters (2007). A justificativa para essa escolha é tripla:

1. **Adequação ao escopo de um TCC.** Uma SLR completa demanda dois ou mais revisores independentes, formulários estruturados de extração e cálculo de concordância inter-avaliador (κ de Cohen), o que ultrapassa o escopo realista de um trabalho de conclusão de curso conduzido por um único autor.
2. **Maturidade da literatura no nicho específico.** A literatura sobre desempenho de criptografia pós-quântica em autenticação web baseada em token JWT é estreita e relativamente recente (concentrada entre 2018 e 2026), de modo que a saturação ocorre rapidamente — não há volume que exija filtragem de centenas de artigos.
3. **Finalidade comparativa, não inferencial.** O capítulo não pretende sintetizar evidência quantitativa (meta-análise) nem mapear exaustivamente um campo; pretende **posicionar este trabalho frente ao estado da arte**, identificar a lacuna que ele preenche e dialogar com 6 a 10 estudos representativos.

O resultado esperado é uma tabela comparativa de 6–10 trabalhos relacionados, acompanhada de prosa que organize os estudos por subgrupos temáticos.

## A.2 Pergunta de Pesquisa Norteadora

> **PQ:** Quais estudos empíricos publicados entre 2018 e 2026 avaliam o desempenho de algoritmos pós-quânticos baseados em reticulados — particularmente Dilithium/ML-DSA e CRYSTALS-Kyber/ML-KEM — em contextos de autenticação ou comunicação segura sobre protocolos da Web, e como esses estudos se posicionam frente a alternativas criptográficas clássicas (RSA, ECDSA, ECDH)?

Essa pergunta define o escopo da busca em quatro dimensões: **tipo de estudo** (empírico, com medições), **algoritmos de interesse**, **domínio de aplicação** (Web/TLS/autenticação) e **referencial de comparação** (clássico). Trabalhos puramente teóricos, análises de segurança formal e estudos sobre criptografia pós-quântica em domínios estranhos à Web (e.g., redes ad hoc veiculares, IoT embarcada) ficam fora do escopo central — podem ser citados, quando pertinente, no Referencial Teórico (Capítulo 3).

## A.3 Bases de Dados Consultadas

A pesquisa será conduzida nas seguintes bases, priorizando aquelas com texto completo aberto e acesso institucional via UFPE:

| Base | URL | Acesso | Tipo de cobertura |
|------|-----|--------|-------------------|
| IACR ePrint Archive | https://eprint.iacr.org | Aberto | Pré-prints de criptografia revisados por pares |
| USENIX Open Access | https://www.usenix.org/publications | Aberto | Anais USENIX Security e correlatos |
| ACM Digital Library | https://dl.acm.org | Institucional (UFPE) | Anais CCS, ASIACCS, CHES |
| IEEE Xplore | https://ieeexplore.ieee.org | Institucional (UFPE) | Anais EuroS&P, S&P, ICC |
| arXiv (cs.CR) | https://arxiv.org/list/cs.CR | Aberto | Pré-prints adicionais não cobertos pelo IACR |
| Google Scholar | https://scholar.google.com | Aberto | Varredura complementar; ruidoso, usado para identificar trabalhos não indexados nas demais bases |

**Justificativa da combinação:** as três primeiras bases concentram conferências top-tier em segurança computacional, nas quais trabalhos sobre PQC aplicado tipicamente são publicados. arXiv e Google Scholar atuam como complemento de cobertura para garantir que pré-prints relevantes e trabalhos publicados em fóruns menos centrais não sejam perdidos.

## A.4 Strings de Busca

As strings foram construídas combinando termos algorítmicos, termos de domínio e termos metodológicos. Os operadores booleanos seguem a sintaxe suportada pela maioria das bases (variações pontuais foram aplicadas quando necessário; ver registro de execução).

| # | String | Objetivo |
|---|--------|----------|
| S1 | `("post-quantum" OR "PQC") AND ("authentication" OR "TLS" OR "JWT") AND ("benchmark" OR "performance")` | Núcleo do tema (intersecção PQC × autenticação × medição) |
| S2 | `("Dilithium" OR "ML-DSA") AND ("performance" OR "latency" OR "evaluation")` | Foco em assinatura pós-quântica baseada em reticulados |
| S3 | `("Kyber" OR "ML-KEM") AND ("KEM" OR "key encapsulation") AND ("benchmark" OR "TLS")` | Foco em KEM pós-quântico |
| S4 | `("hybrid" OR "hybridization") AND ("post-quantum" OR "PQC") AND ("TLS" OR "authentication")` | Modo híbrido — relevante para o Capítulo 4 deste trabalho |
| S5 | `("post-quantum" OR "PQC") AND ("REST" OR "API" OR "web authentication" OR "OAuth" OR "JWT")` | Domínio Web stricto sensu — possível lacuna do estado da arte |

**Observação:** strings que retornam zero resultados em bases relevantes são, em si, evidência da lacuna que motiva o presente trabalho. Tais "buscas vazias" serão documentadas como achado e citadas explicitamente na narrativa do capítulo.

## A.5 Critérios de Inclusão

Para um estudo ser elegível à tabela comparativa, deve satisfazer **todos** os critérios abaixo:

- **CI1.** Publicado entre janeiro de 2018 e a data de execução da busca (corte temporal estabelecido a partir do início da Round 2 do processo NIST PQC).
- **CI2.** Reporta medições empíricas em pelo menos uma das três dimensões: latência, consumo de memória ou tamanho de payload.
- **CI3.** Avalia ao menos um dos algoritmos da família lattice-based de interesse: Dilithium, ML-DSA, CRYSTALS-Kyber ou ML-KEM. Estudos que avaliam Falcon e/ou SPHINCS+ em comparação direta com os anteriores também são elegíveis.
- **CI4.** Disponibiliza texto completo (acesso aberto, acesso institucional UFPE ou pré-print válido).
- **CI5.** Idioma: inglês ou português.
- **CI6.** Tipo de publicação: artigo em conferência revisada por pares, artigo em periódico, ou pré-print do IACR/arXiv com vinculação institucional verificável.

## A.6 Critérios de Exclusão

Um estudo é excluído quando qualquer um dos critérios abaixo se aplica:

- **CE1.** Trabalho exclusivamente teórico — sem medições experimentais.
- **CE2.** Foco exclusivo em hardware especializado (FPGA, ASIC) sem contraparte software acessível para comparação.
- **CE3.** Posters, abstracts estendidos, tutoriais, slides e relatórios técnicos sem revisão por pares (exceção: relatórios NIST oficiais, que são tratados como referência normativa no Capítulo 3, não como trabalho relacionado).
- **CE4.** Surveys e revisões da literatura — não compõem trabalhos relacionados, mas podem ser citados no Referencial Teórico (Capítulo 3).
- **CE5.** Duplicatas — quando o mesmo grupo publica versões incrementais do mesmo experimento, retém-se a versão mais recente ou mais completa.
- **CE6.** Trabalhos fora do domínio Web (e.g., PQC em redes veiculares, IoT embarcada com restrições severas de recursos), exceto quando explicitamente comparam com algum baseline também avaliado neste TCC.

## A.7 Procedimento de Seleção

A seleção segue o fluxo PRISMA simplificado abaixo (3 etapas, em vez das 4 da SLR completa):

1. **Identificação.** Execução das strings S1–S5 nas seis bases listadas. Registro do número bruto de resultados por par (string, base) em planilha de execução.
2. **Triagem por título e resumo.** Leitura de título e resumo de cada resultado único (após deduplicação). Aplicação dos critérios de inclusão CI1–CI3 e dos critérios de exclusão CE1, CE3, CE4. Decisão binária: incluir para leitura completa, ou descartar (com justificativa de 1 linha).
3. **Leitura completa e extração.** Leitura integral dos candidatos remanescentes. Aplicação dos critérios restantes (CI4–CI6, CE2, CE5, CE6). Preenchimento da ficha de extração descrita na próxima seção.

## A.8 Ficha de Extração

Para cada trabalho selecionado, registram-se os seguintes campos:

| Campo | Conteúdo |
|-------|----------|
| Autor(es) e ano | Citação ABNT abreviada |
| Veículo | Conferência / periódico / repositório |
| Algoritmos avaliados | Quais primitivas PQC e quais baselines clássicos |
| Domínio de aplicação | TLS, SSH, JWT, raw bench, outro |
| Plataforma | Hardware, sistema operacional, linguagem |
| Métricas | Latência, memória, tamanho, throughput, energia |
| Tamanho da amostra | N de iterações, número de runs |
| Resultado-chave | Achado principal em 1–2 frases |
| Relação com este TCC | Lacuna preenchida ou complementaridade |

Os campos *Domínio de aplicação*, *Plataforma* e *Métricas* serão expostos na tabela comparativa do capítulo. Os demais alimentam a narrativa de prosa.

## A.9 Critério de Parada

A busca é encerrada quando ocorre **qualquer um** dos seguintes:

- **CP1.** Saturação: três strings consecutivas retornam apenas trabalhos já catalogados na tabela de candidatos, sem novos elegíveis.
- **CP2.** Quantidade-alvo atingida: 8 a 10 estudos selecionados após aplicação integral dos critérios — limite superior recomendado para um capítulo de TCC com tabela comparativa.
- **CP3.** Esgotamento das bases sem novos candidatos elegíveis.

O critério efetivamente disparado é registrado no encerramento da busca e mencionado na seção de Metodologia da Revisão do capítulo.

## A.10 Estratégia de Execução Adotada Neste Trabalho

A execução das buscas foi organizada em **duas levas complementares**, divididas conforme a natureza do acesso a cada base:

- **Primeira leva — bases abertas.** As buscas em IACR ePrint, USENIX Open Access, arXiv e Google Scholar foram executadas pelo autor utilizando as interfaces públicas dessas bases, com triagem inicial dos resultados por leitura de título e resumo.
- **Segunda leva — bases com paywall.** As buscas em ACM Digital Library, IEEE Xplore e Springer foram executadas pelo autor por meio do acesso institucional da UFPE (Portal de Periódicos CAPES via CAFe), com leitura integral dos PDFs e fichamento conforme o procedimento descrito na Seção 8.

A divisão visa maximizar cobertura sem incorrer em custos de assinatura individual e organizar o esforço por tipo de acesso. A integração das duas levas é tratada como passe único na contabilidade do PRISMA simplificado (Seção 7); a procedência de cada trabalho é, no entanto, registrada na ficha de extração para fins de auditoria.

## A.11 Subgrupos Temáticos Esperados

Os trabalhos selecionados serão agrupados, na narrativa do capítulo, em quatro subgrupos progressivamente mais próximos do escopo deste TCC:

1. **Benchmarks de primitivas PQC isoladas** — estudos sobre custo computacional puro dos algoritmos, sem integração a protocolos.
2. **PQC em protocolos de rede (TLS, SSH, QUIC)** — estudos que medem o impacto do PQC no handshake e no transporte, sem foco em autenticação por token.
3. **Esquemas híbridos clássico+PQC** — estudos sobre estratégias de migração e o custo da dupla autenticação.
4. **PQC em autenticação Web baseada em token (JWT, OAuth, OIDC)** — subgrupo no qual o presente trabalho se insere e no qual a literatura é mais escassa, evidenciando a lacuna que o TCC procura preencher.

A organização em ordem crescente de proximidade temática é deliberada e cumpre função argumentativa: prepara o leitor para a justificativa da contribuição declarada no Capítulo 1.

## A.12 Limitações Declaradas do Protocolo

Para fins de transparência metodológica e para antecipar potenciais arguições da banca, registram-se as seguintes limitações:

- **L1.** Revisor único — risco de viés de seleção não mitigado por concordância inter-avaliador. Mitigação adotada: registro explícito dos critérios e da justificativa de exclusão de cada candidato.
- **L2.** Cobertura restrita a inglês e português — trabalhos relevantes publicados em alemão, francês ou chinês podem ter sido omitidos. Mitigação: nenhuma direta; limitação aceita.
- **L3.** Recorte temporal de 2018 em diante — estudos seminais anteriores (e.g., Bernstein/Lange 2017) entram no Referencial Teórico, não em Trabalhos Relacionados.
- **L4.** Dependência de busca textual — trabalhos que utilizem terminologia divergente das strings podem ter sido perdidos. Mitigação: ampliação iterativa das strings durante a fase de identificação, com registro das variantes utilizadas.
- **L5.** Acesso institucional descontínuo — alguns artigos de paywall podem permanecer inacessíveis. Tais casos são registrados como "consultado apenas via abstract" e tratados com cautela na extração.

Estas limitações serão sumarizadas no próprio capítulo de Trabalhos Relacionados, em parágrafo de fechamento da seção de Metodologia da Revisão.

## A.13 Execução e Resultado da Seleção

A execução do protocolo ocorreu em maio de 2026, organizada nas duas levas descritas na Seção A.10. O Quadro A.1 resume o fluxo de seleção, no formato PRISMA simplificado de três etapas estabelecido na Seção A.7.

**Quadro A.1** — Fluxo de seleção dos trabalhos relacionados.

| Etapa | Resultado |
|-------|-----------|
| Identificação | Strings S1–S5 executadas nas seis bases (Seção A.3), em duas levas (bases abertas e bases de acesso institucional). No Google Scholar, cada string retornou da ordem de mil resultados brutos, dos quais os vinte primeiros por string foram triados. |
| Triagem (título e resumo) | Cem registros triados na segunda leva — 16 incluídos, 16 em dúvida e 68 excluídos; após consolidação com a primeira leva, **26 candidatos únicos**. |
| Leitura completa e auditoria | Os candidatos foram lidos integralmente e submetidos a três rodadas de auditoria de metadados (autores, ano, veículo e existência efetiva da publicação), com correção de discrepâncias em cinco trabalhos e descarte de uma referência cuja existência não pôde ser confirmada. |
| Seleção final | **Onze trabalhos** compõem a tabela comparativa (Tabela 2.1); três trabalhos adicionais, de relevância histórica ou de apoio, são citados na narrativa sem integrar a tabela. |

Registra-se um achado relevante da etapa de identificação: a string S5 — a mais diretamente alinhada ao nicho deste trabalho, combinando termos de criptografia pós-quântica a termos de autenticação Web por token (REST, API, OAuth, JWT) — não retornou candidatos diretamente elegíveis na varredura do Google Scholar. Essa "busca vazia" constitui, em si, evidência empírica da escassez de literatura no recorte específico do presente trabalho, conforme discutido na Seção 2.7.

O critério de parada efetivamente acionado foi o **CP2** (quantidade-alvo atingida), com a faixa-alvo ajustada de 6–10 para 6–12 estudos em razão da densidade do subgrupo de trabalhos sobre TLS. O Quadro A.2 lista os onze trabalhos selecionados, na numeração adotada na Tabela 2.1 do Capítulo 2.

**Quadro A.2** — Trabalhos selecionados para a tabela comparativa.

| TR | Trabalho (ano) | Subgrupo temático |
|----|----------------|-------------------|
| TR1 | Alkhulaifi; El-Alfy (2020) | 1 — PQC em autenticação Web por token |
| TR2 | Kalpana; Saravana Kumar (2025) | 1 — PQC em autenticação Web por token |
| TR3 | Schardong (2024) | 1 — PQC em autenticação Web por token |
| TR4 | Giron; Perin; Nascimento; Custódio (2023) | 2 — Esquemas híbridos clássico + PQC |
| TR5 | Paul; Kuzovkova; Lahr; Niederhagen (2022) | 2 — Esquemas híbridos clássico + PQC |
| TR6 | Sikeridis; Kampanakis; Devetsikiotis (2020) | 3 — PQC em TLS, mTLS e sessão |
| TR7 | Sosnowski et al. (2023) | 3 — PQC em TLS, mTLS e sessão |
| TR8 | Anastasova; Kampanakis (2025) | 3 — PQC em TLS, mTLS e sessão |
| TR9 | Olushola; Meenakshi (2025) | 3 — PQC em TLS, mTLS e sessão |
| TR10 | Abbasi; Cardoso; Váz; Silva; Martins (2025) | 4 — Benchmarks cross-plataforma |
| TR11 | Demir; Gorgulu; Onbasli (2026) | 4 — Benchmarks cross-plataforma |

Fonte: Elaborado pelo autor (2026).
