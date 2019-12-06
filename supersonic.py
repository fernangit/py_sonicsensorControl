#!/usr/bin/python
"""
HC-SR04(gnd)  GPIO6�ԃs��(GND)
HC-SR04(trig) GPIO21�ԃs��
HC-SR04(echo) GPIO20�ԃs��
HC-SR04(vcc)  GPIO4�ԃs��(5V)
"""

import RPi.GPIO as GPIO
import time


def pulse_in(pin, value=GPIO.HIGH, timeout=1.0):
    """
    �s���ɓ��͂����p���X�����o���܂��B
    value��HIGH�Ɏw�肵���ꍇ�Apulse_in�֐��͓��͂�HIGH�ɕς��Ɠ����Ɏ��Ԃ̌v�����n�߁A
    �܂�LOW�ɖ߂�܂ł̎���(�܂�p���X�̒���)���}�C�N���b�P��(*1)�ŕԂ��܂��B
    �^�C���A�E�g���w�肵���ꍇ�́A���̎��Ԃ𒴂������_��0��Ԃ��܂��B
    *1 python�̏ꍇ��time�p�b�P�[�W�̎d�l�ɂ������ˑ��ł����A�T��nanosec�ŕԂ�Ǝv���܂��B
    :param pin: �s���ԍ��A�܂���GPIO �ԍ�(GPIO.setmode�Ɉˑ��B)
    :param value: �p���X�̎��(GPIO.HIGH �� GPIO.LOW�Bdefault:GPIO.HIGH)
    :param timeout: �^�C���A�E�g(default:1sec)
    :return: �p���X�̒����i�b�j�^�C���A�E�g����0
    """
    start_time = time.time()
    not_value = (not value)

    # �O�̃p���X���I������̂�҂�
    while GPIO.input(pin) == value:
        if time.time() - start_time > timeout:
            return 0

    # �p���X���n�܂�̂�҂�
    while GPIO.input(pin) == not_value:
        if time.time() - start_time > timeout:
            return 0

    # �p���X�J�n�������L�^
    start = time.time()

    # �p���X���I������̂�҂�
    while GPIO.input(pin) == value:
        if time.time() - start_time > timeout:
            return 0

    # �p���X�I���������L�^
    end = time.time()

    return end - start

def init_sensors(trig, echo, mode=GPIO.BCM):
    """
    ���������܂�
    :param trig: Trigger�p�s���ԍ��A�܂���GPIO �ԍ�
    :param echo: Echo�p�s���ԍ��A�܂���GPIO �ԍ�
    :param mode: GPIO.BCM�A�܂��� GPIO.BOARD (default:GPIO.BCM)
    :return: �Ȃ�
    """
    GPIO.cleanup()
    GPIO.setmode(mode)
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

def get_distance(trig, echo, temp=15):
    """
    �������擾���܂��B�擾�Ɏ��s�����ꍇ��0��Ԃ��܂��B
    :param trig: Trigger�p�s���ԍ��A�܂���GPIO �ԍ�(GPIO.setmode�Ɉˑ��B)(GPIO.OUT)
    :param echo: Echo�p�s���ԍ��A�܂���GPIO �ԍ�(GPIO.setmode�Ɉˑ��B)(GPIO.IN)
    :param temp: �擾�\�ł���Ή��x(default:15��)
    :return: �����i�����j�^�C���A�E�g���� 0
    """

    # �o�͂�������
    GPIO.output(trig, GPIO.LOW)
    time.sleep(0.3)
    # �o��(10us�ȏ�҂�)
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.000011)
    # �o�͒�~
    GPIO.output(trig, GPIO.LOW)

    # echo ����p���X���擾
    dur = pulse_in(echo, GPIO.HIGH, 1.0)

    # ( �p���X���� x 331.50 + 0.61 * ���x ) x (�P�ʂ�cm�ɕϊ�) x ����
    # return dur * (331.50 + 0.61 * temp) * 100 / 2
    return dur * (331.50 + 0.61 * temp) * 50


if __name__ == "__main__":

    GPIO_TRIG = 21
    GPIO_ECHO = 20

    init_sensors(GPIO_TRIG, GPIO_ECHO)
    while True:
        print("�����F{0} cm".format(get_distance(GPIO_TRIG, GPIO_ECHO)))
        time.sleep(2)
