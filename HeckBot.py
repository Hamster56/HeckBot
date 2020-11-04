import discord
from discord.ext import commands

bot = discord.Client()

bot = commands.Bot(command_prefix='!')

heck_list= []

#heck_emoji = bot.get_emoji(631567436373688320)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(pass_context= True)
async def heck(ctx, members: commands.Greedy[discord.Member]) :
    for x in members :
        heck_list.append(x.id)
        await ctx.send(f"{x.name} added to list")
    print(heck_list)

@bot.event
async def on_message(message) :
    if message.author.id in heck_list :
        print('Found in list')
        await message.add_reaction('<:Heck:773607864706269244>')
    await bot.process_commands(message)

bot.run('token')
