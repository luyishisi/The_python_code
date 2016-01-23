#!/usr/bin/env python

# -*- coding: UTF-8 -*-



import urllib2, httplib
from BeautifulSoup import BeautifulSoup

def getIpAddr():
    '''从http://www.ip.cn网站获取外网ip和地理位置'''
    url = 'http://www.ip.cn'
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    # 通过<div class="well">标签找到位置信息

    find_div = soup.find('div',{'class':'well'})
    ip = find_div.code.text
    # 定位地理位置信息

    # 1.获得中文地理位置

    no = find_div.contents[0].text.find(';')
    addr = find_div.contents[0].text[no + 1:]
    
    # 2.获取en文地理位置

    # <p>GeoIP: Nanjing, Jiangsu, China</p>

    addrEn = find_div.contents[1].text
    # 得到拼音字符串，然后进行分割,得到addr列表

    addrEn = addrEn.split(':')
    # addr取原列表中的最后一个元素

    addrEn = addrEn[-1]
    # 将包含位置信息的字符串用','再次分割，得到城市、省份

    addrEn = addrEn.split(',')
    # 去除字符串两边多余的空格

    print '外网IP：', ip
    print addr
    for n in range(len(addrEn)):
        addrEn[n] = addrEn[n].strip()
        print addrEn[n], # 逗号是为了print后不换行

    print
    #print [ip, addr, addrEn]


if __name__ == '__main__':
    getIpAddr()
