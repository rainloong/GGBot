from nonebot import get_driver,on_command
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.rule import to_me

import requests

from .config import Config

__plugin_meta = PluginMetadata(
    name="weather",
    description="",
    usage="",
    config=Config,
)

global_config = get_driver().config
config = Config.parse_obj(global_config)


weather = on_command("天气", rule=to_me(), aliases={"weather", "查天气"}, priority=10, block=True)

async def get_img():
    url = 'https://api.vvhan.com/api/ip'
    img = requests.get(url)
    return img

@weather.handle()
async def handle_function():
    img=get_img()
    await weather.send(MessageSegment.image(img))