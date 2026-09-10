import os
from flask import Flask
import discord
from threading import Thread

# 1. Mini-Webserver für Render (damit der Port belegt wird)
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

# 2. Discord Bot Setup
intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Eingeloggt als {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if self.user in message.mentions:
            query = message.content.replace(f'<@!{self.user.id}>', '').replace(f'<@{self.user.id}>', '').strip()
            if not query:
                query = "gaming gear"
            
            affiliate_code = "0UL1P0M5K"
            gtbuy_url = f"https://www.gtbuy.com/search?q={query.replace(' ', '+')}&ref={affiliate_code}"
            
            embed = discord.Embed(
                title=f"Suchergebnisse für: {query}",
                description="Finde die besten Angebote direkt bei GTBuy!",
                color=0x00ff00
            )
            embed.add_field(name="Dein Affiliate-Link", value=f"[Hier klicken]({gtbuy_url})", inline=False)
            embed.set_footer(text=f"Affiliate Code: {affiliate_code}")
            
            await message.channel.send(embed=embed)

client = MyClient(intents=intents)

# 3. Starten
if __name__ == "__main__":
    keep_alive()
    token = os.getenv("DISCORD_TOKEN")
    if token:
        client.run(token)
    else:
        print("FEHLER: Kein DISCORD_TOKEN gefunden!")
