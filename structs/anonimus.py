from discord import Interaction, InputTextStyle, Embed
from discord.ui import button, View, InputText, Modal
from asyncio import create_task

from core import settings

from logger import loguru_log

class ButtonMessage(View):
    def __init__(self):
        super().__init__(timeout=None)

    @button(label="", emoji="<:plus:1202579798090715186>", custom_id="send_anonim")
    async def send_anonim_message(self, b, interaction: Interaction):
        await interaction.response.send_modal(ModalMessage())

class ModalMessage(Modal):
    def __init__(self):
        super().__init__(timeout=None, title='Анонимное сообщение')
        self.add_item(
            InputText(
                label='Сообщение',
                style=InputTextStyle.long,
                placeholder='Вы так же можете использовать упоминания.\n<@id-пользователя>\n<#id-канала>'
            )
        )
    
    async def logging(self, interaction: Interaction):
        channel = interaction.guild.get_channel_or_thread(settings.ids.ANONIM_LOG_CHANNEL)
        if not channel:
            channel = await interaction.guild.fetch_channel()
            if not channel:
                loguru_log.warning("Канал логирования сообщений анонимных каналов не найден")
                return
        embed = Embed(
            color=settings.color.MAIN, 
            description=f"```{self.children[0].value}```"
        ).set_author(name=interaction.user.display_name, url=interaction.user.display_avatar)
        await channel.send(embed=embed)

    async def callback(self, interaction: Interaction):
        await interaction.response.defer()
        create_task(self.logging(interaction))

        content = self.children[0].value
        embed = Embed(
            color=settings.color.MAIN, 
            description=content
        )
        await interaction.message.channel.send(embed=embed, view=ButtonMessage())
