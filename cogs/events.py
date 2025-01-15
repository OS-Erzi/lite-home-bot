import discord

from discord.ext import commands

from structs import (
    ButtonMessage,
    CombineView,
    TicketAction,
    Ticket,
    Verify,
    Roles,
    Rules
)

class Events(commands.Cog):
    def __init__(self, client: discord.Client):
        self.client = client
        self.auto_load = [
            ButtonMessage, Ticket,
            TicketAction, Verify,
            CombineView, Roles,
            Rules
        ]
        

    def load_static_view(self) -> bool:
        try:
            for view in self.auto_load:
                self.client.add_view(view())
        except:
            return False
        finally:
            return True

    @commands.Cog.listener()
    async def on_ready(self):
        self.load_static_view()

def setup(client):
    client.add_cog(Events(client))
