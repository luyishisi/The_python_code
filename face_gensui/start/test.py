f = open('weizhi.txt','r')
begin = f.read()
f.close()

x =int(begin[2:5:]) 
y =int(begin[6:9:])
z =int(begin[10:13])/2
x = x + z
y = y + z
print("x=",x,"y=",y,"z=",z)
f = open('zhongxin.txt','w')
f.write(str(x)+" "+str(y)+" "+str(z))
f.close()
