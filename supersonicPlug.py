#!/usr/bin/python
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

def main()
    GPIO_TRIG = 21
    GPIO_ECHO = 20
    DIS_THRESH = 50 #50cm
    ON_COUNT = 5 #10sec
    OFF_COUNT = 15 #30sec

    sonic.init_sensors(GPIO_TRIG, GPIO_ECHO)
    var plugStatus = OFF
    var onCount = 0
    var offCount = 0
    while True:
        var distance = sonic.get_distance(GPIO_TRIG, GPIO_ECHO)
        if distance < DIS_THRESH:
            offCount = 0
            onCount++
            if onCount >= ON_COUNT and plugStatus == OFF:
                #Plug ON
                onCount = 0
                plugStatus = ON
                plug.control('192.168.0.2', 'on')
                jt.jtalk('いらっしゃい')
        else:
            onCount = 0
            offCount++
            if offCount >= OFF_COUNT and plugStatus == ON:
                #Plug OFF
                offCount = 0
                plugStatus = OFF
                plug.control('192.168.0.2', 'off')
                jt.jtalk('またね')

        print("距離：{0} cm".format(distance)
        time.sleep(2) #2sec wait


if __name__ == "__main__":
    main()

