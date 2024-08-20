import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("Вы забыли загрузить картинку :(")

@bot.command()
async def com(ctx):
    await ctx.send(f'Команды: $hello, $check, $proekt')

@bot.command()
async def proekt(ctx):
    await ctx.send(f'Мой проект направлен на создание простой в использовании системы искусственного интеллекта, которая автоматически распознаёт разные виды фруктов и сообщает их калорийность. Идея в том, чтобы пользователи могли легко определить, какой это фрукт и сколько он содержит калорий, просто загрузив его фото. Проект нацелен на то, чтобы сделать процесс получения информации о фруктах быстрым и доступным, а также помочь пользователям принимать осознанные решения о своем питании.')



bot.run("YOUR TOKEN")