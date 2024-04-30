# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@author: hou
@time: 2023-01-01
模块注释：
"""
"""
pyecharts 模块
"""

# 导入 pyecharts 模块中的 柱状图 Bar 类
from pyecharts.charts import Bar
import aspose.words as aw

# 导入 配置 相关类
from pyecharts.options import *

# 创建柱状图对象
bar = Bar()

# 设置 x 轴数据
bar.add_xaxis(["河北", "河南", "山东", "山西"])

# 设置 y 轴数据
bar.add_yaxis("GDP", [40391, 58887, 82875, 22870])

# 生成柱状图
bar.render()
pass
# Load an existing Word document
doc = aw.Document("D:\Download\Awesome-pyecharts.htm")

# Specify image save options
# Set save format as PNG
imageOptions = aw.saving.ImageSaveOptions(aw.SaveFormat.PNG)

# Change the image's brightness and contrast.
# Both are on a 0-1 scale and are at 0.5 by default.
imageOptions.image_brightness = 0.3
imageOptions.image_contrast = 0.7

# Save the pages as PNG
for page in range(0, doc.page_count):
    extractedPage = doc.extract_pages(page, 1)
    extractedPage.save(f"Page_{page + 1}.jpg", imageOptions)
pass