# 1. Introdução

## 1.1 Contexto

A autenticação é um dos pilares da segurança em aplicações web contemporâneas. Em arquiteturas baseadas em APIs REST (*Representational State Transfer*) e microsserviços, o modelo predominante é a autenticação por token: após um login bem-sucedido, o servidor emite um token assinado que o cliente reapresenta a cada requisição subsequente, dispensando a manutenção de estado de sessão no servidor. O formato mais difundido para esse token é o JSON Web Token (JWT), especificado pela RFC 7519 (JONES; BRADLEY; SAKIMURA, 2015b), cuja variante de assinatura mais comum em produção é o RS256 — assinatura RSA com função de resumo SHA-256. A segurança desse esquema repousa, em última instância, sobre o algoritmo RSA (RIVEST; SHAMIR; ADLEMAN, 1978), cuja robustez decorre da dificuldade computacional de fatorar inteiros de grande magnitude.

Essa garantia, contudo, é condicionada ao poder computacional disponível ao atacante. Shor (1997) demonstrou que um computador quântico de escala suficiente seria capaz de resolver o problema da fatoração de inteiros — e o do logaritmo discreto — em tempo polinomial, o que tornaria vulneráveis tanto o RSA quanto a criptografia de curvas elípticas. Embora computadores quânticos com essa capacidade ainda não existam, a comunidade de segurança trata a ameaça como concreta e antecipável. O *National Institute of Standards and Technology* (NIST) reconheceu formalmente o risco em relatório técnico que recomendava o início imediato da preparação para a transição criptográfica (CHEN et al., 2016), e a própria literatura de referência consolidou a criptografia pós-quântica (PQC, do inglês *Post-Quantum Cryptography*) como agenda prioritária (BERNSTEIN; LANGE, 2017).

A urgência dessa preparação é reforçada pelo cenário conhecido como *harvest now, decrypt later*: um adversário pode interceptar e armazenar comunicações cifradas no presente para decifrá-las no futuro, quando dispuser de capacidade quântica suficiente (MOSCA, 2018). Dados sensíveis com longo prazo de confidencialidade ficam, portanto, expostos antes mesmo de o computador quântico existir, o que desloca o problema da migração de um horizonte distante para uma decisão de engenharia do presente — propriedade frequentemente designada como *crypto-agility*, isto é, a capacidade de um sistema substituir seus algoritmos criptográficos sem reescrever sua arquitetura (BINDEL et al., 2017).

Em resposta a esse cenário, o NIST conduziu, entre 2016 e 2024, um processo público de padronização de algoritmos pós-quânticos. Os primeiros padrões definitivos — publicados como *Federal Information Processing Standards* (FIPS) — vieram a público em agosto de 2024: o FIPS 203, que normatiza o mecanismo de encapsulamento de chave ML-KEM (*Module-Lattice-Based Key-Encapsulation Mechanism*), derivado do CRYSTALS-Kyber (NIST, 2024a); e o FIPS 204, que normatiza o esquema de assinatura digital ML-DSA (*Module-Lattice-Based Digital Signature Algorithm*), derivado do CRYSTALS-Dilithium (NIST, 2024b). Ambos fundamentam-se em problemas matemáticos sobre reticulados, considerados resistentes a ataques quânticos. Com a publicação desses padrões, a questão deixou de ser *se* a migração ocorrerá e passou a ser *como* conduzi-la — em particular, a que custo de desempenho nas aplicações que dela dependem.

## 1.2 Problema

A padronização dos algoritmos pós-quânticos resolveu a lacuna normativa, mas não a lacuna empírica. Apesar de os algoritmos ML-DSA-44 e ML-KEM-512 já estarem disponíveis em bibliotecas maduras, ainda são escassos os estudos que avaliam seu desempenho prático em sistemas reais de autenticação web baseada em token. A maior parte da literatura de benchmarking concentra-se no protocolo de transporte TLS (*Transport Layer Security*) — medindo o tempo de *handshake*, o tamanho de certificados ou o impacto em conexões de rede (SIKERIDIS; KAMPANAKIS; DEVETSIKIOTIS, 2020; DEMIR; GORGULU; ONBASLI, 2026) — e não a camada de aplicação na qual o token é gerado e verificado.

Soma-se a isso uma limitação metodológica recorrente: boa parte das avaliações disponíveis reporta apenas microbenchmarks, isto é, o custo da primitiva criptográfica isolada. Esse recorte, embora útil, não captura o custo agregado em nível de serviço — a latência efetiva de uma operação de login ou de verificação de token, o tamanho do token transmitido no cabeçalho HTTP (*HyperText Transfer Protocol*) e o consumo de memória no fluxo integrado de autenticação. São justamente essas grandezas que determinam a viabilidade prática da adoção por uma equipe de desenvolvimento. Adicionalmente, o modo híbrido — no qual algoritmos clássicos e pós-quânticos operam simultaneamente para permitir migração gradual — é tipicamente estudado no nível do *handshake* TLS, e não na camada de token, onde sua aplicação a cenários reais de coexistência de clientes permanece pouco explorada.

Desse conjunto de lacunas decorre a questão de pesquisa que norteia este trabalho: **como implementar autenticação pós-quântica em aplicações web reais mantendo desempenho aceitável?** Responder a essa pergunta exige não apenas implementar os algoritmos padronizados em um sistema de autenticação funcional, mas medir, em condições controladas e reprodutíveis, o custo concreto de sua adoção frente ao esquema clássico hoje dominante — o JWT RS256 sobre RSA-2048.

## 1.3 Justificativa

A relevância deste trabalho deriva, em primeiro lugar, do seu momento. A publicação dos padrões FIPS 203 e FIPS 204 em 2024 transforma a avaliação prática da criptografia pós-quântica em demanda imediata para desenvolvedores e arquitetos de software, que passam a dispor de algoritmos oficialmente recomendados, mas carecem de dados que orientem decisões de adoção em seus próprios sistemas. Sistemas de autenticação web constituem infraestrutura crítica — mediam o acesso a APIs, microsserviços e dados sensíveis —, de modo que qualquer degradação de desempenho introduzida pela migração tem impacto direto na experiência do usuário e no custo operacional.

Decisões dessa natureza não devem ser tomadas com base em suposições. A percepção difundida de que a criptografia pós-quântica seria intrinsecamente custosa precisa ser confrontada com medições empíricas conduzidas em um cenário realista de autenticação. Quando esses dados são levantados, observa-se que o principal custo da adoção não recai necessariamente sobre o tempo de processamento, mas sobre o tamanho dos artefatos transmitidos — um *trade-off* cuja correta caracterização é essencial para guiar a engenharia de protocolos de autenticação resistentes a ataques quânticos.

Por fim, o modo híbrido oferece um caminho de transição pragmático. Ao emitir simultaneamente um token clássico e um token pós-quântico, um servidor pode atender, no mesmo período de migração, tanto clientes legados quanto clientes já atualizados, sem ruptura de compatibilidade (BINDEL et al., 2017). Avaliar o custo adicional dessa estratégia é, portanto, contribuição de valor prático direto para equipes que precisam migrar sistemas em produção sem interromper sua operação. Este trabalho contribui com uma avaliação empírica, aberta e reprodutível desse espaço de decisão — um nicho ainda não coberto, de forma integrada, pela literatura consultada.

## 1.4 Objetivos

### 1.4.1 Objetivo Geral

Projetar, implementar e avaliar um sistema de autenticação web que suporte criptografia clássica, pós-quântica e híbrida, comparando seu desempenho por meio de um protocolo de benchmarking controlado e reprodutível, de modo a fornecer recomendações práticas para a adoção de algoritmos pós-quânticos em cenários de autenticação por token.

### 1.4.2 Objetivos Específicos

Para alcançar o objetivo geral, definem-se os seguintes objetivos específicos:

(i) implementar um sistema de autenticação web que integre o modo clássico (RSA-2048 com JWT RS256), o modo pós-quântico puro (assinatura ML-DSA-44 e encapsulamento de chave ML-KEM-512, ou Kyber512) e o modo híbrido de tokens duplos, segundo princípios de Clean Architecture que isolem as implementações criptográficas das demais camadas;

(ii) desenvolver um protocolo de benchmarking controlado que meça latência, consumo de memória e tamanho de payload nas três abordagens, isolando a operação criptográfica de fatores externos como entrada e saída de rede, parsing HTTP e acesso ao banco de dados;

(iii) comparar quantitativamente o desempenho dos modos clássico, pós-quântico e híbrido nas operações de login, verificação de token e troca de chaves por encapsulamento (KEM, do inglês *Key-Encapsulation Mechanism*);

(iv) avaliar a reprodutibilidade dos resultados por meio de múltiplas execuções independentes, quantificando a variabilidade inter-execução pelo coeficiente de variação;

(v) validar os resultados obtidos confrontando-os com as especificações de desempenho publicadas pelo NIST e com a literatura de benchmarks pós-quânticos.

## 1.5 Estrutura do Trabalho

Além desta introdução, o trabalho organiza-se em mais cinco capítulos. O Capítulo 2 apresenta os trabalhos relacionados, posicionando esta pesquisa frente ao estado da arte em criptografia pós-quântica aplicada a autenticação e comunicação segura, e identificando as lacunas que motivam a contribuição. O Capítulo 3 estabelece o referencial teórico, fundamentando a criptografia assimétrica clássica (RSA-2048 e JWT RS256), a ameaça quântica decorrente do algoritmo de Shor, a padronização do NIST e os algoritmos pós-quânticos avaliados (ML-DSA-44 e ML-KEM-512). O Capítulo 4 detalha a metodologia, descrevendo a arquitetura do sistema implementado, os três modos de autenticação e o protocolo de benchmarking adotado. O Capítulo 5 apresenta e discute os resultados, abrangendo latência, uso de memória, tamanho de tokens e chaves, reprodutibilidade, comparação com as referências do NIST e análise do modo híbrido. Por fim, o Capítulo 6 sintetiza as conclusões, retoma os objetivos à luz dos resultados obtidos, reconhece as limitações do estudo e aponta direções para trabalhos futuros.
