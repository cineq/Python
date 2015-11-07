""" Window Painter """

from PyQt4 import QtGui
import pyqtgraph

class MainWindow(QtGui.QWidget):
	def __init__(self):
		super().__init__()
		self.main_layout = QtGui.QGridLayout()

		self.gScene = QtGui.QGraphicsScene()

		self.write_description()

		self.gScene.addItem(self.description)
		self.view = QtGui.QGraphicsView(self.gScene)

		self.main_layout.addWidget(self.view, 0, 0, )
		self.create_plot()
		self.setLayout(self.main_layout)

		# Init Menu

	def write_description(self):
		self.description = QtGui.QGraphicsTextItem("Robot Analyzer !!!")
		self.description_font = QtGui.QFont()
		self.description_font.setStyle(QtGui.QFont.StyleOblique)
		self.description.setFont(self.description_font)

	def create_plot(self):

		self.plot = pyqtgraph.plot()
		self.main_layout.addWidget(self.plot, 0, 1, )