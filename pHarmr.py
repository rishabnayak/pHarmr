# pHarmr CORE
# Author: Jason Smith
# Last Updated: 201810260453

#=======================================================
# Load Libraries
import time
import datetime
import Adafruit_DHT
import os
import glob
import serial
from Adafruit_IO import Client, Feed
#-------------------------------------------------------

#=======================================================
# CONSTANTS
READ_TIMEOUT = 12
DHT_DATA_PIN = 5
PORT = "/dev/ttyACM0"
#-------------------------------------------------------


#=======================================================
# DS18B20 (temp) initializing and reading
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28-001*')[0]
device_folder1 = glob.glob(base_dir + '28-002*')[0]
device_file = device_folder + '/w1_slave'
device_file1 = device_folder1 + '/w1_slave'
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
def read_temp_raw1():
    f1 = open(device_file1, 'r')
    lines1 = f1.readlines()
    f1.close()
    return lines1
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(5)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        print('Reservoir Temp: ' + str('%.1f'%temp_f))
        return temp_f
def read_temp1():
    lines1 = read_temp_raw1()
    while lines1[0].strip()[-3:] != 'YES':
        time.sleep(5)
        lines1 = read_temp_raw1()
    equals_pos = lines1[1].find('t=')
    if equals_pos != -1:
        temp_string = lines1[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        print('Channel Temp: ' + str('%.1f'%temp_f))
        return temp_f
#------------------------------------------------------


#======================================================
# SEN0161 (pH) initializing and reading
ph_sensor = serial.Serial(PORT,9600)
ph_sensor.flushInput()
ph_out = ''
#-----------------------------------------------------


#=====================================================
# Adafruit IO connection setup
ADAFRUIT_IO_KEY = 'fa8007a47db04ca29386bdcca2f0c203'
ADAFRUIT_IO_USERNAME ='pHarmr'
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
temperature_feed = aio.feeds('temperature')
humidity_feed = aio.feeds('humidity')
utemp1_feed = aio.feeds('utemp')
utemp2_feed = aio.feeds('utemp2')
ph_feed = aio.feeds('ph')
#----------------------------------------------------


#====================================================
# DHT22 (temp/humidity) setup
dht22_sensor = Adafruit_DHT.DHT22
#----------------------------------------------------


#=======================================================================================================
# pHarmr Core Functionality and DB output
while True:
        os.system('clear')
        print('pHarmr Operational DataDump @ ' + datetime.datetime.now().strftime("%y-%m-%d  %H:%M|%S"))
        print('--------------------------------------------------------')
        humidity, temperature = Adafruit_DHT.read_retry(dht22_sensor,DHT_DATA_PIN)
        if humidity is not None and temperature is not None and ph_sensor.inWaiting() > 0::
                temperature = '%.1f'%(temperature * 9.0 / 5.0 + 32.0)
                humidity = '%.1f'%(humidity)
                inputValue = ph_sensor.readline()
                ph_out = inputValue.decode()
                print('Temp={0:0.1f}*F Humidity={1:0.1f}%'.format(temperature * 9.0 / 5.0 + 32.0, humidity))
                print('pH Level : ' + str(ph_out))
                aio.send(temperature_feed.key,str(temperature))
                aio.send(humidity_feed.key, str(humidity))
                aio.send(utemp1_feed.key, str('%.1f'%read_temp()))
                aio.send(utemp2_feed.key, str('%.1f'%read_temp1()))
                aio.send(ph_feed.key,ph_out)
        print('--------------------------------------------------------')
#--------------------------------------------------------------------------------------------------------

        time.sleep(READ_TIMEOUT)
