estados = {
    0: {
        'frases': ['Digite "iniciar" para começar o jogo e "reiniciar" caso queira voltar ao início.'],
        'proximos_estados': {
            '[iI]nicia(r)*': 1
        },
        'tempo_limite': 0
    },
    1: {
        'frases': ['Olá! Eu sou Bina seu robô assistente. Você foi "sugado" para dentro do seu computador enquanto trabalhava em um código. Minha missão é ajudá-lo a sair de dentro da máquina e para isso você terá 3 opções de saída: impressora, monitor ou alto-falante, mas primeiro preciso saber como você foi sugado. Para me responder você terá sempre de fazer conversões decimais-binárias, pois meu interpretador está danificado. A resposta deverá ter 8 bits (00000000) sendo ela o respectivo valor em binário da opção (X) escolhida. OPÇÃO (10) = teclado, OPÇÃO (15) = mouse, OPCÃO (20) = microfone.'],
        'proximos_estados': {
            '00001010': 2,
            '00001111': 3,
            '00010100': 4,
            'reiniciar': 1 
        },
        'tempo_limite': 0
    },
    2: {
        'frases': ['Certo, como você foi sugado pro computador pelo teclado, eu recomendo sair do PC pela impressora, se desejar seguir esse rumo, OPCÃO (12) = sair pela impressora, caso não queira "reiniciar".'],
        'proximos_estados': {
            '00001100': 5,
            'reiniciar': 1
        },
        'tempo_limite': 0
    },
    3: {
        'frases': ['Certo, como você foi sugado pro computador pelo mouse, eu recomendo sair do PC pelo monitor, se desejar seguir esse rumo, OPÇÃO (19) = sair pelo monitor, caso não queira "reiniciar".'],
        'proximos_estados': {
            '00010011': 6,
            'reiniciar': 1
        },
        'tempo_limite': 0       
    },
    4: {
        'frases': ['Certo, como você foi sugado pro computador pelo microfone, eu recomendo sair do PC pelo alto-falante, se desejar seguir esse rumo, OPÇÃO (21) = sair pelo alto-falante, caso não queira "reiniciar".'],
        'proximos_estados': {
            '00010101': 7,
            'reiniciar': 1
        },
        'tempo_limite': 0
    },
    5: {
        'frases': ['VOCÊ FOI IMPRESSO!'],
        'proximos_estados': {
            'reiniciar': 1
        },
        'tempo_limite': 0
    },

    6: {
        'frases': ['VOCÊ FOI PIXELADO!'],
        'proximos_estados': {
            'reiniciar': 1
        },
        'tempo_limite': 0
    },
    
    7: {
        'frases': ['VOCÊ FOI SONORIZADO!'],
        'proximos_estados': {
            'reiniciar': 1
        },
        'tempo_limite': 0
    }
}
partidas = {}