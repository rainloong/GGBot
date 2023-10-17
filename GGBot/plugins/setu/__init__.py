import json

from nonebot import get_driver, on_command
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.plugin import PluginMetadata
from nonebot.rule import to_me
import requests
# import json

from .config import Config

__plugin_meta = PluginMetadata(
    name="setu",
    description="",
    usage="",
    config=Config,
)

global_config = get_driver().config
config = Config.parse_obj(global_config)

setu=on_command("涩图", rule=to_me(), aliases={'色图','setu','黄图'}, priority=10, block=True)

@setu.handle()
async def handle_function():
    img = get_setu()
    await setu.send(MessageSegment.image(img))

def get_setu(tag):
    url = 'https://api.lolicon.app/setu/v2?'+tag
    res = requests.get(url)
    result = json.loads(res.text)
    img = result['data']['urls']['original']
    return img