import time
import serial
import numpy as np

ser = serial.Serial('COM4', 9600, timeout=1)

ser.write("c".encode('utf-8'))  # "c"는 센서 내 모듈에서 지속적으로 데이터를 보내달라고 하는 신호

# 시리얼 포트 연결이 불안정해서 관련된 코드를 추가해야함
# 예를들어 받아온 데이터의 타입이 OO이면 True쪽 코드를 실행하면 되고
# False(빈값)이면 해당 프로세스를 다시 루프를 돌리는 식으로?


while True:

    result = ser.readline()

    data = result.decode()

    splitdata = data.split(", ")

    # splitdata = splitdata.replace("'", "")

    # list(np.float_(splitdata))

    COp = float(splitdata[1])

    CO = COp/1000

    print("CO: ", CO, "ppm")
    # print(type(splitdata[1]))


ser.close()
