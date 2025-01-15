import asyncio
import os

from discord import Interaction, Member, ButtonStyle, Embed, File
from discord.ui import View, Item, Button, button
from discord.ext import commands
from datetime import datetime

from core import settings
from logger import loguru_log

class TicketAction(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.ticket_handler = None

        self.accepting_button = Button(label="", emoji=settings.emoji.ACCEPT_TICKET, custom_id="accepting")
        self.accepting_button.callback = self.accept_callback
        self.add_item(self.accepting_button)

        self.close_button = Button(label="", emoji=settings.emoji.CLOSE_TICKET, custom_id="close", style=ButtonStyle.danger)
        self.close_button.callback = self.close_callback
        self.add_item(self.close_button)
        
    async def save_history(self, interaction: Interaction):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        channel_id = interaction.channel.id
        
        # Создаем директорию logger/logs/, если она не существует
        log_dir = os.path.join("logger", "tickets")
        os.makedirs(log_dir, exist_ok=True)

        # Формируем имя файла с использованием channel_id
        filename = os.path.join(log_dir, f"Билет-{channel_id}.txt")

        messages = await interaction.channel.history(limit=500).flatten()
        messages.reverse()
        try:
            with open(filename, "w", encoding="utf-8") as file:
                for message in messages:
                    file.write(
                        f"{message.created_at.strftime('%Y-%m-%d %H:%M:%S')} - {message.author.display_name}: {message.clean_content}\n")
        except Exception as e:
            loguru_log.error(f"Ошибка сохраниня логов билета. {e}")
        finally:
            log_channel = interaction.guild.get_channel_or_thread(1215690462162194452)
            if log_channel:
                with open(filename, "rb") as file:
                    await log_channel.send(f"Билет - {interaction.channel.name} был закрыт",
                                        file=File(file, f"{channel_id}.txt"))
            else:
                loguru_log.error("Канал логирования не указан, данные потеряны.")

    def check_perm_roles(self, member: Member) -> bool:
        if not member.guild_permissions.administrator and not any(
            role.id in settings.bot.LIST_ROLE_SUPPORT_FOR_TICKET for role in member.roles
            ):
            return True
        return False

    async def accept_callback(self, interaction: Interaction):
        await interaction.response.defer()
        if self.check_perm_roles(interaction.user):
            raise commands.BadArgument('NotModer')
        self.accepting_button.disabled = True
        await interaction.message.channel.edit(name=interaction.message.channel.name.replace('🟠', '🟢'))
        await interaction.message.channel.set_permissions(interaction.user, read_messages=True, send_messages=True)
        await interaction.followup.send(f'{interaction.user.mention} принял ваш билет')
        await interaction.edit_original_response(view=self)

    async def close_callback(self, interaction: Interaction):
        await interaction.response.defer()
        channel_permissions = interaction.message.channel.permissions_for(interaction.user)
        if not (channel_permissions.read_messages and channel_permissions.send_messages):
            await interaction.followup.send('Это не ваш тикет.', ephemeral=True)
            return

        self.disable_all_items()
        await interaction.edit_original_response(view=self)
        await interaction.message.channel.edit(name=interaction.message.channel.name.replace('🟢', '🔴').replace('🟠', '🔴'))
        await interaction.followup.send(f'{interaction.user.mention} успешно закрыл билет обращения.')
        await asyncio.sleep(5)
        await interaction.message.channel.edit(sync_permissions=True)
        await self.save_history(interaction=interaction)
        await interaction.message.channel.delete(reason='Закрытие билета')

    async def on_error(
            self, error: Exception, item: Item, interaction: Interaction
    ):
        if isinstance(error, commands.BadArgument) and error.args[0] == 'NotStaff':
            e = Embed(color=settings.color.MAIN, description='Данная команда вам не доступна')
            await interaction.followup.send(embed=e, ephemeral=True)
        elif isinstance(error, commands.BadArgument) and error.args[0] == 'NotRank':
            e = Embed(color=settings.color.MAIN, description='Ваш ранг не позволяет совершить данное действие')
            await interaction.followup.send(embed=e, ephemeral=True)
        elif isinstance(error, commands.BadArgument) and error.args[0] == 'NotModer':
            e = Embed(color=settings.color.MAIN, description='Данное действие не достпуно для вашего ранга.')
            await interaction.followup.send(embed=e, ephemeral=True)
        else:
            print(error)

class Ticket(View):
    def __init__(self):
        super().__init__(timeout=None)

    @button(label='Подать билет обращения', emoji='<:ticket:1216008704877531146>', custom_id='ticket', style=ButtonStyle.secondary)
    async def ticket_button(self, button: Button, interaction: Interaction):
        await interaction.response.defer()
        category = interaction.guild.get_channel(settings.ids.TICKET_CATEGORY)

        if category is None:
            await interaction.followup.send('При создании билета произошла ошибка.', ephemeral=True)
            return

        try:
            ticket_channel = await interaction.guild.create_text_channel(name=f'・🟠・{interaction.user.display_name}', category=category)
            await ticket_channel.set_permissions(interaction.user, read_messages=True, send_messages=True)
        except Exception as e:
            loguru_log.error("Бот не смог создать канал в заданной категории.")
        finally:
            embed = Embed(
                color=settings.color.MAIN, 
                description='**Поддержка свяжется с вами в ближайшее время.**\n**Чтобы закрыть этот запрос, нажмите кнопку ниже.**'
            )
            await ticket_channel.send(content=interaction.user.mention, embed=embed, view=TicketAction())