import json
from pathlib import Path

from nonebot import get_driver, on_command
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.rule import to_me
from nonebot.adapters import Message
from nonebot.params import CommandArg

from PIL import Image, ImageDraw, ImageFont
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

weather = on_command("天气", aliases={"weather", "查天气"}, priority=10, block=True)


@weather.handle()
async def handle_function(args: Message = CommandArg()):
    # url = 'https://api.vvhan.com/api/ip'
    if city := args.extract_plain_text():
        url = "https://restapi.amap.com/v3/weather/weatherInfo?key=dae0a34e7240bace0cfe82441c6d5765&city=" + city
    res = requests.get(url)
    result = json.loads(res.text)
    if result['lives'] == []:
        txt = "收复" + city + "，指日可待"
        await weather.finish(MessageSegment.text(txt))
    wea = result['lives'][0]['weather']
    temperature = result['lives'][0]['temperature']
    winddirection = result['lives'][0]['winddirection']
    humidity = result['lives'][0]['humidity']
    reporttime = result['lives'][0]['reporttime']
    windpower = result['lives'][0]['windpower']

    get_back(city, wea, temperature, winddirection, humidity, reporttime, windpower)
    path = Path("img/天气.png")
    await weather.send(MessageSegment.image(path))


def get_back(city, weather, temperature, winddirection, humidity, reporttime, windpower):
    old_img = Image.open(r"img/原神背景.png")
    X, Y = old_img.size
    new_img = old_img.resize((600, 400), Image.ANTIALIAS)
    draw = ImageDraw.Draw(new_img)
    newfont = ImageFont.truetype('font/HanYiTiJian.ttf', 34)

    draw.text((40, 50), "旅行者好呀！", font=newfont, fill="blue")
    draw.text((40, 100), "测定时间：" + reporttime, font=newfont, fill="blue")
    draw.text((40, 175), "城市：" + city, font=newfont, fill="blue")
    draw.text((340, 175), "天气：" + weather, font=newfont, fill="blue")
    draw.text((40, 250), "湿度：" + humidity, font=newfont, fill="blue")
    draw.text((340, 250), "气温：" + temperature + "℃", font=newfont, fill="blue")
    draw.text((40, 325), "风向：" + winddirection + "风", font=newfont, fill="blue")
    draw.text((340, 325), "风力：" + windpower + "级", font=newfont, fill="blue")
    new_img.save("img/天气.png")
    return ""
