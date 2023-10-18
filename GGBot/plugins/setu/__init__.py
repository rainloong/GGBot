import json

from nonebot import get_driver, on_command
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.plugin import PluginMetadata
from nonebot.rule import to_me
from nonebot.adapters import Message
from nonebot.params import CommandArg
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

setu = on_command("涩图", aliases={'色图', 'setu', '黄图'}, priority=10, block=True)


@setu.handle()
async def handle_function(args: Message = CommandArg()):
    tag = []
    if location := args.extract_plain_text():
        for t in location:
            if t == " ":
                tag = location.split(" ")
                break
        if tag == [] and location != "":
            tag.append(location)
    img = get_setu(tag)
    if img == '':
        await setu.send(MessageSegment.text("你咋想的"))
        await setu.send(MessageSegment.text("这图有没有你心里没数吗"))
    else:
        await setu.send(MessageSegment.image(img))


def get_setu(tag):
    url = 'https://api.lolicon.app/setu/v2?'
    if tag == []:
        url = url
    else:
        for i in tag:
            if str(0) <= i <= str(2):
                url = url + "r18=" + i +'&'
            else:
                url = url + "tag=" + i + '&'
    res = requests.get(url)
    result = json.loads(res.text)
    if result['data'] == []:
        return ""
    else:
        print(url)
        print(result)
        img = result['data'][0]['urls']['original']
        return img
