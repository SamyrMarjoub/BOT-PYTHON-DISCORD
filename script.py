import asyncio
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from generate_text import generate_random_event  # Importar a função generate_text
from generate_text import get_random_event_results
import time
max_tokens = 1000  # Máximo de tokens gerados

# Configurar a política de loop de eventos para Windows
if os.name == 'nt':  # Verifica se está no Windows
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Carregar variáveis de ambiente do .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot logado como {bot.user.name}!')

@bot.command(name='start')
async def start(ctx):
    await ctx.send(f'Hayoo!, {ctx.author.name}, saudações! Pronto para embarcar no seu evento diario, rumo ao desconhecido nessa terra fantastica de xxx?')
    await ctx.send(f'Responda com "Sim" ou "Não".')
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ['sim', 'não']

    try:
        msg = await bot.wait_for('message', check=check, timeout=30.0)
    except asyncio.TimeoutError:
        await ctx.send('Você demorou muito para responder.')
    else:
        if msg.content.lower() == 'sim':
            await ctx.send('Você escolheu "sim". Vamos continuar!')
            time.sleep(2)
            await ctx.send('Gerando evento aleatorio diario...')
            response = generate_random_event('Nome: "Diana", "Sexo": "Feminino", Localização:"Planicies", Armas:"Martelo e escudo", level:"40"', max_tokens)
            await ctx.send(response)
            time.sleep(5)
            await ctx.send('----------------------------------')
            time.sleep(2)
            await ctx.send('Certo! O evento acabou. mostrando resultados agora')
            await ctx.send('----------------------------------')
            resultados = get_random_event_results(response, max_tokens)
            await ctx.send(resultados)

    
            
        else:
            await ctx.send('Você escolheu "não". Fim da interação.')


@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Olá, {ctx.author.name}!')

@bot.command(name='s')
async def hello(ctx):
    await ctx.send(f'Olá, {ctx.author.name}!')

@bot.command(name='generate')
async def generate(ctx, *, prompt: str):

    # Chamar a função de geração de texto
    response = generate_random_event(prompt, max_tokens)
    resultados = get_random_event_results(response, max_tokens)
    
    # Enviar a resposta no Discord
    await ctx.send(response)
    await ctx.send('Certo! O evento acabou. mostrando resultados agora')
    await ctx.send(resultados)
    

# Iniciar o bot
bot.run(TOKEN)
