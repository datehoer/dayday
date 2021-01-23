import requests
import re
from lxml import etree
c_1 = input('请输入要下载的书籍的关键字:')
source = requests.get('http://www.biquge.info/modules/article/search.php?searchkey='+c_1).content.decode('utf8')
import time
titles = etree.HTML(source).xpath('//*[@id="wrapper"]/table//tr/td[1]/a/text()')
hrefs = etree.HTML(source).xpath('//*[@id="wrapper"]/table//tr/td[1]/a/@href')
n = 1
for i in titles:
    print(str(n)+'\t'+i)
    n = n+1
c_2 = int(input('请输入要下载的书籍序号'))-1
chapter_page = 'http://www.biquge.info'+hrefs[c_2]
chapter_source = requests.get(chapter_page).content.decode('utf8')
chapter_lists = etree.HTML(chapter_source).xpath('//*[@id="list"]/dl/dd/a/@href')
for h in chapter_lists:
    chapter_href = chapter_page+h
    content_source = requests.get(chapter_href).content.decode('utf8')
    title = etree.HTML(content_source).xpath('//h1/text()')[0]
    contents = '\n'.join(etree.HTML(content_source).xpath('//*[@id="content"]/text()'))
    print(title)
    print(contents)
    time.sleep(1)
    op = open(titles[c_2]+'.txt','a+',encoding='utf8')
    op.write(title+contents)
    op.close()
