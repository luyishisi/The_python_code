# -*- coding: utf-8 -*-

import os
import urllib.request
import sys
import json

'''
def get_token():
    apiKey = "Ll0c53MSac6GBOtpg22ZSGAU"
    secretKey = "44c8af396038a24e34936227d4a19dc2"

    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;

    res = urllib.request.urlopen(auth_url) 
    print(res.read())
    json_data = res.read()
    
    return json.loads(json_data)['access_token']
'''
if __name__ == "__main__":
    #token = get_token()

    fileHandle = open ( 'weather.txt', 'r' ) 
    weather = fileHandle.read() 
    fileHandle.close() 

    
    #url = "http://tsn.baidu.com/text2audio?tex="+sys.argv[1]+"&lan=zh&per=1&pit=1&spd=7&cuid=7519663&ctp=1&tok="+token
    url = "http://tsn.baidu.com/text2audio?tex="+weather+"&lan=zh&per=1&pit=1&spd=7&cuid=7519663&ctp=1&tok=24.91b892cbba2c73d07f9fba69182b7960.2592000.1456136364.282335-7519663"


    os.system('mpg123 "%s"'%(url))
    #这个在linux可以运行的。也可以自行从我git下载mpg123.然后在window命令行运行。
    a = input()
    #print(token)

    #测试数据
    #24.91b892cbba2c73d07f9fba69182b7960.2592000.1456136364.282335-7519663
'''
http://tsn.baidu.com/text2audio?tex=城市名:杭州
更新时间:16-01-23 18:00
天气:多云 [无持续风向6-7级(34~43km/h)]
当前温度:-8 (0 ---> -8)&lan=zh&per=0&pit=5&spd=7&cuid=7519663&ctp=1&tok=24.91b892cbba2c73d07f9fba69182b7960.2592000.1456136364.282335-7519663&qq-pf-to=pcqq.c2c
'''
