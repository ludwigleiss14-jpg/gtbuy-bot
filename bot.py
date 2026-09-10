import os
from flask import Flask
import discord
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Eingeloggt als {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions:
        query = message.content.replace(f'<@!{client.user.id}>', '').replace(f'<@{client.user.id}>', '').strip()
        if not query:
            query = "gaming gear"
        
        affiliate_code = "0UL1P0M5K"
        gtbuy_url = f"https://www.gtbuy.com/search?q={query.replace(' ', '+')}&ref={affiliate_code}"
        
        embed = discord.Embed(
            title=f"Suchergebnisse für: {query}",
            description=খার Finde die besten Angebote direkt bei GTBuy!",
            color=0x00ff00
        )
        embed.add_field(name="Dein Affiliate-Link", value=f"[Hier klicken]({gtbuy_url})", inline=False)
        embed.set_footer(text=f"Affiliate Code: {affiliate_code}")
        
        await message.channel.send(embed=embed)

if __name__ == "__main__":
    keep_alive()
    client.run(os.getenv("DISCORD_TOKEN"))
