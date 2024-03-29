# -*- coding: utf-8 -*-
import discord
import random
import asyncio
import os
from discord.commands import Option

intents = discord.Intents.default()
intents.message_content = False
client = discord.Bot(intents=intents)

NFs ="アプリケーションは反応しています。上のような表示が出てしまう原因をただいま調査中です。"
NF =discord.Embed(title=NFs,description="ご迷惑をおかけして申し訳ありません。")
NDM=discord.Embed(title="この機能はDMでは使えません。",color=0xff0033)
assm=discord.Embed(title="アシスタント機能を呼び出します。")
@client.event 
async def on_ready():
    print("ログインしました")
    print(client.user.name)
    print(client.user.id)
    print("------")
    while True:
     await client.change_presence(activity=discord.Game(name="コマンドは/hで確認できます"))
     await asyncio.sleep(10)
     await client.change_presence(activity=discord.Game(name="/assと入力すると簡単なアシスタントが反応します"))
     await asyncio.sleep(10)


def callnick(message):
  try:
    nick = message.author.nick
    if nick is None:
      return message.author.name
    else:
      return nick  
  except AttributeError as e : 
    return message.author.name

def listget(list):
  with open(list, "r",encoding="utf-8_sig") as h: 
    data = h.read() 
  textlist = data.split("\n")
  return textlist

def brand(message,list):
  choice =random.choice(listget(list))
  embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice+ "です。")
  return embed

#/as用　変数が違う
def callnickas(user):
  nick = user.nick
  if nick is None:
    return user.name
  else:
    return nick   

def brandas(user,list):
  choice =random.choice(listget(list))
  embed=discord.Embed(title=f"{callnickas(user)}さんのブキは",description=choice+ "です。")
  return embed


def mkhelp():
  embed=discord.Embed(title="このBOTで使えるコマンドは以下の通りです。",color=0xfd832c)
  embed.add_field(name="❗以下のコマンドはスラッシュコマンドで利用できます❗",value="[スラッシュコマンドとは(動画)](https://twitter.com/discord_jp/status/1377063239067037701)")
  embed.add_field(name="スラッシュコマンドが利用できない場合、ブキルーレットBotをもう一度招待する必要があります。\n",value="[招待はこちらから](https://discord.com/api/oauth2/authorize?client_id=718346812410298398&permissions=19327413248&scope=bot%20applications.commands)", inline=False)
  commandin =["\n🌟ssb","\n🌟sssb","\n🌟h","\n🌟mw","\n🌟ass"]
  commandout =["指定されたブキ種類の中から指定された人数分ランダムに選びます。\n人数とブキ種類を指定しないと全ブキの中から1つランダムに選びます。\n","指定されたブキ種類の中から1つランダムに選びます。結果はDMに送られます。\n","コマンド一覧を表示します。\n","アタマ、フク、クツのギアパワーを1つずつランダムに選びます。\n","簡単なアシスタントを呼び出します。\n(DMでは呼び出せません)"]
  for i in range(len(commandin)):
    embed.add_field(name=commandin[i], value=commandout[i], inline=False)
  embed.add_field(name="❗スラッシュコマンドは以上です❗",value=  "スラッシュコマンドを利用するにはブキルーレットBotをもう一度招待する必要があります。\n[招待はこちらから](https://discord.com/api/oauth2/authorize?client_id=718346812410298398&permissions=19327413248&scope=bot%20applications.commands)", inline=False)
  embed.add_field(name="❗スラッシュコマンドの不具合でたまにアプリケーションが応答しませんでしたと出る場合がありますが、応急処置としてそのあとにスラッシュコマンドの結果を送るようにしています。❗",value=  "不具合の原因は調査中です。ご迷惑をおかけして申し訳ありません。", inline=False)
  embed.add_field(name="\n🌟不具合などがあれば以下のリンクからご連絡ください。",value="[discordサーバー](https://discord.gg/N5aqrYeHaa)")
  return embed

#New code with slash command
def brandn(message,bukis):
  list = listchoose(bukis)
  choice =random.choice(listget(list))
  embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice+ "です。")
  return embed

def listchoose(bukis):
  if bukis == "シューター":
    list = "bukis/shooter.txt"
  elif bukis == "ヒーロー":
    list = "bukis/hero.txt"
  elif bukis == "マニューバー":
    list = "bukis/dualies.txt"
  elif bukis == "チャージャー":
    list = "bukis/charger.txt"
  elif bukis == "スロッシャー":
    list = "bukis/shosher.txt"
  elif bukis == "フデ":
    list = "bukis/brush.txt"
  elif bukis == "ローラー":
    list = "bukis/roller.txt"
  elif bukis == "ブラスター":
    list = "bukis/blaster.txt"
  elif bukis == "スピナー":
    list = "bukis/splatling.txt"
  elif bukis == "シェルター":
    list = "bukis/brella.txt"
  elif bukis == "buki":
    list = "bukis/buki.txt"
  return list

@client.slash_command(description="指定されたブキ種類のなかから人数分のブキをランダムに選びます。")
async def ssb(
    ctx,
    人数: Option(int, '人数を入力してください(1~20)。入力がなければ1人分の結果を返します。',required=False, min_value=1, max_value=20,default=1),
    ブキ種類: Option(str, 'ブキの種類を選択してください。入力がなければすべてのブキから選ばれます。', required=False, default="buki",choices=["シューター", "ヒーロー", "マニューバー","チャージャー","スロッシャー","フデ","ローラー","ブラスター","シェルター","スピナー"]),
):
    
    if 人数==1:
      try:
        await ctx.respond(embed=brandn(ctx,ブキ種類))
      except discord.errors.NotFound as e:
        await ctx.channel.send(embed=NF)
        await ctx.channel.send(embed=brandn(ctx,ブキ種類))
    else:
      list = listchoose(ブキ種類)
      ch=str(random.choice(listget(list)))
      choice = str(ch)
      for i in range(人数-1):
        ch=str(random.choice(listget(list)))
        choice = str(choice) +"\n"+str(ch)
      embed=discord.Embed(title=f"{callnick(ctx)}さんたちのブキは",description=choice +"\n"+ "です。")
      try:
        await ctx.respond(embed=embed)
      except discord.errors.NotFound as e:
        await ctx.channel.send(embed=NF)
        await ctx.channel.send(embed=embed)

@client.slash_command(description="指定されたブキ種類のなかからブキを一つランダムに選び、DMに送ります。")
async def ssbd(
    ctx,
    ブキ種類: Option(str, 'ブキの種類を選択してください。入力がなければすべてのブキから選ばれます。', required=False, default="buki",choices=["シューター", "ヒーロー", "マニューバー","チャージャー","スロッシャー","フデ","ローラー","ブラスター","シェルター","スピナー"]),
):
    
    dm = await ctx.author.create_dm()
    await dm.send(embed=brandn(ctx,ブキ種類))
    sent=discord.Embed(title="DMに結果を送信しました。",color=0xffffff)
    try:
      await ctx.respond(embed=sent)
    except discord.errors.NotFound as e:
      await ctx.channel.send(embed=NF)
      await ctx.channel.send(embed=sent)

@client.slash_command(description="ブキルーレットBotのコマンド一覧を表示します。")
async def h(ctx):
    try:
      await ctx.respond(embed=mkhelp())
    except discord.errors.NotFound as e:
      await ctx.channel.send(embed=NF)
      await ctx.channel.send(embed=mkhelp())


@client.slash_command(description="アタマ、フク、クツのギアパワーを1つずつランダムに選びます。")
async def mw(ctx):
        embed=discord.Embed(title="このメインギアパワーがついたギアを使いましょう",color=0xf038db)
        embed.add_field(name="アタマ", value=random.choice(listget("armer/atama.txt")), inline=False)
        embed.add_field(name="フク", value=random.choice(listget("armer/huku.txt")), inline=False)
        embed.add_field(name="クツ", value=random.choice(listget("armer/kutu.txt")), inline=False)
        try:
          await ctx.respond(embed=embed)
        except discord.errors.NotFound as e:
          await ctx.channel.send(embed=NF)
          await ctx.channel.send(embed=embed) 

@client.slash_command(description="簡単なアシスタントを呼び出します(DMでは呼び出せません)")
async def ass(ctx):
        try:
          sv= f"{client.get_guild(ctx.guild.id)}のみなさん"
        except AttributeError as e : 
          #sv=f"{callnick(message)}さん"
          try:
            await ctx.respond(embed=NDM)
            return
          except discord.errors.NotFound as e:
            await ctx.channel.send(embed=NF)
            await ctx.channel.send(embed=NDM) 
            return #DMだとリアクションが反応しないのでDMを使わないようにする
        home=discord.Embed(title=f"こんにちは！{sv}",description="このメッセージについているリアクションを押すと以下のように動きます。(時間が経つと反応してくれなくなることがありますがその時はもう一度/ass(スラッシュコマンド)を入力してください。)",colour=0xe52349)
        home.add_field(name="1⃣", value="全ブキの中から1つランダムに選びます", inline=False)
        home.add_field(name="2⃣", value="全ブキの中から1つランダムに選びます。\n結果はDMに送られます。", inline=False)
        home.add_field(name="📖", value="このbotで使用できるコマンドをすべて表示します。", inline=False)
        home.add_field(name="注意", value="リアクションの仕様上同時押しに反応できず、\n同時にリアクションを押されてしまうと片方は無視されます。\n無視された場合は申し訳ありませんがもう一度やり直してください.", inline=False)
        try:
          await ctx.respond(embed=assm)
        except discord.errors.NotFound as e:
          await ctx.channel.send(embed=NF)
          await ctx.channel.send(embed=assm) 
        msg = await ctx.channel.send(embed=home)
        #reaction
        await msg.add_reaction("1⃣")
        await msg.add_reaction("2⃣")
        await msg.add_reaction("📖")
        def check(reaction, user):
            emoji = str(reaction.emoji)
            if user.bot == True: 
             pass
            else:
             return emoji == '1⃣' or emoji == '2⃣' or emoji == '📖' and reaction.message == msg 
        while True:
          reaction, user = await client.wait_for("reaction_add", check=check)
          #print(str(user)+str(client.user))
          if user.bot == True:  
            pass
          if reaction.message!= msg:
            pass
          elif str(reaction.emoji) == "1⃣":
            await ctx.channel.send(embed=brandas(user,"bukis/buki.txt"))
            await msg.remove_reaction(str(reaction.emoji), user)
          elif str(reaction.emoji) == "2⃣":
            dm = await user.create_dm()
            await dm.send(embed=brandas(user,"bukis/buki.txt"))
            await msg.remove_reaction(str(reaction.emoji), user)
          elif str(reaction.emoji) == "📖":
            if user== client.user: #こいつだけ誤動作するので
              pass
            else:
              await ctx.channel.send(embed=mkhelp())
              await msg.remove_reaction(str(reaction.emoji), user)
              await msg.delete()
              home=discord.Embed(title="",description="このメッセージについているリアクションを押すと以下のように動きます。(時間が経つと反応してくれなくなることがありますがその時はもう一度/ass(スラッシュコマンド)を入力してください。)",colour=0xe52349)
              home.add_field(name="1⃣", value="全ブキの中から1つランダムに選びます", inline=False)
              home.add_field(name="2⃣", value="全ブキの中から1つランダムに選びます。\n結果はDMに送られます。", inline=False)
              home.add_field(name="📖", value="このbotで使用できるコマンドをすべて表示します。", inline=False)
              home.add_field(name="注意", value="リアクションの仕様上同時押しに反応できず、\n同一テキストチャンネルで同時にリアクションを押されてしまうと片方は無視されます。\n無視された場合は申し訳ありませんがもう一度やり直してください。", inline=False)
              msg = await ctx.channel.send(embed=home)
              #reaction
              await msg.add_reaction("1⃣")
              await msg.add_reaction("2⃣")
              await msg.add_reaction("📖")
            
client.run(os.environ['DISCORD_BOT_TOKEN'])
