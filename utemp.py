import os
import glob
import time
from Adafruit_IO import Client, Feed

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
ADAFRUIT_IO_KEY = 'fa8007a47db04ca29386bdcca2f0c203'
ADAFRUIT_IO_USERNAME = 'pHarmr'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)


utemp_feed = aio.feeds('utemp')

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f

while True:
    aio.send(utemp_feed.key, str('%.2f'%read_temp()))
    time.sleep(1)
