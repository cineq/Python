""" Robot Analyzer made by Marcin Kurpiel """

import serial
import sys
import pyqtgraph
from PyQt4 import QtGui
import queue
import time
import WindowPainter
from threading import Thread


def com_thread(com_queue,
			   port='COM5',
			   baud_rate=115200):
	try:
		ser = serial.Serial(port, baud_rate)
	except serial.SerialException:
		print("Exception")
		return
	print("Communication thread created")
	while True:
		line = ser.read(10)
		com_queue.put(line)


def plot_thread(plot_queue):
	while True:
		print(plot_queue.get())


def main():
	com_queue = queue.Queue()
	read_com = Thread(target=com_thread, args=(com_queue, ))
	plot = Thread(target=plot_thread, args=(com_queue, ))

	read_com.start()
	plot.start()

	app = QtGui.QApplication(sys.argv)
	main_window = WindowPainter.MainWindow()
	main_window.show()
	app.exec_()

	read_com.join()
	plot.join()


if __name__ == "__main__":
	main()
