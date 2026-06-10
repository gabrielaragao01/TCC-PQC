# LISTA DE FIGURAS

| | | |
|---|---|---:|
| Figura 4.1 | Organização em camadas do sistema de autenticação implementado | p. — |
| Figura 5.1 | Latência média das operações de assinatura e verificação na camada de serviço | p. — |

# LISTA DE TABELAS

| | | |
|---|---|---:|
| Tabela 2.1 | Síntese comparativa dos trabalhos relacionados | p. — |
| Tabela 4.1 | Componentes do ambiente experimental | p. — |
| Tabela 4.2 | Operações criptográficas avaliadas no protocolo experimental | p. — |
| Tabela 5.1 | Latência da geração de pares de chaves no nível de primitiva (raw crypto) | p. — |
| Tabela 5.2 | Latência das operações de assinatura e verificação no nível de serviço | p. — |
| Tabela 5.3 | Latência das operações Kyber512 no nível de serviço | p. — |
| Tabela 5.4 | Comparação entre o nível de serviço e a primitiva criptográfica isolada | p. — |
| Tabela 5.5 | Pico de alocação de memória por operação (tracemalloc, peak bytes) | p. — |
| Tabela 5.6 | Tamanho dos elementos transmitidos via rede | p. — |
| Tabela 5.7 | Coeficiente de variação inter-run das operações avaliadas | p. — |
| Tabela 5.8 | Comparação ML-DSA-44 (Dilithium2): este trabalho versus referência NIST | p. — |
| Tabela 5.9 | Comparação Kyber512: este trabalho versus referência NIST | p. — |
| Tabela 5.10 | Comparação entre modos isolados e modo híbrido na camada de serviço | p. — |

# LISTA DE QUADROS

| | | |
|---|---|---:|
| Quadro A.1 | Fluxo de seleção dos trabalhos relacionados | p. — |
| Quadro A.2 | Trabalhos selecionados para a tabela comparativa | p. — |

# SUMÁRIO

| Seção | Título | Página |
|-------|--------|-------:|
| **1** | **INTRODUÇÃO** | p. — |
| 1.1 | Objetivos | |
| **2** | **TRABALHOS RELACIONADOS** | p. — |
| 2.1 | Metodologia da Revisão | |
| 2.2 | PQC em Autenticação Web por Token | |
| 2.3 | Esquemas Híbridos Clássico e Pós-Quântico | |
| 2.4 | PQC em TLS e Protocolos de Sessão | |
| 2.5 | Benchmarks Cross-Plataforma de Primitivas Pós-Quânticas | |
| 2.6 | Síntese Comparativa | |
| 2.7 | Síntese das Lacunas Identificadas | |
| **3** | **REFERENCIAL TEÓRICO** | p. — |
| 3.1 | Criptografia Assimétrica Clássica: RSA-2048 e JWT RS256 | |
| 3.1.1 | RSA-2048 | |
| 3.1.2 | JSON Web Token e o esquema RS256 | |
| 3.2 | Computação Quântica e a Ameaça à Criptografia Clássica | |
| 3.3 | Padronização NIST para Criptografia Pós-Quântica | |
| 3.4 | ML-DSA-44: Assinatura Digital Pós-Quântica | |
| 3.5 | ML-KEM-512 (Kyber512): Encapsulamento de Chave Pós-Quântico | |
| 3.6 | Autenticação Web com APIs REST | |
| 3.7 | Métricas de Desempenho | |
| **4** | **METODOLOGIA** | p. — |
| 4.1 | Caracterização da Pesquisa | |
| 4.2 | Arquitetura do Sistema Implementado | |
| 4.3 | Implementação dos Modos de Autenticação | |
| 4.3.1 | Modo Clássico (RSA-2048 + JWT RS256) | |
| 4.3.2 | Modo PQC Puro (ML-DSA-44 + Kyber512) | |
| 4.3.3 | Modo Híbrido | |
| 4.4 | Protocolo de Benchmarking | |
| 4.4.1 | Configuração Experimental | |
| 4.4.2 | Medição de Memória | |
| 4.4.3 | Ambiente de Execução | |
| 4.4.4 | Validação de Reprodutibilidade | |
| 4.5 | Operações Avaliadas | |
| 4.6 | Ameaças à Validade | |
| 4.6.1 | Validade Interna | |
| 4.6.2 | Validade Externa | |
| 4.6.3 | Validade de Construto | |
| **5** | **RESULTADOS E DISCUSSÃO** | p. — |
| 5.1 | Latência das Operações Criptográficas | |
| 5.1.1 | Geração de Chaves | |
| 5.1.2 | Operações de Assinatura e Verificação | |
| 5.1.3 | Operações KEM | |
| 5.2 | Comparação Service Layer vs Raw Crypto | |
| 5.3 | Uso de Memória | |
| 5.4 | Tamanho de Tokens e Chaves | |
| 5.5 | Reprodutibilidade e Validação Estatística | |
| 5.6 | Comparação com Referências NIST | |
| 5.7 | Análise do Modo Híbrido | |
| **6** | **CONCLUSÃO** | p. — |
| 6.1 | Síntese dos Resultados | |
| 6.2 | Limitações | |
| 6.3 | Trabalhos Futuros | |
| | **REFERÊNCIAS** | p. — |
| | **APÊNDICE A — PROTOCOLO DA REVISÃO DE LITERATURA** | p. — |
