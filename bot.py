import discord
import random
import time
import logging
from discord.ext import commands

# This is for me to log to a file if there are any errors that occur and to log bugs for fixing
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

raid_list = list()

# Greetings List
greetings = ["We will persevere!",
             "Our enemies will fall!",
             "Victory lies ahead!",
             "Hello, stranger.",
             "We survive.",
             "Must not... give up.",
             "What do you need, stranger?",
             "This curse has not broken me yet. * croaking noises *",
             "A dark wind is blowing.",
             "Are ye here to lend a hand?",
             "How can I help ye?",
             "I'd rather be hammerin' than talkin'.",
             "I'm not much for small talk.",
             "Speak yer piece, if ye must.",
             "Speak your peace!",
             "Hmm?",
             "Yes?",
             "The Naaru have not forgotten us.",
             "Each day is a blessing.",
             "Good fortune!",
             "Open your heart to the light.",
             "Hey there!",
             "Ya got my attention.",
             "How are ya?",
             "Talk to me.",
             "'Lo!",
             "Well met.",
             "Hey.",
             "Greetings!",
             "Salutations!",
             "Honored, I'm sure.",
             "Good day to you.",
             "My, you're a tall one!",
             "Hey, how ya doin'?",
             "Welcome, friend.",
             "Hmm, interesting.",
             "Time is money, friend.",
             "Yeah, what do ya want?",
             "Wisdom to Elisande.",
             "Greetings.",
             "Our destiny is at hand.",
             "We no longer hide."
             ]

# This is the basic discord bot setup
client = discord.Client()
bot = commands.Bot(command_prefix="$")


# Confirmation that the bot has started and connected
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


# When someone types hello, hi or hey in chat will generate a random WoW greeting back
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower().startswith('hello') \
            or message.content.lower().startswith('hi') \
            or message.content.lower().startswith('hey'):
        list_choice = random.randint(1, len(greetings))

        await message.channel.send(greetings[list_choice])

    await bot.process_commands(message)


@bot.event
async def on_member_join(member):
    await bot.get_channel(762038415474425887).send(f"{member.name} has joined The Axe of Grombrindal guild, welcome friend")


# This is the start of the roll dice function
@bot.command()
async def roll(ctx, *args):
    players = dict()
    for arg in args:
        number = random.randint(1, 100)
        players[arg] = number
        await ctx.send(f'{arg} rolled the dice and got a {number}')
        time.sleep(1.2)

    v = list(players.values())
    k = list(players.keys())
    winner = k[v.index(max(v))]
    await ctx.send(f'and the winner is {winner}')


# this is the creation of raid events that you can create a raid event to be viewed by members
raid_list = []


# raid creation command
@bot.command()
async def raid_create(ctx, raid_name, players, date, raid_time, description):
    global raid_list
    temp = [raid_name, players, date, raid_time, description]
    raid_list.append(temp)
    print(raid_list)
    await ctx.send(f'{temp[0]} raid has been created for {temp[1]}, and will take place on {temp[2]} at {temp[3]}')


# raid search command for regular members
@bot.command()
async def raid_events(ctx):
    for raid in raid_list:
        embeded = discord.Embed(
            title=f'{raid[0]} Raid.',
            description=raid[4],
            colour=discord.Color.dark_orange()
        )
        embeded.set_footer(text="See you all there!")
        embeded.set_image(url='https://cdn.discordapp.com/avatars/762972780727631873/cb3674efcc266269387c1365eee126e8'
                              '.png?size=256')
        embeded.set_thumbnail(url='https://cdn.discordapp.com/avatars/762972780727631873'
                                  '/cb3674efcc266269387c1365eee126e8.png?size=256')
        embeded.set_author(name="Axe of Grombrindal Guild Master", icon_url='https://cdn.discordapp.com/avatars'
                                                                            '/762972780727631873'
                                                                            '/cb3674efcc266269387c1365eee126e8.png'
                                                                            '?size=256')
        embeded.add_field(name='Where', value=raid[0], inline=False)
        embeded.add_field(name='Players', value=raid[1], inline=True)
        embeded.add_field(name="Date", value=raid[2], inline=True)
        embeded.add_field(name="Time", value=raid[3], inline=True)

        await ctx.send(embed=embeded)



bot.run("NzYyOTcyNzgwNzI3NjMxODcz.X3w7xg.RwwDYmafeqSORjNEmKvw5uCf9Xo")
