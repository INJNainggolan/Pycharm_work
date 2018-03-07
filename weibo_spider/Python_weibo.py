# -*- coding: utf-8 -*-
import re
import urllib
import urllib.request
import os
import stat
import itertools
import re
import sys
import requests
import json
import time
import socket
import urlparse
import csv
import random
from datetime import datetime, timedelta
import lxml.html
from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np

from zipfile import ZipFile
from StringIO import StringIO
from downloader import Downloader
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
from itertools import product
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json,urllib.request
def download(url, headers, num_try=2):
    while num_try >0:
        num_try -= 1
        try:
            content = requests.get(url, headers=headers)
            return content.text

        except urllib2.URLError as e:
            print 'Download error', e.reason

    return None
header_dict = {
                'Content-Type':'application/json; charset=utf-8',
                'Accept':'application/json, text/plain, */*',
                'Accept-Encoding':'gzip, deflate, br',
                'Accept-Language':'zh-CN,zh;q=0.9',
                'Connection':'keep-alive',
                'Cookie':'...',
                'Host':'m.weibo.cn',
                'Referer':'https://m.weibo.cn/u/1241148864?display=0&retcode=6102',
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
                'X-Requested-With':'XMLHttpRequest'
               }

def wordcloudplot(txt):
    path = '/Users/cy/Downloads/msyh.ttf'
    path = unicode(path, 'utf8').encode('gb18030')
    alice_mask = np.array(PIL.Image.open('/Users/cy/Desktop/1.jpg'))
    wordcloud = WordCloud(font_path=path,
                          background_color="white",
                          margin=5, width=1800, height=800, mask=alice_mask, max_words=2000, max_font_size=60,
                          random_state=42)
    wordcloud = wordcloud.generate(txt)
    wordcloud.to_file('/Users/cy/Desktop/2.jpg')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


def main():
    a = []
    f = open(r'/Users/cy/Downloads/a.json', 'r').read()
    words = list(jieba.cut(f))
    for word in words:
        if len(word) > 1:
            a.append(word)
    txt = r' '.join(a)
    wordcloudplot(txt)

def get_comment(que):
    f = open('/Users/cy/Downloads/a.json', 'w')
    total_number = 10
    for each in que:
        for i in range(1,total_number):
            textmood = {"id": each,
                        "page": i}
            textmood = json.dumps(textmood)
            uu = 'https://m.weibo.cn/status/' + str(each)
            header = {'Connection': 'keep-alive',
                      'Cookie': '.......',
                      'Accept-Language': 'zh-CN,zh;q=0.8',
                      'Host': 'm.weibo.cn',
                      'Referer':uu,
                      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
                      'X-Requested-With': 'XMLHttpRequest'
                      }
            url = 'https://m.weibo.cn/api/comments/show?id=%s&page=%s'%(str(each),str(i))
            print url

            req = urllib2.Request(url=url, data=textmood, headers=header)
            res = urllib2.urlopen(req)
            res = res.read()
            contents = res
            d = json.loads(contents, encoding="utf-8")
            total_numbers = d['total_number']
            print total_numbers
            tto = total_numbers / 10 + 1
            if total_number > tto:
                 total_number = min(tto,10)
            if 'data' in d:
                data = d['data']
                if data != "":
                    for each_one in data:
                        if each_one != "":
                            if each_one['text'] != "":
                                mm = each_one['text'].split('<')
                                if  r'回复' not in mm[0]:
                                    index = mm[0]#filter(lambda x: x not in '0123456789', mm[0])
                                    print index
                                    f.write(index.encode("u8"))

def get_identified():

    que = []
    url = 'https://m.weibo.cn/api/container/getIndex?uid=1241148864&luicode=10000011&lfid=100103type%3D3%26q%3D%E5%BC%A0%E6%9D%B0&featurecode=20000180&type=uid&value=1241148864&containerid=1076031241148864'
    for i in range(1,3):
        if i > 1:
            url = 'https://m.weibo.cn/api/container/getIndex?uid=1241148864&luicode=10000011&lfid=100103type%3D3%26q%3D%E5%BC%A0%E6%9D%B0&featurecode=20000180&type=uid&value=1241148864&containerid=1076031241148864&page='+str(i)
        print url

        req = download(url, header_dict,2)
        print req
        d = json.loads(req,encoding="utf-8")
        print d

        try:
            data = d['data']['cards']
            print data
        except KeyError,e:
            print e.message

        if data != "":
            for each in data:
                print each['itemid']
                mm = each['itemid']
                if mm != "":
                    identity = mm.split('-')
                    num = identity[1][1:]
                    que.append(num)
                    print num

    get_comment(que)

if __name__ == '__main__':
    get_identified()
    main()