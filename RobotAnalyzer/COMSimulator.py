""" Serial COM simulator """

import serial
from time import sleep

def main():
	ser = serial.Serial(port='COM3', baudrate=115200, )
	print(ser.name)
	while True:
		print(str("Siemanko").encode())
		ser.write("Siemanko".encode())
		sleep(1)

if __name__ == "__main__":
	main()