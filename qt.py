import os
import sys
import webbrowser
from process import rtlize
from PyQt4 import QtGui, QtCore

language = 'arabic'

t_text = dict(
        arabic = dict(
            title = u'الرسام الحر',
            copy = u'نسخ',
            reset = u'مسح',
            quit = u'خروج',
            help = u'تعليمات',
            help_doc = 'help_arabic.html',
            ),
        english = dict(
            title = 'The Free Ressam (Er Ressam il Hur)',
            copy = 'Copy',
            reset = 'Reset',
            quit = 'Quit',
            help = 'Help',
            help_doc = 'help_english.html',
                   )
        )

def get_text(name):
    """Basic (read: naive) mechanism for multi-language UI"""
    return t_text[language][name]

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.resize(250, 150)
window.setWindowTitle('Qt Window')
window.setWindowIcon(QtGui.QIcon('art/icon.png'))

vbox = QtGui.QVBoxLayout()
hbox = QtGui.QHBoxLayout()

quit_btn = QtGui.QPushButton(get_text('quit'))
window.connect(quit_btn, QtCore.SIGNAL('clicked()'), app, QtCore.SLOT('quit()'))
textArea = QtGui.QTextEdit()

hbox.addStretch(1)
hbox.addWidget(quit_btn)

vbox.addWidget(textArea)
vbox.addLayout(hbox)

window.setLayout(vbox)
window.show()

sys.exit(app.exec_())

