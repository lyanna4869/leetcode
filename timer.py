import os
import time

def beeper(interval, duration, times, times_interval):
    """
    实现一个隔指定时间(interval)蜂鸣指定次数的蜂鸣器
    :param interval: 指定间隔时间
    :param duration: 每次蜂鸣的时长
    :param times: 蜂鸣次数。蜂鸣两次指定1，蜂鸣三次指定2.
    :param times_interval: 蜂鸣次数之间的短间隔。
    :return:
    """
    time.sleep(interval)
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
    while times:
        time.sleep(times_interval)
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        times -= 1


interval = 300  # seconds
duration = 2  # seconds
freq = 550  # Hz
beeper(interval, duration, times=1, times_interval=1)
