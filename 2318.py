import discord
from discord.ext.commands import Bot
from discord.ext import commands

bot = discord.Client()
bot_prefix="!"
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready() :
    print("Bot çevrimiçi!")
    print("İsim : {}".format(bot.user.name))
    print("ID : {}".format(bot.user.id))
    print(str(len(bot.servers)) + " tane serverda çalışıyor!")
    print(str(len(set(bot.get_all_members()))) + " tane kullanıcaya erişiyor!")
    await bot.change_presence(game=discord.Game(name='2318 botu çalışır durumda!'))

@bot.command(pass_context=True)
async def yirmi15(ctx) :
    await bot.say("Ben bot 2318'im!")

bot.run("NDA5MzU2MTM1NDgxNzM3MjE2.DVda7g.6MWVKoLxwhNvrFfB672H48xQQCw")