#coding=utf-8
import re
import requests
from lxml import html 
import lxml.html
from lxml import etree
k=1
for x in range(10):
	source='https://movie.douban.com/top250?start={}&filter='.format(x*25)
	r=requests.get(source).content
	web=html.fromstring(r)
	
	for i in web.xpath('//div[@class="info"]'): 
		print ("Top "),k,(" :")
		# grab title
		title=i.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0]
		# grab english title
		# entitle=i.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[1]
		# grab info
		info=i.xpath('//div[@class="bd"]/p/text()')
		info_1=info[0].replace(" ","").replace("\n","")
		date=info[1].replace(" ","").replace("\n","").split('/')[0]
		country=info[1].replace(" ","").replace("\n","").split('/')[1]
		genre=info[1].replace(" ","").replace("\n","").split('/')[2]
		rate = i.xpath('//span[@class="rating_num"]/text()')[0]
		gradenum=i.xpath('//div[@class="star"]/span[4]/text()')[0]
		print title.encode('GBK', 'ignore'), info_1.encode('GBK', 'ignore'), date.encode('GBK', 'ignore'), country.encode('GBK', 'ignore'), genre.encode('GBK', 'ignore'),rate.encode('GBK', 'ignore'),gradenum.encode('GBK', 'ignore')+'\n'
		
# write into file
		with open("G:\Python\crampler\Top250.txt","a") as f:
			f.write("TOP%s\n影片名称：%s\n评分：%s %s\n上映日期：%s\n上映国家：%s\n%s\n" % (k, title.encode('utf-8'), rate.encode('utf-8'), gradenum.encode('utf-8'), date.encode('utf-8'), country.encode('utf-8'), info_1.encode('utf-8')))
			f.write("\n============================\n")
		k+=1
	

