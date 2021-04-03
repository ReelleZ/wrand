import discord 
import random
import asyncio
import os

client = discord.Client()
@client.event 
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name='コマンドは/hまたは📖で確認できます'))

def callnick(message):
       nick = message.author.nick
       if nick is None:
        return message.author.name
       else:
        return nick    

@client.event
async def on_message(message): 
       global choice
       choice = False
       if message.content == 'ブキ1' or message.content == '1️⃣':
            with open("buki.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'ブキ4'or message.content == '4️⃣':
             with open("buki.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
             textlist = data.split("\n")
             choice1 =random.choice(textlist)
             choice2 =random.choice(textlist)
             choice3 =random.choice(textlist)
             choice4 =random.choice(textlist)
             embed=discord.Embed(title=f"{callnick(message)}さんたちのブキは",description=choice1+"\n"+choice2+"\n"+choice3+"\n"+choice4+"\n"+"です。")
             await message.channel.send(embed=embed)
       elif message.content == 'ヒーロー1':
            with open("hero.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'シューター1':
            with open("shooter.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'ブラスター1':
            with open("blaster.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'ローラー1':
            with open("roller.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'フデ1':
            with open("brush.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'チャージャー1':
            with open("charger.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)  
       elif message.content == 'スロッシャー1':
            with open("shosher.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'スピナー1':
            with open("splatling.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'マニューバー1':
            with open("dualies.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'シェルター1':
            with open("brella.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content =='擬似':
            embed=discord.Embed(title="",description="")
            embed.set_image(url='https://cdn.discordapp.com/attachments/712589650694504508/719929619624624188/gijikaku.png')
            await message.channel.send(embed=embed)
       elif message.content == "ブキ1d" or message.content == '1️⃣1️⃣':
            with open("buki.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'ヒーロー1d':
            with open("hero.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'シューター1d':
            with open("shooter.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'ブラスター1d':
            with open("blaster.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'ローラー1d':
            with open("roller.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'フデ1d':
            with open("brush.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'チャージャー1d':
            with open("charger.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'スロッシャー1d':
            with open("shosher.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'スピナー1d':
            with open("splatling.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'マニューバー1d':
            with open("dualies.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'シェルター1d':
            with open("brella.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content.startswith("ブキ"):
            # 数字だけを抽出
            command = message.content[2:]
            with open("buki.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            try:
            	num=int(command)
            	choice=random.choice(textlist)
            	if num==1:
            		embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice +"です。")
            		await message.channel.send(embed=embed)
            	elif num>20:
            		embed=discord.Embed(title="数字が大きすぎます。1〜20の間でお願いします。")
            		await message.channel.send(embed=embed)
            	else:
            		for i in range(num-1):
            			ch=random.choice(textlist) 
            			choice = str(choice) +"\n"+str(ch)
            		embed=discord.Embed(title=f"{callnick(message)}さんたちのブキは",description=choice +"\n"+ "です。")
            		await message.channel.send(embed=embed)
            except ValueError as e:
            	pass

       elif message.content == '/mw' or message.content == '🧢':
            with open("atama.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choicea =random.choice(textlist) 
            with open("huku.txt", "r",encoding="utf-8_sig") as g: 
              data = g.read() 
            textlist = data.split("\n")
            choiceb =random.choice(textlist) 
            with open("kutu.txt", "r",encoding="utf-8_sig") as h: 
              data = h.read() 
            textlist = data.split("\n")
            choicec =random.choice(textlist) 
            embed=discord.Embed(title="このメインギアパワーがついたギアを使いましょう",color=0xf038db)
            embed.add_field(name="アタマ", value=choicea, inline=False)
            embed.add_field(name="フク", value=choiceb, inline=False)
            embed.add_field(name="クツ", value=choicec, inline=False)
            await message.channel.send(embed=embed)
       if message.content == '/h' or message.content == '📖':
         embed=discord.Embed(title="このBOTで使えるコマンドは以下の通りです。(ブキ〇〇のみ数字部分は半角全角どちらでも大丈夫ですが他のコマンドの数字は半角で入力してください。)",color=0xfd832c)
         commandin =["\n🌟「ブキ1」または1️⃣","\n🌟「ブキ4」または4️⃣","\n🌟「(シューター1、マニューバー1、チャージャー1、スロッシャー1、フデ1、ローラー1、ブラスター1、シェルター1、スピナー1)のどれか」","\n🌟「ヒーロー1」","\n🌟「ブキ1d」または1️⃣1️⃣","\n🌟「(シューター1d、マニューバー1d、チャージャー1d、スロッシャー1d、フデ1d、ローラー1d、ブラスター1d、シェルター1d、スピナー1d)のどれか」","\n🌟「ヒーロー1d」","\n🌟/mwまたは🧢"]
         commandout =["全ブキの中から1つランダムに選びます。\n","全ブキの中から4つランダムに選びます。\nリーグマッチなどでお使いください。\nまた、1と4以外の数字でも反応します。\n","それぞれのブキ種の中から1つランダムに選びます。\n","ヒーローブキの中から1つランダムに選びます。\n","全ブキの中から1つランダムに選びます。\n結果はDMに送られます。\n","それぞれのブキ種の中から1つランダムに選びます。\n結果はDMに送られます。\n","ヒーローブキの中から1つランダムに選びます。\n結果はDMに送られます。\n","アタマ、フク、クツのギアパワーを1つずつランダムに選びます。\n"]
         for i in range(len(commandin)):
           embed.add_field(name=commandin[i], value=commandout[i], inline=False)
         embed.add_field(name="\n🌟不具合などがあれば以下のリンクからご連絡ください。",value="[Twitter](https://twitter.com/st6Rstar2000)\n[BOT作者のdiscordサーバー](https://discord.gg/qeVg3wgaXd)")
         await message.channel.send(embed=embed)

client.run(os.environ['DISCORD_BOT_TOKEN'])
