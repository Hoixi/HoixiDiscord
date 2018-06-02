import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
import os

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

@bot.command(pass_context=True)
async def a(ctx, member:discord.Member):
    urll = ["https://media1.tenor.com/images/49a21e182fcdfb3e96cc9d9421f8ee3f/tenor.gif" , 
            "https://media1.tenor.com/images/b0de026a12e20137a654b5e2e65e2aed/tenor.gif" ,
           "https://78.media.tumblr.com/680b69563aceba3df48b4483d007bce3/tumblr_mxre7hEX4h1sc1kfto1_500.gif"]
    embed = discord.Embed(title=ctx.message.author.name + " sana sarılıyor " + member.name )
    embed.set_image(url=random.choice(urll))
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def sil (ctx, number):
    mgs = []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit=number):
        mgs.append(x)
    await bot.delete_messages(mgs)

@bot.command(pass_context=True)
async def s (ctx):
    mgs = ctx.message.content.split("1")
    await bot.delete_message(ctx.message)
    await bot.send_message(ctx.message.channel , mgs)



bot.run(os.environ.get('token'))
