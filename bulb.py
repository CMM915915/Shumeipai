import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(25, GPIO.LOW)

ser = serial.Serial("/dev/ttyUSB0", 9600)
ser.flushInput()


# ser.write("play,001,$")

def main():
    while True:
        count = ser.inWaiting()
        if count != 0:
            print(count)
            recv = int.from_bytes(ser.read(count), byteorder='big', signed=False)
            print(recv)
            print(type(recv))
            if (recv == 2):
                GPIO.output(23, GPIO.HIGH)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(25, GPIO.LOW)
                print("hong deng")
            if (recv == 3):
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(25, GPIO.HIGH)
                print("lv deng")
            if (recv == 4):
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.HIGH)
                GPIO.output(25, GPIO.LOW)
                print("lan deng")
            ser.flushInput()
        time.sleep(0.1)


if __name__ == '__main__':
    main()