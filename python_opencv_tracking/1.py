#coding:utf-8
# 导入必要的软件包
import argparse
import datetime
import imutils
import time
import cv2
 
# 创建参数解析器并解析参数
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())
  
# 如果video参数为None，那么我们从摄像头读取数据
if args.get("video", None) is None:
    camera = cv2.VideoCapture(0)
    time.sleep(0.25)
           
# 否则我们读取一个视频文件
else:
    camera = cv2.VideoCapture(args["video"])
                
# 初始化视频流的第一帧
firstFrame = None
k = 0
# 遍历视频的每一帧
while True:
    # 获取当前帧并初始化occupied/unoccupied文本
    (grabbed, frame) = camera.read()
    text = "Unoccupied"
 
    # 如果不能抓取到一帧，说明我们到了视频的结尾
    if not grabbed:
        break
 
    # 调整该帧的大小，转换为灰阶图像并且对其进行高斯模糊
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
 
    # 如果第一帧是None，对其进行初始化
    if firstFrame is None:
        firstFrame = gray
        continue
# 计算当前帧和第一帧的不同
    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
 
    # 扩展阀值图像填充孔洞，然后找到阀值图像上的轮廓
    thresh = cv2.dilate(thresh, None, iterations=2)
    (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
 
    # 遍历轮廓
    for c in cnts:
        # if the contour is too small, ignore it
        if cv2.contourArea(c) < args["min_area"]:
            continue
 
        # compute the bounding box for the contour, draw it on the frame,
        # and update the text
        # 计算轮廓的边界框，在当前帧中画出该框
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Occupied"
# draw the text and timestamp on the frame
    # 在当前帧上写文字以及时间戳
    cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
        (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    
    s = time.ctime()    
    miao = s[17:19:1]
    int_miao = int(miao)
    if int_miao%10 == 5:
        print (miao)
        time.sleep(1)
        continue

    #显示当前帧并记录用户是否按下按键
    cv2.imshow("Security Feed", frame)
    cv2.imshow("Thresh", thresh)
    cv2.imshow("Frame Delta", frameDelta)
    key = cv2.waitKey(1) & 0xFF
 
    # 如果q键被按下，跳出循环
    if key == ord("q"):
        break
# 清理摄像机资源并关闭打开的窗口
camera.release()
cv2.destroyAllWindows()
