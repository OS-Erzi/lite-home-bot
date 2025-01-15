from discord import Embed, Guild, TextChannel
from discord.ext import commands

from structs import (
    ButtonMessage,
    CombineView,
    Ticket,
    Verify,
    Roles,
    Rules
)

from typing import Optional

from core import settings
from logger import loguru_log

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def get_channel(self, guild: Guild, channel_id: int):
        channel = guild.get_channel(channel_id)
        if not channel:
            channel = await guild.fetch_channel(channel_id)
        return channel
    
    @commands.command(name="навигация")
    @commands.has_guild_permissions(administrator=True)
    async def set_navigation(self, ctx: commands.Context):
        embed = Embed(
            color=settings.color.MAIN, 
            description=settings.description.NAVIGATION
        ).set_image(url=settings.images.INVISIBLE_BANNER)

        embed_image = Embed(
            color=settings.color.MAIN
        ).set_image(url=settings.images.NAVIGATION_BANNER)

        try:
            channel = await self.get_channel(ctx.guild, settings.ids.NAVIGATION)
            if not channel:
                raise
        except Exception as e:
            await ctx.message.add_reaction(settings.emoji.NO)
            loguru_log.error(f"Ошибка при поиске канала в гильдии: {e}")
        finally:
            await ctx.message.add_reaction(settings.emoji.YES)
            await channel.send(embeds=[embed_image, embed], view=CombineView())

    @commands.command(name="тикеты")
    @commands.has_guild_permissions(administrator=True)
    async def set_ticket(self, ctx: commands.Context):
        embed = Embed(
            color=settings.color.MAIN, 
            title="➤ Билет обращения", 
            description=settings.description.TICKET
        ).set_image(url=settings.images.INVISIBLE_BANNER)
        embed.set_footer(text="Для открытия билета обращения используйте кнопку ниже.")

        embed_image = Embed(
            color=settings.color.MAIN
        ).set_image(url=settings.images.TICKET_BANNER)

        try:
            channel = await self.get_channel(ctx.guild, settings.ids.TICKET)
            if not channel:
                raise
        except Exception as e:
            await ctx.message.add_reaction(settings.emoji.NO)
            loguru_log.error(f"Ошибка при поиске канала в гильдии: {e}")
        finally:
            await ctx.message.add_reaction(settings.emoji.YES)
            await channel.send(embeds=[embed_image, embed], view=Ticket())

    @commands.command(name="верификация")
    @commands.has_guild_permissions(administrator=True)
    async def set_verify(self, ctx: commands.Context, season: str):
        channel: Optional[TextChannel] = None
        try:
            channel = await self.get_channel(ctx.guild, settings.ids.VERIFY)
            if not channel:
                raise
        except Exception as e:
            await ctx.message.add_reaction(settings.emoji.NO)
            loguru_log.error(f"Ошибка при поиске канала в гильдии: {e}")
        finally:
            await ctx.message.add_reaction(settings.emoji.YES)

            view = Verify()
            embeds = await view.start_func(season)
            await channel.send(embeds=embeds, view=Verify())

    @set_verify.error
    async def set_verify_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{settings.bot.PREFIX}верификация `весна/осень/зима/любое другое` `🌲/🍁/🎄/🌳`")
        else:
            loguru_log.error(f"Произошла неизвестная ошибка: {error}")
            await ctx.send("Произошла неизвестная ошибка. Пожалуйста, свяжитесь с администратором.")
    
    @commands.command(name="правила")
    @commands.has_guild_permissions(administrator=True)
    async def set_rules(self, ctx: commands.Context):
        try:
            channel = await self.get_channel(ctx.message, settings.ids.RULES)
            if not channel:
                raise
        except Exception as e:
            loguru_log.error(f"Ошибка при поиске канала в гильдии: {e}")
            await ctx.message.add_reaction(settings.emoji.NO)
        finally:
            await ctx.message.add_reaction(settings.emoji.YES)

            view = Rules()
            embeds = await view.create_rules_list()
            await channel.send(embeds=embeds, view=view)

    @commands.command(name="роли")
    @commands.has_guild_permissions(administrator=True)
    async def set_roles(self, ctx: commands.Context):
        embed = Embed(
            title="Игровые роли",
            description="・Ниже вы можете выбрать нужные игровые роли.",
            color=settings.color.MAIN,
        )
        embed.set_image(url=settings.images.GAME_ROLES_BANNER)
        
        try:
            channel = await self.get_channel(ctx.guild, settings.ids.ROLES)
            if not channel:
                raise
        except Exception as e:
            loguru_log.error(f"Ошибка при поиске канала в гильдии: {e}")
            await ctx.message.add_reaction(settings.emoji.NO)
        finally:
            await ctx.message.add_reaction(settings.emoji.YES)
            await channel.send(embed=embed, view=Roles())

    @commands.command(name="анонимы")
    @commands.has_guild_permissions(administrator=True)
    async def set_roles(self, ctx: commands.Context):
        embed = Embed(
            description=">           Чатик для анонимного общения",
            color=settings.color.MAIN,
        )
        
        try:
            channel = await ctx.guild.fetch_channel(settings.ids.ANONIM)
            if not channel:
                raise
        except Exception as e:
            loguru_log.error(f"Ошибка при поиске канала в гильдии: {e}")
            await ctx.message.add_reaction(settings.emoji.NO)
        finally:
            await ctx.message.add_reaction(settings.emoji.YES)
            await channel.send(embed=embed, view=ButtonMessage())

def setup(client):
    client.add_cog(Commands(client))
