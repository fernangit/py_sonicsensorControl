# ras_py_sonicsensorControl
mesure distance by sonicsensor on the raspberry pie  
---
HC-SR04超音波センサーによる超音波測定

## HOW TO USE
### 配線  
ラズパイとHC－SR04を接続する。
* HC-SR04(gnd)→GPIO6番ピン(GND)
* HC-SR04(trig)→GPIO21番ピン
* HC-SR04(echo)→GPIO20番ピン
* HC-SR04(vcc)→GPIO4番ピン(5V)

#### スクリプト実行  
以下のコマンドで計測距離表示  
```
python3 supersonic.py
```

#### モジュールからの呼び出し
```
import supersonic as sonic
    GPIO_TRIG = 21
    GPIO_ECHO = 20
    DIS_THRESH = 50 #50cm

    sonic.init_sensors(GPIO_TRIG, GPIO_ECHO)
    while True:
        var distance = sonic.get_distance(GPIO_TRIG, GPIO_ECHO);

```


## 参考情報
超音波距離センサの仕組み[HC-SR04とラズパイの場合]  
https://mio.yokohama/?p=532  
測距センサー(HC-SR04)とRaspberry Piをつないでみる  
https://umiushizn.blogspot.com/2017/10/hc-sr04raspberry-pi.html  

