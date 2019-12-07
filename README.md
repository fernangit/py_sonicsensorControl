# ras_py_sonicsensorControl
mesure distance by sonicsensor on the raspberry pie  
---
HC-SR04�����g�Z���T�[�ɂ�钴���g����

## HOW TO USE
### �z��  
���Y�p�C��HC�|SR04��ڑ�����B
* HC-SR04(gnd)��GPIO6�ԃs��(GND)
* HC-SR04(trig)��GPIO21�ԃs��
* HC-SR04(echo)��GPIO20�ԃs��
* HC-SR04(vcc)��GPIO4�ԃs��(5V)

#### �X�N���v�g���s  
�ȉ��̃R�}���h�Ōv�������\��  
```
python3 supersonic.py
```

#### ���W���[������̌Ăяo��
```
import supersonic as sonic
    GPIO_TRIG = 21
    GPIO_ECHO = 20
    DIS_THRESH = 50 #50cm

    sonic.init_sensors(GPIO_TRIG, GPIO_ECHO)
    while True:
        var distance = sonic.get_distance(GPIO_TRIG, GPIO_ECHO);

```


## �Q�l���
�����g�����Z���T�̎d�g��[HC-SR04�ƃ��Y�p�C�̏ꍇ]  
https://mio.yokohama/?p=532  
�����Z���T�[(HC-SR04)��Raspberry Pi���Ȃ��ł݂�  
https://umiushizn.blogspot.com/2017/10/hc-sr04raspberry-pi.html  

