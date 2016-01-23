#coding:utf-8
import cv2
import time
capture=cv2.VideoCapture(0)
#将capture保存为motion-jpeg,cv_fourcc为保存格式
size = (int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
#cv_fourcc值要设置对，不然无法写入，而且不报错，坑
video=cv2.VideoWriter("VideoTest.avi", cv2.cv.CV_FOURCC('I','4','2','0'), 30, size)
#isopened可以查看摄像头是否开启
print capture.isOpened()
num=0
s = time.ctime()
#要不断读取image需要设置一个循环
while True:
    ret,img=capture.read()
    #视频中的图片一张张写入
    video.write(img)
    cv2.imshow('Video',img)
    key=cv2.waitKey(3)#里面数字为delay时间，如果大于0为刷新时间，
    #超过指定时间则返回-1，等于0没有返回值,但也可以读取键盘数值，

    s = time.ctime()[8:19:1]
    print s
    cv2.imwrite('%s.jpg' %s,img)
    num=num+1
    if key==ord('q'):#ord为键盘输入对应的整数,
        break
video.release()
