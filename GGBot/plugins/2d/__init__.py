import json

from nonebot import get_driver, on_command
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.plugin import PluginMetadata
from nonebot.rule import to_me
import requests
# import json

from .config import Config

__plugin_meta = PluginMetadata(
    name="2D",
    description="",
    usage="",
    config=Config,
)

global_config = get_driver().config
config = Config.parse_obj(global_config)

twoD=on_command("二次元", rule=to_me(), aliases={}, priority=10, block=True)

@twoD.handle()
async def handle_function():
    img = get_pic()
    await twoD.send(MessageSegment.image(img))

def get_pic():
    url = 'https://api.vvhan.com/api/acgimg?type=json'
    res = requests.get(url)
    result = json.loads(res.text)
    img = result['imgurl']
    return img