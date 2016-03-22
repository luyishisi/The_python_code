#coding = utf-8
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getimg(html):
    reg = r"./jpg"
    print reg
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print imglist
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1

html = getHtml('http://tieba.baidu.com/p/4133040044')

print (getimg(html))
