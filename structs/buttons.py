from discord import Interaction, Embed, ButtonStyle, SelectOption, Color
from discord.ui import button, select, View, Button, Select

from typing import List

from core import settings

from logger import loguru_log

class CombineView(View):
    def __init__(self):
        super().__init__(timeout=None)

    async def commands_callback_func(self, interaction: Interaction):
        set_commands = {
            "Экономика": [
                "`/профиль` - Меню всех систем",
                "`/рейтинг` - Статистика ативности",
                "`/клан` - Команды кланов",
                "`/дуэль` - Объявить дуэль",
                "`/сделать предложение` - Сыграть свадьбу"
            ],
            "Прочие команды": [
                "`/реакция` - Гифка взаимодействия",
                "`/аватар` - Вывести аватар участника",
                "`/помощь` -  Расширеное меню помощи"
            ]
        }
        description_text = ""
        for category, commands in set_commands.items():
            description_text += f"```{category}```\n{settings.emoji.WWDOT}" + f"\n{settings.emoji.WWDOT}".join(commands) + "\n\n"

        description_text += "```Системы постоянно обновляются и некоторые команды могут быть отключены или отсутствовать в списке.```"

        embed = Embed(color=settings.color.MAIN, description=description_text)
        embed.set_image(url=settings.images.COMMANDS_BANNER)

        try:
            await interaction.followup.send(embed=embed, ephemeral=True)
        except Exception as e:
            loguru_log.warning("Бот не смог ответить на интерактивность.")

    
    async def roles_callback_func(self, interaction: Interaction):
        operator_roles = Embed(
            color=settings.color.MAIN, description=(
                "```Служебные роли```\n"
                f"{settings.emoji.WWDOT}<:adm:1210697207578362006>{interaction.guild.get_role(1026521499424796702).mention} - Владелец\n"
                f"{settings.emoji.WWDOT}<:opr:1210697209524256818>{interaction.guild.get_role(1185205547507654686).mention} - Куратор\n"
                f"{settings.emoji.WWDOT}<:mod:1210697211298451476>{interaction.guild.get_role(885096089747861524).mention} - Модерация\n"
                f"{settings.emoji.WWDOT}<:sup:1210697213253124106>{interaction.guild.get_role(1128087010041663559).mention} - Сапорт\n"
                f"{settings.emoji.WWDOT}<:staff:1210697215463661645>{interaction.guild.get_role(1210261190165667993).mention} - Персонал\n"
            )
        ).set_image(url=settings.images.INVISIBLE_BANNER)

        spec_roles = Embed(
            color=settings.color.MAIN, description=(
            f"\n```Спец-роли```\n"
            f"{settings.emoji.WWDOT}<:media:1145326691238035456>{interaction.guild.get_role(1144848875220369469).mention} - Медиа-партнер\n"
            )
        ).set_image(url=settings.images.INVISIBLE_BANNER)

        activity_roles = Embed(
            color=settings.color.MAIN, description=(
            f"\n```Роли активности```\n"
            f"{settings.emoji.WWDOT}<:flame:1210697217388707860>{interaction.guild.get_role(885094070102396938).mention}\n"
            f"{settings.emoji.WWDOT}<:granet:1210697218982420520>{interaction.guild.get_role(789562023624179785).mention}\n"
            f"{settings.emoji.WWDOT}<:purpure:1210697220806934528>{interaction.guild.get_role(888088697583595590).mention}\n"
            f"{settings.emoji.WWDOT}<:lagoon:1210697222648238101>{interaction.guild.get_role(789564066988556308).mention}\n"
            f"{settings.emoji.WWDOT}<:active:1210697224695316591>{interaction.guild.get_role(789561533482139698).mention}\n"
            f"{settings.emoji.WWDOT}<:newbie:1210697226360193076>{interaction.guild.get_role(1155509570941243492).mention}\n"
            )
        ).set_image(url=settings.images.INVISIBLE_BANNER)

        at_roles = Embed(
            color=settings.color.MAIN, description=(
            f"\n```Определяющие роли```\n"
            f"{settings.emoji.WWDOT}<:rings:1291786302127083570>{interaction.guild.get_role(1289519797515714561).mention} - роль супругов\n"
            f"{settings.emoji.WWDOT}<:18:1164942551090999398>{interaction.guild.get_role(1143498221805649990).mention} - возрастная роль\n"
            f"{settings.emoji.WWDOT}<:mars:1215613011012755466>{interaction.guild.get_role(1129171280386588682).mention} - гендерная роль\n"
            f"{settings.emoji.WWDOT}<:venus:1215613014271590420>{interaction.guild.get_role(1129171315027353781).mention} - гендерная роль\n"
            f"{settings.emoji.WWDOT}<:at:1215613008567476234>{interaction.guild.get_role(1070799191175090229).mention} - пинг роль\n"
            )
        ).set_image(url=settings.images.INVISIBLE_BANNER)

        donate_roles = Embed(
            color=settings.color.MAIN, description=(
            f"\n```Роли поддержки сервера```\n"
            f"{settings.emoji.WWDOT}<:cristal_miku_pink:1143216584605847674>{interaction.guild.get_role(852844600862965800).mention} - роль бустера сервера\n"
            f"{settings.emoji.WWDOT}<:cristal_miku:1143216561214197841>{interaction.guild.get_role(1080780049147506718).mention} - роль донатера сервера\n"
            )
        ).set_image(url=settings.images.INVISIBLE_BANNER)

        other_roles = Embed(
            color=settings.color.MAIN, description=(
            f"\n```Прочие роли```"
            f"```На сервере действует система кланов, временных значков и кастомных ролей. Для получения подробной информации используйте команду /помощь.```"
            )
        ).set_image(url=settings.images.INVISIBLE_BANNER)

        try:
            await interaction.followup.send(embeds=[operator_roles, spec_roles, activity_roles, at_roles, donate_roles, other_roles], ephemeral=True)
        except Exception as e:
            loguru_log.warning("Бот не смог ответить на интерактивность.")

    async def channels_callback_func(self, interaction: Interaction):
        embed1 = Embed(
            color=settings.color.MAIN, description=(
                "```Информация```\n"
                "<#1152370942459265094> - навигация по сервера\n"
                "<#1255768631506374687> - свод правил сервера\n"
                "<#1052999397933338675> - посты с новостями сервера\n"
                "<#1130010811482521641> - выбрать роли для профиля\n"
                "<#1055456631346974720> - поддержать сервер монетой\n"
                "<#887634994095333376> - розыгрыши проводимые персоналом\n"
            )
        ).set_image(url=settings.images.INVISIBLE_BANNER)

        embed2 = Embed(
            color=settings.color.MAIN, description=(
                "\n```Сервер```\n"
                "<#1255769036839583795> - оставить заявку на роли персонала сервера\n"
                "<#1255769104573272145> - отправить билет обращения к персоналу\n"
                "<#1255769163151183943> - советы по улучшению сервера\n"
            )
        ).set_image(url=settings.images.INVISIBLE_BANNER)

        embed3 = Embed(
            color=settings.color.MAIN, description=(
                "\n```Ивенты```\n"
                "<#1129818771087962123> Анонсы событий\n"
                "<#1129818848049238157> Трибуна событий\n"
            )
        ).set_image(url=settings.images.INVISIBLE_BANNER)
        
        embed4 = Embed(
            color=settings.color.MAIN, description=(
                "\n```Чаты```\n"
                "<#851561175261904906> - главный чатик сервера\n"
                "<#1129819092849786901> - управление экономикой\n"
                "<#1215361619417374791> - чат анонимного для общения\n"
                "<#1210276717353115708> - работа с нейросетью\n"
                "<#1053010366906499153> - Место для флуда\n"
            )
        ).set_image(url=settings.images.INVISIBLE_BANNER)
        
        embed5 = Embed(
            color=settings.color.MAIN, description=(
                "\n```Интересное```\n"
                "<#1129819439764869130> - полезные статейки\n"
                "<#1255769340255404093> - поиск тимейтов\n"
                "<#708983964001632307> - галерея скришнотов\n"
                "<#1217534390876377138> - место для творчества\n"
            )
        ).set_image(url=settings.images.INVISIBLE_BANNER)
        
        embed6 = Embed(
            color=settings.color.MAIN, description=(
                "\n```Приватные каналы```\n"
                "<#1204755658180927529> - настройка временного канала\n"
                "<#1204755659850252328> - создание временного канала\n"
            )
        ).set_image(url=settings.images.INVISIBLE_BANNER)

        embed7 = Embed(
            color=settings.color.MAIN, description=(
                "\n```Кланы```\n"
                "<#1221537889188319303> - управление своим кланом\n"
            )
        ).set_image(url=settings.images.INVISIBLE_BANNER)

        try:
            await interaction.followup.send(embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7], ephemeral=True)
        except Exception as e:
            loguru_log.warning("Бот не смог ответить на интерактивность.")

    @select(placeholder="Выберите нужное", max_values=1, custom_id="navigation", min_values=1, options=[
            SelectOption(label="Команды сервера", value="coms", emoji="<:code:1216006960009318610>"),
            SelectOption(label="Роли сервера", value="roles", emoji="<:rolemasks:1216006209388150916>"),
            SelectOption(label="Каналы сервера", value="channels", emoji="<:channels:1216006207203053659>")
            ])
    async def select_menu_callback(self, select: Select, interaction: Interaction):
        await interaction.response.edit_message(view=self)
        argm_list = {
            "coms": self.commands_callback_func,
            "roles": self.roles_callback_func,
            "channels": self.channels_callback_func
        }
        await argm_list[select.values[0]](interaction)

    @button(label=" ", custom_id="alerts", style=ButtonStyle.gray, emoji="<:at:1215613008567476234>")
    async def button3_callback(self, Button: Button, interaction: Interaction):
        await interaction.response.defer()
        role_obj = interaction.guild.get_role(settings.ids.ALERT_ROLE)
        
        try:
            if role_obj is None:
                embed = Embed(color=Color.red(), description="Ошибка: \"Уведомления\" не найдена")
                await interaction.followup.send(embed=embed, ephemeral=True)
                loguru_log.warning("Роль Уведомлений не найдена.")
                return

            if role_obj in interaction.user.roles:
                await interaction.user.remove_roles(role_obj)
                e = Embed(color=settings.color.MAIN, description=f"Роль {role_obj.mention} была удалена")
                await interaction.followup.send(embed=e, ephemeral=True)
            else:
                await interaction.user.add_roles(role_obj)
                e = Embed(color=settings.color.MAIN, description=f"Роль {role_obj.mention} была добавлена")
                await interaction.followup.send(embed=e, ephemeral=True)
        except Exception as e:
            loguru_log.warning("Бот не имеет достаточно прав для выдачи ролей.")

    @button(label=" ", custom_id="nsfw", style=ButtonStyle.gray, emoji="<:18:1164942551090999398>")
    async def button4_callback(self, Button: Button, interaction: Interaction):
        await interaction.response.defer()
        role_obj = interaction.guild.get_role(settings.ids.RATE_ROLE)
    
        try:
            if role_obj is None:
                e = Embed(color=Color.red(), description="Ошибка: Роль 18+ не найдена")
                await interaction.followup.send(embed=e, ephemeral=True)
                loguru_log.warning("Роль Возратного определения не найдена.")
                return

            if role_obj in interaction.user.roles:
                await interaction.user.remove_roles(role_obj)
                e = Embed(color=settings.color.MAIN, description=f"Роль {role_obj.mention} была удалена")
                await interaction.followup.send(embed=e, ephemeral=True)
            else:
                await interaction.user.add_roles(role_obj)
                e = Embed(color=settings.color.MAIN, description=f"Роль {role_obj.mention} была добавлена")
                await interaction.followup.send(embed=e, ephemeral=True)
        except Exception as e:
            loguru_log.warning("Бот не имеет достаточно прав для выдачи ролей.")

class Roles(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    async def edit_user_roles_func(self, interaction: Interaction) -> None:
        role_ids = interaction.data["values"]
        roles = [interaction.guild.get_role(int(role_id)) for role_id in role_ids]

        for role in roles:
            if role in interaction.user.roles:
                await interaction.user.remove_roles(role, reason="Выбор игровой роли")
            else:
                await interaction.user.add_roles(role, reason="Выбор игровой роли")
        
    @select(placeholder="Выберите нужное", max_values=19, min_values=0, custom_id="roles", options=[
        SelectOption(label="Apex", value="1194478734892339300", emoji=settings.emoji.WWDOT),
        SelectOption(label="Battlefield", value="1071743262655787078", emoji=settings.emoji.WWDOT),
        SelectOption(label="Counter Strike 2", value="885759236322250752", emoji=settings.emoji.WWDOT),
        SelectOption(label="Dayz", value="887651961682415636", emoji=settings.emoji.WWDOT),
        SelectOption(label="Dead by Daylight", value="1071741847824773251", emoji=settings.emoji.WWDOT),
        SelectOption(label="Dota 2", value="1026606302144770108", emoji=settings.emoji.WWDOT),
        SelectOption(label="Escape from Tarkov", value="1194479057664999494", emoji=settings.emoji.WWDOT),
        SelectOption(label="Garry\'s mod", value="887650842113634304", emoji=settings.emoji.WWDOT),
        SelectOption(label="Genshin Impact", value="887651719624937482", emoji=settings.emoji.WWDOT),
        SelectOption(label="GTA online", value="887657104138207313", emoji=settings.emoji.WWDOT),
        SelectOption(label="Hearts of Iron 4", value="887651481296199690", emoji=settings.emoji.WWDOT),
        SelectOption(label="Hunt: Showdown", value="1128092541519134820", emoji=settings.emoji.WWDOT),
        SelectOption(label="Minecraft", value="887651191704662067", emoji=settings.emoji.WWDOT),
        SelectOption(label="Osu", value="1070736521486946345", emoji=settings.emoji.WWDOT),
        SelectOption(label="Phasmophobia", value="1071743259191287828", emoji=settings.emoji.WWDOT),
        SelectOption(label="Pubg", value="972477227071594510", emoji=settings.emoji.WWDOT),
        SelectOption(label="Rust", value="1071742107326369903", emoji=settings.emoji.WWDOT),
        SelectOption(label="StalCraft", value="1209850945719238697", emoji=settings.emoji.WWDOT),
        SelectOption(label="Valorant", value="887650690544074763", emoji=settings.emoji.WWDOT),
        SelectOption(label="Warframe", value="933323293300248587", emoji=settings.emoji.WWDOT),
        SelectOption(label="War Thunder", value="1071741252778852443", emoji=settings.emoji.WWDOT),
    ])
    async def select_rol_menu_callback(self, select: Select, interaction: Interaction):
        try:
            await interaction.response.edit_message(view=self)
            await self.edit_user_roles_func(interaction)
        except Exception as e:
            loguru_log.error("Возникла ошибка, бот не моет редактировать роли")
        finally:
            embed = Embed(color=settings.color.MAIN, description="Выбранные роли успешно добавлены в профиль.")
            embed.set_image(url=settings.images.INVISIBLE_BANNER)
            await interaction.followup.send(embed=embed, ephemeral=True)

class Verify(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @staticmethod
    async def start_func(season: str) -> Embed:
        stik = {"весна": "🌲", "осень": "🍁", "зима": "🎄"}
        stiker = stik.get(season, "🌳")
        embeds = []

        embed = Embed(color=settings.color.MAIN).set_image(url=settings.images.VERIFY_BANNER)
        embeds.append(embed)

        embed = Embed(
            color=settings.color.MAIN,
            description="Для получения доступа к серверу пожалуйста\nподтвердите что вы человек пройдя **верификацию**."
        )
        embed.set_footer(text="Для прохождения верификации используйте кнопку ниже.")
        embed.set_image(url=settings.images.INVISIBLE_BANNER)

        embeds.append(embed)
        return embeds
    
    @button(label="Верификация", custom_id="verify", style=ButtonStyle.gray, emoji="<:verify:1164956498917605517>")
    async def button1_callback(self, button: Button, interaction: Interaction):
        await interaction.response.defer()
        role = interaction.guild.get_role(1155509570941243492)
        try:
            await interaction.user.add_roles(role)
            await interaction.followup.send("В канале <#1152370942459265094> вы можите ознакомится с информацией о серверe.", ephemeral=True)
        except:
            loguru_log.warning("Бот не имеет достаточно прав для выдачи ролей.")


class Rules(View):
    def __init__(self):
        super().__init__(timeout=None)

        self.memo_button = Button(label="Дополнение", custom_id="memo", emoji="<:info:1274962773008191490>")
        self.memo_button.callback = self.memo_callback
        self.add_item(self.memo_button)
    
    @staticmethod
    async def create_rules_list() -> List[Embed]:
        embeds = []
        #Start embed
        start_embed = Embed(
            title="Политика сервера.", 
            color=settings.color.RULES, 
            description="После входа на сервер, "
                        "вы автоматически "
                        "соглашаетесь и принимаете "
                        "правила/положение "
                        "сервера.\n\nНаш сервер "
                        "придерживается всех "
                        "официальных правил "
                        "Discord-серверов, "
                        "потому следует прежде "
                        "всего просмотреть ссылки "
                        "ниже:"
                        "\n\n[・Terms of Service]("
                        "https://discord.com/terms)\n[・Community Guidelines](https://discord.com/guidelines)")
        start_embed.set_image(url=settings.images.RULES_BANNER)
        embeds.append(start_embed)

        #Правила
        rules_argument_list = [
            {
                "description": "```ansi\n[2;34m[1.1][0m Незнание правил не освобождает от ответственности.```",
                "author": "1. Общие правила",
                "image_url": False
            },
            {
                "description": "```ansi\n[2;34m[1.2][0m Запрещается вводить в заблуждение членов команды и других пользователей проекта. Запрещается провоцировать на нарушение правил.```",
                "author": None,
                "image_url": False
            },
            {
                "description": "```ansi\n[2;34m[1.3][0m Запрещено распространение личной информации, без согласия её владельца.```",
                "author": None,
                "image_url": False
            },
            {
                "description": "```ansi\n[2;34m[1.4][0m Запрещено бурное обсуждение политики, а также негативные высказывания, ведущие к конфликту, дискриминации или розни. Запрещено также распространение нацистской символики, в том числе в профиле.```",
                "author": None,
                "image_url": False
            },
            {
                "description": "```ansi\n[2;34m[1.5][0m Запрещена реклама сторонних проектов, каналов Discord, сомнительных интернет ресурсов, и др.```",
                "author": None,
                "image_url": False
            },
            {
                "description": "```ansi\n[2;34m[1.6][0m Запрещено задавать личные вопросы после отказа человека на них отвечать.```",
                "author": None,
                "image_url": False
            },
            {
                "description": "```ansi\n[2;34m[1.7][0m Запрещен спам, флуд, оффтоп и мультипостинг.```",
                "author": None,
                "image_url": False
            },
            {
                "description": "```ansi\n[2;34m[1.8][0m Запрещено попрошайничать или выпрашивать что-либо у участников сервера и персонала сервера, в особенности после отказа.```",
                "author": None,
                "image_url": False
            },
            {
                "description": "```ansi\n[2;34m[1.9][0m Запрещена неконструктивная критика в сторону администрации, призывы покинуть сервер, попытки обмана администрации.```",
                "author": None,
                "image_url": False
            },
            {
                "description": "```ansi\n[2;34m[1.10][0m Запрещена пропаганда наркотиков, терроризма, материалов, содержащих сцены сексуального характера и т.п. Так же запрещено прямо или косвенно восхвалять суицид и всё выше перечисленного.```",
                "author": None,
                "image_url": False
            },
            {
                "description": "```ansi\n[2;34m[1.11][0m Запрещено размещать и распространять шокирующий, аморальный, сексуальный контент, а так же контент вызывающий эпилептические приступы.```",
                "author": None,
                "image_url": False
            },
            {
                "description": "```ansi\n[2;34m[1.12][0m Не провоцируйте и не поддерживайте развитие конфликтных ситуаций.```",
                "author": None,
                "image_url": True
            },
            {
                "description": "```ansi\n[2;34m[2.1][0m Запрещено транслировать контент, запрещенный правилами сервера (пункт 1.11).```",
                "author": "2. Голосовые каналы",
                "image_url": False
            },
            {
                "description": "```ansi\n[2;34m[2.2][0m Запрещено злоупотреблять программными средства для трансляции медиа SoundPad и тп.```",
                "author": None,
                "image_url": False
            },
            {
                "description": "```ansi\n[2;34m[2.3][0m Запрещено использовать нецензурную брань в оскорбительных целях. Злоупотреблять матом, мешая общению и комфорту других пользователей. Вести непристойные, аморальные разговоры.```",
                "author": None,
                "image_url": True
            },
            {
                "description": "```ansi\n[2;34m[3.1][0m Запрещено чрезмерное упоминание ролей / пользователей без веской причины.```",
                "author": "3. Текстовые каналы",
                "image_url": False
            },
            {
                "description": "```ansi\n[2;34m[3.2][0m Запрещено распространять контент запрещенный правилами сервера (пункт 1.11).```",
                "author": None,
                "image_url": False
                
            },
            {
                "description": "```ansi\n[2;34m[3.3][0m Запрещено использовать транслит при общении (Исключение короткие английские фразы - ok). Так же запрещено использовать иные языки кроме русского в основных чатах.```",
                "author": None,
                "image_url": False
            },
            {
                "description": "```ansi\n[2;34m[4.1][0m Приватный канал считается таковым, если он был закрыт владельцем.```",
                "author": "4. Приватные каналы", 
                "image_url": True
            }
        ]

        embed = Embed(color=settings.color.RULES)
        for args in rules_argument_list:
            if args["image_url"]:
                embed.set_image(url=settings.images.RULES_BANNER)
                embeds.append(embed)
                
                embed = Embed(color=settings.color.RULES)
            else:
                embed.set_image(url=settings.images.INVISIBLE_BANNER)
                if args["author"]:
                    embed.set_author(name=args["author"])
                
                embed.add_field(name="", value=f"{args['description']}", inline=False)

        # Отправляем оставшийся эмбед, если он содержит поля
        if len(embed.fields) > 0 or embed.author:
            embed.set_image(url=settings.images.INVISIBLE_BANNER)
            embeds.append(embed)
        return embeds

    @staticmethod
    def get_color(number: int) -> str:
        number = f"ansi\n[2;34m[{number}][0m"
        return number
    
    #callback func
    async def memo_callback(self, interaction: Interaction):
        await interaction.response.defer()
        argm_embed_list = [
            {
                "description": "```{0} Оскорбления — это любые проявления ненормативной лексики или уничижительных выражений в адрес других участников, включая завуалированные намёки.```",
                "author": "Термины",
                "image": False
            },
            {
                "description": "```{0} Троллинг — это преднамеренная провокация и насмешка в интернет-общении.```",
                "author": None,
                "image": False
            },
            {
                "description": "```{0} Завуалированный мат — это использование ненормативных слов, заменённых на аналогичные, но с очевидным смыслом. Замена символов также считается нарушением.```",
                "author": None,
                "image": False
            },
            {
                "description": "```{0} Спам — это повторяющиеся сообщения, которые имеют минимальные отличия.```",
                "author": None,
                "image": False
            },
            {
                "description": "```{0} Флуд — это неструктурированный поток текста, заполняющий текстовое или голосовое пространство.```",
                "author": None,
                "image": False
            },
            {
                "description": "```{0} Оффтоп — это сообщения, которые не соответствуют теме конкретного текстового канала. Например, обсуждение в канале, предназначенном для другой темы, или отправка неуместных материалов.```",
                "author": None,
                "image": False
            },
            {
                "description": "```{0} Мультипостинг — это отправка нескольких сообщений от одного участника за короткий промежуток времени, которые составляют единое целое.```",
                "author": None,
                "image": True
            },
            {
                "description": "```{0} Запрещено использовать ники и названия, которые:\n› имеют оскорбительный или аморальный смысл;\n› содержат слова \"Админ\", \"Модер\" и подобные;\n› включают ненормативную лексику;\n› используют запрещённые символы;\n› касаются тем, связанных с суицидом.\nАдминистрация оставляет за собой право запрещать любые другие слова и символы.```",
                "author": "Памятка",
                "image": False
            },
            {
                "description": "```{0} Запрещено использовать оскорбительные, порнографические или нецензурные изображения в качестве аватаров и баннеров. Администрация может запретить любые изображения по своему усмотрению.```",
                "author": None,
                "image": False
            },
            {
                "description": "```{0} Права одного человека заканчиваются там, где начинаются права другого. Уважайте собеседников, избегайте неприятных тем и оскорбительных высказываний. Взаимопонимание и уважение — основа нашего общения.```",
                "author": None,
                "image": False
            },
            {
                "description": "```{0} Запрещены действия, которые нарушают работу сервера и его правила. Это включает сообщения типа \"Умею дюпать питомцев\", а также распространение багов и глюков.```",
                "author": None,
                "image": False
            },
            {
                "description": "```{0} Запрещено раскрытие личной информации пользователей без их согласия, включая ФИО, адреса, места работы и учёбы, а также фотографии, на которых видно лицо пользователя.```",
                "author": None,
                "image": False
            },
            {
                "description": "```{0} Запрещено использование громких и резких звуков, музыки, фонов шума и криков в голосовых каналах. Перед входом в голосовой канал убедитесь, что ваш микрофон работает корректно.```",
                "author": None,
                "image": False
            },
            {
                "description": "```{0} Запрещена реклама (в том числе в личных сообщениях), обсуждение других серверов и проектов, а также использование статусов и ников с приглашениями на другие серверы без согласия администрации.```",
                "author": None,
                "image": False
            },
            {
                "description": "```{0} Участники обязаны соблюдать правила поведения во время мероприятий. Не допускается использование оскорбительных выражений, спама и флуда.```",
                "author": None,
                "image": False
            },
            {
                "description": "```{0} В голосовых каналах во время мероприятий необходимо соблюдать тишину до получения слова. Уважайте других участников и их право на высказаться.```",
                "author": None,
                "image": False
            },
            {
                "description": "```{0} Администрация оставляет за собой право временно или навсегда блокировать пользователей, нарушающих правила. В случае конфликта, обращайтесь к администрации для разрешения ситуации.```",
                "author": None,
                "image": False
            },
            {
                "description": "```{0} Все участники должны быть готовы к изменениям в правилах. Объявления о изменениях будут размещены в соответствующем канале.```",
                "author": None,
                "image": True
            },
        ]
        
        embeds = []
        memo_list = []
        embed = Embed(color=settings.color.MAIN)
        for index, args in enumerate(argm_embed_list, start=1):
            memo_list.append(args['description'])
            if args["image"]:
                embed.set_image(url=settings.images.INVISIBLE_BANNER)
                embeds.append(embed)
                
                embed = Embed(color=settings.color.MAIN)
            else:
                embed.set_image(url=settings.images.INVISIBLE_BANNER)
                if args["author"]:
                    embed.set_author(name=args["author"])
                
                embed.add_field(name="", value=f"{args['description'].format(self.get_color(index))}", inline=False)

        # Отправляем оставшийся эмбед, если он содержит поля
        if len(embed.fields) > 0 or embed.author:
            embed.set_image(url=settings.images.INVISIBLE_BANNER)
            embeds.append(embed)
    
        await interaction.followup.send(embeds=embeds, ephemeral=True)

