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
            inplace = u'معالجة النص في مكانه',
            quit = u'خروج',
            help = u'تعليمات',
            help_doc = 'help_arabic.html',
            ),
        english = dict(
            title = 'The Free Ressam (Er Ressam il Hur)',
            copy = 'Copy',
            reset = 'Reset',
            inplace = 'Process InPlace',
            quit = 'Quit',
            help = 'Help',
            help_doc = 'help_english.html',
                   )
        )

def get_text(name):
    """Basic (read: naive) mechanism for multi-language UI"""
    return t_text[language][name]

app = QtGui.QApplication(sys.argv)
app.setLayoutDirection(QtCore.Qt.RightToLeft)

# XXX: doesn't work right ..
def setClipboardText(text):
    clipboard = app.clipboard()
    clipboard.setText(text)
    event = QtCore.QEvent(QtCore.QEvent.Clipboard)
    app.sendEvent(clipboard, event)

window = QtGui.QWidget()
window.resize(450, 250)
window.setWindowTitle(get_text('title'))
window.setWindowIcon(QtGui.QIcon('art/icon.png'))

vbox = QtGui.QVBoxLayout()
hbox = QtGui.QHBoxLayout()
edithbox = QtGui.QHBoxLayout()

textArea = QtGui.QTextEdit()
outText = QtGui.QTextEdit()
smallBar = QtGui.QToolBar()
smallBar.setOrientation(QtCore.Qt.Vertical)

def copy():
    text = unicode(textArea.toPlainText())
    rtl = rtlize(text)
    setClipboardText(rtl)

def process_inplace():
    text = unicode(textArea.toPlainText())
    rtl = rtlize(text)
    textArea.setText(rtl)
quitBtn = QtGui.QPushButton(get_text('quit'))
window.connect(quitBtn, QtCore.SIGNAL('clicked()'), app, QtCore.SLOT('quit()'))

copyBtn = QtGui.QPushButton(get_text('copy'))
window.connect(copyBtn, QtCore.SIGNAL('clicked()'), copy)

clearAction = QtGui.QAction(QtGui.QIcon('art/clear.png'), get_text('reset'), smallBar)
window.connect(clearAction, QtCore.SIGNAL('triggered()'), textArea, QtCore.SLOT('clear()'))
inplaceAction = QtGui.QAction(QtGui.QIcon('art/inplace.png'), get_text('inplace'), smallBar)
inplaceAction.setShortcut('Ctrl+R')
window.connect(inplaceAction, QtCore.SIGNAL('triggered()'), process_inplace)
smallBar.addAction(clearAction)
smallBar.addAction(inplaceAction)

edithbox.addWidget(textArea)
edithbox.addWidget(smallBar)

hbox.addWidget(copyBtn)
hbox.addStretch(1)
hbox.addWidget(quitBtn)

vbox.addLayout(edithbox)
vbox.addSpacing(20)
vbox.addLayout(hbox)

window.setLayout(vbox)
window.show()

exit_code = app.exec_()
sys.exit(exit_code)

