from os import getenv
from dotenv import load_dotenv
import discord
from discord.ext import commands
from random import choice
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='')

# Dicionário com as definições da máquina de estados do jogo.
estados = {
    0: {
        'frases': ['Digite "iniciar" para começar o jogo e "reiniciar" caso queira voltar ao início.'],
        'proximos_estados': {
            'iniciar': 1
        }
    },
    1: {
        'frases': ['Olá! Eu sou Bina seu robô assistente. Você foi "sugado" para dentro do seu computador enquanto trabalhava em um código. Minha missão é ajudá-lo a sair de dentro da máquina e para isso você terá 3 opções de saída: impressora, monitor ou alto-falante, mas primeiro preciso saber como você foi sugado. Para me responder você terá sempre de fazer conversões decimal-binária, pois meu interpretador está danificado. A resposta deverá ter 8 bits (00000000) sendo ela o respectivo valor em binário da opção (X) escolhida. OPÇÃO (10) = teclado, OPÇÃO (15) = mouse, OPCÃO (20) = microfone.'],
        'proximos_estados': {
            '00001010': 2,
            '00001111': 3,
            '00010100': 4,
            'reiniciar': 1 
        }
    },
    2: {
        'frases': ['Certo, como você foi sugado pro computador pelo teclado, eu recomendo sair do PC pela impressora, se desejar seguir esse rumo, OPCÃO (12) = sair pela impressora, caso não queira "reiniciar".'],
        'proximos_estados': {
            '00001100': 5,
            'reiniciar': 1
        }
    },
    3: {
        'frases': ['Certo, como você foi sugado pro computador pelo mouse, eu recomendo sair do PC pelo monitor, se desejar seguir esse rumo, OPÇÃO (19) = sair pelo monitor, caso não queira "reiniciar".'],
        'proximos_estados': {
            '00010011': 6,
            'reiniciar': 1
        }       
    },
    4: {
        'frases': ['Certo, como você foi sugado pro computador pelo microfone, eu recomendo sair do PC pelo alto-falante, se desejar seguir esse rumo, OPÇÃO (21) = sair pelo alto-falante, caso não queira "reiniciar".'],
        'proximos_estados': {
            '00010101': 7,
            'reiniciar': 1
        }
    },
    5: {
        'frases': ['VOCÊ FOI IMPRESSO!'],
        'proximos_estados': {
            'reiniciar': 1
        }
    },

    6: {
        'frases': ['VOCÊ FOI PIXELADO!'],
        'proximos_estados': {
            'reiniciar': 1
        }
    },
    
    7: {
        'frases': ['VOCÊ FOI SONORIZADO!'],
        'proximos_estados': {
            'reiniciar': 1
        }
    },
}

# Dicionário com os estados correntes de cada jogador.
partidas = {}


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.event
async def on_message(msg):
    # Verificar se a mensagem não tem o próprio bot como autor.
    if msg.author.id == msg.channel.me.id:
        return

    # Verificar se o jogador ainda não começou a partida,
    # o que significa que precisa colocá-lo no estado zero (0).
    if msg.author.id not in partidas:
        partidas[msg.author.id] = 0

    # Em ordem de operação:
    # 0) Obter o ID do jogador:
    #    msg.author.id
    # 1) Obter o estado atual do jogador:
    #    partidas[msg.author.id]
    # 2) Obter a definição completa desse estado:
    #    estados[partidas[msg.author.id]]
    # 3) Filtrar desse estado apenas a lista de próximos estados:
    #    estados[partidas[msg.author.id]]['proximos_estados']
    # 4) Filtrar dessa lista as chaves (frases) quem levam a próximos estados:
    #    estados[partidas[msg.author.id]]['proximos_estados'].keys()
    # 5) Verificar se a frase do usuário está na lista de chaves (frases) do estado:
    if msg.content in estados[partidas[msg.author.id]]['proximos_estados'].keys():
        #
        # 6) Atualizar o estado do jogador, fazendo-o avançar no jogo:
        partidas[msg.author.id] = estados[partidas[msg.author.id]]['proximos_estados'][msg.content]
        #
        # 7) Enviar para o jogador a mensagem do estado (já atualizado)
        #
        # Em ordem de operação:
        # 7.0) Obter o ID do jogador:
        #    msg.author.id
        # 7.1) Obter o estado atual do jogador:
        #    partidas[msg.author.id]
        # 7.2) Obter a definição completa desse estado:
        #    estados[partidas[msg.author.id]]
        # 7.3) Filtrar desse estado apenas a lista de frases:
        #    estados[partidas[msg.author.id]]['frases']
        # 7.4) Sortear uma frase dessa lista:
        #   choice(estados[partidas[msg.author.id]]['frases'])
        await msg.channel.send(choice(estados[partidas[msg.author.id]]['frases']))
    #
    # Caso contrário, avisar que a mensagem não avança no jogo
    else:
        #
        # Se o jogador está no primeiro estado...
        if partidas[msg.author.id] == 0:
            #
            # ...ajudar com uma dica:
            await msg.channel.send(choice(estados[partidas[msg.author.id]]['frases']))
        else:
            #
            # Nos estados seguintes, a resposta padrão de HAL:
            await msg.channel.send('Desculpe, não entendi.')


bot.run(getenv('DISCORD_TOKEN'))