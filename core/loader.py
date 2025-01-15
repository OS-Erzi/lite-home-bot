from discord import Intents, CustomActivity

from .base import ProjectType
from core import settings

class ProjectRun(ProjectType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

def start_loader():
    intents = Intents.all()
    activity = CustomActivity(name="Мульти-бот система")
    bot = ProjectRun(intents=intents, activity=activity, command_prefix=settings.bot.PREFIX)
    bot.run(settings.bot.TOKEN)