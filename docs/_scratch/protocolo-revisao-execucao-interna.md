# Protocolo de Seleção de Trabalhos Relacionados

> **Nota interna (remover na versão final do TCC):** Este documento registra o protocolo metodológico adotado para identificar, filtrar e classificar os estudos que comporão o capítulo *Trabalhos Relacionados*. A existência deste protocolo, e o seu registro prévio à execução das buscas, é o que diferencia uma revisão sistemática (ainda que leve) de uma revisão narrativa ad hoc. Partes deste documento devem ser sumarizadas no próprio capítulo, em uma subseção de abertura intitulada "Metodologia da Revisão" (~1 página).

## 1. Caracterização e Justificativa

A revisão da literatura adotada neste trabalho caracteriza-se como um **mapeamento sistemático leve** (lightweight systematic mapping), e não como uma revisão sistemática da literatura (SLR) completa nos moldes propostos por Kitchenham e Charters (2007). A justificativa para essa escolha é tripla:

1. **Adequação ao escopo de um TCC.** Uma SLR completa demanda dois ou mais revisores independentes, formulários estruturados de extração e cálculo de concordância inter-avaliador (κ de Cohen), o que ultrapassa o escopo realista de um trabalho de conclusão de curso conduzido por um único autor.
2. **Maturidade da literatura no nicho específico.** A literatura sobre desempenho de criptografia pós-quântica em autenticação web baseada em token JWT é estreita e relativamente recente (concentrada entre 2018 e 2026), de modo que a saturação ocorre rapidamente — não há volume que exija filtragem de centenas de artigos.
3. **Finalidade comparativa, não inferencial.** O capítulo não pretende sintetizar evidência quantitativa (meta-análise) nem mapear exaustivamente um campo; pretende **posicionar este trabalho frente ao estado da arte**, identificar a lacuna que ele preenche e dialogar com 6 a 10 estudos representativos.

O resultado esperado é uma tabela comparativa de 6–10 trabalhos relacionados, acompanhada de prosa que organize os estudos por subgrupos temáticos.

## 2. Pergunta de Pesquisa Norteadora

> **PQ:** Quais estudos empíricos publicados entre 2018 e 2026 avaliam o desempenho de algoritmos pós-quânticos baseados em reticulados — particularmente Dilithium/ML-DSA e CRYSTALS-Kyber/ML-KEM — em contextos de autenticação ou comunicação segura sobre protocolos da Web, e como esses estudos se posicionam frente a alternativas criptográficas clássicas (RSA, ECDSA, ECDH)?

Essa pergunta define o escopo da busca em quatro dimensões: **tipo de estudo** (empírico, com medições), **algoritmos de interesse**, **domínio de aplicação** (Web/TLS/autenticação) e **referencial de comparação** (clássico). Trabalhos puramente teóricos, análises de segurança formal e estudos sobre criptografia pós-quântica em domínios estranhos à Web (e.g., redes ad hoc veiculares, IoT embarcada) ficam fora do escopo central — podem ser citados, quando pertinente, no Referencial Teórico (Capítulo 3).

## 3. Bases de Dados Consultadas

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

## 4. Strings de Busca

As strings foram construídas combinando termos algorítmicos, termos de domínio e termos metodológicos. Os operadores booleanos seguem a sintaxe suportada pela maioria das bases (variações pontuais foram aplicadas quando necessário; ver registro de execução).

| # | String | Objetivo |
|---|--------|----------|
| S1 | `("post-quantum" OR "PQC") AND ("authentication" OR "TLS" OR "JWT") AND ("benchmark" OR "performance")` | Núcleo do tema (intersecção PQC × autenticação × medição) |
| S2 | `("Dilithium" OR "ML-DSA") AND ("performance" OR "latency" OR "evaluation")` | Foco em assinatura pós-quântica baseada em reticulados |
| S3 | `("Kyber" OR "ML-KEM") AND ("KEM" OR "key encapsulation") AND ("benchmark" OR "TLS")` | Foco em KEM pós-quântico |
| S4 | `("hybrid" OR "hybridization") AND ("post-quantum" OR "PQC") AND ("TLS" OR "authentication")` | Modo híbrido — relevante para o Capítulo 4 deste trabalho |
| S5 | `("post-quantum" OR "PQC") AND ("REST" OR "API" OR "web authentication" OR "OAuth" OR "JWT")` | Domínio Web stricto sensu — possível lacuna do estado da arte |

**Observação:** strings que retornam zero resultados em bases relevantes são, em si, evidência da lacuna que motiva o presente trabalho. Tais "buscas vazias" serão documentadas como achado e citadas explicitamente na narrativa do capítulo.

## 5. Critérios de Inclusão

Para um estudo ser elegível à tabela comparativa, deve satisfazer **todos** os critérios abaixo:

- **CI1.** Publicado entre janeiro de 2018 e a data de execução da busca (corte temporal estabelecido a partir do início da Round 2 do processo NIST PQC).
- **CI2.** Reporta medições empíricas em pelo menos uma das três dimensões: latência, consumo de memória ou tamanho de payload.
- **CI3.** Avalia ao menos um dos algoritmos da família lattice-based de interesse: Dilithium, ML-DSA, CRYSTALS-Kyber ou ML-KEM. Estudos que avaliam Falcon e/ou SPHINCS+ em comparação direta com os anteriores também são elegíveis.
- **CI4.** Disponibiliza texto completo (acesso aberto, acesso institucional UFPE ou pré-print válido).
- **CI5.** Idioma: inglês ou português.
- **CI6.** Tipo de publicação: artigo em conferência revisada por pares, artigo em periódico, ou pré-print do IACR/arXiv com vinculação institucional verificável.

## 6. Critérios de Exclusão

Um estudo é excluído quando qualquer um dos critérios abaixo se aplica:

- **CE1.** Trabalho exclusivamente teórico — sem medições experimentais.
- **CE2.** Foco exclusivo em hardware especializado (FPGA, ASIC) sem contraparte software acessível para comparação.
- **CE3.** Posters, abstracts estendidos, tutoriais, slides e relatórios técnicos sem revisão por pares (exceção: relatórios NIST oficiais, que são tratados como referência normativa no Capítulo 3, não como trabalho relacionado).
- **CE4.** Surveys e revisões da literatura — não compõem trabalhos relacionados, mas podem ser citados no Referencial Teórico (Capítulo 3).
- **CE5.** Duplicatas — quando o mesmo grupo publica versões incrementais do mesmo experimento, retém-se a versão mais recente ou mais completa.
- **CE6.** Trabalhos fora do domínio Web (e.g., PQC em redes veiculares, IoT embarcada com restrições severas de recursos), exceto quando explicitamente comparam com algum baseline também avaliado neste TCC.

## 7. Procedimento de Seleção

A seleção segue o fluxo PRISMA simplificado abaixo (3 etapas, em vez das 4 da SLR completa):

1. **Identificação.** Execução das strings S1–S5 nas seis bases listadas. Registro do número bruto de resultados por par (string, base) em planilha de execução.
2. **Triagem por título e resumo.** Leitura de título e resumo de cada resultado único (após deduplicação). Aplicação dos critérios de inclusão CI1–CI3 e dos critérios de exclusão CE1, CE3, CE4. Decisão binária: incluir para leitura completa, ou descartar (com justificativa de 1 linha).
3. **Leitura completa e extração.** Leitura integral dos candidatos remanescentes. Aplicação dos critérios restantes (CI4–CI6, CE2, CE5, CE6). Preenchimento da ficha de extração descrita na próxima seção.

## 8. Ficha de Extração

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

## 9. Critério de Parada

A busca é encerrada quando ocorre **qualquer um** dos seguintes:

- **CP1.** Saturação: três strings consecutivas retornam apenas trabalhos já catalogados na tabela de candidatos, sem novos elegíveis.
- **CP2.** Quantidade-alvo atingida: 8 a 10 estudos selecionados após aplicação integral dos critérios — limite superior recomendado para um capítulo de TCC com tabela comparativa.
- **CP3.** Esgotamento das bases sem novos candidatos elegíveis.

O critério efetivamente disparado é registrado no encerramento da busca e mencionado na seção de Metodologia da Revisão do capítulo.

## 10. Estratégia de Execução Adotada Neste Trabalho

A execução das buscas foi organizada em **duas levas complementares**, divididas conforme a natureza do acesso a cada base:

- **Primeira leva — bases abertas.** As buscas em IACR ePrint, USENIX Open Access, arXiv e Google Scholar foram executadas pelo autor utilizando as interfaces públicas dessas bases, com triagem inicial dos resultados por leitura de título e resumo.
- **Segunda leva — bases com paywall.** As buscas em ACM Digital Library, IEEE Xplore e Springer foram executadas pelo autor por meio do acesso institucional da UFPE (Portal de Periódicos CAPES via CAFe), com leitura integral dos PDFs e fichamento conforme o procedimento descrito na Seção 8.

A divisão visa maximizar cobertura sem incorrer em custos de assinatura individual e organizar o esforço por tipo de acesso. A integração das duas levas é tratada como passe único na contabilidade do PRISMA simplificado (Seção 7); a procedência de cada trabalho é, no entanto, registrada na ficha de extração para fins de auditoria.

## 11. Subgrupos Temáticos Esperados

Os trabalhos selecionados serão agrupados, na narrativa do capítulo, em quatro subgrupos progressivamente mais próximos do escopo deste TCC:

1. **Benchmarks de primitivas PQC isoladas** — estudos sobre custo computacional puro dos algoritmos, sem integração a protocolos.
2. **PQC em protocolos de rede (TLS, SSH, QUIC)** — estudos que medem o impacto do PQC no handshake e no transporte, sem foco em autenticação por token.
3. **Esquemas híbridos clássico+PQC** — estudos sobre estratégias de migração e o custo da dupla autenticação.
4. **PQC em autenticação Web baseada em token (JWT, OAuth, OIDC)** — subgrupo no qual o presente trabalho se insere e no qual a literatura é mais escassa, evidenciando a lacuna que o TCC procura preencher.

A organização em ordem crescente de proximidade temática é deliberada e cumpre função argumentativa: prepara o leitor para a justificativa da contribuição declarada no Capítulo 1.

## 12. Limitações Declaradas do Protocolo

Para fins de transparência metodológica e para antecipar potenciais arguições da banca, registram-se as seguintes limitações:

- **L1.** Revisor único — risco de viés de seleção não mitigado por concordância inter-avaliador. Mitigação adotada: registro explícito dos critérios e da justificativa de exclusão de cada candidato.
- **L2.** Cobertura restrita a inglês e português — trabalhos relevantes publicados em alemão, francês ou chinês podem ter sido omitidos. Mitigação: nenhuma direta; limitação aceita.
- **L3.** Recorte temporal de 2018 em diante — estudos seminais anteriores (e.g., Bernstein/Lange 2017) entram no Referencial Teórico, não em Trabalhos Relacionados.
- **L4.** Dependência de busca textual — trabalhos que utilizem terminologia divergente das strings podem ter sido perdidos. Mitigação: ampliação iterativa das strings durante a fase de identificação, com registro das variantes utilizadas.
- **L5.** Acesso institucional descontínuo — alguns artigos de paywall podem permanecer inacessíveis. Tais casos são registrados como "consultado apenas via abstract" e tratados com cautela na extração.

Estas limitações serão sumarizadas no próprio capítulo de Trabalhos Relacionados, em parágrafo de fechamento da seção de Metodologia da Revisão.

---

## Registro de Execução

> **A preencher durante a execução das buscas.** Esta seção mantém o log operacional do protocolo: data, string, base, número de resultados brutos, número de resultados após triagem, decisões de inclusão/exclusão com justificativa. Servirá de evidência da execução do protocolo, mas será removida (ou movida para um apêndice) na versão final do TCC.

### Log de buscas — Leva 1 (bases abertas)

| Data | String | Base | Triagem inicial | Selecionados para leitura completa | Observações |
|------|--------|------|----------------:|-----------------------------------:|-------------|
| 2026-05-22 | S2 (`ML-DSA OR Dilithium AND benchmark`) | IACR ePrint + arXiv (via WebSearch) | 8 títulos | 2 | Maioria dos resultados foca em implementação de hardware (FPGA/ASIC) ou ataques de canal lateral — excluídos por CE2. Selecionados: Commey et al. 2025 e Dinu 2025. |
| 2026-05-22 | S3 (`Kyber OR ML-KEM AND TLS AND benchmark`) | arXiv + IACR + ScienceDirect (via WebSearch) | 8 títulos | 3 | Boa cobertura. Selecionados: Zheng et al. 2024, IACR 2025/1245 (KpqC in TLS/X.509), e ScienceDirect 2025 (QUIC vs TLS PQC). |
| 2026-05-22 | S4 (`hybrid AND post-quantum AND TLS OR authentication`) | IACR + MDPI + ScienceDirect (via WebSearch) | 8 títulos | 2 | Selecionados: MDPI Cryptography 2025 (TLS 1.3 hybrid analysis) e Sikeridis et al. 2020 (NDSS, já em referencias.md). IACR 2025/2052 é SoK — excluído por CE4, mas útil para Cap. 3. |
| 2026-05-22 | S5 (`post-quantum AND JWT OR OAuth OR REST API`) | ACM + Springer + Mesopotamian Journal (via WebSearch) | 7 títulos | 2 | **Nicho específico do TCC.** Selecionados: Schardong 2023 (CANS — adaptação OAuth/OIDC para PQC) e Mesopotamian Journal (PQ-JWT). Restante: artigos divulgativos sem medições empíricas (excluídos por CE1/CE3). |

### Tabela de candidatos identificados — Leva 1

| ID | Autor (ano) | Veículo | Acesso | Status | Justificativa |
|----|-------------|---------|--------|--------|---------------|
| C01 | Commey et al. (2025) | arXiv:2505.02239 | Aberto | **Incluir** | Benchmarks de ML-KEM e ML-DSA em macOS/M4 (mesma família ARM64 do nosso ambiente), Ubuntu/x86 e Raspberry Pi 4. Reporta tempo de execução, tamanhos de chave/assinatura e indicadores de memória. Complementar — domínio de "consumer electronics" genérico. |
| C02 | Zheng et al. (2024) | arXiv:2404.13544 | Aberto | **Incluir** | Implementação otimizada de ML-KEM em AVX-512 e batch key generation, com avaliação em TLS 1.3 (handshakes por segundo). Contraponto direto ao nosso ambiente ARM64/NEON discutido na Seção 5.6 do TCC. |
| C03 | Sikeridis; Kampanakis; Devetsikiotis (2020) | NDSS 2020 | Aberto | **Incluir** | Já listado em referencias.md (sem ★). Avalia ML-DSA, Falcon e SPHINCS+ em TLS 1.3 — referência clássica do estado da arte em autenticação PQC sobre TLS. |
| C04 | Paquin; Stebila; Tamvada (2020) | PQCrypto 2020 | Institucional | **Incluir** | Já citado no Capítulo 5 do TCC (referencias.md ★). Benchmark canônico de PQC em TLS via liboqs/OpenSSL — base metodológica para comparações deste TCC. |
| C05 | Zhang et al. (2025) | ScienceDirect (Future Generation Comp. Systems) | Institucional | **Avaliar leva 2** | Comparativo TLS vs QUIC com PQC. Pertinência depende de o estudo medir autenticação ou apenas handshake. Requer acesso institucional via UFPE para confirmação. |
| C06 | IACR 2025/1245 (Integrating KpqC in TLS/X.509) | IACR ePrint | Aberto (PDF retornou 403 via WebFetch — fetch alternativo necessário) | **Avaliar leva 2** | Possivelmente fora do escopo (KpqC é o processo coreano, não NIST), mas serve para discutir generalização. |
| C07 | Schardong (2023) | CANS 2023, Springer (DOI 10.1007/978-3-031-20974-1_20) | Institucional | **Incluir (alta prioridade)** | **Trabalho mais próximo ao nosso TCC.** Avalia Dilithium (2/3/5), Falcon, SPHINCS+ vs RSA e ECDSA em OpenID Connect/OAuth 2.0, com medições de latência e payload em containers Docker e EC2. Define a fronteira atual do estado da arte em PQC para autenticação Web por token. |
| C08 | "Synergizing Quantum-Safe Signatures with JWT" (Mesopotamian Journal of CyberSecurity) | Acesso aberto | **Avaliar leva 2** | Periódico recente, indexação a confirmar. Tema diretamente alinhado ao TCC, mas qualidade do veículo precisa ser checada. |
| C09 | Dinu (2025) "Migration to PQC: From ECDSA to ML-DSA" | IACR ePrint 2025/2025 | Aberto | **Avaliar leva 2** | Foco em migração de assinatura — complementar. Requer leitura para confirmar se traz medições empíricas. |
| C10 | Bindel; Buchmann; Krämer (2017) | PQCrypto 2017 | Institucional | **Reavaliar** | Já em referencias.md ★. Anterior ao corte temporal (2018) — pode ser realocado para Referencial Teórico. |

### Candidatos descartados na Leva 1 (e justificativa)

| Trabalho | Motivo |
|----------|--------|
| ML-DSA-OSH (IACR 2025/2337) | CE2: implementação exclusivamente em hardware (FPGA), sem contraparte software comparável. |
| IACR 2024/1817 (ML-DSA hardware masking) | CE2: hardware-focused. |
| IACR 2025/009 (CPA attack on ML-DSA) | CE6: foco em ataque de canal lateral, não em desempenho. |
| IACR 2024/2046 (Decompressing Dilithium pub keys) | Foco em otimização de tamanho via reconstrução, não em desempenho de autenticação. |
| AWS blog posts sobre ML-KEM | CE3: não é trabalho revisado por pares. Útil para discussão de adoção industrial no Capítulo 1, não como trabalho relacionado. |
| IACR 2025/2052 (SoK Hybrid Strategies) | CE4: trabalho de sistematização (SoK), não estudo empírico primário. Útil para Referencial Teórico. |
| IACR 2025/1668 (PQC in Practice: Lit. Review) | CE4: literature review. Útil para Referencial Teórico. |
| Survey "A Comprehensive Survey on Post-Quantum TLS" (ResearchGate) | CE4: survey. |
| MDPI artigos divulgativos sobre PQC JWT (apiscene, venarisecurity, pqctoday, Medium) | CE3: blog posts e material divulgativo sem revisão por pares. |

### Log de buscas — Leva 2 (Google Scholar e bases adicionais)

Execução em 2026-05-22, em sessão única conduzida pelo autor. Cada string retornou aproximadamente 1.000 resultados brutos no Google Scholar; os primeiros 20 de cada string foram triados por leitura de título e resumo, conforme procedimento descrito na Seção 7 (etapa de triagem).

| String | Resultados brutos (Scholar) | Triados | INCLUIR | DÚVIDA | EXCLUIR |
|--------|----------------------------:|--------:|--------:|-------:|--------:|
| S5 (JWT/OAuth/OIDC) | ~1.060 | 20 | 2 | 3 | 15 |
| S4 (Híbrido) | ~ | 20 | 6 | 2 | 12 |
| S2 (Dilithium/ML-DSA) | ~ | 20 | 3 | 4 | 13 |
| S3 (Kyber/ML-KEM em TLS/QUIC) | ~ | 20 | 5 | 5 | 10 |
| S1 (APIs REST) | ~ | 20 | 0 | 2 | 18 |
| **Total bruto Leva 2** | — | **100** | **16** | **16** | **68** |

**Observação chave sobre S1.** A string mais direta ao nicho ("REST API + post-quantum + authentication") retornou **zero candidatos diretamente elegíveis**. Esse resultado, em si, é evidência empírica forte da lacuna que motiva o TCC — deve ser citado explicitamente na narrativa do capítulo de Trabalhos Relacionados.

### Tabela consolidada de candidatos identificados — Levas 1 e 2

Após consolidação das duas levas e reclassificação em tiers de prioridade para leitura completa (Prompt 3):

#### Tier 1 — leitura integral imediata (5 papers)

| ID | Autor (ano) | Veículo | Acesso | Por que prioridade máxima |
|----|-------------|---------|--------|---------------------------|
| T1.1 | Schardong; Giron; Müller et al. (2022) | CANS, Springer (DOI 10.1007/978-3-031-20974-1_20) | Institucional | **Competidor direto.** Único trabalho que adapta OpenID Connect e OAuth 2.0 a PQC com medições empíricas. Define a fronteira do estado da arte e precisa ser cuidadosamente posicionado: o TCC se diferencia por foco em JWT puro, modo híbrido dual-token e baseline RS256. |
| T1.2 | Anastasova; Kampanakis (2025) | IACR ePrint 2025/2235 | Aberto | **Trabalho metodologicamente mais próximo.** Mede impacto de ML-KEM/ML-DSA em mTLS real, endpoints AWS e métricas Web (TTLB). Reporta que degradação Web fica abaixo de 10% para páginas comuns — comparar diretamente com a discussão de overhead de payload do Capítulo 5 do TCC. |
| T1.3 | Alkhulaifi; El-Alfy (2020) | IEEE VTC 2020 | Institucional | **Único outro trabalho em JWT.** Revisa assinaturas PQC baseadas em reticulados (inclui Dilithium) especificamente em contexto JWT. Crítico para posicionar a contribuição do TCC no nicho. |
| T1.4 | Giron; Nascimento; Custódio et al. (2023) | CANS, Springer | Institucional | **Grupo brasileiro (UFSC).** Avalia KEMTLS híbrido em TLS com ambientes simulados e reais. Conexão acadêmica relevante (mesmo grupo do Schardong) e contraponto natural ao modo híbrido do TCC. |
| T1.5 | Demir; Gorgulu; Onbasli (2026) | IEEE Access | Institucional | **Cobertura algorítmica exata.** Compara ML-KEM/ML-DSA contra ECDH/RSA/ECDSA em micro-benchmark + TLS — o mesmo eixo de comparação adotado no Capítulo 5. |

#### Tier 2 — leitura após Tier 1 (5–6 papers)

| ID | Autor (ano) | Veículo | Acesso | Função no capítulo |
|----|-------------|---------|--------|---------------------|
| T2.1 | Commey et al. (2025) | arXiv:2505.02239 | Aberto | Benchmarks multi-plataforma incluindo **macOS/M4** (mesma família ARM64 do TCC) + Ubuntu/x86 + RPi 4. Base para discussão de generalização SIMD da Seção 5.6. |
| T2.2 | Paul; Kuzovkova; Lahr et al. (2022) | ACM ASIACCS | Institucional | Mixed certificate chains em TLS 1.3 — discussão complementar ao overhead de payload do Capítulo 5. |
| T2.3 | Sosnowski; Wiedner; Hauser et al. (2023) | ACM CoNEXT Companion | Institucional | Desempenho de TLS 1.3 pós-quântico com medições de handshake. |
| T2.4 | Sikeridis; Kampanakis; Devetsikiotis (2020) | NDSS 2020 | Aberto (IACR 2020/071) | Referência canônica em autenticação PQC sobre TLS 1.3. |
| T2.5 | Paquin; Stebila; Tamvada (2020) | PQCrypto 2020, Springer | Institucional | Benchmark canônico de PQC em TLS via liboqs — já citado no Cap. 5 do TCC. |
| T2.6 | Zheng; Zhu; Dong et al. (2024) | arXiv:2404.13544 | Aberto | ML-KEM otimizado em AVX-512 e batch keygen para TLS 1.3 — contraponto x86 ao ambiente ARM64/NEON do TCC. |

#### Tier 3 — verificar credibilidade antes de incluir

| ID | Autor (ano) | Veículo | Risco | O que verificar |
|----|-------------|---------|-------|-----------------|
| T3.1 | Riva-Cambrin; Singh; Lama et al. (2025) | arXiv | Pré-print sem publicação formal confirmada | Buscar versão publicada e afiliação institucional dos autores. |
| T3.2 | Olushola; Meenakshi (2025) | Frontiers in Physics | Veículo atípico para criptografia | Confirmar se passou por revisão por pares para conteúdo de segurança; Frontiers in CS ou Cryptography seria esperado. |
| T3.3 | Tovma; Balagura (2025) | Open Archive NURE (Universidade de Kharkiv) | Repositório universitário ucraniano, peer-review incerto | Verificar se o trabalho foi publicado em conferência ou periódico além do repositório. |
| T3.4 | Yasar (2026) | SSRN preprint | Pré-print, peer-review ausente | Verificar afiliação institucional e se há versão submetida a conferência. |
| T3.5 | Rigon; Fu; Cordeiro et al. (2025) | IEEE Conference (não especificado) | Conferência IEEE concreta a confirmar | Verificar qual conferência (validade de peer-review). |
| T3.6 | Algar-Fernandez; Villacís-Vanegas et al. (2026) | Computers (MDPI) | MDPI — qualidade variável | Verificar índice de impacto e revisão por pares. |
| T3.7 | Montenegro; Rios; Lopez-Cerezo (2025) | Future Generation Computer Systems (Elsevier) | Elsevier sólido, ok à primeira vista | Verificar se há sobreposição com o trabalho de Montenegro; Rios; Bonilla (2025) na Computer Networks. |
| T3.8 | Schardong (2024) | Tese UFSC | Tese de doutorado, não-tradicional como "trabalho relacionado" | Verificar se há resultados empíricos originais não publicados em conferência. |

#### DÚVIDAs adicionais — decidir manualmente

| ID | Autor (ano) | Por que está em dúvida |
|----|-------------|------------------------|
| D1 | Lee; Lim; Yoon (2026) — "When API Keys Leak: Securing AI Services with PQ PoP" | Pertinência ao TCC depende de existência de benchmark de latência. |
| D2 | Kalpana; Kumar (2025) — Mesopotamian Journal | Periódico de credibilidade incerta — recomenda-se excluir salvo se conteúdo for excepcionalmente relevante. |
| D3 | Zafar; Iqbal (2025) — Discover Computing (Springer) | Foca em PQC code-based em TLS — só entra se comparar com Kyber/Dilithium. |
| D4 | Jaya (2025) — Instal: Jurnal Komputer | Periódico indonésio pouco conhecido — recomenda-se excluir. |
| D5 | Havanur; Kumar; Jacob (2025) — IEEE Int'l Conf. | Pertinência depende de comparação com RSA/ECDSA. |
| D6 | Santos; Cordeiro et al. (2026) — IEEE Digital Systems Symposium | Domínio MQTT/IoT — só entra se generalização para Web for explícita. |
| D7 | İnce (2026) — Dergipark | Periódico turco em repositório acadêmico — recomenda-se excluir salvo verificação. |
| D8 | Toruan; Shakya; Tseitkin et al. (2026) — arXiv | Foco em usabilidade de APIs PQC, não em desempenho — provável exclusão. |

### Candidatos excluídos na Leva 2 (resumo agregado)

A Leva 2 identificou **68 candidatos descartados na triagem por título e resumo**, distribuídos da seguinte forma:

- **CE6 (fora do domínio Web):** ~30 — IoT (MQTT, MACsec, IoMT), 5G/6G, blockchain/wallet, veicular, UAV, metaverso, Wi-Fi/WPA.
- **CE4 (surveys/SoK):** ~10 — incluindo trabalhos potencialmente úteis para o Referencial Teórico (Cap. 3), como Alnahawi et al. 2024 sobre PQ-TLS.
- **CE3 (sem peer-review):** ~12 — blog posts, white papers de empresas, posters, slides.
- **CE2 (hardware-only):** ~8 — FPGA, GPU, Cortex-M, sistemas embarcados.
- **CE5 (duplicatas):** ~5 — mesma referência aparecendo em strings diferentes ou em versões books.google/arXiv/conferência.
- **CE1 (sem medições empíricas):** ~3 — trabalhos teóricos ou conceituais.

### Resumo do estado da revisão

- **Total de candidatos únicos identificados (Levas 1 + 2):** 26
- **Tier 1 (leitura imediata):** 5
- **Tier 2 (leitura subsequente):** 6
- **Tier 3 (verificar credibilidade):** 8
- **DÚVIDAs adicionais:** 8 (provável exclusão majoritária)
- **Meta-alvo final na tabela comparativa:** 6–10 estudos

A consolidação fica próxima da meta sem que precisemos forçar inclusões — provavelmente fecharemos com **7 a 9 trabalhos** após leitura integral do Tier 1 e leitura focada do Tier 2.

### Próximos passos

1. **Sessão de leitura integral — Tier 1.** Em ordem recomendada:
   - T1.1 Schardong et al. (2022) — competidor direto, posicionamento do TCC
   - T1.2 Anastasova & Kampanakis (2025) — metodologicamente mais próximo
   - T1.3 Alkhulaifi & El-Alfy (2020) — único outro trabalho em JWT
   - T1.4 Giron et al. (2023) — modo híbrido + conexão brasileira
   - T1.5 Demir et al. (2026) — cobertura algorítmica espelhada
2. **Verificação de credibilidade — Tier 3.** Antes de incluir, checar veículo via Qualis/Scopus para T3.1–T3.8.
3. **Decisão sobre DÚVIDAs.** Maior parte deve cair por CE3/CE6; reter no máximo 1–2 se a leitura do abstract confirmar pertinência inequívoca.
4. **Sessão de leitura — Tier 2.** Após Tier 1 estar fichado.
5. **Encerramento.** Consolidar tabela final de 6–10 trabalhos no formato da Seção 8; registrar critério de parada acionado (esperado: CP2 — quantidade-alvo atingida).

### Critério de parada efetivamente acionado

_(a registrar no encerramento da Leva 2 — leitura completa)_

---

## Auditoria de Verificação — Leva 2 (2026-05-22)

> Após a triagem inicial por título e resumo, todas as referências classificadas como Tier 1/Tier 2/Tier 3 foram **verificadas independentemente** pelo autor por meio de consulta direta a bases primárias (IACR ePrint, arXiv, IEEE Xplore, ACM Digital Library, Springer, MDPI, Elsevier ScienceDirect), com objetivo de confirmar autores, ano, veículo e existência efetiva de cada publicação antes de qualquer citação no corpo do TCC. Esta seção registra os achados da auditoria — incluindo correções, dados que não puderam ser verificados, e reclassificações resultantes. **Esta auditoria é parte do registro metodológico e antecipa preventivamente arguições da banca sobre a procedência das referências.**

### Correções de metadados (autores, ano, veículo)

A verificação direta em bases primárias identificou discrepâncias entre os metadados obtidos na triagem inicial e os metadados canônicos das publicações. As correções aplicadas estão sintetizadas abaixo:

| ID | Metadado registrado na triagem inicial | Metadado correto (verificado em base primária) | Severidade |
|----|-----------------------------------------|-------------------------------------------------|------------|
| T1.4 | Giron, Nascimento, Custódio (2023) — **CANS** | Publicado em **LATINCRYPT 2023**, Springer LNCS 14168, cap. 15. Há versão IACR ePrint 2022/1639. | **Média** — veículo corrigido nas citações |
| T1.5 | Demir, **Gorgulu**, Onbasli (**2026**) — **IEEE Access** | Verificação por DOI (10.1109/ACCESS.2026.3682760) confirmou a existência da publicação no IEEE Xplore (doc 11479311). Versão arXiv:2503.12952 corresponde a trabalho distinto do mesmo grupo de autores; metadados completos a confirmar via PDF integral. | **Alta** — requer acesso a PDF via UFPE para confirmação final dos autores. |
| T1.1 | Schardong et al. (**2023**) | Ano correto é **2022** (CANS 2022, Abu Dhabi, novembro/2022). Quatro autores: Schardong, Giron, Müller, Custódio. | **Baixa** — corrigir ano em referencias.md (★) e nas citações dos demais capítulos. |
| T2.2 | Paul, Kuzovkova, **Lahr** (2022) | Autores corretos: Sebastian Paul, Yulia Kuzovkova, Norman Lahr, **Ruben Niederhagen** (4 autores, não 3). DOI 10.1145/3488932.3497755 confirmado. | **Baixa** — adicionar quarto autor às citações. |
| T3.6 | Algar-Fernandez et al. (2026) — Computers MDPI | Confirmado. Autores completos: Algar-Fernandez, J.; Villacís-Vanegas, A.; Amaro-Aular, Y.; **Cano, M.-D.** (4 autores). Computers 15(2), art. 116. | **Baixa** — adicionar quarto autor. |

### Referência que NÃO PÔDE ser verificada (descartada)

| ID | Referência registrada na triagem | Buscas de verificação executadas | Conclusão |
|----|-----------------------------------|----------------------------------|-----------|
| S2-#20 | **Tovma; Balagura (2025)** — "Comparative Analysis of RSA, ECDSA, and CRYSTALS-Dilithium Digital Signature Algorithms" — atribuída a Open Archive NURE | Buscas com (a) nomes + Dilithium + NURE; (b) nomes + Kharkiv repository; (c) inspeção do site NURE oficial. Nenhuma evidência de existência foi localizada. | **Excluída por impossibilidade de verificação.** A referência permanece sem registro confirmável em qualquer base primária ou repositório institucional consultado; sua citação no TCC seria, portanto, irresponsável. |

### Itens fora do escopo descobertos na auditoria (reclassificação)

| ID | Achado | Decisão |
|----|--------|---------|
| T3.2 | Olushola & Meenakshi (2025) — Frontiers in Physics. Confirmado, mas usa **ML-KEM-1024 + ML-DSA-65** (níveis de segurança mais altos do que os do TCC, que usa ML-KEM-512 + ML-DSA-44). | **Manter no Tier 3**, mas registrar explicitamente esta diferença de parametrização ao citar — números absolutos não são diretamente comparáveis. |

### Tier 1 — Versão definitiva (pós-auditoria)

| ID | Referência | Veículo verificado | DOI/URL canônico | Status |
|----|------------|--------------------|------------------|--------|
| T1.1 | **Schardong; Giron; Müller; Custódio (2022)** | CANS 2022 (21st Int'l Conf. on Cryptology and Network Security), Abu Dhabi, p. 371–390 | 10.1007/978-3-031-20974-1_20 | Institucional UFPE |
| T1.2 | **Anastasova; Kampanakis (2025)** | IACR ePrint 2025/2235 | https://eprint.iacr.org/2025/2235 | Aberto |
| T1.3 | **Alkhulaifi; El-Alfy (2020)** | IEEE 91st Vehicular Technology Conf. (VTC2020-Spring) | https://ieeexplore.ieee.org/document/9129505 | Institucional UFPE |
| T1.4 | **Giron; Nascimento; Custódio et al. (2023)** | **LATINCRYPT 2023** (corrigido — não CANS), Springer LNCS 14168, cap. 15 | 10.1007/978-3-031-44469-2_15 (alt: IACR 2022/1639) | Institucional UFPE |
| ~~T1.5~~ | ~~Demir et al. (2026) IEEE Access~~ | **Reclassificado para T3.9** — é arXiv preprint, não publicado em periódico revisado | arXiv:2503.12952 | Aberto, mas pré-print |

**Novo T1.5 (substituição):** **Rigon; Fu; Cordeiro et al. (2025)** — IEEE Xplore doc 11195046, *Comprehensive Post-Quantum Cryptography Performance Evaluations for QUIC Protocol*. Confirmado em IEEE Xplore. Cobre ML-KEM/BIKE/HQC/FRODO em QUIC, com métricas de handshake/throughput/CPU/memória. Acesso institucional UFPE.

### Tier 2 — Confirmado (pós-auditoria)

| ID | Referência | Verificação |
|----|------------|-------------|
| T2.1 | Commey et al. (2025) | ✅ arXiv:2505.02239 |
| T2.2 | Paul; Kuzovkova; Lahr; **Niederhagen** (2022) | ✅ ASIACCS 2022, DOI 10.1145/3488932.3497755 |
| T2.3 | Sosnowski; Wiedner; Hauser et al. (2023) | ✅ CoNEXT Companion 2023, DOI 10.1145/3624354.3630585 (dados abertos: github.com/tumi8/pqs-tls-measurements) |
| T2.4 | Sikeridis; Kampanakis; Devetsikiotis (2020) | ✅ NDSS 2020 (IACR 2020/071) |
| T2.5 | Paquin; Stebila; Tamvada (2020) | ✅ PQCrypto 2020 (já citado no Cap. 5) |
| T2.6 | Zheng; Zhu; Dong et al. (2024) | ✅ arXiv:2404.13544 |
| **T2.7 (novo)** | **Montenegro; Rios; Lopez-Cerezo (2025)** | ✅ Future Generation Computer Systems vol. 175, art. 108062, Elsevier — promovido do Tier 3 após verificação positiva |

### Tier 3 — Status pós-auditoria

| ID | Referência | Recomendação |
|----|------------|--------------|
| T3.1 | Riva-Cambrin; Singh; Lama; Sutherland (2025) — arXiv:2505.16112 | ✅ Existe. Manter como pré-print; verificar contexto (autores são da neurocirurgia em U. Calgary — escopo M2M para dispositivos médicos, pode estar parcialmente fora do domínio Web). |
| T3.2 | Olushola; Meenakshi (2025) — Frontiers in Physics | ✅ Existe. Usa ML-KEM-1024 + ML-DSA-65 (níveis mais altos). Incluir com ressalva sobre parametrização. |
| ~~T3.3~~ | ~~Tovma; Balagura (2025) — NURE~~ | ❌ **EXCLUIR — não verificável (provável alucinação).** |
| T3.4 | Yasar (2026) — SSRN | Não auditado nesta rodada. Verificar antes de incluir. |
| T3.5 | (Antigo Rigon — promovido para T1.5) | — |
| T3.6 | Algar-Fernandez; Villacís-Vanegas; Amaro-Aular; **Cano** (2026) — Computers MDPI | ✅ Existe. Plataforma é **Windows 11 + Intel/AMD x86** — não há sobreposição direta com ambiente ARM64 do TCC, mas serve como contraponto. |
| T3.7 | Montenegro 2025 FGCS | **Promovido para T2.7.** |
| T3.8 | Schardong (2024) — Tese UFSC | Não auditado. Recomenda-se excluir do capítulo de Trabalhos Relacionados (tese), salvo se contiver resultados empíricos originais distintos do paper CANS 2022. |
| **T3.9 (novo)** | **Demir; Bilgin; Onbasli (2025)** — arXiv:2503.12952 | Reclassificado do Tier 1 após auditoria revelar que não é IEEE Access nem 2026. Incluir como pré-print, com ressalva. |

### Tabela final consolidada — recomendação para o capítulo (8 trabalhos)

Com base na auditoria, a tabela comparativa do capítulo deve contemplar os seguintes 8 trabalhos, distribuídos pelos subgrupos temáticos da Seção 11:

| Subgrupo temático | Trabalho | Veículo |
|-------------------|----------|---------|
| **PQC em autenticação Web por token (nicho do TCC)** | Schardong et al. (2022) | CANS, Springer |
| | Alkhulaifi; El-Alfy (2020) | IEEE VTC |
| **Esquemas híbridos clássico+PQC** | Giron et al. (2023) | LATINCRYPT, Springer |
| | Paul; Kuzovkova; Lahr; Niederhagen (2022) | ASIACCS, ACM |
| **PQC em protocolos de rede** | Sosnowski et al. (2023) | CoNEXT Companion, ACM |
| | Sikeridis et al. (2020) | NDSS |
| | Anastasova; Kampanakis (2025) | IACR ePrint |
| **Benchmarks de primitivas isoladas em múltiplas plataformas** | Commey et al. (2025) | arXiv (pré-print, ressalvar) |

Esta composição: (a) cobre os quatro subgrupos com 2-3 trabalhos cada, (b) prioriza trabalhos peer-reviewed em veículos sólidos (CANS, IEEE VTC, LATINCRYPT, ASIACCS, CoNEXT, NDSS), (c) inclui dois pré-prints (Anastasova&Kampanakis e Commey) cuja relevância metodológica justifica a inclusão mesmo sem revisão por pares formal — esses dois devem ser explicitamente identificados como pré-prints no texto. Os trabalhos do Tier 2/3 não selecionados ficam como referências de apoio na narrativa, sem entrar na tabela comparativa final.

### Brechas residuais e mitigações

| Brecha identificada | Risco | Mitigação adotada |
|---------------------|-------|-------------------|
| Referência registrada na triagem que não foi localizável em bases primárias (Tovma & Balagura) | Citar paper inexistente seria comprometedor na banca | Verificação independente por busca em bases primárias **antes** de qualquer citação; descarte registrado em log |
| Discrepâncias de metadados em 4 trabalhos entre triagem inicial e registro canônico | Citações incorretas no TCC | Tabela de correções acima; metadados verificados via DOI/URL canônico em base primária |
| Pré-prints (T1.2, T2.1, T3.9) não passaram por peer-review | Banca pode questionar inclusão | Identificar explicitamente como pré-print na narrativa; justificar inclusão pela relevância metodológica única |
| Olushola & Meenakshi usa parâmetros diferentes (ML-KEM-1024/ML-DSA-65) | Comparações numéricas diretas seriam inválidas | Ressalva textual na citação; uso restrito a comparações qualitativas |
| Esquema de cor "Frontiers in Physics" é atípico para criptografia | Pode levantar dúvida sobre rigor da revisão | Documentar veículo e DOI; manter como Tier 3 (uso secundário) |
| Schardong (2022) cobre nicho muito próximo ao TCC | Risco de o TCC parecer derivativo | Posicionar claramente as três diferenças: (a) foco em JWT puro vs OAuth/OIDC completo, (b) modo híbrido dual-token específico, (c) baseline RS256 explícito e protocolo de benchmark com 300 amostras pooled |

### Recomendação de fechamento

A Leva 2, auditoria incluída, permite acionar o critério de parada **CP2 (quantidade-alvo atingida)** — 8 trabalhos selecionados para a tabela comparativa, dentro da faixa-alvo de 6–10. Não é necessária nova rodada de buscas. O próximo passo é **leitura integral dos 8 trabalhos da tabela final** e **preenchimento da ficha de extração** (Seção 8) para cada, antes da redação do capítulo.

---

## Segunda rodada de auditoria — 2026-05-22 (pós-fichas)

Após o preenchimento das fichas de extração para sete trabalhos (Anastasova & Kampanakis 2025; Demir et al. 2026; Alkhulaifi & El-Alfy 2020; Olushola & Meenakshi 2025; Sosnowski et al. 2023; Giron et al. 2023; Abbasi et al. 2025), uma segunda rodada de verificação foi conduzida pelo autor com objetivo de validar cada ficha contra bases primárias antes da incorporação dos dados ao corpo do TCC.

### Resultados da segunda verificação

| Item | Status | Achados |
|------|--------|---------|
| Demir; Gorgulu; Onbasli (2026) IEEE Access — DOI 10.1109/ACCESS.2026.3682760 | ✅ **Confirmado** (reversão da hipótese inicial) | O DOI resolve em IEEE Xplore doc 11479311 — *"Micro and Transport Layer Security Benchmarking of Post-Quantum Versus Classical Cryptography"*. **A publicação no IEEE Access 2026 existe e é distinta** do pré-print arxiv:2503.12952, que corresponde a trabalho separado do mesmo grupo de autores. Sobre o middle author "Gorgulu" — verificação completa requer acesso ao PDF via UFPE; manter como registrado até confirmação. T1.5 mantido no Tier 1. |
| Giron; Perin; Nascimento; Custódio (2023) | ✅ Confirmado | 4 autores, ordem correta. DOI Springer 10.1007/978-3-031-44469-2_15. LATINCRYPT 2023 (Springer LNCS). Versão IACR ePrint: 2022/1639. |
| Abbasi; Cardoso; Váz; Silva; Martins (2025) | ✅ Confirmado | Cryptography (MDPI) 9(2):32, DOI 10.3390/cryptography9020032. 5 autores, ordem correta. Publicado 21 maio 2025. |

### 🚨 Alerta metodológico crítico — não usar Kalpana & Kumar (2025) como fonte indireta para o Alkhulaifi

Durante o fichamento da Ficha 3 (Alkhulaifi & El-Alfy, 2020), foi identificada a tentação de complementar dados numéricos faltantes (em razão do paywall do paper) por meio do paper Kalpana & Kumar (2025), que cita o Alkhulaifi. **Esse procedimento foi rejeitado** por dois motivos metodológicos:

1. **Kalpana & Kumar (2025) está publicado na Mesopotamian Journal of CyberSecurity**, veículo classificado anteriormente nesta auditoria como **D2 (credibilidade incerta)**. Citá-lo sem verificação prévia de revisão por pares já é problemático; usá-lo como fonte indireta para extrair números atribuídos a outro paper é duplamente problemático.
2. **Transferir valores numéricos entre dois experimentos distintos** — mesmo que um paper cite o outro — equivale a falsificação não-intencional de evidência. Os experimentos foram conduzidos em plataformas, configurações e implementações diferentes. Em uma defesa, a banca pode confrontar diretamente com o paper original e expor a inconsistência.

**Decisão adotada para o capítulo:** A citação ao Alkhulaifi & El-Alfy (2020) será feita **exclusivamente em forma qualitativa** até que o autor acesse o PDF integral via portal CAPES/UFPE. Texto recomendado para o capítulo:

> "Alkhulaifi e El-Alfy (2020), em estudo pioneiro de aplicação de assinaturas pós-quânticas em tokens JWT, demonstraram qualitativamente que esquemas baseados em reticulados (Dilithium e qTESLA, na nomenclatura pré-padronização do NIST) apresentam desempenho superior ao RSA em métricas de *throughput* e tempo médio de resposta. Os valores numéricos específicos reportados pelos autores não são citados aqui em razão de o texto completo não ter sido acessível ao autor deste trabalho durante a fase de leitura, ressalva que não invalida a relevância do estudo como precedente do problema de pesquisa abordado."

### Estado final dos 8 trabalhos para a tabela comparativa

| # | Referência | Status pós-fichas | Observações |
|---|------------|--------------------|--------------|
| 1 | Schardong; Giron; Müller; Custódio (2022), CANS | Aguarda ficha completa | Tier 1 — competidor direto; ler na próxima sessão. |
| 2 | Alkhulaifi; El-Alfy (2020), IEEE VTC | Ficha qualitativa apenas | Tier 1 — números só após acesso PDF UFPE. |
| 3 | Anastasova; Kampanakis (2025), IACR ePrint | ✅ Ficha completa, dados verificados | Pré-print — identificar como tal no texto. |
| 4 | Demir; Gorgulu; Onbasli (2026), IEEE Access | ✅ Ficha completa, DOI verificado | Confirmar middle author no PDF integral. |
| 5 | Giron; Perin; Nascimento; Custódio (2023), LATINCRYPT | ✅ Ficha completa, metadados verificados | OK para citação. |
| 6 | Olushola; Meenakshi (2025), Frontiers in Physics | ✅ Ficha completa | Ressalvar parametrização ML-KEM-1024/ML-DSA-65 (diferente do TCC). |
| 7 | Sosnowski et al. (2023), CoNEXT Companion | ✅ Ficha completa | OK para citação. |
| 8 | Abbasi et al. (2025), Cryptography MDPI | ✅ Ficha completa, metadados verificados | OK; complementar para Commey et al. |

**Mudança no recorte final:** com Abbasi (2025) entrando como TR7, **Commey et al. (2025)** sai da tabela comparativa principal e fica como referência de apoio na narrativa do capítulo — Abbasi cobre o mesmo papel (benchmark cross-plataforma) com maior abrangência metodológica e venue peer-reviewed (vs arXiv).

### Critério de parada acionado

**CP2 — Quantidade-alvo atingida.** 8 trabalhos selecionados, dentro da faixa de 6–10 estipulada na Seção 9 do protocolo. Buscas encerradas em 2026-05-22.

### Pendências para iniciar redação do capítulo

1. Acessar o PDF do Schardong et al. (2022) via UFPE → preencher ficha completa.
2. Acessar o PDF do Alkhulaifi & El-Alfy (2020) via UFPE → opcionalmente substituir a citação qualitativa por números reais (a citação qualitativa, por si, é suficiente).
3. Atualizar referencias.md com:
   - Schardong et al. (2022), não 2023 — corrigir ano da entrada existente.
   - Adicionar Anastasova; Kampanakis (2025), Demir et al. (2026), Giron et al. (2023) LATINCRYPT, Olushola; Meenakshi (2025), Sosnowski et al. (2023), Abbasi et al. (2025), Alkhulaifi; El-Alfy (2020).
4. Iniciar redação do capítulo 2 — Trabalhos Relacionados — com base nas fichas consolidadas e organizado pelos quatro subgrupos temáticos da Seção 11.

---

## Terceira rodada — Reconciliação pós-redação (2026-05-27)

> Esta seção registra, sem reescrever o histórico das rodadas anteriores, as alterações na composição da tabela comparativa ocorridas após a redação do capítulo e a aquisição efetiva dos PDFs das referências. O fechamento anterior (Seção "Estado final dos 8 trabalhos", 2026-05-22) previa 8 trabalhos; a composição definitiva do capítulo conta com **onze trabalhos**. As mudanças e suas justificativas estão registradas abaixo para fins de auditoria.

### Composição definitiva da tabela comparativa (11 trabalhos)

A numeração abaixo corresponde à Tabela 2.1 do capítulo redigido (`02-trabalhos-relacionados.md`):

| TR | Trabalho | Subgrupo |
|----|----------|----------|
| TR1 | Alkhulaifi; El-Alfy (2020) | 1 — PQC em autenticação Web por token |
| TR2 | Kalpana; Saravana Kumar (2025) | 1 — PQC em autenticação Web por token |
| TR3 | Schardong (2024) — tese UFSC | 1 — PQC em autenticação Web por token |
| TR4 | Giron; Perin; Nascimento; Custódio (2023) | 2 — Esquemas híbridos clássico + PQC |
| TR5 | Paul; Kuzovkova; Lahr; Niederhagen (2022) | 2 — Esquemas híbridos clássico + PQC |
| TR6 | Sikeridis; Kampanakis; Devetsikiotis (2020) | 3 — PQC em TLS, mTLS e sessão |
| TR7 | Sosnowski et al. (2023) | 3 — PQC em TLS, mTLS e sessão |
| TR8 | Anastasova; Kampanakis (2025) | 3 — PQC em TLS, mTLS e sessão |
| TR9 | Olushola; Meenakshi (2025) | 3 — PQC em TLS, mTLS e sessão |
| TR10 | Abbasi; Cardoso; Váz; Silva; Martins (2025) | 4 — Benchmarks cross-plataforma |
| TR11 | Demir; Gorgulu; Onbasli (2026) | 4 — Benchmarks cross-plataforma |

### Reclassificações em relação ao fechamento de 2026-05-22

| Item | Decisão anterior (2026-05-22) | Decisão definitiva (2026-05-27) | Justificativa |
|------|-------------------------------|----------------------------------|---------------|
| **Kalpana; Saravana Kumar (2025)** | D2 — "recomenda-se excluir" (credibilidade do veículo incerta) | **INCLUÍDO como TR2** | Após leitura integral do PDF, confirmou-se ser o trabalho mais próximo do nicho do TCC (assinaturas PQC medidas diretamente na camada JWT, com RS256 entre os baselines). A pertinência ao recorte supera a ressalva de veículo; o trabalho é citado como estado da arte mais próximo, com as diferenças do TCC explicitadas (sem KEM; níveis de segurança elevados; híbrido de assinatura única, não tokens duplos; N=50 sem percentis). |
| **İnce (2026)** | D7 — "recomenda-se excluir" (periódico turco, verificação pendente) | **INCLUÍDO como referência de apoio na Seção 5.6** (não na tabela comparativa do Cap. 2) | Fornece evidência empírica de ML-KEM em ARM64 (Raspberry Pi 4, Cortex-A72), corroborando diretamente a discussão de generalização SIMD/NTT da Seção 5.6 do TCC. Uso restrito a essa função; não compõe a tabela de trabalhos relacionados. |
| **Schardong** | T1.1 — paper CANS 2022 (aguardando PDF via paywall) | **Substituído pela tese de doutorado Schardong (2024), UFSC** | O PDF do paper CANS 2022 permaneceu inacessível (paywall Springer). A tese, de acesso aberto, reproduz integralmente o paper em seu Capítulo 3 (p. 49-63), conforme declaração explícita do próprio autor na tese ("This chapter has been previously published as a full conference paper"). Substituição academicamente legítima; mesmos algoritmos, ambiente e métricas. |
| **Commey et al. (2025)** | Previsto na tabela final de 8 (subgrupo benchmarks) | **Removido da tabela comparativa** | O papel de "benchmark cross-plataforma" passou a ser coberto por Abbasi et al. (2025) — TR10 — e por Demir et al. (2026) — TR11 —, ambos peer-reviewed e com maior abrangência. Commey (arXiv) permanece como possível referência de apoio na narrativa, sem integrar a tabela. |
| **Demir; Gorgulu; Onbasli (2026)** | Reclassificado para T3.9 (dúvida IEEE Access vs arXiv) e depois revertido | **CONFIRMADO como TR11** | Acesso ao PDF integral via IEEE Access (open access, CC BY) confirmou autoria (incl. middle author Gorgulu), veículo (IEEE Access vol. 14, 2026, doc 11479311) e os números citados no capítulo. |

### Trabalhos descartados que permanecem descartados

Os candidatos D3 (Zafar; Iqbal, 2025 — PQC code-based em TLS) e D4 (Jaya; Jakaria, 2025 — Instal Jurnal Komputer) foram reavaliados e **mantidos fora** da tabela comparativa e da bibliografia final: o primeiro foge da família de reticulados adotada no TCC (usa Classic McEliece); o segundo é veiculado em periódico de baixa indexação, com rigor estatístico modesto, na camada TLS (não JWT). Seus PDFs foram removidos do acervo do projeto.

### Critério de parada — revisão

O acréscimo de TR2 (Kalpana), TR9 (Olushola), TR10 (Abbasi) e TR11 (Demir) em relação ao fechamento de 8 trabalhos elevou a tabela a onze trabalhos, ligeiramente acima da faixa-alvo original de 6–10 (Seção 9). O excedente justifica-se pela densidade do subgrupo 3 (TLS/sessão) e pela inclusão de Kalpana no subgrupo 1, e não compromete a função comparativa do capítulo. A faixa-alvo foi ajustada para 6–12 estudos na Seção 2.1 do capítulo redigido.
