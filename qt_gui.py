"""
    Author: Hasen il Judy
    License: GPL v2
"""
import os
import sys
import webbrowser
from process import rtlize, restore
from PyQt4 import QtGui, QtCore

language = 'arabic'

t_text = dict(
        arabic = dict(
            title = u'الرسام الحر',
            copy = u'نسخ',
            reset = u'مسح',
            restore = u'معالجة عكسية',
            quit = u'خروج',
            help = u'تعليمات',
            help_doc = 'help_arabic.html',
            lang = u'English',
            ),
        english = dict(
            title = 'The Free Ressam (Er Ressam il Hur)',
            copy = 'Copy',
            reset = 'Reset',
            restore = 'Reverse Process',
            quit = 'Quit',
            help = 'Help',
            help_doc = 'help_english.html',
            lang = 'عربي'
                   )
        )

def get_text(name):
    """Basic (read: naive) mechanism for multi-language UI"""
    return t_text[language][name]

shortcuts = dict(
        copy = 'Ctrl+T',
        reset = 'Ctrl+E',
        quit = 'Ctrl+W',
        restore = 'Ctrl+R',
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
    textArea.setFont(QtGui.QFont("Arial", 12, 75))

    textBar = QtGui.QToolBar()
    textBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
    textBar.setIconSize(QtCore.QSize(50, 50))
    textBar.setFloatable(False)
    textBar.setMovable(False)


    toolBar = QtGui.QToolBar()
    toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
    toolBar.setIconSize(QtCore.QSize(30, 30))

    def help():
        help_doc = get_text('help_doc')
        webbrowser.open(os.path.join('docs', help_doc))

    def copy():
        text = unicode(textArea.toPlainText())
        rtl = rtlize(text)
        setClipboardText(rtl)

    def unprocess():
        # remember cursor position (doesn't really work, oh well)
        cursor = textArea.textCursor()
        # Restore text
        text = unicode(textArea.toPlainText())
        restored = restore(text)
        textArea.setText(restored)
        # restore cursor
        textArea.setTextCursor(cursor)
        

    clearAction = QtGui.QAction(QtGui.QIcon('art/clear.png'), 
            get_text('reset'), window)
    clearAction.setShortcut('Ctrl+E')
    window.connect(clearAction, QtCore.SIGNAL('triggered()'),
            textArea, QtCore.SLOT('clear()'))

    restoreAction = QtGui.QAction(QtGui.QIcon('art/restore.png'),
            get_text('restore'), window)
    restoreAction.setShortcut('Ctrl+R')
    window.connect(restoreAction, QtCore.SIGNAL('triggered()'), unprocess)

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


    textBar.addAction(copyAction)
    textBar.addAction(restoreAction)
    textBar.addAction(clearAction)

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
