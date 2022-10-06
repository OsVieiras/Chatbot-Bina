frases = {
    'inventario_insuficiente': 'Sem mais vidas.',
    'erro': 'Desculpe, não entendi.'
}

estados = {
    0: {
        'frases': ['Digite "iniciar" para começar o jogo e "reiniciar", caso queira voltar ao início.'],
        'proximos_estados': {
            '[iI]nicia(r)*': 1
        },
        
    },
    1: {
        'frases': ['Olá! Eu sou Bina seu robô assistente. Você foi "sugado" para dentro do seu computador enquanto trabalhava em um código. Minha missão é ajudá-lo a sair de dentro da máquina e para isso você terá 3 opções de saída: impressora, monitor ou alto-falante, mas primeiro preciso saber como você foi sugado. Para me responder você terá sempre de fazer conversões decimais-binárias, pois meu interpretador está danificado. A resposta deverá ter 8 bits (00000000) sendo ela o respectivo valor em binário da opção (X) escolhida. OPÇÃO (10) = teclado, OPÇÃO (15) = mouse, OPCÃO (20) = microfone.'],
        'proximos_estados': {
            '00001010': 2,
            '00001111': 3,
            '00010100': 4,
            '[rR]einicia(r)*': 1 
        },
        'inventario': {}
    },
    2: {
        'frases': ['Certo, como você foi sugado pro computador pelo teclado, eu recomendo sair do PC pela impressora, se desejar seguir esse rumo, OPCÃO (12) = sair pela impressora, caso não queira "reiniciar".'],
        'proximos_estados': {
            '00001100': 5,
            '[rR]einicia(r)*': 1
        },
        'inventario': {}
    },
    3: {
        'frases': ['Certo, como você foi sugado pro computador pelo mouse, eu recomendo sair do PC pelo monitor, se desejar seguir esse rumo, OPÇÃO (19) = sair pelo monitor, caso não queira "reiniciar".'],
        'proximos_estados': {
            '00010011': 6,
            '[rR]einicia(r)*': 1
        },
        'inventario': {}       
    },
    4: {
        'frases': ['Certo, como você foi sugado pro computador pelo microfone, eu recomendo sair do PC pelo alto-falante, se desejar seguir esse rumo, OPÇÃO (21) = sair pelo alto-falante, caso não queira "reiniciar".'],
        'proximos_estados': {
            '00010101': 7,
            '[rR]einicia(r)*': 1
        },
        'inventario': {}
    },
    5: {
        'frases': ['Certo! Seguiremos o nosso caminho em direção a impressora, por aqui nós enfrentaremos alguns problemas. Nosso primeiro desafio será enfrentrar um trânsito de bits que estão seguindo rumo ao processador, temos que decodificar algumas sequências binárias que por ventura vierem em nossa direção, assim, nenhum dado será perdido por não ter conseguido chegar ao processador. Devemos fazer isso para não corrermos o risco de ser enviados para a assitência técnica por estar apresentando problemas, e acabar sendo formatados/apagados para sempre. OPÇÃO (27) = seguir.'],
        'proximos_estados': {
            '00011011': 8,
            '[rR]einicia(r)*': 1
        },
        'inventario': {}
    },

    6: {
        'frases': ['Certo! Seguiremos o nosso caminho em direção ao monitor, por aqui nós enfrentaremos alguns problemas. Nosso primeiro desafio será enfrentrar um trânsito de bits que estão seguindo rumo ao processador, temos que decodificar algumas sequências binárias que por ventura vierem em nossa direção, assim, nenhum dado será perdido por não ter conseguido chegar ao processador. Devemos fazer isso para não corrermos o risco de ser enviados para a assitência técnica por estar apresentando problemas, e acabar sendo formatados/apagados para sempre. OPÇÃO (27) = seguir.'],
        'proximos_estados': {
            '00011011': 8,
            '[rR]einicia(r)*': 1
        },
        'inventario': {}
    },
    
    7: {
        'frases': ['Certo! Seguiremos o nosso caminho em direção ao alto-falante, por aqui nós enfrentaremos alguns problemas. Nosso primeiro desafio será enfrentrar um trânsito de bits que estão seguindo rumo ao processador, temos que decodificar algumas sequências binárias que por ventura vierem em nossa direção, assim, nenhum dado será perdido por não ter conseguido chegar ao processador. Devemos fazer isso para não corrermos o risco de ser enviados para a assitência técnica por estar apresentando problemas, e acabar sendo formatados/apagados para sempre. OPÇÃO (27) = seguir.'],
        'proximos_estados': {
            '00011011': 8,
            '[rR]einicia(r)*': 1
        },
        'inventario': {}
    },

    8: {
        'frases': ['BITS ESTÃO VINDO EM NOSSA DIREÇÃO!!! CONVERTÁ-OS, SOME-OS E ENVIE O VALOR DA SOMA AO USUÁRIO: 00000100 + 00010000'],
        'proximos_estados': {
            '20': 9,
            '[rR]einicia(r)*': 1
        },
        'inventario': {}
    },

    9: {
        'frases': ['Por incrível que pareça, alguém estava somando 4 + 16 na calculadora, quem tem acesso ao seu computador? Eu até ia rir disso, mas sou um robô. Bem vamos seguir. Logo a frente temos um endereço IPV4 vindo em nossa direção, vamos convertê-lo e enviá-lo ao processador. CONVERTA: 192.168.36.15'],
        'proximos_estados': {
            '11000000.10101000.00100100.00001111': 10,
            '[rR]einicia(r)*': 1
        },
        'inventario': {}
    },

    10: {
        'frases': ['Você está indo muito bem! Faz as conversões tão rápido quanto eu, poderia até tomar o meu lugar e virar um robô se quisesse (risos robóticos malignos?!), mas claro estou apenas comentando. Você acabou de converter um IPV4, que muito provavelmente é o endereço privado do seu computador, guarde esse valor com você, pode ser útil para nós mais a frente. Estão vindo mais bits em nossa direção, OPÇÃO (44) = desviar, OPÇÃO (33) = converter, OPÇÃO (22) = ignorar.'],
        'proximos_estados': {
            '00101100': 11,
            '00100001':12,
            '00010110': 13,
            '[rR]einicia(r)*': 1
        },
        'inventario': {}
    },

    11: {
        'frases': ['Você acabou de perder sua única vida. Você não conseguiu desviar de todos os bits que estavam vindos em sua direção e o computador apresentou falhas, agora suas opções de escolha para seguir diferentes rumos estão limitadas. OPÇÃO (39) = seguir.'],
        'proximos_estados': {
            '00100111': 14,
            '[rR]einicia(r)*': 1
        },
        'inventario': {'Vida'}
    },

    12: {
        'frases': ['Certo, faça a conversão, subtraia e retorne o valor ao usuário: 00010110 - 00001001'],
        'proximos_estados': {
            '15': 14,
            '[rR]einicia(r)*': 1
        },
        'inventario': {}
    },

    13: {
        'frases': ['Você acabou de perder sua única vida. Você ignorou os bits que estavam vindos em sua direção e o computador apresentou falhas, agora suas opções de escolha para seguir diferentes rumos estão limitadas. OPÇÃO (39) = seguir.'],
        'proximos_estados': {
            '00100111': 14,
            '[rR]einicia(r)*': 1
        },
        'inventario': {'Vida'}
    },

    14: {
        'frases': ['Vamos seguir nossa jornada e agora preciso perguntar novamente, pois chegamos a camada de enlace do computador e é aqui que você tomará um rumo diferente na história, escolha o componente pelo qual você deseja sair, pelo seu respectivo MAC address (Você pode copiar e colar o MAC do componente desejado). (00:1B:C9:4B:E3:57) = impressora, (02:4A:F8:4D:73:B7) = monitor, (44:F9:D2:4C:2F:8F) = alto-falante.'],
        'proximos_estados': {
            '00:1B:C9:4B:E3:57': 16,
            '02:4A:F8:4D:73:B7': 17,
            '44:F9:D2:4C:2F:8F': 18,
            '[rR]einicia(r)*': 1
        },
        'inventario': {}
    },

    16: {
        'frases': ['Você foi impresso!'],
        'proximos_estados': {
            
            '[rR]einicia(r)*': 1
        },
        'inventario': {}
    },

    17: {
        'frases': ['Você foi pixelado!'],
        'proximos_estados': {
            
            '[rR]einicia(r)*': 1
        },
        'inventario': {'Vida'}
    },

    18: {
        'frases': ['Você foi sonorizado!'],
        'proximos_estados': {
            
            '[rR]einicia(r)*': 1
        },
        'inventario': {'Vida'}
    },

}
partidas = {}