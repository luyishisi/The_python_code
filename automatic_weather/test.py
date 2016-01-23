#coding:utf-8
name = "浙江省杭州市"
if name.find(u"省") !=-1:# 包含'省'   
    #print u'有省'  
    name=name.split(u'省')[1]  
if name.find(u"市") != -1:#包含‘市’  
    #print u'有市'  
    name=name.split(u'市')[0]  
print (name)
fileHandle = open ( 'test.txt', 'w' ) 
fileHandle.write ( name ) 
fileHandle.close() 
