#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PIL:Python Imaging Library
from PIL import Image

# 打开一个png图像文件，（当前路径）
im = Image.open('./day13/advanced.png')
# 获得图像尺寸
w, h = im.size
print('Origin image size %s X %s' % (w, h))
# 缩放到50%
im.thumbnail((w/2, h/2))
print('Resize image to: %s X %s' % (w/2, h/2))
# im.sava('thumbnail.png', 'png')

# 模糊效果
from PIL import Image, ImageFilter
im = Image.open('./day13/advanced.png')
# 应用模糊
im2 = im.filter(ImageFilter.BLUR)
# im2.sava('blur.png', 'png')

# PIL的ImageDraw提供了一系列的绘图方法，
# 生成字母验证码
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def rndChar():
	return char(random.randint(65, 90))
# 随机颜色
def rndColor():
	return (random.randint(64, 255), random(64, 255), random(64, 255))
	
# 随机颜色2
def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
# 240 x 60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('/opt/openoffice4/share/fonts/truetype/Arimo-Italic.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')