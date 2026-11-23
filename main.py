import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 反応する言葉と返信内容
responses = {
    "響はゲイですか？": "ゲイです！！",
    "りくはゲイですか？": "ゲイです！",
    "れいじはゲイですか？": "ちがいます！",
    "ゆうきはゲイですか？": "ちがいます！",
    "しね": "お前が死ねよカス！",
    "死ね": "お前が死ねよカス！"
}

@bot.event
async def on_ready():
    print(f"{bot.user} でログインしました！")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    for word, reply in responses.items():
        if word in message.content:
            await message.channel.send(reply)
            break

    await bot.process_commands(message)

bot.run("MTU3NDA3OTg2MTYyOTEzMjkyMg.GkyfZd.PHlYBxTMvO_wG7MNoX_IorplyuqLYakBnU-kN4")
