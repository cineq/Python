""" Window Painter """

from PyQt4 import QtGui


class MainWindow(QtGui.QWidget):
	def __init__(self):
		super().__init__()

		self.loadGraphics()

	def loadGraphics(self):
		self.main_layout = QtGui.QGridLayout()

		self.gScene = QtGui.QGraphicsScene()

		self.description = QtGui.QGraphicsTextItem("Robot Analyzer !!!")
		self.description_font = QtGui.QFont()
		self.description_font.setStyle(QtGui.QFont.StyleOblique)
		self.description.setFont(self.description_font)

		self.gScene.addItem(self.description)
		self.view = QtGui.QGraphicsView(self.gScene)

		self.main_layout.addWidget(self.view, 0, 0, )
		self.setLayout(self.main_layout)