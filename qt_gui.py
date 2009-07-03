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

shortcuts = dict(
        copy = 'Ctrl+T',
        reset = 'Ctrl+E',
        quit = 'Ctrl+W',
        inplace = 'Ctrl+R',
        )

def get_shortcut(name):
    return shortcuts[name]

def tooltip(widget, name):
    widget.setToolTip(u"%s %s" % (get_text(name), get_shortcut(name)))

def setClipboardText(text):
    app = QtGui.QApplication.instance()
    clipboard = app.clipboard()
    clipboard.setText(text)
    event = QtCore.QEvent(QtCore.QEvent.Clipboard)
    app.sendEvent(clipboard, event)

def main():
    app = QtGui.QApplication(sys.argv)
    app.setLayoutDirection(QtCore.Qt.RightToLeft)

    window = QtGui.QWidget()
    window.resize(750, 350)
    window.setWindowTitle(get_text('title'))
    window.setWindowIcon(QtGui.QIcon('art/icon.png'))

    vbox = QtGui.QVBoxLayout()
    hbox1 = QtGui.QHBoxLayout()
    hbox2 = QtGui.QHBoxLayout()
    edithbox = QtGui.QHBoxLayout()

    textArea = QtGui.QTextEdit()
    textBar = QtGui.QToolBar()
    textBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
    textBar.setIconSize(QtCore.QSize(30, 30))
    textBar.setFloatable(False)
    textBar.setMovable(False)


    toolBar = QtGui.QToolBar()
    toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
    toolBar.setIconSize(QtCore.QSize(50, 50))

    def help():
        help_doc = get_text('help_doc')
        webbrowser.open(os.path.join('docs', help_doc))

    def copy():
        text = unicode(textArea.toPlainText())
        rtl = rtlize(text)
        setClipboardText(rtl)

    def process_inplace():
        text = unicode(textArea.toPlainText())
        rtl = rtlize(text)
        textArea.setText(rtl)

    clearAction = QtGui.QAction(QtGui.QIcon('art/clear.png'), 
            get_text('reset'), window)
    clearAction.setShortcut('Ctrl+E')
    window.connect(clearAction, QtCore.SIGNAL('triggered()'),
            textArea, QtCore.SLOT('clear()'))

    inplaceAction = QtGui.QAction(QtGui.QIcon('art/inplace.png'),
            get_text('inplace'), window)
    inplaceAction.setShortcut('Ctrl+R')
    window.connect(inplaceAction, QtCore.SIGNAL('triggered()'), process_inplace)

    copyAction = QtGui.QAction(QtGui.QIcon('art/copy.png'),
            get_text('copy'), window)
    copyAction.setShortcut('Ctrl+T')
    window.connect(copyAction, QtCore.SIGNAL('triggered()'), copy)

    helpAction = QtGui.QAction(QtGui.QIcon('art/help.png'), 
            get_text('help'), window)
    helpAction.setShortcut('Ctrl+H')
    helpAction.setShortcut('F1')
    window.connect(helpAction, QtCore.SIGNAL('triggered()'), help)

    quitAction = QtGui.QAction(QtGui.QIcon('art/quit.png'),
            get_text('quit'), window)
    quitAction.setShortcut('Ctrl+W')
    window.connect(quitAction, QtCore.SIGNAL('triggered()'),
            app, QtCore.SLOT('quit()'))

    textBar.addAction(clearAction)
    textBar.addAction(inplaceAction)
    textBar.addAction(copyAction)

    toolBar.addAction(quitAction)
    toolBar.addAction(helpAction)

    vbox.addWidget(textArea)
    vbox.addWidget(textBar)
    vbox.addSpacing(20)
    vbox.addWidget(toolBar)

    window.setLayout(vbox)
    window.show()

    exit_code = app.exec_()
    sys.exit(exit_code)

if __name__ == '__main__':
    main()
