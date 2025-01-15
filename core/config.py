from pydantic_settings import SettingsConfigDict, BaseSettings
from pydantic import BaseModel, Field, HttpUrl, validator

from discord import Color

from typing import Optional
from enum import Enum

class EnvBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

class EmojiEnum(str, Enum):
    CROSS = "✖"
    PLUS = "➕"
    YES = "✔"
    WWDOT = "⚪"

class BotSettings(EnvBaseSettings):
    TOKEN: str
    OWNER_ID: int
    CLIENT_ID: int

    PREFIX: str 
    FOLDER_PATH: str = Field(default="cogs", alias="CUSTOM_COGS_FOLDER")
    LOAD_TITLE: str = "LOAD_TITLE"

    LIST_ROLE_SUPPORT_FOR_TICKET: list = [1026521499424796702, 885096089747861524, 1185205547507654686]

class ColorCFG(EnvBaseSettings):
    MAIN: int = Field(default=0x2b2d31, alias="MAIN_COLOR")
    RULES: int = Field(default=0xffffff, alias="RULES_COLOR")

    @validator("MAIN", "RULES", pre=True)
    def validate_color(cls, v):
        if isinstance(v, str):
            # Если значение - строка, пробуем преобразовать её в целое число
            try:
                return int(v, 16)
            except ValueError:
                raise ValueError("MAIN_COLOR must be a valid hex color code")
        elif isinstance(v, int):
            # Если значение уже целое число, просто возвращаем его
            return v
        else:
            raise ValueError("MAIN_COLOR must be a string or an integer")

class ImagesURL(EnvBaseSettings):
    VERIFY_BANNER: Optional[HttpUrl] = None
    RULES_BANNER: Optional[HttpUrl] = None
    COMMANDS_BANNER: Optional[HttpUrl] = None
    INVISIBLE_BANNER: Optional[HttpUrl] = None

    TICKET_BANNER: Optional[HttpUrl] = None
    NAVIGATION_BANNER: Optional[HttpUrl] = None
    GAME_ROLES_BANNER: Optional[HttpUrl] = None

class IDCfg(EnvBaseSettings):
    OWNER: int = Field(default=0, alias="OWNER_ID")
    GUILDID: int = Field(default=0, alias="GUILD_ID")

    VERIFY: int = Field(default=0, alias="VERIFY_CHANNEL_ID")
    RULES: int = Field(default=0, alias="RULES_CHANNEL_ID")
    TICKET: int = Field(default=0, alias="TICKET_CHANNEL_ID")
    ROLES: int = Field(default=0, alias="ROLES_CHANNEL_ID")
    NAVIGATION: int = Field(default=0, alias="NAVIGATION_CHANNEL_ID")
    ANONIM: int = Field(default=0, alias="ANONIM_CHANNEL_ID")

    TICKET_CATEGORY: int = Field(default=0, alias="ID_CATEGORY_FOR_TICKETS")

    ANONIM_LOG_CHANNEL: int = 0
    ALERT_ROLE: int = Field(default=0, alias="ALERT_ROLE_ID")
    RATE_ROLE: int = Field(default=0, alias="RATE_ROLE_ID")

class EmojiCfg(EnvBaseSettings):
    ACCEPT_TICKET: str = Field(default=EmojiEnum.PLUS, alias="ACCEPT_TICKET")
    CLOSE_TICKET: str = Field(default=EmojiEnum.CROSS, alias="CLOSE_TICKET")

    NO: str = Field(default=EmojiEnum.CROSS, alias="CROSS_EMOJI")
    YES: str = Field(default=EmojiEnum.YES, alias="CHECKMARK_EMOJI")
    WWDOT: str = Field(default=EmojiEnum.WWDOT, alias="STARTMARK_EMOJI")

class DescriptionCfg(EnvBaseSettings):
    ERROR: str = "Ошибка: Неизвестный код | Обратитесь к персоналу | <#1129818461909033010>"
    SUCFULL: str = 'Команда `{0}` выполнена'

    NAVIGATION: str = "Приветствую тебя!\n\nСпасибо, что выбрал Display Duga.\nПриглашаю тебя лучше узнать наш сервер.\n\nЧтобы начать, выбери раздел."
    TICKET: str = "Вы можете открыть свой билет для решения какого-либо\nвопроса касательно нашего сервера."

class Settings(BaseModel):
    bot: BotSettings = Field(default_factory=BotSettings)
    color: ColorCFG = Field(default_factory=ColorCFG)
    ids: IDCfg = Field(default_factory=IDCfg)
    emoji: EmojiCfg = Field(default_factory=EmojiCfg)
    description: DescriptionCfg = Field(default_factory=DescriptionCfg)
    images: ImagesURL = Field(default_factory=ImagesURL)


def get_settings() -> Settings:
    settings = Settings()
    return settings