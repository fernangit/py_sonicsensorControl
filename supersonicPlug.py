#!/usr/bin/python
import tplink_smartplug_py3 as plug
import supersonic as sonic
import jtalk as jt

def main()
    GPIO_TRIG = 21
    GPIO_ECHO = 20
    DIS_THRESH = 50 #50cm

    var plugStatus = ON
    sonic.init_sensors(GPIO_TRIG, GPIO_ECHO)
    while True:
        var distance = sonic.get_distance(GPIO_TRIG, GPIO_ECHO);
        if(distance < DIS_THRESH)
        {
            if(plugStatus == OFF){
                #Plug ON
                plugStatus = ON
                plug.control('192.168.0.2', 'on')
                jt.jtalk('いらっしゃいっ')
            }
        }
        else
        {
            if(plugStatus == ON){
                #Plug OFF
                plugStatus = OFF
                plug.control('192.168.0.2', 'off')
                jt.jtalk('またねっ')
            }
        }
        print("距離：{0} cm".format(distance)

        time.sleep(2)


if __name__ == "__main__":
    main()

