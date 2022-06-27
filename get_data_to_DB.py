import minimalmodbus
import os
import sys
import time
import requests
import json
import serial

ser = serial.Serial('COM4', 9600, timeout=1)  # CO (USBport)


instrument1 = minimalmodbus.Instrument('COM5', 1)  # CO2 (USBport, slave ID)
instrument1.serial.baudrate = 9600
instrument1.serial.parity = 'N'
instrument1.serial.stopbits = 1
instrument1.serial.timeout = 5
instrument1.serial.bytesize = 8


def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)
    print("Restart")
    time.sleep(2)


while True:
    try:
        result = ser.readline()

        data = result.decode()

        splitdata = data.split(", ")

        COp = float(splitdata[1])

        sensor_CO = COp/1000

        sensor_CO2 = instrument1.read_register(
            0, 0)   # (sensor address, float)

        print("CO: ", sensor_CO, "ppm")
        print("CO2: ", sensor_CO2, "ppm")

        time.sleep(2)

        b_CO2 = {
            "inputData": sensor_CO2,
            "sensorManageId": 5
        }

        b_CO = {
            "inputData": sensor_CO,
            "sensorManageId": 6
        }

        headers = {'Content-Type': 'application/json; charset=utf-8'}

        url = "apiserver/api/sensor-data"
        response = requests.post(url, headers=headers, data=json.dumps(b_CO2))
        response = requests.post(url, headers=headers, data=json.dumps(b_CO))
        print(response)

        print("전송  완  료!!")

    except Exception as e:
        print(e)

        restart()


time.sleep(2)
