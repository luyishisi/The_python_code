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
    #url = "http://tsn.baidu.com/text2audio?tex="+sys.argv[1]+"&lan=zh&per=1&pit=1&spd=7&cuid=7519663&ctp=1&tok="+token
    url = "http://tsn.baidu.com/text2audio?tex="+"陆熠十四"+"&lan=zh&per=1&pit=1&spd=7&cuid=7519663&ctp=1&tok=24.91b892cbba2c73d07f9fba69182b7960.2592000.1456136364.282335-7519663"


    os.system('mpg123 "%s"'%(url))
    a = input()
    #print(token)

     
    #24.91b892cbba2c73d07f9fba69182b7960.2592000.1456136364.282335-7519663

http://tsn.baidu.com/text2audio?tex=%E5%8F%AF%E4%BB%A5%E9%80%9A%E8%BF%87%E8%B0%83%E7%94%A8%E7%99%BE%E5%BA%A6%E8%AF%AD%E9%9F%B3%E5%90%88%E6%88%90%E6%9D%A5%E6%9C%97%E8%AF%BB%E5%A4%A9%E6%B0%94%E6%83%85%E5%86%B5%E4%BA%86&lan=zh&per=0&pit=5&spd=7&cuid=7519663&ctp=1&tok=24.91b892cbba2c73d07f9fba69182b7960.2592000.1456136364.282335-7519663&qq-pf-to=pcqq.c2c
