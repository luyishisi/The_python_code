#coding:utf-8
import subprocess
#p = subprocess.popen(["mpg123","http://tsn.baidu.com/text2audio?tex=hello my name is luyi&lan=zh&per=0&pit=5&spd=2&cuid=7519663&ctp=1&tok=24.91b892cbba2c73d07f9fba69182b7960.2592000.1456136364.282335-7519663&qq-pf-to=pcqq.c2c"])
p = subprocess.Popen('ls',shell=True,stdout=subprocess.PIPE)
stdoutput,erroutput = p.communicate('/home/zoer')

print stdoutput[0]
print erroutput

