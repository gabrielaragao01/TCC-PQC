# Referência ABNT — TCC CIn/UFPE

Guia de formatação baseado nos padrões observados nos TCCs nota 10 do CIn/UFPE (Sistemas de Informação, 2025), em conformidade com ABNT NBR 14724 e NBR 6023.

---

## Formatação Física do Documento

| Elemento | Especificação |
|----------|--------------|
| Margens | Superior: 3 cm / Inferior: 2 cm / Esquerda: 3 cm / Direita: 2 cm |
| Espaçamento entre linhas | 1,5 (corpo do texto) |
| Espaçamento de parágrafos | Sem espaço adicional entre parágrafos (apenas recuo de 1,25 cm) |
| Fonte | Times New Roman 12 ou Arial 12 |
| Alinhamento | Justificado |
| Numeração de páginas | Canto superior direito, a partir da introdução |
| Recuo de parágrafo | 1,25 cm na primeira linha |
| Citação longa (> 3 linhas) | Recuo 4 cm, fonte 10, espaçamento simples, sem aspas |

**Títulos de capítulos:** MAIÚSCULAS, negrito, alinhado à esquerda, numerado.  
**Títulos de subseções:** Título Case, negrito (nível 1) ou itálico (nível 2), numerados.

---

## Elementos Pré-textuais Obrigatórios

1. **Capa** — Instituição, centro, curso, nome do autor, título, cidade, ano
2. **Folha de rosto** — igual à capa + natureza do trabalho + orientador
3. **Folha de aprovação** — banca examinadora com nome e instituição, data de defesa
4. **Resumo em português** — parágrafo único, 150–500 palavras, palavras-chave ao final
5. **Abstract** — tradução do resumo, keywords ao final
6. **Listas** — lista de figuras, lista de tabelas (se houver 3 ou mais de cada)
7. **Sumário** — com numeração de seções e páginas correspondentes

---

## Figuras

**Legenda:** ABAIXO da figura.  
**Formato:** `Figura X — Descrição em título case.`  
**Fonte:** linha abaixo da legenda, tamanho 10: `Fonte: Elaborado pelo autor (2025).`  
**Chamada no texto:** antes da figura, ex.: "como ilustrado na Figura 3" ou "conforme apresentado na Figura 5".

Exemplo:
```
[figura aqui]

Figura 3 — Arquitetura do sistema de autenticação híbrida implementado.
Fonte: Elaborado pelo autor (2025).
```

Para figura adaptada de outra fonte:
```
Fonte: Adaptado de NIST (2024).
```

---

## Tabelas

**Legenda:** ACIMA da tabela.  
**Formato:** `Tabela X — Descrição em título case.`  
**Fonte:** linha abaixo da tabela, tamanho 10: `Fonte: Elaborado pelo autor (2025).`  
**Chamada no texto:** antes da tabela.

Exemplo:
```
Tabela 2 — Latência média das operações criptográficas (N=100).

| Operação | Algoritmo | Média (ms) | P95 (ms) |
|----------|-----------|-----------|---------|
| ...      | ...       | ...       | ...     |

Fonte: Elaborado pelo autor (2025).
```

---

## Citações no Texto (ABNT NBR 10520)

### Citação Indireta (paráfrase)

```
(AUTOR, ANO)          → no final da frase
Autor (ANO)           → integrado à frase
Autor e Autor (ANO)   → dois autores
Autor et al. (ANO)    → três ou mais autores
```

Exemplos:
- A padronização de algoritmos pós-quânticos foi concluída em 2024 (NIST, 2024).
- Bernstein e Lange (2017) discutem os critérios de segurança para algoritmos resistentes a ataques quânticos.
- Chen et al. (2016) descrevem o processo de seleção de candidatos PQC promovido pelo NIST.

### Citação Direta Curta (até 3 linhas)

Entre aspas, no corpo do texto:
```
Conforme NIST (2024, p. 5), "ML-DSA is a digital signature scheme based on
the hardness of lattice problems."
```

### Citação Direta Longa (mais de 3 linhas)

Recuo de 4 cm, fonte 10, espaçamento simples, sem aspas:
```
   Conforme estabelecido pelo NIST (2024, p. 12):

      The security of ML-DSA is based on the hardness of finding short
      vectors in module lattices. This problem is believed to be hard
      for both classical and quantum computers, making ML-DSA suitable
      for post-quantum applications.
```

---

## Referências Bibliográficas (ABNT NBR 6023)

### Formato Geral

As referências ficam ao final do trabalho, em ordem alfabética, espaçamento simples com espaço duplo entre referências.

### Artigo em Periódico

```
SOBRENOME, Nome. Título do artigo. Nome do Periódico, cidade, v. X, n. Y,
p. XX–XX, mês ano.
```

Exemplo:
```
ALAGIC, Gorjan et al. Status report on the third round of the NIST
post-quantum cryptography standardization process. NIST Internal Report,
Gaithersburg, n. 8413, 2022.
```

### Artigo em Conferência (Proceedings)

```
SOBRENOME, Nome. Título do trabalho. In: NOME DA CONFERÊNCIA, n., ano, cidade.
Anais [...]. Local: Editora, ano. p. XX–XX.
```

### Padrão / Norma / Especificação Técnica (como FIPS)

```
NIST. Federal Information Processing Standard 204: Module-Lattice-Based
Digital Signature Standard (ML-DSA). Gaithersburg: National Institute of
Standards and Technology, 2024. Disponível em:
https://doi.org/10.6028/NIST.FIPS.204. Acesso em: 15 jan. 2025.

NIST. Federal Information Processing Standard 203: Module-Lattice-Based
Key-Encapsulation Mechanism Standard (ML-KEM). Gaithersburg: National
Institute of Standards and Technology, 2024. Disponível em:
https://doi.org/10.6028/NIST.FIPS.203. Acesso em: 15 jan. 2025.
```

### Livro

```
SOBRENOME, Nome. Título: subtítulo. Edição. Cidade: Editora, ano.
```

### Repositório / Software (GitHub)

```
OPEN QUANTUM SAFE. liboqs: C library for post-quantum cryptographic algorithms.
Versão 0.15.0. 2024. Disponível em: https://github.com/open-quantum-safe/liboqs.
Acesso em: XX mês 2025.
```

### Documento Online (RFC, Spec, Site)

```
JONES, M.; BRADLEY, J.; SAKIMURA, N. JSON Web Token (JWT). RFC 7519,
Internet Engineering Task Force (IETF), maio 2015. Disponível em:
https://datatracker.ietf.org/doc/html/rfc7519. Acesso em: XX mês 2025.
```

---

## Numeração de Seções

```
1 INTRODUÇÃO
1.1 Contexto
1.2 Problema
1.3 Justificativa
1.4 Objetivos
1.4.1 Objetivo Geral
1.4.2 Objetivos Específicos

2 TRABALHOS RELACIONADOS

3 REFERENCIAL TEÓRICO
3.1 Criptografia Assimétrica Clássica
3.1.1 RSA-2048
3.1.2 JWT RS256
...
```

Não existe nível além de 3 dígitos (3.4.1 é o máximo). Se precisar de mais subdivisão, use alíneas (a), b), c)) ou itens em lista.

---

## Resumo — Estrutura Recomendada

O resumo deve conter em aproximadamente 250–350 palavras:
1. Contexto e problema (1 frase)
2. Objetivo do trabalho (1 frase)
3. Metodologia resumida: o que foi implementado e como foi avaliado
4. Principais resultados com números representativos
5. Conclusão e implicações

Ao final: `Palavras-chave: criptografia pós-quântica; autenticação web; ML-DSA-44; Kyber512; benchmarking.`

---

## Abreviaturas e Siglas

- Definir na primeira ocorrência no texto: "algoritmo de Assinatura Digital Baseado em Módulo de Reticulado (ML-DSA-44)"
- Incluir lista de abreviaturas se o trabalho tiver mais de 10 siglas distintas
- Não definir novamente após a primeira vez, salvo em resumo/abstract
