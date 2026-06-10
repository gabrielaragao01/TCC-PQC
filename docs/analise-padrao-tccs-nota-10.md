# Análise de Padrões — TCCs Nota 10 do CIn/UFPE

**Elaborado por:** Análise assistida — para uso do autor Gabriel Aragão Correia de Araújo  
**Data:** Maio de 2026  
**Finalidade:** Orientar a escrita do TCC sobre autenticação web com criptografia pós-quântica

---

## 1. PDFs Analisados

| Arquivo | Autor | Tema | Páginas | Data de Defesa |
|---------|-------|------|---------|---------------|
| `TCCMariaClaraBarretto.pdf` | Maria Clara F. G. Barretto | Aprendizado de Máquina interpretável para triagem da doença renal crônica (CKD) | ~44 | Dez/2025 |
| `TCC-Rodrigo-Barbosa-de-Oliveira.pdf` | Rodrigo Barbosa de Oliveira | Classificação de massas mamárias em mamografias digitalizadas com CNNs e Vision Transformers | 158 | Dez/2025 |
| `TCC Geydson Renan Lopes.pdf` | Geydson Renan Marques Lopes | Apoio ao diagnóstico de demências em estágios iniciais com EEG e Machine Learning | 31 | Dez/2025 |
| `TCC_UFPE___GUILHERME_LOPES_2025_2 (2).pdf` | Guilherme Lopes Rabello De Barros Correia | O impacto do unlearning na interpretabilidade de LLMs | 32 | Dez/2025 |

**Instituição comum:** Centro de Informática (CIn), Universidade Federal de Pernambuco (UFPE).  
**Curso:** Graduação em Sistemas de Informação.  
**Observação:** Nenhum trecho de texto desses TCCs foi reproduzido neste documento. Apenas padrões estruturais e estilísticos foram extraídos.

---

## 2. Padrões Encontrados

### 2.1 Estrutura Geral

Todos os três TCCs apresentam a seguinte ordem de elementos:

**Pré-textuais:**
- Capa, folha de rosto, folha de aprovação com banca (2 membros + orientador)
- Resumo em português + Abstract em inglês, com 5–6 palavras-chave em cada idioma
- Listas de figuras e tabelas (quando aplicável)
- Sumário numerado

**Textuais:**
- Introdução com subsseções numeradas
- Trabalhos Relacionados (capítulo dedicado em todos os três)
- Referencial Teórico (capítulo dedicado em dois dos três)
- Metodologia (capítulo dedicado, altamente detalhado)
- Resultados e Discussão (integrado em todos os três)
- Conclusão com subseções

**Pós-textuais:**
- Referências bibliográficas

### 2.2 Tamanho por Seção

| Seção | Geydson (31p) | Guilherme (32p) | Maria Clara (44p) | Rodrigo (158p) | Recomendado para Gabriel |
|-------|---------------|-----------------|-------------------|----------------|--------------------------|
| Resumo/Abstract | 1p | 2p | 1p | 1p | 1p |
| Introdução | 3p | 2p | 4p | 10p | 5p |
| Trabalhos Relacionados | 4p | integrado | 3p | 8p | 4p |
| Referencial Teórico | 3p | integrado (Cap. 2) | integrado | 12p | 8p |
| Metodologia | 8p | 4p | 6p | 55p* | 8p |
| Resultados e Discussão | 8p | 9p | 10p | 45p* | 10p |
| Conclusão | 2p | 2p | 4p | 5p | 3p |
| Referências | 2p | 4p | 2p | 3p | 3p |
| **Total** | **31p** | **32p** | **44p** | **158p** | **~42–45p** |

*O TCC de 158 páginas inclui implementações de código detalhadas e análise exhaustiva de múltiplos modelos (14 arquiteturas). Não é necessário para o TCC de Gabriel replicar esse volume.

**Observação sobre o Guilherme:** ele funde Trabalhos Relacionados + Referencial Teórico em um único capítulo (Cap. 2). Para um TCC focado, essa fusão é válida e produz texto mais enxuto. Para Gabriel, recomenda-se manter os dois separados (a fundamentação criptográfica de RSA, ML-DSA e Kyber tem peso próprio que justifica capítulo dedicado).

### 2.3 Introdução

Os três TCCs estruturam a introdução com subsseções numeradas, seguindo uma progressão invariável:

1. **Dado contextual / estatística** que ancora o problema no mundo real (publicações, relatórios oficiais)
2. **Apresentação do problema** que o trabalho endereça (técnico/científico)
3. **Justificativa** de por que a solução proposta é relevante agora
4. **Lacuna** na literatura que o trabalho preenche
5. **Objetivos**: geral (uma frase) + específicos (numerados, verbos no infinitivo)

Essa progressão é consistente. Nenhum TCC começa pela solução ou pela metodologia.

### 2.4 Objetivos

Padrão uniforme nos três TCCs:
- Objetivo geral: frase única com verbo no infinitivo + escopo do trabalho
- Objetivos específicos: numerados com letras (a, b, c) ou algarismos romanos entre parênteses (i, ii, iii), sempre com verbo no infinitivo: *implementar*, *avaliar*, *comparar*, *analisar*, *desenvolver*, *validar*

### 2.5 Trabalhos Relacionados

**Três dos quatro TCCs** (Maria Clara, Rodrigo, Geydson) incluem uma **tabela comparativa** de estudos. As colunas variam, mas sempre incluem: referência, contexto/abordagem, métricas ou resultados-chave, e limitação ou diferença em relação ao trabalho atual. O texto organiza os estudos por subgrupos temáticos antes da tabela e sintetiza as lacunas após.

**Exceção (Guilherme):** ele não usa tabela comparativa. Em vez disso, organiza os trabalhos relacionados em **subseções em prosa**, agrupadas por paradigma matemático ("Métodos Baseados em Alinhamento e Preferência"; "Métodos Baseados em Gradiente e Otimização"; "Métodos Baseados em Representação e Destilação"). Cada método ganha uma anatomia fixa: **nome → ideia central → função de perda formal (equação numerada) → interpretação**. Esse padrão é válido quando os trabalhos relacionados têm naturezas matemáticas muito heterogêneas, dificultando uma comparação tabular justa.

**Recomendação para Gabriel:** manter a tabela. Trabalhos sobre benchmarks PQC têm métricas comparáveis (latência, memória, payload, plataforma), favorecendo o formato tabular.

### 2.6 Referencial Teórico

Dois dos três TCCs dedicam um capítulo separado para fundamentação teórica. O padrão observado para cada conceito:
1. Definição
2. Funcionamento (sem código)
3. Relevância para o trabalho
4. Citação a fonte primária ou revisão seminal

**Nenhum dos TCCs descreve implementação de código na fundamentação teórica.** A teoria justifica as escolhas metodológicas; o código aparece apenas na metodologia.

### 2.7 Metodologia

É o capítulo mais detalhado nos quatro TCCs. Padrões observados:
- Começa com uma classificação da pesquisa (experimental, aplicada, quantitativa)
- Descreve o ambiente/dados antes de descrever os experimentos
- Usa fórmulas matemáticas **numeradas** quando pertinente (normalização, métricas, validação cruzada)
- Justifica cada decisão metodológica: "por que N=100?", "por que esse protocolo de validação?"
- Apresenta tabelas de configuração (hiperparâmetros, versões de bibliotecas, parâmetros do experimento)

**Apresentação formal de métricas (padrão Guilherme):** cada métrica é introduzida com a anatomia: definição em prosa → fórmula numerada → explicação de cada termo → relevância para o trabalho. Exemplo do TCC dele para a métrica de Spearman:
1. "Esta métrica avalia a relação monotônica entre dois ranqueamentos."
2. Fórmula com numeração (e.g., `(3.1)`).
3. "Onde $R(x_i)$ e $R(y_i)$ representam as posições (ranks) do $i$-ésimo elemento..."
4. "Uma correlação alta indica que o modelo manteve a hierarquia de importância dos tokens."

Para Gabriel: aplicar esse padrão ao apresentar CV, latência, throughput e tamanho de payload.

### 2.8 Resultados e Discussão

Padrão consistente nos quatro:
1. Apresentar tabela ou figura com resultado numérico
2. Referenciar no texto pelo número ("conforme a Tabela X" / "como ilustrado na Figura Y")
3. Texto analisa **por quê** o resultado ocorre, não apenas descreve o número
4. Compara com estudos da literatura ou com valores de referência esperados
5. Discute implicação prática

Nenhum TCC apresenta resultados apenas como dump de números. Toda tabela tem análise imediata.

**Subseções como perguntas de pesquisa (padrão Guilherme):** ele estrutura cada subseção dos Resultados como uma pergunta a ser respondida:
- "4.1 O unlearning impacta a interpretabilidade de LLM?"
- "4.2 Qual método de unlearning mais impacta a interpretabilidade?"
- "4.3 Sensibilidade de acordo com o tamanho do input"

Esse padrão torna o texto mais direto e força o autor a responder objetivamente em cada subseção. Recomenda-se adotar pelo menos nas subseções principais.

**Subseção dedicada a "Comportamentos Inesperados" (Guilherme, Seção 4.4):** achados que contrariam tendências gerais ganham espaço próprio. Inclui anomalias positivas (resultado melhor que o esperado) e negativas. Para o TCC do Gabriel, candidatos: `pqc_sign` ARM64 sub-ms vs. especificação NIST x86_64; outliers de variância em operações específicas.

**Padrão causal "anomalia → fenômeno → citação":** ao explicar um resultado anômalo, atribua-o a um fenômeno nomeado já descrito na literatura. Exemplo do Guilherme: "A degradação severa causada pelo NPO pode ser atribuída ao fenômeno de 'Reference Model Bias' identificado no trabalho de Fan et al. (2024)."

**Resultados sem tabelas, baseados em figuras (Guilherme):** o capítulo de Resultados dele tem 9 figuras e 0 tabelas — diferente dos outros três TCCs. Isso é válido quando as análises são distribucionais ou de dispersão (box plots, scatter plots, sensibilidade). Para o TCC do Gabriel, recomenda-se manter o equilíbrio tabela + figura: tabelas para latências comparativas e CV; figuras para distribuição e sensibilidade.

### 2.9 Conclusão

Os quatro TCCs dividem a conclusão em subseções explícitas:
- **Síntese dos resultados**: responde cada objetivo específico com o resultado obtido
- **Limitações**: lista explicitamente as limitações do trabalho, sem tentar escondê-las. Esse padrão parece valorizado pela banca.
- **Trabalhos futuros**: extensões naturais do trabalho

**Padrão Guilherme — concisão valorizada:** limitações agrupadas em 2 categorias ("Recursos Computacionais", "Restrições das Bibliotecas") e trabalhos futuros com apenas 2 itens numerados. Mostra que **não é necessário ser exaustivo** — é melhor poucas limitações bem contextualizadas que uma lista longa diluída.

**Frase-síntese memorável (padrão Guilherme):** a conclusão termina com uma sentença prescritiva/conceitual quotável. Exemplo dele:
> "A interpretabilidade não deve ser tratada como um componente passivo, mas como uma ferramenta ativa de auditoria."

Para Gabriel, candidato análogo:
> "PQC já é viável em desempenho para autenticação web; o obstáculo restante não é computacional, mas de tamanho de payload."

### 2.10 Figuras e Tabelas

Padrão ABNT observado nos três:
- **Tabelas**: legenda ACIMA, "Fonte: Elaborado pelo autor(a) (2025)."
- **Figuras**: legenda ABAIXO, "Fonte: Elaborado pelo autor(a) (2025)."
- Sempre referenciadas no texto antes de aparecerem
- Frequência alta na seção de Resultados: aproximadamente uma figura ou tabela por página

### 2.11 Citações e Referências

Dois estilos identificados:
- **Autor-data ABNT** (Maria Clara e Rodrigo): `(AUTOR, ANO)` ou `Autor (ANO) afirma que...`
- **Numérico** (Geydson): `[1]`, `[2]`, com lista de referências numerada ao final

O estilo autor-data é mais comum e aparece nos dois TCCs mais longos. **Recomendação para Gabriel: adotar autor-data ABNT.**

### 2.12 Tom de Escrita

Características identificadas:
- Terceira pessoa em todos os três: "o presente trabalho", "os resultados obtidos", "observa-se que"
- Linguagem precisa e mensurável: não "rápido", mas "latência média de X ms"
- Sem linguagem coloquial ou marketeira
- Parágrafos médios: 6–10 linhas. Nem muito curtos nem blocos de 20 linhas.
- Cada parágrafo tem ideia central clara

---

## 3. Aplicação ao TCC de Gabriel

### 3.1 Pontos Fortes do Projeto

O projeto de Gabriel já tem características que facilitam a escrita de um TCC nota 10:

1. **Dados reais e completos**: N=100, warmup=10, 20 operações, 3 runs independentes, 2000+ amostras brutas em CSV. Isso é metodologia rigorosa por padrão.

2. **Comparação multidimensional**: não apenas latência — também memória, tamanho de token, reprodutibilidade, validação NIST. Os TCCs nota 10 valorizam profundidade analítica.

3. **Resultado contraintuitivo**: ML-DSA-44 é mais rápido que RSA em sign (8,0× no service layer; 842× em crypto bruto). Isso é o tipo de achado que torna um TCC memorável. A banca vai querer entender por quê — o trabalho deve explicar.

4. **Modo híbrido**: capítulo natural de discussão de migração gradual, que conecta os resultados a uma aplicação prática imediata.

5. **Validação NIST (Fase 6)**: poucos TCCs de graduação comparam resultados com especificações de um órgão normativo internacional. Isso é diferencial.

### 3.2 Desafios de Escrita para Este Tema

**Desafio 1: Fundamentação teórica sem virar tutorial de código**
O referencial teórico deve explicar RSA, ML-DSA-44 e Kyber512 como algoritmos criptográficos (princípios matemáticos, segurança, parâmetros), não como classes Python ou funções de API. O código fica na metodologia, não no referencial.

**Desafio 2: Transformar números em narrativa**
A tabela de benchmark tem muitos números. A tentação é listar tudo. O padrão dos TCCs nota 10 é escolher os resultados mais significativos, explicar o porquê de cada um, e construir uma narrativa coerente sobre o que os dados revelam.

**Desafio 3: Apresentar o resultado principal com contexto adequado**
"PQC é mais rápido que RSA" é o resultado central — mas precisa de contexto: (a) em qual operação (sign é 8,0× no service layer; verify é 1,3×; keygen é 2206× em crypto bruto), (b) por qual razão técnica, (c) qual é o trade-off (token 7,4× maior), (d) o que isso significa para um sistema em produção.

**Desafio 4: Trabalhos relacionados específicos para PQC**
A literatura sobre benchmarks PQC em sistemas web de autenticação é menor que em ML/IA. É necessário buscar artigos de conferências como USENIX Security, CCS, CHES, NDSS, e também relatórios técnicos do NIST e artigos do IACR ePrint.

### 3.3 Diferencial Esperado pela Banca

Com base no que diferencia os TCCs nota 10 analisados:

1. **Tabela comparativa de trabalhos relacionados** — obrigatória
2. **Discussão de limitações explícita** — não minimizar, contextualizar
3. **Cada resultado quantitativo tem análise causal** — por que isso acontece?
4. **Conexão entre resultado e aplicação prática** — o que isso significa para desenvolvedores?
5. **Validação de reprodutibilidade** — o CV% dos 3 runs é um diferencial concreto

---

## 4. Estrutura Recomendada para o TCC de Gabriel

```
ELEMENTOS PRÉ-TEXTUAIS
  Capa
  Folha de Rosto
  Folha de Aprovação
  Resumo (PT) + Abstract (EN)
  Lista de Figuras
  Lista de Tabelas
  Sumário

1. INTRODUÇÃO (~5 páginas)
   1.1 Contexto: a ameaça dos computadores quânticos à criptografia
   1.2 Problema: gap de benchmarks práticos em autenticação web com PQC
   1.3 Justificativa: padronização NIST 2024 e urgência de migração
   1.4 Objetivos
       1.4.1 Objetivo Geral
       1.4.2 Objetivos Específicos

2. TRABALHOS RELACIONADOS (~4 páginas)
   Texto organizado por subgrupos temáticos
   Tabela 1: Síntese de estudos relacionados
   Síntese das lacunas identificadas

3. REFERENCIAL TEÓRICO (~8 páginas)
   3.1 Criptografia Assimétrica Clássica: RSA-2048 e JWT RS256
   3.2 Computação Quântica e a Ameaça à Criptografia Clássica
   3.3 Padronização NIST para Criptografia Pós-Quântica
   3.4 ML-DSA-44: Assinatura Digital Pós-Quântica
   3.5 ML-KEM-512 (Kyber512): Encapsulamento de Chave Pós-Quântico
   3.6 Autenticação Web com APIs REST
   3.7 Métricas de Desempenho para Avaliação de Algoritmos

4. METODOLOGIA (~8 páginas)
   4.1 Caracterização da Pesquisa
   4.2 Arquitetura do Sistema Implementado
   4.3 Implementação dos Modos de Autenticação
       4.3.1 Modo Clássico (RSA-2048 + JWT RS256)
       4.3.2 Modo PQC Puro (ML-DSA-44 + Kyber512)
       4.3.3 Modo Híbrido
   4.4 Protocolo de Benchmarking
       4.4.1 Configuração Experimental
       4.4.2 Medição de Memória
       4.4.3 Ambiente de Execução
       4.4.4 Validação de Reprodutibilidade
   4.5 Operações Avaliadas

5. RESULTADOS E DISCUSSÃO (~10 páginas)
   5.1 Latência das Operações Criptográficas
       5.1.1 Geração de Chaves
       5.1.2 Assinatura e Verificação
       5.1.3 Operações KEM
   5.2 Comparação Service Layer vs Raw Crypto
   5.3 Uso de Memória
   5.4 Tamanho de Tokens e Chaves
   5.5 Reprodutibilidade e Validação Estatística
   5.6 Comparação com Referências NIST
   5.7 Análise do Modo Híbrido e Viabilidade de Migração

6. CONCLUSÃO (~3 páginas)
   6.1 Síntese dos Resultados
   6.2 Limitações
   6.3 Trabalhos Futuros

REFERÊNCIAS
```

**Total estimado: 40–50 páginas.** Isso é compatível com a faixa dos TCCs analisados (31–44p para trabalhos centrados em benchmarks e comparações; o TCC de 158p é excepcionalmente longo por incluir detalhamento de 14 arquiteturas neurais).

---

## 5. Recomendações Práticas para Começar

### Ordem de Escrita Sugerida

Não comece pela introdução — ela é a última coisa que se escreve bem. Sugestão:

1. **Metodologia primeiro** (você conhece o projeto, é mais fácil começar)
2. **Resultados e Discussão** (os dados estão nos CSVs, organize e analise)
3. **Referencial Teórico** (pesquise e explique os algoritmos)
4. **Trabalhos Relacionados** (pesquise artigos, monte a tabela)
5. **Conclusão** (responde os objetivos com base nos resultados)
6. **Introdução** (agora você sabe o que o trabalho faz, justifique e posicione)
7. **Resumo** (síntese do trabalho completo)

### Primeiro Parágrafo da Introdução

Comece com um dado concreto sobre computação quântica, não com uma definição. Por exemplo: cite o progresso de qubits, o algoritmo de Shor, e por que isso ameaça RSA. Depois conecte ao problema da autenticação web. Depois à solução proposta. Esse é o padrão dos TCCs nota 10.

### Sobre Trabalhos Relacionados

Para este tema específico, busque em:
- **IACR ePrint** (iacr.org/eprint) — artigos sobre benchmarks PQC
- **NIST Reports** — relatórios do processo de padronização
- **USENIX Security / CCS / CHES** — conferências top em segurança computacional
- **Google Scholar**: "post-quantum cryptography web authentication benchmark", "ML-DSA latency", "Kyber performance TLS"

A tabela de trabalhos relacionados deve ter 6–10 estudos. Organize por: benchmarks puros de PQC → PQC em protocolos de rede → PQC em autenticação web → modo híbrido.

### Sobre o Referencial Teórico

Para ML-DSA-44 e Kyber512: cite diretamente os FIPS 203 e FIPS 204. Para RSA: cite Rivest, Shamir, Adleman (1978) ou uma referência moderna de criptografia (ex.: Boneh & Shoup, "A Graduate Course in Applied Cryptography"). Para JWT: cite RFC 7519.

Escreva cada seção do referencial como se fosse explicar para um colega de SI que sabe programar mas nunca estudou criptografia. Use matemática quando necessário, mas sempre com texto explicativo.

---

## 6. Riscos de Escrita a Evitar

### Risco 1: Resultado sem análise
Apresentar uma tabela com 20 linhas de números e passar para o próximo capítulo. **Solução**: para cada operação principal, um parágrafo de análise. Para grupos de operações similares, um parágrafo comparativo.

### Risco 2: Afirmar que PQC é "melhor" sem contexto
ML-DSA-44 é mais rápido que RSA em sign, mas o token é 7,4× maior (451 B → 3.342 B, medido no Cap. 5). **Solução**: apresentar o trade-off completo, não apenas o lado favorável.

### Risco 3: Misturar código com teoria
Colocar nomes de funções Python, imports ou código no referencial teórico. **Solução**: referencial teórico é matemática e conceitos. Código vai na metodologia, e mesmo assim de forma resumida (fluxograma ou pseudocódigo, não o código real).

### Risco 4: Limitações omitidas ou minimizadas
Escrever "os resultados são válidos para qualquer plataforma" quando foram coletados em ARM64 macOS. **Solução**: explicitar que os resultados são específicos para ARM64/Python e que validação em x86_64 é trabalho futuro.

### Risco 5: Objetivos específicos não respondidos na conclusão
Listar 5 objetivos na introdução e a conclusão não mencionar o que foi alcançado em cada um. **Solução**: a conclusão deve ter uma correspondência explícita com cada objetivo específico.

### Risco 6: Introdução muito técnica
Começar a introdução explicando como funciona o problema de Shor ou como o Kyber funciona matematicamente. **Solução**: a introdução é contextual e motivacional; os detalhes técnicos ficam no referencial teórico.

### Risco 7: Ausência de tabela comparativa de trabalhos relacionados
Descrever os trabalhos em parágrafos mas sem a tabela síntese. **Solução**: a tabela é característica dos TCCs nota 10 e ajuda a banca a visualizar o posicionamento do trabalho.

---

## Apêndice: Artefatos Disponíveis no Projeto

Para facilitar a escrita, os seguintes artefatos já existem e devem ser referenciados no TCC:

| Artefato | Localização | Uso no TCC |
|---------|------------|-----------|
| Dados brutos de benchmark | `results/raw_samples.csv` | Metodologia + Resultados |
| Estatísticas resumidas | `results/summary_stats.csv` | Tabelas de Resultados |
| Gráfico de latência (bar) | `results/latency_comparison.png` | Figura em Resultados 5.1 |
| Gráfico box plot | `results/latency_boxplot.png` | Figura em Resultados 5.1 |
| Gráfico violin | `results/latency_violin.png` | Figura em Resultados (opcional) |
| Gráfico de memória | `results/memory_comparison.png` | Figura em Resultados 5.3 |
| Gráfico de payload | `results/payload_sizes.png` | Figura em Resultados 5.4 |
| Validação inter-run | `results/multi_run/` | Figura em Resultados 5.5 |
| Relatório consolidado | `results/benchmark_report.pdf` | Referência interna |
| Comparação NIST | `docs/nist_comparison.md` | Tabela em Resultados 5.6 |
| Diário de desenvolvimento | `docs/context.md` | Referência interna (não citar diretamente) |
