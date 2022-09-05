from datetime import datetime
from PIL import ImageGrab
from cv2.cv2 import *
import numpy as np
# from cv2.cv2 import VideoWriter_fourcc
from pynput import keyboard
import threading
from commons.common import base
import os
Basepath = base()
file_name = os.path.join(Basepath, 'images')


def video_record():
    global name
    name = datetime.now().strftime("%Y-%m-%d %H-%M-%S") # 当前时间（文件命名）
    name = file_name + '\\' + name
    screen = ImageGrab.grab()       # 获取当前屏幕
    width, high = screen.size       # 获取当前屏幕的大小
    fourcc = VideoWriter_fourcc('X', 'V', 'I', 'D')     # MPEG-4编码,文件后缀可为.avi .asf .mov等
    video = VideoWriter('%s.avi' % name, fourcc, 16, (width, high))      # （文件名，编码器，帧率，视频宽高）
    print("record start !!!")
    while True:
        if flag:
            print("record end !!!")
            video.release()     # 释放
            break
        img = ImageGrab.grab()      # 图片为RGB模式
        imm = cvtColor(np.array(img), COLOR_RGB2BGR)  # 转为opencv的BGR模式
        video.write(imm)
def video_info():
    # 视频信息
    # video = VideoCapture('%s.avi' % name)
    video = VideoCapture('%s.avi' % name)
    fps = video.get(CAP_PROP_FPS)
    frames = video.get(CAP_PROP_FRAME_COUNT)
    print('帧率=%.1f' % (fps))
    print('帧数=%.1f' % (frames))
    print('分辨率=(%d,%d)' % (int(video.get(CAP_PROP_FRAME_WIDTH)), int(video.get(CAP_PROP_FRAME_HEIGHT))))
    print('时间=%.2f秒' % (int(frames) / fps))
    return


def on_press(key):  # 监听按键
    global flag
    # if key == keyboard.Key.home:
    # if key == keyboard.Key.enter:
    if key:
        flag = True
        return False  # 返回False，键盘监听结束


# if __name__ == '__main__':
import time

flag = None
def video_run(flag):
    # flag = False
    th = threading.Thread(target=video_record)
    th.start()
    # with keyboard.Listener(on_press=on_press(flag)) as listener:
    #     listener.join()
    on_press(flag)
    print('---')
    time.sleep(10)
    print(file_name)
    flag = True
    th.join()
    video_info()
# video_run(flag)