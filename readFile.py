#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@author:    anke
@contact:   anke.wang@foxmail.com
@file:      readFile.py
@time:      2019/11/26 4:42 PM

@desc:      读取搜狗文件并进行相关操作
            搜狗日志：https://www.sogou.com/labs/resource/ftp.php?dir=/Data/SogouQ/SogouQ.zip
            
            访问时间\t用户ID\t[查询词]\t该URL在返回结果中的排名\t用户点击的顺序号\t用户点击的URL
            其中，用户ID是根据用户使用浏览器访问搜索引擎时的Cookie信息自动赋值，即同一次使用浏览器输入的不同查询对应同一个用户ID    
'''
import os
import io
from wordCloud import WordCloud


class ReadFile:
    def readFile(self, rootPath='./', suffix='filter'):
        wf = io.open('datas/wordCount.txt', "w", encoding='utf-8')
        for dirPath, dirNames, fileNames in os.walk(rootPath):
            for filename in fileNames:
                if filename.endswith(suffix):
                    i = os.path.join(dirPath, filename)
                    print i
                    with io.open(i, 'r', encoding='utf-8') as f:
                        c = 0
                        while 1:
                            c += 1
                            line = f.readline()
                            if not line:
                                break
                            st = line.split('\t')
                            sts = st[1].replace('[', '').replace(']', '') + " "
                            wf.write(sts)
                    f.close()
            wf.close()


if __name__ == '__main__':
    ReadFile().readFile('/Users/anke/data/SogouQ')
    cloud = WordCloud('datas/wordCount.txt', 'output.jpg')
    cloud.drawing()
