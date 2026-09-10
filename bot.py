import os
import discord

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

if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN")
    if token:
        client.run(token)
    else:
        print("FEHLER: Kein DISCORD_TOKEN gefunden!")
