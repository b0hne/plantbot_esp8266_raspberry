import socket
from time import sleep
from machine import Pin, UART
import uos
from ntptime import settime
import utime

SERVER_IP = '192.168.178.3'
NUM_PLANTS = 3

light_pin = Pin(5, Pin.OUT)
light_pin.off()

uos.dupterm(None, 1)
uart = UART(0, 9600)
uart.init(9600, bits=8, parity=None, stop=1, timeout=1800000)

count = 0
while True:
    try:
        if not count:
            print('set time')
            settime()
    except:
        print('no time available')
    print('localtime ', utime.localtime()[3])
    if (18 <= utime.localtime()[3] or utime.localtime()[3] <= 1):

        light_pin.off()
        print('light on')
    else:
        light_pin.on()
        print('light off')

    if not (count % 30):
        for i in range(NUM_PLANTS):
            try:
                val = uart.readline()
                val = val.decode()
                print('val ', val)
            except:
                print('no data')
                val = -1
            if val != -1:
                soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    print('trying')
                    soc.connect((SERVER_IP, 1234))
                    print('connected')
                    soc.send(val)
                    print('send')
                except:
                    print('connection failed')
                soc.close()
    count += 1
    print(count)
    count %= 1440
    sleep(1)
