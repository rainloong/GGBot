from PIL import Image, ImageDraw, ImageFont

old_img = Image.open(r"img/原神背景.png")
X, Y = old_img.size
new_img = old_img.resize((600, 400), Image.ANTIALIAS)
draw = ImageDraw.Draw(new_img)
newfont = ImageFont.truetype('font/HanYiTiJian.ttf', 34)

city = "南湖区"
weather = "晴"
temperature = "25"
winddirection = "南"
windpower = "≤3"
humidity = "47"
reporttime = "2023-10-18 14:07:16"


draw.text((40, 50), "旅行者好呀！", font=newfont, fill="blue")
draw.text((40, 100), "时间：" + reporttime, font=newfont, fill="blue")
draw.text((40, 175), "城市：" + city, font=newfont, fill="blue")
draw.text((340, 175), "天气：" + weather, font=newfont, fill="blue")
draw.text((40, 250), "湿度：" + humidity, font=newfont, fill="blue")
draw.text((340, 250), "气温：" + temperature+"℃", font=newfont, fill="blue")
draw.text((40, 325), "风向：" + winddirection + "风", font=newfont, fill="blue")
draw.text((340, 325), "风力：" + windpower + "级", font=newfont, fill="blue")


new_img.show()
