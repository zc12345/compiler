#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from lex_analyzer import lex_analyzer

# 从文本文档读取输入代码段
try:
    with open("test.txt","r") as input_program:
        print("成功读取文件：")
        line_no = 0
        for line in input_program:
            print("line%d"%line_no,line)
            if line[0] == '#':#跳过#开头的注释
                line_no = line_no + 1
                continue
            else:
                lex_analyzer(line,line_no)
                line_no = line_no + 1
        print("="*20,"源程序读取结束！","="*20)
except IOError as err:
    print("文件读取失败或者文件不存在！")