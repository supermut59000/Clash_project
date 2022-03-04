import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import datetime
import matplotlib.pyplot as plt
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '..//Module//')

from Clash_API_call import Clash_API_Call
from DATABASE_HANDLER import Data_handler_my_sql
load_dotenv('..//.env')


host = os.getenv("DATABASE_IP")
database = os.getenv("DATABSE_NAME")
user = os.getenv("DATABASE_USR")
password = os.getenv("DATABASE_PASSWORD")

PATH = os.getcwd()

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == "suceee":
            break
    print(
        f"{bot.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
    )





@bot.command()
async def help_bot(ctx):
    embed = discord.Embed(
        title="Liste des commandes",
        description="Tracked        Normal",
        color=discord.Color.blue(),
    )
    embed.add_field(name="Deck",value="$deckt <player pseudo> or $deck <player tag>",inline=False)
    embed.add_field(name="Info",value="$infot <player pseudo> or $info <player tag>",inline=False)
    embed.add_field(name="Track",value="$track <player tag>",inline=False)
    embed.add_field(name="Tropies graph",value="$tr <player name>",inline=False)
    embed.add_field(name="Reset tropies graph",value="$reset_tr",inline=False)
    await ctx.send(embed=embed)
    return


@bot.command()
async def deckt(ctx, player_pseudo: str):
    database_handler = Data_handler_my_sql(host, user, password, database)
    player_tag = database_handler.get_usr_pseudo(player_pseudo)[0]
    avg_lvl = Clash_API_Call.creation_png_of_the_deck(player_tag[1:])
    embed = discord.Embed(
        title="Deck actuelle de "
        + player_pseudo,
        description="",
        color=discord.Color.blue(),
    )
    embed.add_field(name="Elixir", value="aaa", inline=True)
    embed.add_field(name="Level moyen", value=avg_lvl, inline=True)

    file = discord.File(PATH + "/deck.png")
    await ctx.send(file=file, embed=embed)
    return


@bot.command()
async def deck(ctx, player_tag: str):
    avg_lvl = Clash_API_Call.creation_png_of_the_deck(player_tag[1:])
    embed = discord.Embed(
        title="Deck actuelle de "
        + Clash_API_Call.API_request_tracked_general_info(player_tag[1:])[1],
        description="",
        color=discord.Color.blue(),
    )
    embed.add_field(name="Elixir", value="aaa", inline=True)
    embed.add_field(name="Level moyen", value=avg_lvl, inline=True)

    file = discord.File(PATH + "/deck.png")
    await ctx.send(file=file, embed=embed)
    return


@bot.command()
async def info(ctx, player_tag: str):
    temp = Clash_API_Call.API_request_tracked_general_info(player_tag[1:])
    embed = discord.Embed(
        title="Info de " + temp[1],
        description="",
        color=discord.Color.blue(),
    )
    embed.add_field(name="Niveau", value=temp[2], inline=True)
    embed.add_field(name="Nb Trophée", value=temp[3][4], inline=False)
    WR = str(round(temp[3][0] / (temp[3][0] + temp[3][1]), 2) * 100) + "%"
    embed.add_field(name="WR", value=WR, inline=True)
    C = str(round(temp[3][3] / temp[3][0], 2) * 100) + "%"
    embed.add_field(name="3C/Win", value=C, inline=True)
    await ctx.send(embed=embed)
    return


@bot.command()
async def infot(ctx, player_pseudo: str):
    database_handler = Data_handler_my_sql(host, user, password, database)
    player_tag = database_handler.get_usr_pseudo(player_pseudo)[0]
    temp = Clash_API_Call.API_request_tracked_general_info(player_tag[1:])
    embed = discord.Embed(
        title="Info de " + player_pseudo,
        description="",
        color=discord.Color.blue(),
    )
    embed.add_field(name="Niveau", value=temp[2], inline=True)
    embed.add_field(name="Nb Trophée", value=temp[3][4], inline=False)
    WR = str(round(temp[3][0] / (temp[3][0] + temp[3][1]), 2) * 100) + "%"
    embed.add_field(name="WR", value=WR, inline=True)
    C = str(round(temp[3][3] / temp[3][0], 2) * 100) + "%"
    embed.add_field(name="3C/Win", value=C, inline=True)
    await ctx.send(embed=embed)
    return


@bot.command()
async def track(ctx, player_tag: str):
    database_handler = Data_handler_my_sql(host, user, password, database)
    temp = Clash_API_Call.API_request_tracked_general_info(player_tag[1:])
    error = database_handler.new_tracked_usr(
        temp[0], temp[1], temp[2], temp[3][4], datetime.datetime.utcnow()
    )
    if error:
        if error[1] == 1062:
            await ctx.send("User déjà tracké")
    else : 
        await ctx.send("Fait")
    return

@bot.command()
async def tracked(ctx):
    database_handler = Data_handler_my_sql(host, user, password, database)
    temp = database_handler.get_tracked_usr()
    embed = discord.Embed(
        title="Liste des tracked_usr",
        description="",
        color=discord.Color.blue(),
    )
    chaine=""
    for i in temp:
        chaine  = chaine + i[0] + "\n"
    embed.add_field(name="0-10",value=chaine,inline=True)
    await ctx.send(embed=embed)
    return

@bot.command()
async def tr(ctx, player_pseudo :str):
    database_handler = Data_handler_my_sql(host, user, password, database)
    temp = database_handler.get_tr_player(player_pseudo)
    x=[]
    y=[]
    for i in temp:
        x.append(i[2])
        y.append(i[1])
    
    embed = discord.Embed(
        title="Info "+player_pseudo,
        description="",
        color=discord.Color.blue(),
    )
    chaine1 = str(x[y.index(min(y))]) + "\n" + str(min(y))
    chaine2 = str(x[y.index(max(y))]) + "\n" + str(max(y))
    embed.add_field(name="MIN",value=chaine1,inline=True)
    embed.add_field(name="MAX",value=chaine2,inline=True)
    plt.plot(x,y)
    plt.savefig("tr.png")
    await ctx.send(file=discord.File(PATH + "/tr.png"))
    await ctx.send(embed=embed)
    plt.clf()
    return



@bot.command()
async def get_log(ctx):
    log = PATH + "/cron.log"
    await ctx.send(file=discord.File(log))
    return


bot.run(TOKEN)
