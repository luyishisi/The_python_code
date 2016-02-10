1.py是测试文件
2.py是成品，能够对目录下的5.jpg进行人脸识别，并且画出一个绿色的框，重点是
能够获取脸的距离位置，目的是通过获取相对位置，不断的重复读取的过程，存储到
文件中，然后达到跟随的目的。

使用指南，
请先安装好环境：
linux
python 2.7.3
opencv 2.3.1-7
安装依赖
sudo apt-get install libopencv-*
sudo apt-get install python-opencv
sudo apt-get install python-numpy

进入start运行2.py可以单独测试人脸识别的功能，欲测试整体不断识别相对位置功能
请运行lianxuzhibo.py文件  python lianxuzhibo.py，如果环境上没有大问题的话
应该能在该目录下出现5.jpg图片文件，如果存在人脸，则会进行识别，建立一个
weizhi.txt文件，存储每次人脸位置的重心，

剩下的部分就是根据这个txt进行摄像头的转换了，这个之后再写，别闲我懒。。过年嘛。。
