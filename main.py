import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def fotoperfil(ctx, miembro: discord.Member = None):
    if miembro is None:
        miembro = ctx.author
    await ctx.send(miembro.display_avatar.url)
@bot.command()
async def gen_pass(ctx, pass_length: int):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    await ctx.send(password)
@bot.command()
async def musica(ctx):
    if ctx.author.voice is None:
        await ctx.send("Entra a un canal de voz.")
        return
    canal = ctx.author.voice.channel
    if ctx.voice_client is None:
        voz = await canal.connect()
    else:
        voz = ctx.voice_client
    if voz.is_playing():
        voz.stop()
    audio = discord.FFmpegPCMAudio(
        "musica.mp3",
        executable=r"C:\Users\tomas\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0-full_build\bin\ffmpeg.exe"
    )

    audio = discord.PCMVolumeTransformer(audio, volume=0.3)

    voz.play(audio)

    await ctx.send(f"Musiquita en {canal.name}")
@bot.command()
async def parar(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send("Frene la musica :)")
    else:
        await ctx.send("No estoy reproduciendo música :c .Para reproducir musica usa $musica")
@bot.command()
async def imagen(ctx):
    with open('images/imagen.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
@bot.command()
async def facto(ctx):
    with open('text.txt', 'r', encoding='utf-8') as f:
        texto = f.read()
        await ctx.send(texto)
@bot.command()
async def meme(ctx):
    meme = random.choice(['meme1.jpg', 'meme2.jpg', 'meme3.jpg'])
    with open(f'images/{meme}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
        print(os.listdir('images'))
def get_random_cr_image():
    url = "https://api.github.com/repos/RoyaleAPI/cr-api-assets/contents/chr"

    res = requests.get(url)
    data = res.json()

    imagenes = []

    for archivo in data:
        if archivo["name"].endswith((".png", ".jpg", ".jpeg", ".webp")):
            imagenes.append(archivo["download_url"])

    return random.choice(imagenes)
@bot.command()
async def cr(ctx):
    imagen_url = get_random_cr_image()
    await ctx.send(imagen_url)
bot.run("tutoken")
