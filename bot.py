import os
import random

import discord
from discord.ext import commands
import platform
from dotenv import load_dotenv
'''
#Костыль на ошибку EventLoop is closed
from functools import wraps

from asyncio.proactor_events import _ProactorBasePipeTransport
def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise
    return wrapper

if platform.system() == 'Windows':
    # Silence the exception here.
    _ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)
#Костыль окончен
'''
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
'''
#Альтернатива Client через Bot

bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print(f'{bot.user.name} welcome to the club, buddy:\n'')

@bot.command(name='99', help='Текст который объяснит что делает бот')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

#Добавление игры в кости( можно сделать Орел и Решку и рандомайзер)

@bot.command(name='roll_dice', help='Simulates rolling dice.')

async def roll(ctx, number_of_dice, number_of_sides):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

#Чтобы не было ошибки str (cannot be interpreted as an integer)(разница в int)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

bot.run(TOKEN)
'''
client = discord.Client()

@client.event
async def on_ready():
    '''
    Тоже что и utils.find()
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    '''
    guild = discord.utils.get(client.guilds, name = GUILD)
    print(
        f'{client.user} welcome to the club, buddy:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Здесь все:\n - {members}')
    print(f'Главный паразит:\n - {owner}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'{member.name}, Салам АЛЕЙКУИМ!!!'
    )
'''
идея сделать словарь-значение для соответствующих фразочек, 
чтобы разнообразить message.content
'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    bot_quotes = [
        'Я на 💯 процентов уверен, что ты позвал меня просто так...',
        'На месте!',
        (
            'Я в своём познании настолько преисполнился, '
            'что как будто бы уже 100 триллионов миллиардов лет проживаю '
            'на триллионах и триллионах таких же планет, понимаешь?'
        ),
    ]

    if message.content == 'Бот' or message.content == 'Bot':
        response = random.choice(bot_quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

client.run(TOKEN)

#Проверка предикатов команд