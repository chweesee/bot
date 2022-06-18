import disnake
from disnake.ext import commands
from disnake.utils import get


class Funni(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="ping", description="Gives the ping, I guess.")
    async def ping(self, ctx: disnake.ApplicationCommandInteraction):
        await ctx.response.send_message("I'm not here to play table tennis, dumbass.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def echo(self, ctx, message_id, *, content):

        await ctx.message.delete()
		
        if message_id == "none":
            await ctx.send(content=content, files=[await a.to_file() for a in ctx.message.attachments])
        else:
            message = await self.client.fetch_message(int(message_id))
            await message.reply(content=content, files=[await a.to_file() for a in ctx.message.attachments])

    @echo.error
    async def nomentionlinkoss(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            pass

def setup(client):
    client.add_cog(Funni(client))
