import sys
from PyQt4 import QtGui, QtCore

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.resize(250, 150)
window.setWindowTitle('Qt Window')
window.setWindowIcon(QtGui.QIcon('art/icon.png'))
quit_btn = QtGui.QPushButton('Quit', window)
quit_btn.setGeometry(10, 10, 60, 35)
window.connect(quit_btn, QtCore.SIGNAL('clicked()'), app, QtCore.SLOT('quit()'))

window.show()

sys.exit(app.exec_())

