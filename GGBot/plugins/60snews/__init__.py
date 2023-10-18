from nonebot import get_driver, on_command
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.plugin import PluginMetadata
from nonebot.rule import to_me

from .config import Config

__plugin_meta = PluginMetadata(
    name="60snews",
    description="",
    usage="",
    config=Config,
)

global_config = get_driver().config
config = Config.parse_obj(global_config)

news = on_command("新闻", aliases={"news", "60s", "今日新闻"}, priority=10, block=True)

@news.handle()
async def handle_function():
    url = 'https://api.vvhan.com/api/60s'
    await news.send(MessageSegment.image(url))
