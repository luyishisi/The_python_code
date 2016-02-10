# -*- coding:utf-8-*-
import cv2
 
capture=cv2.VideoCapture(0)
#将capture保存为motion-jpeg,cv_fourcc为保存格式
size = (int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
#cv_fourcc值要设置对，不然无法写入，而且不报错，坑
video=cv2.VideoWriter("VideoTest.avi", cv2.cv.CV_FOURCC('I','4','2','0'), 30, size)
#isopened可以查看摄像头是否开启
print capture.isOpened()
num=0
#要不断读取image需要设置一个循环
while True:
    ret,img=capture.read()
    #视频中的图片一张张写入
    video.write(img)
    cv2.imshow('Video',img)
    key=cv2.waitKey(1)#里面数字为delay时间，如果大于0为刷新时间，
    #超过指定时间则返回-1，等于0没有返回值,但也可以读取键盘数值，
    cv2.imwrite('%s.jpg'%(str(num)),img)
    num=num+1
    if key==ord('q'):#ord为键盘输入对应的整数,
        break
video.release()
#如果不用release方法的话无法储存，要等结束程序再等摄像头关了才能显示保持成功
capture.release()#把摄像头也顺便关了
 
cv2.destroyAllWindows()
