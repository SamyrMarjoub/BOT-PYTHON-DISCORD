import asyncio
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from generate_text import generate_text  # Importar a função generate_text

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
    await ctx.send(f'Okay!, {ctx.author.name}')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Olá, {ctx.author.name}!')

@bot.command(name='generate')
async def generate(ctx, *, prompt: str):
    max_tokens = 300  # Máximo de tokens gerados

    # Chamar a função de geração de texto
    response = generate_text(prompt, max_tokens)
    
    # Enviar a resposta no Discord
    await ctx.send(response)

# Iniciar o bot
bot.run(TOKEN)
