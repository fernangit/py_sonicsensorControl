#!/usr/bin/python
import time
import tplink_smartplug_py3 as plug
import supersonic as sonic
import jtalk as jt
"""
自動判別の場合 
$ sudo amixer cset numid=3 0
ライン出力の場合 
$ sudo amixer cset numid=3 1
HDMI出力の場合 
$ sudo amixer cset numid=3 2
"""
GPIO_TRIG = 21
GPIO_ECHO = 20
DIS_THRESH = 100 #100cm
ON_COUNT = 2 #10sec
OFF_COUNT = 4 #30sec

def main():
    sonic.init_sensors(GPIO_TRIG, GPIO_ECHO)

    plugStatus = False
    onCount = 0
    offCount = 0
    while True:
        distance = sonic.get_distance(GPIO_TRIG, GPIO_ECHO)
        if distance < DIS_THRESH:
            print('distance < DIS_THRESH')
            offCount = 0
            onCount = onCount+1
            if onCount >= ON_COUNT and plugStatus == False:
                #Plug ON
                onCount = 0
                plugStatus = True
                plug.control('192.168.0.106', 'on')
#                jt.jtalk('いらっしゃい')
        else:
            print('distance >= DIS_THRESH')
            onCount = 0
            offCount = offCount+1
            if offCount >= OFF_COUNT and plugStatus == True:
                #Plug OFF
                offCount = 0
                plugStatus = False
                plug.control('192.168.0.106', 'off')
#                jt.jtalk('またね')
       
#        print('距離：{0} cm'.format(sonic.get_distance(GPIO_TRIG, GPIO_ECHO)))
        print('距離：{0} cm'.format(distance))
        print('onCount:{0}, offCount:{1}, plugStatus:{2}'.format(onCount, offCount, plugStatus))
        time.sleep(2) #2sec wait


if __name__ == "__main__":
    main()
