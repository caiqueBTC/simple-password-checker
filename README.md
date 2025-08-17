## Verificador de Força Bruta e feedback de senha em Python

Este repositório contém um script de linha de comando, desenvolvido em Python, que analisa a força de uma senha fornecida pelo usuário. O programa verifica critérios de segurança e oferece uma estimativa do tempo necessário para quebrar a senha por meio de um ataque de força bruta.
Aviso Importante

Este script realiza cálculos matemáticos para estimar a força de uma senha. Para senhas extremamente longas (com centenas de caracteres), o número de combinações possíveis pode se tornar tão grande que excede os limites computacionais de um programa padrão, podendo gerar um erro de OverflowError. Isso não representa um risco para a sua máquina ou sistema operacional, mas é uma demonstração prática dos limites da computação ao lidar com números astronomicamente grandes. O script é leve e seguro para uso em qualquer computador pessoal.
Funcionalidades

    Análise de Critérios: Verifica se a senha atende aos seguintes requisitos:

        Comprimento mínimo de 8 caracteres.

        Presença de letras minúsculas (a-z).

        Presença de letras maiúsculas (A-Z).

        Presença de números (0-9).

        Presença de caracteres especiais (ex: !@#$%).

    Classificação de Força: Classifica a senha como Forte, Média ou Fraca, com base no número de critérios atendidos.

    Estimativa de Tempo para Quebra: Calcula e exibe o tempo estimado que um computador de alta performance (assumindo 10 bilhões de tentativas por segundo) levaria para adivinhar a senha.

Instruções de Uso

    Pré-requisitos:

        É necessário ter o Python 3 instalado no sistema.

    Execute o script:

        Abra um terminal, navegue até o diretório onde o arquivo verificadorDeSenha.py está localizado e execute o seguinte comando:

        python3 verificadorDeSenha.py

    Teste uma senha:

        O programa solicitará a inserção de uma senha. Após digitá-la e pressionar Enter, a análise completa será exibida no terminal.

Metodologia da Estimativa

A estimativa de tempo para quebra é baseada no conceito de entropia de senha, uma medida logarítmica da sua imprevisibilidade. A entropia, medida em bits, quantifica o quão difícil é adivinhar uma senha. O cálculo segue as seguintes etapas:

    Determinação do Conjunto de Caracteres (N): A força de uma senha cresce exponencialmente com o tamanho do "conjunto" de caracteres possíveis. O script identifica os tipos de caracteres presentes e calcula o tamanho total deste conjunto (N):

        Letras minúsculas (a-z): +26 possibilidades

        Letras maiúsculas (A-Z): +26 possibilidades

        Números (0-9): +10 possibilidades

        Símbolos comuns: +32 possibilidades
        Uma senha que utiliza todos os tipos tem um conjunto de N = 94 caracteres possíveis para cada posição.

    Cálculo de Combinações Totais: O número total de combinações que um invasor precisaria testar é N^L, onde L é o comprimento (length) da senha. Cada caractere adicional multiplica o número total de combinações pelo tamanho do conjunto (N). Isso demonstra que aumentar o comprimento da senha é o fator mais impactante para a sua segurança, devido ao crescimento exponencial.

    Estimativa de Tempo: O total de combinações é dividido por uma taxa de tentativas por segundo. O valor de 10 bilhões (10^10) de tentativas por segundo foi escolhido como uma estimativa realista e conservadora para um ataque dedicado. Sistemas modernos de quebra de senhas, utilizando múltiplos arrays de GPUs (Unidades de Processamento Gráfico) de alta performance, podem alcançar e até superar essa marca, especialmente para algoritmos de hash mais simples. O resultado da divisão é então convertido para um formato legível (minutos, dias, anos, etc.).

Exemplos de Análise
Senha Fraca

    Exemplo: 12345678

    Análise: Esta senha atende ao critério de comprimento, mas falha em todos os outros. Ela utiliza apenas um tipo de caractere (números), resultando em um conjunto de caracteres muito pequeno (N = 10). O total de combinações é 10^8, ou 100 milhões, um número trivial para um computador.

    Saída do Script:

    Resultado: Senha Fraca
    Tempo estimado para quebra: Instantaneamente

Senha Média

    Exemplo: Senha123

    Análise: Uma melhoria significativa. Utiliza um conjunto de N = 26+26+10 = 62 caracteres. O total de combinações é 62^8, um número consideravelmente maior, mas ainda vulnerável a ataques dedicados.

    Saída do Script:

    Resultado: Senha Média
    Tempo estimado para quebra: 2.1 segundos

Senha Forte

    Exemplo: Tr@v!nha@2025

    Análise: Esta senha é excelente. Com 14 caracteres e utilizando todos os quatro tipos de caracteres (N = 94), o número de combinações possíveis (94^14) torna um ataque de força bruta muito mais demorado.

    Saída do Script:

    Resultado: Senha Forte
    Tempo estimado para quebra: 4.2 séculos

Senha Praticamente Inquebrável

    Exemplo: MeuC@chorroG0staDeP@oComOvo!

    Análise: Este é um exemplo de uma "passphrase" (frase-senha). Seu grande comprimento (L = 31), combinado com o uso de todos os tipos de caracteres (N = 94), eleva o número de combinações possíveis (94^31) a um nível astronômico.

    Saída do Script:

    Resultado: Senha Forte
    Tempo estimado para quebra: Milênios (praticamente inquebrável)

    Neste nível, o tempo necessário para testar todas as combinações excede a idade do universo, tornando a quebra por força bruta uma impossibilidade prática com a tecnologia atual e previsível.
