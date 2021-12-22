 # 下拉模式
 #-*- coding: utf-8 -*-23
from RPi import GPI04
import time
#采用BCM引脚编号
GPI0. setmode(GPI0. BCM)
#关闭誊告)
GPI0. setwarnings(False)
# 输入引脚11
channel = 18
#设置GPIO输入模式，使用GPIO内置的下拉电阻，即开关断开情况下输入为LOW13
GPI0. setup( channel, GPIO.IN, pull_up_down = GPI0. PUD_DOWIN)
#检测LOW -> HIGH的变化
GPI0. add_event_detect( channel, GPI0. RISING,bouncetime = 200)
#开关闭台的处理19
def on_switch_pressed():
    print(' open')
    try:
        while True:
            	#如果检测到电平RISING， 说明开关朗合
            	if GPI0. event. _detected( channel):
            	    on_switch. pressed()
                    #可以在循环中做其他检测
                    time. sleep(0.01)# 10毫秒的检测间隔
    except Exception as e:
        print(e) #清理占用的GPIO资源33 GPI0. cleanupO)
# 清理占用的GPIO资源
GPIO.cleanup()
# 上拉模式
#采用BCM引脚编号
GPI0. setmode(GPI0. BCM)
#关闭誊告)
GPI0. setwarnings(False)
# 输入引脚
channel = 18
#设置GPIO输入模式，使用GPIO内置的下拉电阻，即开关断开情况下输入为LOW13
GPI0. setup( channel, GPIO.IN, pull_up_down = GPI0.PUD_UP)
#检测LOW -> HIGH的变化
GPI0. add_event_detect( channel, GPI0.FALLING,bouncetime = 200)
#开关闭台的处理
def on_switch_pressed():
    print(' open')
    try:
        while True:
            	#如果检测到电平RISING， 说明开关朗合
            	if GPI0. event_detected( channel):
            	    on_switch_pressed()
                    #可以在循环中做其他检测
                    time. sleep(0.01)# 10毫秒的检测间隔
    except Exception as e:
        print(e) #清理占用的GPIO资源33 GPI0. cleanupO)
# 清理占用的GPIO资源
GPIO.cleanup()

