import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
 
qtCreatorFile = "scrap.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
	self.pushButton.clicked.connect(self.ucitaj)

    def ucitaj(self):
	print "Hey"
	tekst = self.lineEdit.text()
	print self.lineEdit.text()
	item = QListWidgetItem("Item %s" % tekst)
	#self.listView.additem(tekst)
	self.listView.addItem(item)
	print tekst

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
