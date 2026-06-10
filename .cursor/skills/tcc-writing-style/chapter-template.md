# Templates de Capítulos — TCC PQC/Autenticação Web

Templates de estrutura para cada capítulo do TCC de Gabriel Aragão. Use como guia de organização, não como texto final. Todo texto deve ser escrito com suas próprias palavras com base nos resultados reais do projeto.

---

## 1. Introdução (~5 páginas)

### 1.1 Contexto

Objetivo: ancorar o problema no mundo real. Responde: por que esse assunto importa agora?

Pontos a cobrir:
- A crescente dependência de infraestruturas digitais em sistemas de autenticação
- O avanço dos computadores quânticos e o horizonte temporal da ameaça (ex.: estimativas NIST, relatório do NCSC)
- O problema de Shor como ameaça concreta ao RSA e ao ECC
- A necessidade de migração criptográfica ("crypto-agility") antes que computadores quânticos suficientemente poderosos existam

Cite fontes primárias: NIST, NSA, documentos de padronização.

### 1.2 Problema

Objetivo: identificar a lacuna específica que este trabalho endereça.

Pontos a cobrir:
- Embora o NIST tenha padronizado algoritmos PQC em 2024 (FIPS 203, FIPS 204), existem poucos estudos que avaliam o desempenho prático desses algoritmos em sistemas reais de autenticação web
- A maioria dos benchmarks disponíveis mede operações criptográficas isoladas (microbenchmarks), não o overhead em nível de serviço (latência de API, tamanho de token, uso de memória integrado)
- O comportamento dos algoritmos PQC em modo híbrido (lado a lado com clássicos) não é amplamente estudado

### 1.3 Justificativa

Objetivo: explicar por que este trabalho é necessário e relevante agora.

Pontos a cobrir:
- Padronização NIST de 2024 torna a avaliação prática urgente para desenvolvedores
- Sistemas web de autenticação são infraestrutura crítica (APIs REST, microserviços)
- A migração para PQC deve ser informada por dados reais de desempenho
- O modo híbrido permite migração gradual sem quebrar compatibilidade

### 1.4 Objetivos

**1.4.1 Objetivo Geral**

> Projetar, implementar e avaliar um sistema de autenticação web que suporte algoritmos de criptografia clássica, pós-quântica e modo híbrido, comparando seu desempenho por meio de benchmarking controlado.

**1.4.2 Objetivos Específicos**

> (i) implementar um sistema de autenticação web com suporte a RSA-2048/JWT RS256, ML-DSA-44 e Kyber512, seguindo princípios de arquitetura limpa;
> (ii) desenvolver um protocolo de benchmarking controlado para medir latência, uso de memória e tamanho de payload nas três abordagens;
> (iii) comparar quantitativamente o desempenho dos algoritmos clássicos, pós-quânticos e híbridos em operações de login, verificação de token e troca de chaves;
> (iv) avaliar a reprodutibilidade dos resultados por meio de múltiplas execuções independentes;
> (v) validar os resultados obtidos em comparação com as especificações de desempenho publicadas pelo NIST.

---

## 2. Trabalhos Relacionados (~4 páginas)

### Estrutura

Parágrafo de abertura: contextualiza a área de pesquisa e os critérios de seleção dos trabalhos.

**Subseção ou parágrafo por grupo temático:**
- Benchmarks de algoritmos PQC (operações criptográficas isoladas)
- PQC aplicado a protocolos de rede (TLS, SSH)
- Autenticação web com algoritmos pós-quânticos
- Estudos de modo híbrido (classical + PQC)

**Tabela 1 — Síntese dos trabalhos relacionados:**

| Referência | Algoritmos | Contexto/Plataforma | Métricas | Limitação |
|-----------|-----------|-------------------|---------|----------|
| Autor (Ano) | ML-DSA-44, Kyber | TLS 1.3, ARM | Latência, throughput | Sem avaliação em nível de serviço web |
| ... | ... | ... | ... | ... |

Legenda: Tabela 1 — Síntese dos trabalhos relacionados com algoritmos pós-quânticos.
Fonte: Elaborado pelo autor (2025).

**Parágrafo final de síntese:** identifica as lacunas que justificam este trabalho. Deve conectar diretamente com os objetivos da Seção 1.4.

---

## 3. Referencial Teórico (~8 páginas)

### 3.1 Criptografia Assimétrica Clássica

**3.1.1 RSA-2048**
- Fundamento matemático: problema da fatoração de inteiros
- Estrutura: chave pública/privada, operações de sign (exponenciação com chave privada) e verify (com chave pública)
- Parâmetros de segurança: por que 2048 bits?
- Complexidade: exponenciação modular, custo O(n²) ou O(n³)

**3.1.2 JWT RS256**
- O que é JWT (JSON Web Token): estrutura header.payload.signature
- O que é RS256: RSA com SHA-256 para assinatura do JWT
- Fluxo de autenticação: geração do token no login, verificação em cada requisição
- Limitações: tamanho do token, custo de geração de chave RSA

### 3.2 Computação Quântica e a Ameaça à Criptografia Clássica

- Algoritmo de Shor: fatoração em tempo polinomial em computador quântico
- Implicação para RSA: uma chave RSA-2048 seria vulnerável com ~4000 qubits lógicos estáveis
- Estado atual: progresso em qubits, horizonte temporal estimado pela comunidade
- "Harvest now, decrypt later": motivação para migrar antes que computadores quânticos existam

### 3.3 Padronização NIST para Criptografia Pós-Quântica

- Processo de seleção: 2016–2024, múltiplas rodadas
- Categorias: KEM (encapsulamento de chave) e assinatura digital
- Padrões aprovados em 2024: FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA)
- Escopo deste trabalho: ML-DSA-44 e ML-KEM-512

### 3.4 ML-DSA-44 (Algoritmo de Assinatura)

- Base matemática: Module Learning With Errors (Module-LWE) sobre reticulados
- Família: Dilithium, renomeado para ML-DSA após padronização FIPS 204
- Variante 44: parâmetros de segurança nível 2 (equivalente a 128 bits clássico)
- Operações: KeyGen, Sign, Verify
- Estrutura do token gerado: tamanho da assinatura (~2.420 bytes)

### 3.5 ML-KEM-512 / Kyber512 (Mecanismo de Encapsulamento)

- Base matemática: Module Learning With Errors, variante para KEM
- Padronizado como FIPS 203 (ML-KEM)
- Operações: KeyGen, Encapsulate, Decapsulate
- Uso no trabalho: troca de chave simétrica efêmera (simulação de handshake PQC)
- Tamanho de chaves: chave pública ~800 bytes, ciphertext ~768 bytes

### 3.6 Autenticação Web com APIs REST

- Protocolo de autenticação baseado em token: fluxo login → token → requisições autenticadas
- Comparação com sessions: stateless vs stateful
- Considerações de segurança: tempo de expiração, rotação de chaves, tamanho do token em headers HTTP

### 3.7 Métricas de Desempenho

- **Latência**: tempo de execução de uma operação (ms). Medir com `time.perf_counter()`.
- **Memória**: pico de alocação durante a operação (bytes). Medir com `tracemalloc`.
- **Tamanho de payload**: bytes totais do token/chave/assinatura transmitido via HTTP.
- **Reprodutibilidade**: coeficiente de variação (CV%) entre múltiplas execuções. CV < 10% indica estabilidade.
- **Warmup**: iterações descartadas antes da medição para eliminar efeitos de inicialização.

---

## 4. Metodologia (~8 páginas)

### 4.1 Caracterização da Pesquisa

> Este trabalho caracteriza-se como uma pesquisa aplicada, de natureza quantitativa e com objetivo descritivo-comparativo. A abordagem experimental envolve a implementação de um sistema de autenticação web e a coleta sistemática de métricas de desempenho em condições controladas.

### 4.2 Arquitetura do Sistema Implementado

- Diagrama da arquitetura em camadas (Figura 1)
- Camadas: API → Serviço → Interfaces Criptográficas → Implementações
- Princípio de inversão de dependência: serviços dependem de interfaces (`IDigitalSignature`, `IKeyEncapsulation`), não de implementações
- Justificativa da escolha arquitetural: substituição de algoritmos sem refatoração das camadas superiores

Tabela X — Módulos do sistema implementado:
| Módulo | Responsabilidade | Arquivo principal |
|--------|-----------------|------------------|
| API Layer | Endpoints REST | `src/api/` |
| Auth Service | Lógica de autenticação | `src/auth/` |
| Crypto Interfaces | Contratos abstratos | `src/crypto/interfaces.py` |
| KEM Implementation | Kyber512 via liboqs | `src/crypto/kem/kyber.py` |
| ... | ... | ... |

### 4.3 Implementação dos Modos de Autenticação

**4.3.1 Modo Clássico**
- RSA-2048: geração de par de chaves na inicialização do serviço
- JWT RS256: assinatura do payload com chave privada RSA, verificação com chave pública
- Formato do token: estrutura JWT padrão RFC 7519

**4.3.2 Modo PQC Puro**
- ML-DSA-44: par de chaves gerado na inicialização
- Token personalizado: formato base64url (header.payload.signature codificados)
- KEM exchange: endpoint de troca de chave com Kyber512 (KeyGen → Encapsulate → Decapsulate)

**4.3.3 Modo Híbrido**
- Composição dos dois serviços anteriores via injeção de dependência
- Token duplo: JWT RS256 + token ML-DSA-44 retornados no mesmo response
- Objetivo: permitir verificação independente com cada algoritmo

### 4.4 Protocolo de Benchmarking

**4.4.1 Configuração Experimental**
- N = 100 iterações por operação
- Warmup = 10 iterações descartadas antes de cada medição
- Instrumento de timing: `time.perf_counter()` (resolução sub-milissegundo)
- Isolamento: timing envolve exclusivamente a operação criptográfica, excluindo I/O, parsing HTTP e acesso ao banco
- Estatísticas coletadas: média, mediana, desvio padrão, P95, P99

**4.4.2 Medição de Memória**
- Instrumento: `tracemalloc` (rastreamento de alocações Python)
- Passes separados: passes A (timing) e B (memória) executados em sequências independentes para evitar interferência de instrumentação
- Métrica reportada: pico de alocação (peak bytes)

**4.4.3 Ambiente de Execução**
- Plataforma: Apple Silicon ARM64, macOS 15
- Python: 3.13
- liboqs: 0.15.0 (compilado do código-fonte)
- Nota: resultados em ARM64 não são diretamente comparáveis com benchmarks x86_64 publicados, mas são validados contra especificações NIST (Seção 5.6)

**4.4.4 Validação de Reprodutibilidade**
- 3 execuções independentes com intervalo de resfriamento entre runs
- Métrica: coeficiente de variação inter-run (CV%) por operação
- Critério: CV < 10% classifica a operação como altamente reprodutível

### 4.5 Operações Avaliadas

Tabela X — Operações avaliadas e seus contextos:

| Operação | Algoritmo | Nível | Descrição |
|----------|-----------|-------|-----------|
| jwt_sign | RSA-2048 | Service | Geração de token JWT no login |
| jwt_verify | RS256 | Service | Verificação de token em requisição autenticada |
| pqc_sign | ML-DSA-44 | Service | Geração de token PQC no login |
| pqc_verify | ML-DSA-44 | Service | Verificação de token PQC |
| kem_keygen | Kyber512 | Service | Geração de par de chaves KEM |
| kem_encapsulate | Kyber512 | Service | Encapsulamento de chave simétrica |
| kem_decapsulate | Kyber512 | Service | Decapsulamento |
| raw_rsa_keygen | RSA-2048 | Raw | Geração de chave RSA pura |
| raw_rsa_sign | RSA-2048 | Raw | Assinatura RSA pura (sem JWT encoding) |
| ... | ... | ... | ... |

---

## 5. Resultados e Discussão (~10 páginas)

> **Opção de estilo (padrão Guilherme):** considerar nomear cada subseção como uma **pergunta de pesquisa** em vez de rótulo descritivo. Exemplos:
> - "5.1 Qual o impacto do paradigma criptográfico na latência?"
> - "5.3 PQC reduz o consumo de memória em relação a RSA?"
> - "5.5 Os resultados são reprodutíveis entre execuções independentes?"
>
> Use perguntas pelo menos nas subseções principais. Mantém o leitor focado no que está sendo respondido.

### 5.1 Latência das Operações Criptográficas

**5.1.1 Geração de Chaves**

Tabela X — Latência de geração de chaves.

Texto: discutir a diferença entre RSA keygen (~57 ms) e ML-DSA-44 keygen (~0,025 ms). Explicar a causa técnica (fatoração de primos grandes vs. operações em reticulados). Implicação para rotação de chaves em produção.

**5.1.2 Operações de Assinatura e Verificação**

Tabela X — Latência de sign/verify na camada de serviço.

Texto: discutir que PQC é mais rápido em sign (contra-intuitivo). Explicar por quê. Discutir que verify é mais próximo entre os dois algoritmos (RSA verify com expoente público pequeno é intrinsecamente rápido).

Figura X — Gráfico de barras comparativo (sign e verify, RSA vs ML-DSA-44).

**5.1.3 Operações KEM**

Tabela X — Latência das operações Kyber512.

Texto: discutir que KEM operations são sub-milissegundo (~0,009–0,010 ms). Implicação para uso em handshake de sessão.

### 5.2 Comparação Service Layer vs Raw Crypto

- Raw crypto mede o algoritmo puro; service layer inclui encoding base64url, construção do token, etc.
- Tabela comparativa dos dois níveis
- Discussão: overhead do encoding é relevante ou negligível?

### 5.3 Uso de Memória

Tabela X — Pico de memória por operação (tracemalloc).

Texto: qual operação consome mais memória? O RSA keygen aloca mais que ML-DSA-44? Qual a implicação para ambientes de alta concorrência?

### 5.4 Tamanho de Tokens e Chaves

Tabela X — Tamanho em bytes dos elementos transmitidos:
| Elemento | Tamanho |
|----------|---------|
| JWT RS256 token | ~200 bytes |
| ML-DSA-44 token | ~3.343 bytes |
| Kyber512 public key | ~800 bytes |
| Kyber512 ciphertext | ~768 bytes |

Texto: o principal trade-off de PQC não é velocidade, é tamanho. Discutir impacto em headers HTTP, latência de rede, CDN caching. Para 1000 requisições autenticadas por segundo, qual é a diferença de banda?

### 5.5 Reprodutibilidade e Validação Estatística

Tabela X — CV% por operação nas 3 runs independentes.

Texto: quantas operações ficaram com CV < 10%? Quais foram exceções? Por quê? (ex.: pqc_sign tem outliers sub-milissegundo em ARM64).

### 5.6 Comparação com Referências NIST

Tabela X — Latência local (ARM64 Python) vs referência NIST (C, x86_64).

Texto: os resultados ARM64 com liboqs Python são mais rápidos que a referência NIST em C/x86_64 para ML-DSA-44 sign. Isso é coerente com a arquitetura NEON do Apple Silicon. Não invalida a comparação; valida que a implementação funciona corretamente.

### 5.7 Análise do Modo Híbrido

Tabela X — Latência do modo híbrido vs modos individuais.

Texto: o modo híbrido soma aproximadamente as latências de cada algoritmo. Qual é a latência total de um login híbrido? É aceitável para uma API web? Discutir a estratégia de migração: hoje híbrido, amanhã PQC puro.

### 5.8 Comportamentos Inesperados

Subseção dedicada a achados que contrariam tendências gerais ou expectativas iniciais. Para cada anomalia, aplicar o padrão **observação → fenômeno nomeado → citação**.

Candidatos a discutir:

- **PQC mais rápido que referência NIST**: `pqc_sign` ARM64 sub-milissegundo apesar de o NIST publicar referências em ciclos x86_64. Atribuir à vetorização NEON do Apple Silicon (citar liboqs benchmarks ARM ou documentação NIST sobre dependência de plataforma).
- **KEM operations sub-milissegundo apesar de FFI Python**: Kyber512 KeyGen, Encapsulate e Decapsulate completam em ~0,01 ms apesar do overhead esperado de chamadas via `ctypes`/`oqs-python`. Discutir a relação entre operações curtas e custo amortizado de FFI.
- **CV inter-run elevado em operações específicas**: se alguma operação ficar com CV > 10%, atribuir explicitamente à natureza do algoritmo (e.g., RSA keygen tem variância intrínseca por testes de primalidade probabilísticos).

Exemplo de texto seguindo o padrão:
> "A operação `pqc_sign` apresentou latência de 0,135 ms em ambiente ARM64, valor inferior ao reportado pela referência NIST x86_64 (0,217 ms). Esse comportamento pode ser atribuído à vetorização SIMD via instruções NEON do Apple Silicon, descrita em [REF], que permite a paralelização de operações de Number-Theoretic Transform (NTT) sobre coeficientes polinomiais. O achado reforça que as latências reportadas pelo NIST representam um limite superior conservador para implementações em hardware moderno."

---

## 6. Conclusão (~3 páginas)

### 6.1 Síntese dos Resultados

Retomar cada objetivo específico com o resultado obtido:

> O objetivo (i) foi atendido mediante a implementação de um sistema em FastAPI com Clean Architecture, suportando três modos de autenticação: clássico (RSA-2048/JWT RS256), PQC puro (ML-DSA-44/Kyber512) e híbrido.

> O objetivo (ii) foi atendido com o desenvolvimento de um protocolo de benchmarking com N=100 iterações, warmup=10, timing por `perf_counter()` e memória por `tracemalloc`, coletando 20 métricas distintas.

> O objetivo (iii) revelou que... [resultado central: PQC mais rápido em sign, trade-off no tamanho do token]

> O objetivo (iv) foi confirmado: 19 de 20 operações apresentaram CV < 10% entre as 3 execuções independentes.

> O objetivo (v) foi validado: os resultados ARM64 são coerentes com as especificações NIST e apresentaram desempenho superior à referência C/x86_64 na operação de assinatura ML-DSA-44.

**Frase-síntese final (padrão Guilherme):** encerre a subseção 6.1 com uma sentença prescritiva ou conceitual quotável que sintetize a mensagem central do trabalho. Pense no que você gostaria que a banca lembrasse uma semana depois da defesa.

Candidatos para este TCC:

> "PQC já é viável em desempenho para autenticação web; o obstáculo restante não é computacional, mas de tamanho de payload."

Ou:

> "A migração para criptografia pós-quântica não é mais uma questão de viabilidade técnica, mas de engenharia de protocolo: o overhead computacional é negligível, mas o overhead de rede exige decisões deliberadas de design."

Ou:

> "Os resultados desafiam a narrativa de que PQC custa caro em desempenho: na latência de assinatura, o ML-DSA-44 é mais rápido que o RSA; o preço é pago em bytes transmitidos, não em ciclos de CPU."

### 6.2 Limitações

Agrupar por **categoria** (2–4 categorias bastam; não precisa ser exaustivo — padrão Guilherme). Sugestão:

**Plataforma de execução.** Os resultados foram coletados em ambiente ARM64 (Apple Silicon, macOS). Embora consistentes com as especificações NIST, não são diretamente generalizáveis para servidores x86_64 em produção. Validação em hardware de produção (cloud x86_64, processadores ARM de servidor como AWS Graviton) é trabalho futuro.

**Cenário de carga.** Os benchmarks medem operações isoladas em condições controladas. O comportamento sob alta concorrência (workers asyncio, múltiplas requisições simultâneas) não foi avaliado. Throughput HTTP foi medido em piloto, mas não incluído nos benchmarks formais por ser dominado pelo bcrypt (~100 ms), mascarando o custo do algoritmo criptográfico.

**Escopo de algoritmos.** A avaliação cobre apenas RSA-2048, ML-DSA-44 e Kyber512 (ML-KEM-512). SPHINCS+/SLH-DSA (FIPS 205) foi excluído devido ao tamanho de assinatura (8–50 KB) que inviabiliza uso em JWT padrão. Variantes de maior nível de segurança (ML-DSA-65, ML-DSA-87, Kyber768, Kyber1024) não foram avaliadas.

**Análise de segurança.** O trabalho foca em desempenho funcional; ataques de canal lateral (timing, cache, energia) sobre a implementação `liboqs` não foram analisados.

### 6.3 Trabalhos Futuros

- Avaliar o mesmo protocolo em servidor x86_64 bare-metal e nuvem pública
- Medir throughput HTTP em cenários de alta concorrência (asyncio, workers múltiplos)
- Investigar estratégias de compressão de tokens PQC para reduzir o overhead de rede
- Estender o modo híbrido para suportar TLS 1.3 com extensões PQC (pq-kem-combiner)
- Avaliar desempenho com FIPS 205 (SLH-DSA) como alternativa de assinatura
- Produzir um guia de migração passo a passo para equipes que usam JWT RS256 em produção
