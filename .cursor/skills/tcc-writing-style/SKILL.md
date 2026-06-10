---
name: tcc-writing-style
description: Use when writing, reviewing, or improving any part of Gabriel Aragão's TCC on post-quantum cryptography authentication. Applies to: drafting chapters, transforming benchmark data into academic text, reviewing tone and structure, formatting citations, deciding section depth, or evaluating whether a section follows CIn/UFPE standards observed in nota 10 TCCs.
---

# TCC Writing Style — CIn/UFPE

## Sobre este TCC

**Autor:** Gabriel Aragão Correia de Araújo
**Curso:** Sistemas de Informação — CIn/UFPE
**Tema:** Autenticação web com criptografia pós-quântica
**Projeto:** FastAPI/Python comparando RSA-2048/JWT RS256, ML-DSA-44/Kyber512 e modo híbrido

Este guia foi construído a partir da análise de **quatro TCCs nota 10 do CIn/UFPE**, todos do curso de Sistemas de Informação, defendidos em 2025 (Maria Clara Barretto — 44p; Rodrigo Barbosa — 158p; Geydson Renan — 31p; Guilherme Lopes — 32p). Use-o toda vez que for escrever ou revisar qualquer parte do TCC.

---

## Estrutura Recomendada para Este TCC

```
Capa / Folha de Rosto / Folha de Aprovação
Resumo + Abstract
Listas de Figuras e Tabelas

1. Introdução (~5p)
   1.1 Contexto
   1.2 Problema
   1.3 Justificativa
   1.4 Objetivos
       1.4.1 Objetivo Geral
       1.4.2 Objetivos Específicos

2. Trabalhos Relacionados (~4p)
   Tabela 1: síntese de estudos (Autor | Ano | Algoritmos | Métricas | Limitações)

3. Referencial Teórico (~8p)
   3.1 Criptografia Assimétrica Clássica: RSA-2048 e JWT RS256
   3.2 Computação Quântica e a Ameaça ao RSA
   3.3 Padronização NIST para PQC (FIPS 203, FIPS 204)
   3.4 ML-DSA-44 e ML-KEM-512 (Kyber512)
   3.5 Autenticação Web com APIs REST
   3.6 Métricas de Desempenho

4. Metodologia (~8p)
   4.1 Caracterização da Pesquisa
   4.2 Arquitetura do Sistema
   4.3 Implementação dos Modos de Autenticação
       4.3.1 Modo Clássico
       4.3.2 Modo PQC Puro
       4.3.3 Modo Híbrido
   4.4 Protocolo de Benchmarking
       4.4.1 Configuração (N=100, warmup=10)
       4.4.2 Medição de Memória
       4.4.3 Ambiente de Execução
   4.5 Métricas Coletadas

5. Resultados e Discussão (~10p)
   5.1 Latência das Operações Criptográficas
   5.2 Comparação Service Layer vs Raw Crypto
   5.3 Uso de Memória
   5.4 Tamanho de Tokens e Chaves
   5.5 Reprodutibilidade (3 runs, CV%)
   5.6 Comparação com Referências NIST
   5.7 Análise do Modo Híbrido

6. Conclusão (~3p)
   6.1 Síntese dos Resultados
   6.2 Limitações
   6.3 Trabalhos Futuros

Referências
```

**Tamanho alvo**: 30–55 páginas no total, com **40–45p como ponto-doce** para este projeto. TCCs nota 10 com escopo focado fecharam em 31–32p (Geydson, Guilherme); trabalhos com mais dimensões de análise chegam a 44p (Maria Clara) ou 158p (Rodrigo, caso excepcional com 14 arquiteturas).

---

## Padrões dos TCCs Nota 10 — CIn/UFPE

### Estrutura de Capítulos

Toda introdução segue esta progressão:
1. Dado ou estatística que ancora o problema no mundo real
2. Apresentação do problema técnico/científico específico
3. Solução proposta e sua relevância
4. Lacuna que o trabalho preenche
5. Objetivos (geral + específicos com verbos no infinitivo)

Essa progressão nunca é invertida. Não comece pela solução. Comece pelo problema.

### Objetivos

- **Objetivo geral**: uma frase, verbo no infinitivo, descreve o propósito central do trabalho.
- **Objetivos específicos**: numerados com (i), (ii), (iii) ou a), b), c). Cada um é uma ação concreta com verbo no infinitivo: *implementar*, *avaliar*, *comparar*, *analisar*, *validar*.

Exemplo de objetivo específico adequado:
> (i) implementar um sistema de autenticação web com suporte a algoritmos clássicos e pós-quânticos em arquitetura de camadas;

### Trabalhos Relacionados

A **tabela comparativa** de estudos relacionados é fortemente recomendada e está presente em 3 dos 4 TCCs analisados. As colunas usuais são: Autor/Ano | Algoritmos/Abordagem | Métricas | Dataset ou Contexto | Limitação ou Diferença. O texto que precede a tabela organiza os estudos por subgrupos temáticos; o texto que segue sintetiza as lacunas que justificam este trabalho.

**Alternativa válida (caso Guilherme):** quando os trabalhos relacionados são de naturezas matemáticas heterogêneas (e.g., funções de perda diferentes, paradigmas distintos), pode-se substituir a tabela por **subseções temáticas em prosa**, agrupando os trabalhos por paradigma (e.g., "Métodos Baseados em Alinhamento e Preferência"; "Métodos Baseados em Gradiente e Otimização"; "Métodos Baseados em Representação"). Cada método ganha então uma anatomia fixa: **nome → ideia central → formulação formal (equação) → interpretação**. Para este TCC, mantenha a tabela — os trabalhos sobre benchmarks PQC têm métricas comparáveis (latência, memória, payload).

**Fusão de TR + Referencial Teórico:** dois dos quatro TCCs (Maria Clara, Guilherme) integram Trabalhos Relacionados e Referencial Teórico num só capítulo. É válido quando o referencial é curto. Para este TCC, recomenda-se manter os dois capítulos separados — a fundamentação criptográfica (RSA, ML-DSA, Kyber) tem peso próprio.

### Referencial Teórico

Não é tutorial de código nem manual de biblioteca. É fundamentação conceitual.

Para cada algoritmo ou protocolo, o padrão observado é:
1. O que é (definição e propósito)
2. Como funciona (princípio matemático ou computacional, sem implementação)
3. Por que é relevante para este trabalho (conexão explícita)
4. Referência a fonte primária ou padronização oficial

### Metodologia

Deve ser reprodutível por um leitor externo. O padrão observado:
- Iniciar com uma classificação da pesquisa (experimental, quantitativa, comparativa)
- Descrever o ambiente antes de descrever os experimentos
- Apresentar fórmulas **numeradas** quando relevantes para a medição (e.g., `(3.1)`, `(3.2)`) com interpretação imediata da notação após cada equação
- Justificar cada escolha de design: por que N=100? Por que warmup=10?

**Apresentação formal de métricas (padrão Guilherme):** ao introduzir cada métrica usada (latência, CV, throughput, etc.), siga a anatomia: **definição em prosa → fórmula numerada → explicação dos termos → relevância para o trabalho**. Exemplo:
> "O Coeficiente de Variação (CV) expressa a variabilidade relativa dos dados em relação à média, calculado por: $CV = (\sigma/\mu) \times 100$ (4.1). Onde $\sigma$ é o desvio padrão e $\mu$ é a média da amostra. Valores de CV abaixo de 10% indicam alta reprodutibilidade (LIS Academy, 2024)."

### Resultados e Discussão

Padrão observado em todos os TCCs nota 10:
1. Apresentar tabela ou figura
2. Texto imediatamente após referencia a figura/tabela pelo número
3. O texto analisa o **porquê** do resultado, não apenas descreve o número
4. Comparação com literatura ou referência teórica
5. Implicação prática ou técnica do resultado

Nunca finalize uma subseção apenas com uma tabela. Sempre analise o que os dados mostram.

**Títulos de subseção como perguntas de pesquisa (padrão Guilherme):** subseções de Resultados podem ser nomeadas como perguntas em vez de rótulos abstratos. Isso torna a leitura mais direta e força o texto a responder objetivamente. Exemplos:
- ❌ "5.1 Latência das Operações Criptográficas"
- ✅ "5.1 Qual o impacto do paradigma criptográfico na latência?"
- ❌ "5.3 Uso de Memória"
- ✅ "5.3 PQC reduz o consumo de memória em relação a RSA?"

Use este padrão pelo menos nas subseções principais; rótulos descritivos continuam válidos para subseções mais técnicas.

**Padrão de explicação causal: anomalia → fenômeno nomeado → citação.** Quando um resultado destoa do esperado, atribua-o explicitamente a um fenômeno já descrito na literatura. Exemplo do TCC do Guilherme:
> "A degradação severa causada pelo NPO pode ser atribuída ao fenômeno de 'Reference Model Bias' identificado no trabalho de Fan et al. (2024)."

Para este TCC, o `pqc_sign` ARM64 sub-ms vs. referência NIST x86_64 pode ser atribuído à **vetorização NEON do Apple Silicon** (citar referência apropriada do liboqs ou de literatura ARM).

**Subseção dedicada a "Comportamentos Inesperados".** Quando há achados que contrariam tendências gerais, dedique uma subseção própria — não esconda dentro de outra. No TCC do Guilherme isso virou a Seção 4.4 ("Comportamentos Inesperados"). Para este TCC, candidatos a essa seção são:
- `pqc_sign` ARM64 superando especificação NIST x86_64
- KEM operations com latência sub-ms apesar do overhead de FFI Python
- Variância elevada (CV inter-run) em operações específicas

**Limites de interpretação estatística com citação de autoridade.** Não afirme limites de CV ou outras métricas estatísticas de cabeça. Cite a fonte. Exemplo do Guilherme:
> "Um CV ≈ 39% é estatisticamente considerado dispersão moderada (LIS Academy, 2024)."

Para este TCC, ao classificar reprodutibilidade como "alta" (CV < 10%), cite uma fonte que estabeleça esse limiar.

### Conclusão

Padrão observado nos 4 TCCs:
- Divisão em subseções explícitas: Síntese → Limitações → Trabalhos Futuros
- Cada objetivo específico da Introdução deve ser retomado com o resultado obtido
- Limitações **agrupadas por categoria** (e.g., "Recursos Computacionais", "Restrições das Bibliotecas") — 2 a 4 categorias bastam, não precisa exaustivo
- Trabalhos Futuros **concisos**, numerados, com ações concretas (2–5 itens é suficiente)

**Frase-síntese memorável no encerramento (padrão Guilherme):** o parágrafo final da conclusão deve conter uma frase quotável que sintetize a mensagem central do trabalho, com tom prescritivo ou conceitual. Exemplo do Guilherme:
> "A interpretabilidade não deve ser tratada como um componente passivo, mas como uma ferramenta ativa de auditoria."

Para este TCC, candidatos a essa frase-síntese:
> "PQC já é viável em desempenho para autenticação web; o obstáculo restante não é computacional, mas de tamanho de payload."

Ou:
> "A migração para criptografia pós-quântica não é mais uma questão de viabilidade técnica, mas de engenharia de protocolo: o overhead computacional é negligível, mas o overhead de rede exige decisões deliberadas de design."

Escreva essa frase pensando no que você gostaria que a banca lembrasse uma semana depois da defesa.

---

## Tom Acadêmico

### Use
- Terceira pessoa: "o presente trabalho", "os resultados obtidos", "observa-se que"
- Voz passiva quando apropriado: "foram coletadas 100 amostras por operação"
- Construções analíticas: "os dados revelam", "a análise indica", "verifica-se que"
- Citações para embasar afirmações factuais
- Linguagem precisa: "latência média de 0,89 ms" em vez de "rápido"

### Evite
- Primeira pessoa: "eu implementei", "meu projeto", "analisei"
- Linguagem coloquial: "bem mais rápido", "muito legal", "super eficiente"
- Afirmações sem suporte: "PQC é melhor que RSA" sem dados
- Listas substituindo análise: não liste dados, analise-os em texto corrido
- Parágrafos de uma frase (muito fragmentados) ou de mais de 15 linhas (difíceis de ler)

---

## Como Transformar Texto Técnico em Acadêmico

### Exemplo 1: Latência

**Texto técnico (evitar):**
> O ML-DSA-44 ficou 6.6x mais rápido que o RSA no sign. Isso é bem melhor.

**Texto acadêmico (usar):**
> Os resultados indicam que o ML-DSA-44 apresentou latência média de 0,135 ms na operação de assinatura, enquanto o JWT RS256 registrou 0,89 ms — uma diferença de aproximadamente 6,6 vezes. Essa vantagem decorre da natureza da operação matemática subjacente: algoritmos baseados em reticulados, como o ML-DSA-44, operam em complexidade O(n log n), enquanto o RSA exige exponenciação modular de alto custo computacional (NIST, 2024). Na camada de serviço, essa diferença tem implicação direta na escalabilidade do sistema de autenticação.

---

### Exemplo 2: Introdução de Algoritmo

**Texto técnico (evitar):**
> O Kyber512 é um KEM que usa Module-LWE. A gente usa ele para trocar chaves simétricas de forma segura.

**Texto acadêmico (usar):**
> O ML-KEM-512, padronizado pelo NIST como FIPS 203, é um mecanismo de encapsulamento de chave (KEM) fundamentado no problema Module Learning With Errors (Module-LWE). Sua segurança repousa na dificuldade computacional de distinguir amostras LWE de amostras uniformemente aleatórias, um problema considerado intratável mesmo para computadores quânticos (NIST, 2024). No contexto deste trabalho, o ML-KEM-512 foi empregado para estabelecer canais de comunicação seguros na troca de chaves simétricas efêmeras, simulando um cenário de autenticação resistente a ataques quânticos.

---

### Exemplo 3: Resultado de Benchmark

**Texto técnico (evitar):**
> A tabela mostra que RSA keygen demorou 57ms e ML-DSA keygen foi 0.025ms. Diferença de 2200x.

**Texto acadêmico (usar):**
> A Tabela X apresenta as latências médias de geração de chaves para os algoritmos avaliados. O RSA-2048 registrou média de 57,3 ms (P95 = 89,4 ms), enquanto o ML-DSA-44 completou a mesma operação em 0,025 ms — diferença de 2.293 vezes. Essa disparidade reflete a natureza intrínseca de cada algoritmo: a segurança do RSA fundamenta-se na dificuldade de fatoração de inteiros de grande magnitude, operação de custo computacional elevado; os algoritmos baseados em reticulados, em contraste, realizam operações matriciais eficientes sobre polinômios em anéis cíclicos. Embora a geração de chaves ocorra apenas na inicialização do serviço, essa diferença torna-se crítica em cenários de rotação frequente de chaves ou autenticação de curta duração (ephemeral keys).

---

## Apresentação de Benchmarks e Métricas

### Tabelas de Latência

Estrutura recomendada:

| Operação | Algoritmo | Média (ms) | Mediana (ms) | P95 (ms) | P99 (ms) |
|----------|-----------|-----------|-------------|---------|---------|
| Sign | RSA-2048 | 0,89 | 0,81 | 1,18 | ... |
| Sign | ML-DSA-44 | 0,135 | 0,10 | 0,18 | ... |

Legenda: **Tabela X — Latência média das operações de autenticação (N=100, warmup=10).**  
Fonte: Elaborado pelo autor (2025).

### Como Discutir Métricas

Para cada operação comparada, responder no texto:
1. Qual é a diferença quantitativa? (número preciso)
2. Por que esse resultado ocorre? (causa técnica)
3. Qual a implicação prática? (para um sistema de autenticação web em produção)
4. Esse resultado é coerente com a literatura ou com a especificação NIST?

### Reprodutibilidade

A validação com 3 runs independentes deve ser apresentada com CV% (coeficiente de variação). Resultados com CV < 10% são classificados como altamente reprodutíveis. Isso deve ser explicitado no texto de resultados.

### Trade-offs

O TCC possui um resultado contraintuitivo importante: PQC é mais rápido que RSA em latência, mas os tokens PQC são 16,7× maiores. Esse trade-off deve ser central na discussão e na conclusão. Não apresente apenas o lado positivo de nenhum algoritmo.

---

## Citações e Referências

Ver `reference.md` para formato ABNT completo.

**Regras resumidas:**
- Citação indireta: `(NIST, 2024)` ou `Bernstein e Lange (2017) demonstram que...`
- Citação direta curta (até 3 linhas): entre aspas no corpo do texto, com (AUTOR, ANO, p. X)
- Citação direta longa (mais de 3 linhas): recuo de 4 cm, sem aspas, tamanho 10, com (AUTOR, ANO, p. X)
- Nunca afirme um fato técnico sem citação, exceto para resultados próprios do trabalho

**Fontes primárias para este TCC:**
- NIST FIPS 203 e FIPS 204 (padrões oficiais) — citar diretamente
- liboqs / OQS — citar o repositório e artigo de referência
- Artigos sobre benchmarks PQC em sistemas web — buscar no Google Scholar

---

## Erros Críticos a Evitar

1. **Tutorial de código na teoria**: não descreva implementação Python na fundamentação teórica. Descreva o algoritmo, não o código.

2. **Tabela sem análise**: nunca apresente tabela ou figura e passe para o próximo parágrafo sem discutir o resultado.

3. **Conclusão que repete a introdução**: a conclusão deve responder aos objetivos específicos com base nos resultados, não resumir o que foi feito.

4. **Limitações omitidas**: todos os TCCs nota 10 têm seção explícita de limitações. Ambiente ARM64 macOS, ausência de teste em x86_64 real, dataset de autenticação sintético, ausência de SPHINCS+ — liste e contextualize.

5. **Objetivos não respondidos na conclusão**: cada objetivo específico deve ser retomado na conclusão com o resultado obtido.

6. **Tom marketeiro**: "revolucionário", "a melhor solução", "supera completamente" — evite. Use linguagem mensurável.

7. **Siglas sem definição**: ML-DSA-44, KEM, JWT, PQC — defina na primeira ocorrência.

8. **Falta de chamada para figura/tabela**: toda Figura X e Tabela Y deve ser mencionada no texto antes de aparecer.

---

## Arquivos de Apoio

- `reference.md` — Formatação ABNT completa (margens, citações, referências)
- `chapter-template.md` — Templates com estrutura de cada capítulo
