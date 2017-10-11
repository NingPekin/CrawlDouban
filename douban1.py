#coding=utf-8

import requests 

# 上节的requests请求网页，得到网页源代码 
url = 'https://movie.douban.com/chart' 
#url=url.decode('utf-8', 'ignore')
r = requests.get(url).content 

# 导入lxml库和html.fromStringh函数来解析html 
from lxml import html 
import lxml.html
from lxml import etree

# 调用html.fromString函数解析html源代码 
sel = html.fromstring(r) 
import re
#catch links
links=sel.xpath('//div[@class="pl2"]/a/@href')
title=sel.xpath('//div[@class="pl2"]/a/text()')
subtitle=sel.xpath('//div[@class="pl2"]/a/span/text()')
contents=sel.xpath('//p[@class="pl"]/text()')
rate=sel.xpath('//div[@class="star clearfix"]/span[@class="rating_nums"]/text()')
numofgrade=sel.xpath('//div[@class="star clearfix"]/span[@class="pl"]/text()')

newtitle=[]
for t in title:
	t=re.sub(r'\s+','',t).replace('/','')
	newtitle.append(t)
#why len is not correct???
count=0
while (count<len(links)):
	# print newtitle[count*2]
	# print links[count]
	# print subtitle[count]
	# print contents[count]
	# print rate[count]
	# print numofgrade[count]+"\n"
	f1=open('G:\Python\crampler\WriteText.txt','a')
	f1.write(newtitle[count*2].encode('utf-8')+links[count].encode('utf-8')+subtitle[count].encode('utf-8')+contents[count].encode('utf-8')+rate[count].encode('utf-8')+numofgrade[count].encode('utf-8')+"\n")
	count=count+1
	f1.close





