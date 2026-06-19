# 2. Trabalhos Relacionados

A literatura sobre criptografia pós-quântica aplicada a sistemas reais é vasta no que diz respeito a protocolos de transporte como TLS, SSH e QUIC, mas significativamente mais escassa quando o escopo é restrito a autenticação web baseada em tokens JWT. Este capítulo identifica, organiza e discute o conjunto de estudos empíricos, publicados entre 2018 e 2026, que avaliam o desempenho dos algoritmos pós-quânticos baseados em reticulados — em particular Dilithium/ML-DSA e CRYSTALS-Kyber/ML-KEM — em contextos próximos ao adotado neste trabalho, permitindo contextualizar a proposta desta pesquisa e evidenciando as contribuições que ela busca oferecer.

## 2.1 Metodologia da Revisão

A seleção dos estudos seguiu um mapeamento sistemático leve (*lightweight systematic mapping*), em lugar de uma revisão sistemática completa nos moldes propostos por Kitchenham e Charters (2007), e foi conduzida por um único revisor — opção justificada pelo escopo de um trabalho de conclusão de curso, incompatível com a concordância inter-avaliador exigida por uma SLR completa, e pela finalidade comparativa, e não inferencial, do capítulo. A pergunta norteadora foi: quais estudos empíricos publicados entre 2018 e 2026 avaliam o desempenho de algoritmos pós-quânticos baseados em reticulados — particularmente Dilithium/ML-DSA e Kyber/ML-KEM — em contextos de autenticação ou comunicação segura na Web, comparando-os com baselines clássicos como RSA, ECDSA e ECDH?

A busca cobriu IACR ePrint, USENIX, ACM Digital Library, IEEE Xplore, Springer LNCS, arXiv (cs.CR) e, em caráter complementar, Google Scholar, combinando termos algorítmicos, de domínio (JWT, OAuth, TLS, REST, web authentication) e metodológicos (benchmark, performance, latency). Foram incluídos estudos empíricos que mediram o desempenho dos algoritmos de interesse frente a baselines clássicos, e excluídos trabalhos puramente teóricos, sem avaliação experimental ou alheios ao domínio web. Da triagem inicial de cerca de cem registros, onze atenderam aos critérios e foram organizados em quatro subgrupos temáticos, apresentados nas Tabelas 2.1 e 2.2. Cada candidato teve metadados e existência efetiva verificados em base primária antes de qualquer citação.

## 2.2 PQC em Autenticação Web por Token

Os três trabalhos deste subgrupo são os únicos da amostra a avaliar PQC especificamente em tokens de autenticação, todos com foco no JWT, e delimitam o estado da arte no nicho exato em que este TCC se insere.

Alkhulaifi e El-Alfy (2020), em estudo pioneiro, comparam Dilithium e qTESLA (Round 2 do NIST) contra o RSA na assinatura e verificação de JWTs, em aplicação Python que adota a mesma biblioteca liboqs aqui empregada. Sob teste de stress HTTP, os esquemas de reticulado mostram superioridade consistente em requisições por segundo e tempo de resposta — no nível NIST 1, o Dilithium atinge cerca de quatro vezes a vazão do RSA-3072 na assinatura. Duas defasagens, porém, separam o trabalho deste TCC: a versão avaliada do Dilithium é anterior à padronização como ML-DSA (FIPS 204, 2024), e o baseline RSA é dimensionado em 3.072 e 7.680 bits, não no RSA-2048 idiomático do RS256 em produção.

Kalpana e Saravana Kumar (2025) conduzem o estudo mais próximo deste recorte, medindo assinaturas pós-quânticas diretamente na camada do JWT. Comparam Falcon-1024, Dilithium5 e SPHINCS+-256 — além de variantes híbridas de assinatura única com Ed25519 — contra esquemas clássicos de JWT (RS256, ES256, PS256 e HS256) em protótipo sobre a pilha MERN. O presente trabalho distingue-se em quatro pontos: restringe-se a assinatura, sem mecanismo de encapsulamento de chave; emprega níveis de segurança elevados, e não o nível 2 do ML-DSA-44; adota a hibridização como assinatura única, e não como tokens duplos; e baseia-se em cinquenta amostras por configuração, sem warmup nem percentis.

Schardong (2024), em tese de doutorado, estende a discussão ao OpenID Connect e ao OAuth 2.0 completos, adaptando TLS, certificados e tokens JWT a algoritmos pós-quânticos (Dilithium, Falcon e SPHINCS+ contra RSA e ECDSA) em ambiente conteinerizado sobre Amazon EC2 multi-região. O achado central — viabilidade técnica com o custo recaindo sobre o tamanho dos artefatos — é consonante com este trabalho. Por avaliar o fluxo OIDC integralmente, contudo, o estudo não isola o JWT como unidade de medição nem testa o modo híbrido de tokens duplos.

## 2.3 Esquemas Híbridos Clássico e Pós-Quântico

Os dois trabalhos deste subgrupo investigam a hibridização no contexto do TLS, confirmando sua viabilidade técnica com custo computacional reduzido frente ao modo pós-quântico puro. Giron, Perin, Nascimento e Custódio (2023) avaliam a variante KEMTLS do TLS 1.3 com múltiplos KEMs (Kyber, Saber, NTRU) em níveis L1–L5 combinados a curvas elípticas, e mostram que a penalidade do modo híbrido é negligível em L1 e L3, crescendo de forma expressiva apenas em L5 — corroborando, em camada distinta, o achado deste TCC de que o híbrido na camada de token também tem custo desprezível. Paul, Kuzovkova, Lahr e Niederhagen (2022) tratam da hibridização na hierarquia de certificados X.509, propondo *mixed certificate chains*, e concluem que o custo dominante é o tamanho das assinaturas pós-quânticas, e não o computacional — observação alinhada à discussão de overhead de payload deste trabalho. Comum aos dois é a localização do híbrido no protocolo de transporte; nenhum aborda a camada de token, espaço ocupado por este TCC.

## 2.4 PQC em TLS e Protocolos de Sessão

Este subgrupo, o mais numeroso da revisão, reflete a maturidade da literatura sobre o impacto da PQC no protocolo TLS. Sikeridis, Kampanakis e Devetsikiotis (2020) constituem a referência canônica, avaliando Dilithium, Falcon e SPHINCS+ em TLS 1.3 e estabelecendo o patamar inicial de viabilidade em produção. Sosnowski et al. (2023) ampliam a análise para a heterogeneidade entre bibliotecas TLS (OpenSSL, BoringSSL, Rustls e WolfSSL sobre liboqs), mostrando que a latência de um mesmo algoritmo pode variar em ordem de magnitude entre implementações — observação que motiva, neste TCC, a identificação explícita da biblioteca e da versão utilizadas (liboqs 0.15.0, Seção 4.4.3). Anastasova e Kampanakis (2025) avançam para produção real, medindo ML-KEM e ML-DSA em endpoints AWS e em conexões mTLS, com degradação abaixo de 10% em redes típicas e aumento expressivo no P90 do handshake em mTLS. Olushola e Meenakshi (2025) deslocam o foco para um protocolo de sessão customizado (ML-KEM-1024 + ML-DSA-65 + AES-256-GCM), reportando latência criptográfica equivalente à do X25519; os níveis de segurança mais altos exigem ressalva na comparação de valores absolutos.

## 2.5 Benchmarks *Cross*-Plataforma de Primitivas Pós-Quânticas

Os dois trabalhos deste subgrupo oferecem o pano de fundo metodológico mais próximo do adotado aqui — benchmarks sistemáticos de primitivas isoladas, posteriormente integradas a um protocolo —, diferindo por não se restringirem à camada de autenticação Web por token. Abbasi et al. (2025) conduzem o benchmark *cross*-plataforma mais abrangente da literatura recente, avaliando múltiplos KEMs e esquemas de assinatura em três ambientes (servidor cloud, laptop e dispositivo IoT), e concluem que o Kyber é o KEM mais eficiente em tempo, memória e energia. Demir, Gorgulu e Onbasli (2026) oferecem a cobertura algorítmica mais próxima deste TCC — ML-KEM 512/768/1024 e ML-DSA 44/65/87 contra RSA-2048/3072 e curvas P-256/384/521 — em microbenchmark e handshake TLS 1.3, com três diferenças metodológicas em relação a este trabalho: ausência da camada JWT/REST, ausência de modo híbrido e plataforma x86_64 em vez de ARM64. O confronto quantitativo direto entre os números desse estudo e os resultados deste TCC é retomado na discussão do Capítulo 5.

## 2.6 Síntese Comparativa e Lacunas Identificadas

As Tabelas 2.1 e 2.2 consolidam os onze trabalhos pelos quatro subgrupos temáticos, sintetizando, para cada estudo, os algoritmos avaliados, o domínio de aplicação, a plataforma experimental, as métricas reportadas e o aspecto do espaço de avaliação que este TCC cobre e o trabalho citado não cobre. A leitura agregada da tabela revela a interseção de três lacunas que, em conjunto, delimitam o espaço de contribuição original deste trabalho.

A primeira é de camada de abstração. Sete dos onze trabalhos avaliam a criptografia pós-quântica no nível do TLS; apenas três tratam diretamente da camada de tokens (Alkhulaifi e El-Alfy, 2020; Kalpana e Saravana Kumar, 2025; Schardong, 2024). Nenhum, porém, isola o JWT como objeto exclusivo de medição com os algoritmos padronizados de menor parâmetro (ML-DSA-44 e ML-KEM-512) e o baseline RS256 sobre RSA-2048: o primeiro usa Dilithium pré-padronização (Round 2), o segundo restringe-se a assinatura em níveis elevados, sem KEM nem amostragem estatística com percentis, e o terceiro trata o JWT como um dos elementos de um fluxo OIDC mais amplo.

A segunda é de linha de base de comparação. O esquema subjacente ao RS256 (RSASSA-PKCS1-v1.5 com SHA-256) figura como baseline apenas nos dois trabalhos da camada de token — e ainda assim dimensionado em 3.072 a 7.680 bits para equiparar níveis NIST, ou diluído entre múltiplos esquemas alternativos. O RS256 sobre RSA-2048, idiomático e predominante em produção, não aparece como referência isolada em nenhum dos onze estudos. Este TCC o adota explicitamente como ponto de ancoragem que está em uso efetivo.

A terceira é de estratégia de hibridização. Quando avaliado, o modo híbrido recai sobre o transporte — KEMTLS (Giron et al., 2023), cadeias de certificado mistas (Paul et al., 2022) ou a combinação X25519 + ML-KEM no handshake (Anastasova e Kampanakis, 2025). Nenhum trabalho avalia a estratégia de tokens duplos, na qual o servidor entrega a cada autenticação um token clássico e um pós-quântico independentes — modelo particularmente relevante para migração gradual e ainda sem avaliação empírica na literatura consultada.

A interseção dessas três lacunas delimita a contribuição deste trabalho. Soma-se a ela o rigor do protocolo de benchmarking adotado — 300 amostras *pooled* a partir de três execuções independentes, com coeficiente de variação inter-execução para validação de reprodutibilidade —, nível de *disclosure* metodológico não uniformemente reportado nos trabalhos das Tabelas 2.1 e 2.2. A contribuição, em síntese, não é apresentar um algoritmo novo nem uma comparação inédita em termos absolutos, mas fechar, com método empírico reproduzível, um quadrante específico do espaço de avaliação que a literatura existente ainda deixa em aberto.

**Tabela 2.1** — Características dos trabalhos relacionados.

| # | Trabalho (ano) | Algoritmos PQC × clássicos | Domínio | Plataforma |
|------|----------------|-----------------------------|---------|------------|
| **Subgrupo 1 — PQC em autenticação Web por token** | | | | |
| TR1 | Alkhulaifi; El-Alfy (2020) | Dilithium, qTESLA (Round 2) × RSA-3072/7680 (RSASSA-PKCS1-v1.5/SHA-256, níveis NIST 1 e 3) | JWT — assinatura e verificação | Python + liboqs (wrapper) + PyCryptoDome (RSA); servidor Ubuntu 18 em VMware, Intel i7-4790K (4 núcleos), 4 GB RAM; stress test HTTP |
| TR2 | Kalpana; Saravana Kumar (2025) | Falcon-1024, Dilithium5, SPHINCS+-256 e híbridos PQC+Ed25519 × RS256, ES256, PS256, HS256 | JWT — geração e verificação de token | macOS, Intel i5; stack MERN |
| TR3 | Schardong (2024) | Dilithium (2/3/5), Falcon (512/1024), SPHINCS+ × RSA, ECDSA | OpenID Connect + OAuth 2.0 (TLS + JWT) | Docker, Amazon EC2 (multi-região) |
| **Subgrupo 2 — Esquemas híbridos clássico + pós-quântico** | | | | |
| TR4 | Giron; Perin; Nascimento; Custódio (2023) | Kyber, Saber, NTRU (L1–L5), Dilithium, Falcon — modo híbrido com curvas NIST | TLS 1.3 via KEMTLS — handshake | Go; redes simuladas 1/5/50/150 ms RTT |
| TR5 | Paul; Kuzovkova; Lahr; Niederhagen (2022) | Dilithium, Falcon, SPHINCS+ × RSA, ECDSA em *mixed certificate chains* | TLS 1.3 — hierarquia de certificados | wolfSSL 4.7.0; clientes Raspberry Pi 3 + notebook Intel i5; servidores Azure (AMD EPYC) em 3 regiões |
| **Subgrupo 3 — PQC em TLS, mTLS e protocolos de sessão** | | | | |
| TR6 | Sikeridis; Kampanakis; Devetsikiotis (2020) | Dilithium, Falcon, SPHINCS+ × RSA, ECDSA | TLS 1.3 — autenticação de servidor | Testbed real (ambiente acadêmico) |
| TR7 | Sosnowski et al. (2023) | Kyber, HQC, BIKE (KEM); Dilithium, Falcon, SPHINCS+ (SA) — incluindo modos híbridos | TLS 1.3 — handshake multi-biblioteca | TUM testbed; OpenSSL, BoringSSL, Rustls, WolfSSL via liboqs |
| TR8 | Anastasova; Kampanakis (2025) † | ML-KEM-768 (híbrido X25519+ML-KEM), ML-DSA-44/65/87 × ECDH X25519, ECDSA P-256 | TLS 1.3 e mTLS em produção AWS | nginx + OpenSSL 3.5 em AWS; medição WebPageTest.org; redes 3G/4G |
| TR9 | Olushola; Meenakshi (2025) | ML-KEM-1024 + ML-DSA-65 + AES-256-GCM × X25519, RSA-3072 | Protocolo de sessão autenticada (não TLS nativo) | Python/C; hardware *commodity*; WAN emulado ~40 ms RTT |
| **Subgrupo 4 — Benchmarks *cross*-plataforma de primitivas pós-quânticas** | | | | |
| TR10 | Abbasi; Cardoso; Váz; Silva; Martins (2025) | Kyber, NTRU, BIKE (KEM); Dilithium, Falcon (SA) × RSA-3072, ECDSA P-384, ECDHE P-256 | Microbenchmark + TLS 1.3 em 3 plataformas | liboqs 0.7.2 + OpenSSL-OQS; Server, Laptop, dispositivo IoT |
| TR11 | Demir; Gorgulu; Onbasli (2026) | ML-KEM-512/768/1024 + ML-DSA-44/65/87 × RSA-2048/3072, ECDHE/ECDSA P-256/384/521 | Microbenchmark + TLS 1.3 (*loopback*) | Intel i5-1135G7, Ubuntu 24.04 (WSL2), OpenSSL 3.5.1; N = 1.000 |

Fonte: Elaborado pelo autor (2026).

**Tabela 2.2** — Métricas avaliadas e diferenças em relação a este TCC.

| # | Trabalho (ano) | Métricas-chave | Diferencial deste TCC |
|------|----------------|----------------|------------------------|
| **Subgrupo 1 — PQC em autenticação Web por token** | | | |
| TR1 | Alkhulaifi; El-Alfy (2020) | Requisições/segundo, tempo médio de resposta | Usa Dilithium pré-NIST (Round 2); sem KEM; sem modo híbrido; baseline RS256 em RSA-3.072/7.680, não em RSA-2.048 |
| TR2 | Kalpana; Saravana Kumar (2025) | Tempo de geração/verificação de token, tamanho de header/payload | Usa níveis PQC elevados (Dilithium5/Falcon-1024), não o nível 2 (ML-DSA-44); sem KEM; híbrido como assinatura única, não tokens duplos; RS256 com RSA-4096 entre múltiplos baselines, não RSA-2048 isolado; N=50 sem percentis |
| TR3 | Schardong (2024) | Latência sob diferentes redes, payload, razão TLS/tempo total | Foco em OIDC/OAuth completo; sem modo híbrido dual-token; sem baseline RS256 isolado |
| **Subgrupo 2 — Esquemas híbridos clássico + pós-quântico** | | | |
| TR4 | Giron; Perin; Nascimento; Custódio (2023) | Latência média de handshake, *hybrid penalty* | Híbrido aplicado no handshake TLS, não na camada de token; sem JWT/REST |
| TR5 | Paul; Kuzovkova; Lahr; Niederhagen (2022) | Tempo de handshake, tamanho da cadeia de certificados | Foco em estrutura de certificados; não trata JWT, REST nem o caminho de autenticação por token |
| **Subgrupo 3 — PQC em TLS, mTLS e protocolos de sessão** | | | |
| TR6 | Sikeridis; Kampanakis; Devetsikiotis (2020) | Tempo de conclusão de handshake, throughput | Referência canônica de PQC em TLS; sem camada de token JWT nem comparação com RS256 |
| TR7 | Sosnowski et al. (2023) | Latência *black-box* e *white-box*, throughput por biblioteca | Mede heterogeneidade entre bibliotecas TLS; não há camada REST nem comparação com JWT RS256 |
| TR8 | Anastasova; Kampanakis (2025) † | Tamanho de handshake, P90 de latência, TTLB, Web metrics | Híbrido no handshake TLS/mTLS em endpoints AWS (X25519+ML-KEM-768), não na camada de token; sem JWT/REST nem baseline RS256/RSA-2048; níveis de parâmetro superiores aos deste TCC |
| TR9 | Olushola; Meenakshi (2025) | Latência criptográfica do handshake | Usa ML-KEM-1024/ML-DSA-65 — níveis mais altos do que os deste TCC; protocolo *ad hoc*, não JWT |
| **Subgrupo 4 — Benchmarks *cross*-plataforma de primitivas pós-quânticas** | | | |
| TR10 | Abbasi; Cardoso; Váz; Silva; Martins (2025) | Keygen/sign/verify (ms), handshake TLS, consumo de energia | Benchmark de primitiva e TLS; não trata camada JWT nem baseline RSA-2048 RS256 |
| TR11 | Demir; Gorgulu; Onbasli (2026) | Tempo de operação (ms), CH→END, tamanho de mensagens TLS | Cobertura algorítmica espelhada à deste TCC, mas sem JWT/REST, sem modo híbrido e em x86_64 |

Fonte: Elaborado pelo autor (2026).

> † Pré-print não submetido a revisão por pares na data de elaboração deste trabalho. Citado pela relevância metodológica de avaliar PQC em ambiente de produção real com métricas Web de usuário final, ressalva mantida explícita no texto de discussão.
