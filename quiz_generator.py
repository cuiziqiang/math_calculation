#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:42:36 2020
@author: qiang.wei
"""

import random
import numpy as np
import time


symbol = ['add', 'subtract', 'multiply', 'divide', 'divide2']
def add(maxsum = 1000):
    first = random.randint(30, maxsum - 10)
    sum_ = random.randint(first + 10, maxsum)
    second = sum_ - first
    line = '$' + str(first) + '+' + str(second) + '=$\\\\\n'
    return line

def subtract(maxsub = 1000):
    second = random.randint(30, maxsub-5)
    first = random.randint(second+5, maxsub)
    line = '$' + str(first) + '-' + str(second) + '=$\\\\\n'
    return line


def multiply():
    second = random.randint(2, 100)
    first = random.randint(2, 9)
    line = '$' + str(first) + '\\times ' + str(second) + '=$\\\\\n'
    return line

def divide():
    second = random.randint(5, 100)
    first = random.randint(2, 9)*second
    line = '$' + str(first) + '\\div ' + str(second) + '=$\\\\\n'
    return line

def divide2():
    second = random.randint(5, 100)
    first = random.randint(1, 9)*second + random.randint(1, second-1)
    line = '$' + str(first) + '\\div ' + str(second) + '=$\\\\\n'
    return line

def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]) #去除[],这两行按数据不同，可以选择
        file.write(s)
    file.close()
    print("保存文件成功")


def main():   
    switch = {'add': add,
              'subtract': subtract,
              'multiply': multiply,
              'divide': divide,
              'divide2': divide2
              }
    lines = []
    i = 0
    while i < 15:
        item=[]
        j = 0
        while j < 50:
            a = random.randint(0,4)
            item.append(switch.get(symbol[a], divide2)())
            j = j + 1
        lines.append(item)
        i = i + 1
    matrix = np.array(lines)

    # doc = Document()
    # paragraph = doc.add_heading('',level=0)  
    # run = paragraph.add_run(text="小学生口算练习题", style=None)
    # paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    # run.font.name = '宋体'
    # run._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
    # run.font.size= Pt(20)
    # time_ = time.asctime( time.localtime(time.time()) )
    # print(time_)
    # paragraph.add_run(text=time_, style=None).font.size= Pt(10)
    # table = doc.add_table(matrix.shape[0], matrix.shape[1], style=None)
    file = open('math.txt','w')
    file.write(' ')
    file.close()

    for i in range(matrix.shape[0]):
        j = 0
        for j in range(matrix.shape[1]):
            # table.cell(i, j).paragraphs[0].add_run(text=str(lines[i][j]), style=None).font.size= Pt(14)
            text_save('math.txt', lines[i][j])
    # doc.save('小学生口算练习题.docx')







if __name__ == '__main__':
    main()