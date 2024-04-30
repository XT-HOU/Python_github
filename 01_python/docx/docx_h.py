# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@author: hou
@time: 2023-01-01
模块注释：
"""
# -*- coding: utf-8 -*-
import os
import sys
import time
import docx
from docx.enum.dml import MSO_THEME_COLOR_INDEX
from docx.shared import Pt


# 创建一个word文档，并且设置标题和正文的内容和字体
def create_doc():
    doc = docx.Document()

    # 1. 标题
    paragraph_title = doc.add_paragraph()
    run = paragraph_title.add_run("念奴娇·赤壁怀古")
    run.font.name = u'宋体'  # 设置字体
    run.font.bold = True  # 字体粗体
    run.font.size = Pt(32)  # 字体大小
    run.font.color.theme_color = MSO_THEME_COLOR_INDEX.ACCENT_1

    # 2. 正文
    text_str = "大江东去，浪淘尽，千古风流人物。\n\n" + "故垒西边，人道是，三国周郎赤壁。\n\n" + "乱石穿空，惊涛拍岸，卷起千堆雪。\n\n" + "江山如画，一时多少豪杰。\n\n"
    text_str = text_str + "遥想公瑾当年，小乔初嫁了，雄姿英发。\n\n" + "羽扇纶巾，谈笑间，樯橹灰飞烟灭。\n\n" + "故国神游，多情应笑我，早生华发。\n\n" + "人生如梦，一尊还酹江月。\n\n"

    paragraph_content = doc.add_paragraph()
    run = paragraph_content.add_run(text_str)
    run.font.name = u'宋体'  # 设置字体
    run.font.bold = False  # 字体粗体
    run.font.size = Pt(16)  # 字体大小

    # 3.保存为word文档
    doc_name = "念奴娇_赤壁怀古.docx"
    doc.save(doc_name)


if __name__ == '__main__':
    create_doc()