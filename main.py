#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#from lex_analyzer import lex_input
from test import lex_input
# 从文本文档读取输入代码段
try:
    with open("test.txt","r") as input_program:
        print("成功读取文件：")
        lex_input(input_program)
except IOError as err:
    print("文件读取失败或者文件不存在！")