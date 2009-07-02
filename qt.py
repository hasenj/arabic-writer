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

# XXX: doesn't work right ..
def setClipboardText(text):
    clipboard = app.clipboard()
    clipboard.setText(text)
    event = QtCore.QEvent(QtCore.QEvent.Clipboard)
    app.sendEvent(clipboard, event)

window = QtGui.QWidget()
window.resize(250, 150)
window.setWindowTitle('Qt Window')
window.setWindowIcon(QtGui.QIcon('art/icon.png'))

vbox = QtGui.QVBoxLayout()
hbox = QtGui.QHBoxLayout()

textArea = QtGui.QTextEdit()

quitBtn = QtGui.QPushButton(get_text('quit'))
window.connect(quitBtn, QtCore.SIGNAL('clicked()'), app, QtCore.SLOT('quit()'))

copyBtn = QtGui.QPushButton(get_text('copy'))
def copy():
    text = unicode(textArea.toPlainText())
    rtl = rtlize(text)
    setClipboardText(rtl)
window.connect(quitBtn, QtCore.SIGNAL('clicked()'), copy)


hbox.addWidget(copyBtn)
hbox.addStretch(1)
hbox.addWidget(quitBtn)

vbox.addWidget(textArea)
vbox.addSpacing(20)
vbox.addLayout(hbox)

window.setLayout(vbox)
window.show()

exit_code = app.exec_()
# sys.exit(exit_code)

