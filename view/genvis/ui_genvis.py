# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/krl1to5/Work/FULL/Sequence-ToolKit/2016/resources/ui/genvis/genvis.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(775, 556)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/img/logos/genvis.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tab_widget = QtWidgets.QTabWidget(self.central_widget)
        self.tab_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_widget.setElideMode(QtCore.Qt.ElideRight)
        self.tab_widget.setDocumentMode(True)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.setMovable(True)
        self.tab_widget.setTabBarAutoHide(False)
        self.tab_widget.setObjectName("tab_widget")
        self.gridLayout.addWidget(self.tab_widget, 0, 0, 1, 1)
        main_window.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 19))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_recent_files = QtWidgets.QMenu(self.menu_file)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/img/icons/open_recent.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_recent_files.setIcon(icon1)
        self.menu_recent_files.setObjectName("menu_recent_files")
        self.menu_edit = QtWidgets.QMenu(self.menubar)
        self.menu_edit.setObjectName("menu_edit")
        self.menu_options = QtWidgets.QMenu(self.menubar)
        self.menu_options.setObjectName("menu_options")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.standart_toolbar = QtWidgets.QToolBar(main_window)
        self.standart_toolbar.setObjectName("standart_toolbar")
        main_window.addToolBar(QtCore.Qt.TopToolBarArea, self.standart_toolbar)
        self.tools_toolbar = QtWidgets.QToolBar(main_window)
        self.tools_toolbar.setObjectName("tools_toolbar")
        main_window.addToolBar(QtCore.Qt.TopToolBarArea, self.tools_toolbar)
        self.applications_toolbar = QtWidgets.QToolBar(main_window)
        self.applications_toolbar.setObjectName("applications_toolbar")
        main_window.addToolBar(QtCore.Qt.TopToolBarArea, self.applications_toolbar)
        self.action_new = QtWidgets.QAction(main_window)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resources/img/icons/new.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new.setIcon(icon2)
        self.action_new.setObjectName("action_new")
        self.action_open = QtWidgets.QAction(main_window)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/resources/img/icons/open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open.setIcon(icon3)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(main_window)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/resources/img/icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save.setIcon(icon4)
        self.action_save.setObjectName("action_save")
        self.action_save_as = QtWidgets.QAction(main_window)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/resources/img/icons/save_as.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save_as.setIcon(icon5)
        self.action_save_as.setObjectName("action_save_as")
        self.action_save_all = QtWidgets.QAction(main_window)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/resources/img/icons/save_all.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save_all.setIcon(icon6)
        self.action_save_all.setObjectName("action_save_all")
        self.action_print = QtWidgets.QAction(main_window)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/resources/img/icons/print.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_print.setIcon(icon7)
        self.action_print.setObjectName("action_print")
        self.action_cut = QtWidgets.QAction(main_window)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/resources/img/icons/cut.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_cut.setIcon(icon8)
        self.action_cut.setObjectName("action_cut")
        self.action_copy = QtWidgets.QAction(main_window)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/resources/img/icons/copy.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_copy.setIcon(icon9)
        self.action_copy.setObjectName("action_copy")
        self.action_paste = QtWidgets.QAction(main_window)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/resources/img/icons/paste.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_paste.setIcon(icon10)
        self.action_paste.setObjectName("action_paste")
        self.action_help = QtWidgets.QAction(main_window)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/resources/img/icons/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_help.setIcon(icon11)
        self.action_help.setObjectName("action_help")
        self.action_about = QtWidgets.QAction(main_window)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/resources/img/icons/about.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about.setIcon(icon12)
        self.action_about.setObjectName("action_about")
        self.action_delete = QtWidgets.QAction(main_window)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/resources/img/icons/delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_delete.setIcon(icon13)
        self.action_delete.setObjectName("action_delete")
        self.action_quit = QtWidgets.QAction(main_window)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/resources/img/icons/quit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_quit.setIcon(icon14)
        self.action_quit.setObjectName("action_quit")
        self.action_close = QtWidgets.QAction(main_window)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/resources/img/icons/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_close.setIcon(icon15)
        self.action_close.setObjectName("action_close")
        self.action_clear_all = QtWidgets.QAction(main_window)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/resources/img/icons/delete_all.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_clear_all.setIcon(icon16)
        self.action_clear_all.setObjectName("action_clear_all")
        self.action_about_genvis = QtWidgets.QAction(main_window)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/resources/img/icons/about_variant.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about_genvis.setIcon(icon17)
        self.action_about_genvis.setObjectName("action_about_genvis")
        self.action_settings = QtWidgets.QAction(main_window)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/resources/img/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_settings.setIcon(icon18)
        self.action_settings.setObjectName("action_settings")
        self.action_exec_genrep = QtWidgets.QAction(main_window)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/resources/img/logos/genrep.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_exec_genrep.setIcon(icon19)
        self.action_exec_genrep.setObjectName("action_exec_genrep")
        self.action_undo = QtWidgets.QAction(main_window)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/resources/img/icons/undo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_undo.setIcon(icon20)
        self.action_undo.setObjectName("action_undo")
        self.action_redo = QtWidgets.QAction(main_window)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/resources/img/icons/redo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_redo.setIcon(icon21)
        self.action_redo.setObjectName("action_redo")
        self.action_exec_gensec = QtWidgets.QAction(main_window)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/resources/img/logos/gensec.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_exec_gensec.setIcon(icon22)
        self.action_exec_gensec.setObjectName("action_exec_gensec")
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.menu_recent_files.menuAction())
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_save_as)
        self.menu_file.addAction(self.action_save_all)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_print)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_close)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_quit)
        self.menu_edit.addAction(self.action_undo)
        self.menu_edit.addAction(self.action_redo)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.action_cut)
        self.menu_edit.addAction(self.action_copy)
        self.menu_edit.addAction(self.action_paste)
        self.menu_edit.addAction(self.action_delete)
        self.menu_edit.addAction(self.action_clear_all)
        self.menu_options.addAction(self.action_settings)
        self.menu_help.addAction(self.action_help)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.action_about_genvis)
        self.menu_help.addAction(self.action_about)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_options.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.standart_toolbar.addAction(self.action_new)
        self.standart_toolbar.addAction(self.action_open)
        self.standart_toolbar.addAction(self.action_save)
        self.standart_toolbar.addAction(self.action_print)
        self.applications_toolbar.addAction(self.action_exec_gensec)
        self.applications_toolbar.addAction(self.action_exec_genrep)

        self.retranslateUi(main_window)
        self.tab_widget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "GenVis"))
        self.menu_file.setTitle(_translate("main_window", "&File"))
        self.menu_recent_files.setTitle(_translate("main_window", "&Recent Files"))
        self.menu_edit.setTitle(_translate("main_window", "&Edit"))
        self.menu_options.setTitle(_translate("main_window", "&Options"))
        self.menu_help.setTitle(_translate("main_window", "&Help"))
        self.standart_toolbar.setWindowTitle(_translate("main_window", "Standar Bar"))
        self.tools_toolbar.setWindowTitle(_translate("main_window", "Tools Bar"))
        self.applications_toolbar.setWindowTitle(_translate("main_window", "Applications Bar"))
        self.action_new.setText(_translate("main_window", "&New"))
        self.action_new.setStatusTip(_translate("main_window", "Create a new file."))
        self.action_new.setShortcut(_translate("main_window", "Ctrl+N"))
        self.action_open.setText(_translate("main_window", "&Open"))
        self.action_open.setStatusTip(_translate("main_window", "Open an existing file."))
        self.action_open.setShortcut(_translate("main_window", "Ctrl+O"))
        self.action_save.setText(_translate("main_window", "&Save"))
        self.action_save.setStatusTip(_translate("main_window", "Save the current document on disk."))
        self.action_save.setShortcut(_translate("main_window", "Ctrl+S"))
        self.action_save_as.setText(_translate("main_window", "Save &As"))
        self.action_save_as.setStatusTip(_translate("main_window", "Save the current document under a new name."))
        self.action_save_as.setShortcut(_translate("main_window", "Ctrl+Shift+S"))
        self.action_save_all.setText(_translate("main_window", "Save A&ll"))
        self.action_save_all.setStatusTip(_translate("main_window", "Save all documents on disk."))
        self.action_print.setText(_translate("main_window", "&Print"))
        self.action_print.setStatusTip(_translate("main_window", "Print the current table."))
        self.action_print.setShortcut(_translate("main_window", "Ctrl+P"))
        self.action_cut.setText(_translate("main_window", "C&ut"))
        self.action_cut.setStatusTip(_translate("main_window", "Cut the current selection content to the clipboard."))
        self.action_cut.setShortcut(_translate("main_window", "Ctrl+X"))
        self.action_copy.setText(_translate("main_window", "&Copy"))
        self.action_copy.setStatusTip(_translate("main_window", "Copy the current selection content to the clipboard."))
        self.action_copy.setShortcut(_translate("main_window", "Ctrl+C"))
        self.action_paste.setText(_translate("main_window", "&Paste"))
        self.action_paste.setStatusTip(_translate("main_window", "Paste the clipboard content into the current selection."))
        self.action_paste.setShortcut(_translate("main_window", "Ctrl+V"))
        self.action_help.setText(_translate("main_window", "&Help"))
        self.action_help.setShortcut(_translate("main_window", "F1"))
        self.action_about.setText(_translate("main_window", "About &Sequence-ToolKit"))
        self.action_delete.setText(_translate("main_window", "&Delete"))
        self.action_delete.setStatusTip(_translate("main_window", "Remove the current selection."))
        self.action_delete.setShortcut(_translate("main_window", "Del"))
        self.action_quit.setText(_translate("main_window", "&Quit"))
        self.action_quit.setStatusTip(_translate("main_window", "Close all tabs and quit the application."))
        self.action_quit.setShortcut(_translate("main_window", "Ctrl+Q"))
        self.action_close.setText(_translate("main_window", "&Close"))
        self.action_close.setStatusTip(_translate("main_window", "Close the current tab."))
        self.action_close.setShortcut(_translate("main_window", "Ctrl+W"))
        self.action_clear_all.setText(_translate("main_window", "C&lear All"))
        self.action_clear_all.setStatusTip(_translate("main_window", "Delete all the content of the table."))
        self.action_clear_all.setShortcut(_translate("main_window", "Shift+Del"))
        self.action_about_genvis.setText(_translate("main_window", "About &GenVis"))
        self.action_about_genvis.setToolTip(_translate("main_window", "About GenVis"))
        self.action_settings.setText(_translate("main_window", "&Settings"))
        self.action_exec_genrep.setText(_translate("main_window", "GenRep"))
        self.action_exec_genrep.setToolTip(_translate("main_window", "Open Report Generator"))
        self.action_undo.setText(_translate("main_window", "Undo"))
        self.action_undo.setShortcut(_translate("main_window", "Ctrl+Z"))
        self.action_redo.setText(_translate("main_window", "Redo"))
        self.action_redo.setShortcut(_translate("main_window", "Ctrl+Shift+Z"))
        self.action_exec_gensec.setText(_translate("main_window", "GenSec"))
        self.action_exec_gensec.setToolTip(_translate("main_window", "Open Sequence Generator"))

import img_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/krl1to5/Work/FULL/Sequence-ToolKit/2016/resources/ui/genvis/genvis.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(775, 556)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/img/logos/genvis.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tab_widget = QtWidgets.QTabWidget(self.central_widget)
        self.tab_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_widget.setElideMode(QtCore.Qt.ElideRight)
        self.tab_widget.setDocumentMode(True)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.setMovable(True)
        self.tab_widget.setTabBarAutoHide(False)
        self.tab_widget.setObjectName("tab_widget")
        self.gridLayout.addWidget(self.tab_widget, 0, 0, 1, 1)
        main_window.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 19))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_recent_files = QtWidgets.QMenu(self.menu_file)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/img/icons/open_recent.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_recent_files.setIcon(icon1)
        self.menu_recent_files.setObjectName("menu_recent_files")
        self.menu_edit = QtWidgets.QMenu(self.menubar)
        self.menu_edit.setObjectName("menu_edit")
        self.menu_options = QtWidgets.QMenu(self.menubar)
        self.menu_options.setObjectName("menu_options")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.standard_toolbar = QtWidgets.QToolBar(main_window)
        self.standard_toolbar.setObjectName("standard_toolbar")
        main_window.addToolBar(QtCore.Qt.TopToolBarArea, self.standard_toolbar)
        self.tools_toolbar = QtWidgets.QToolBar(main_window)
        self.tools_toolbar.setObjectName("tools_toolbar")
        main_window.addToolBar(QtCore.Qt.TopToolBarArea, self.tools_toolbar)
        self.applications_toolbar = QtWidgets.QToolBar(main_window)
        self.applications_toolbar.setObjectName("applications_toolbar")
        main_window.addToolBar(QtCore.Qt.TopToolBarArea, self.applications_toolbar)
        self.action_new = QtWidgets.QAction(main_window)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resources/img/icons/new.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new.setIcon(icon2)
        self.action_new.setObjectName("action_new")
        self.action_open = QtWidgets.QAction(main_window)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/resources/img/icons/open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open.setIcon(icon3)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(main_window)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/resources/img/icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save.setIcon(icon4)
        self.action_save.setObjectName("action_save")
        self.action_save_as = QtWidgets.QAction(main_window)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/resources/img/icons/save_as.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save_as.setIcon(icon5)
        self.action_save_as.setObjectName("action_save_as")
        self.action_save_all = QtWidgets.QAction(main_window)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/resources/img/icons/save_all.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save_all.setIcon(icon6)
        self.action_save_all.setObjectName("action_save_all")
        self.action_print = QtWidgets.QAction(main_window)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/resources/img/icons/print.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_print.setIcon(icon7)
        self.action_print.setObjectName("action_print")
        self.action_cut = QtWidgets.QAction(main_window)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/resources/img/icons/cut.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_cut.setIcon(icon8)
        self.action_cut.setObjectName("action_cut")
        self.action_copy = QtWidgets.QAction(main_window)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/resources/img/icons/copy.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_copy.setIcon(icon9)
        self.action_copy.setObjectName("action_copy")
        self.action_paste = QtWidgets.QAction(main_window)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/resources/img/icons/paste.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_paste.setIcon(icon10)
        self.action_paste.setObjectName("action_paste")
        self.action_help = QtWidgets.QAction(main_window)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/resources/img/icons/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_help.setIcon(icon11)
        self.action_help.setObjectName("action_help")
        self.action_about = QtWidgets.QAction(main_window)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/resources/img/icons/about.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about.setIcon(icon12)
        self.action_about.setObjectName("action_about")
        self.action_delete = QtWidgets.QAction(main_window)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/resources/img/icons/delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_delete.setIcon(icon13)
        self.action_delete.setObjectName("action_delete")
        self.action_quit = QtWidgets.QAction(main_window)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/resources/img/icons/quit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_quit.setIcon(icon14)
        self.action_quit.setObjectName("action_quit")
        self.action_close = QtWidgets.QAction(main_window)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/resources/img/icons/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_close.setIcon(icon15)
        self.action_close.setObjectName("action_close")
        self.action_clear_all = QtWidgets.QAction(main_window)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/resources/img/icons/delete_all.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_clear_all.setIcon(icon16)
        self.action_clear_all.setObjectName("action_clear_all")
        self.action_about_genvis = QtWidgets.QAction(main_window)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/resources/img/icons/about_variant.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about_genvis.setIcon(icon17)
        self.action_about_genvis.setObjectName("action_about_genvis")
        self.action_settings = QtWidgets.QAction(main_window)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/resources/img/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_settings.setIcon(icon18)
        self.action_settings.setObjectName("action_settings")
        self.action_exec_genrep = QtWidgets.QAction(main_window)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/resources/img/logos/genrep.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_exec_genrep.setIcon(icon19)
        self.action_exec_genrep.setObjectName("action_exec_genrep")
        self.action_undo = QtWidgets.QAction(main_window)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/resources/img/icons/undo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_undo.setIcon(icon20)
        self.action_undo.setObjectName("action_undo")
        self.action_redo = QtWidgets.QAction(main_window)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/resources/img/icons/redo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_redo.setIcon(icon21)
        self.action_redo.setObjectName("action_redo")
        self.action_exec_gensec = QtWidgets.QAction(main_window)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/resources/img/logos/gensec.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_exec_gensec.setIcon(icon22)
        self.action_exec_gensec.setObjectName("action_exec_gensec")
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.menu_recent_files.menuAction())
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_save_as)
        self.menu_file.addAction(self.action_save_all)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_print)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_close)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_quit)
        self.menu_edit.addAction(self.action_undo)
        self.menu_edit.addAction(self.action_redo)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.action_cut)
        self.menu_edit.addAction(self.action_copy)
        self.menu_edit.addAction(self.action_paste)
        self.menu_edit.addAction(self.action_delete)
        self.menu_edit.addAction(self.action_clear_all)
        self.menu_options.addAction(self.action_settings)
        self.menu_help.addAction(self.action_help)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.action_about_genvis)
        self.menu_help.addAction(self.action_about)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_options.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.standard_toolbar.addAction(self.action_new)
        self.standard_toolbar.addAction(self.action_open)
        self.standard_toolbar.addAction(self.action_save)
        self.standard_toolbar.addAction(self.action_print)
        self.applications_toolbar.addAction(self.action_exec_gensec)
        self.applications_toolbar.addAction(self.action_exec_genrep)

        self.retranslateUi(main_window)
        self.tab_widget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "GenVis"))
        self.menu_file.setTitle(_translate("main_window", "&File"))
        self.menu_recent_files.setTitle(_translate("main_window", "&Recent Files"))
        self.menu_edit.setTitle(_translate("main_window", "&Edit"))
        self.menu_options.setTitle(_translate("main_window", "&Options"))
        self.menu_help.setTitle(_translate("main_window", "&Help"))
        self.standard_toolbar.setWindowTitle(_translate("main_window", "Standard Bar"))
        self.tools_toolbar.setWindowTitle(_translate("main_window", "Tools Bar"))
        self.applications_toolbar.setWindowTitle(_translate("main_window", "Applications Bar"))
        self.action_new.setText(_translate("main_window", "&New"))
        self.action_new.setStatusTip(_translate("main_window", "Create a new file."))
        self.action_new.setShortcut(_translate("main_window", "Ctrl+N"))
        self.action_open.setText(_translate("main_window", "&Open"))
        self.action_open.setStatusTip(_translate("main_window", "Open an existing file."))
        self.action_open.setShortcut(_translate("main_window", "Ctrl+O"))
        self.action_save.setText(_translate("main_window", "&Save"))
        self.action_save.setStatusTip(_translate("main_window", "Save the current document on disk."))
        self.action_save.setShortcut(_translate("main_window", "Ctrl+S"))
        self.action_save_as.setText(_translate("main_window", "Save &As"))
        self.action_save_as.setStatusTip(_translate("main_window", "Save the current document under a new name."))
        self.action_save_as.setShortcut(_translate("main_window", "Ctrl+Shift+S"))
        self.action_save_all.setText(_translate("main_window", "Save A&ll"))
        self.action_save_all.setStatusTip(_translate("main_window", "Save all documents on disk."))
        self.action_print.setText(_translate("main_window", "&Print"))
        self.action_print.setStatusTip(_translate("main_window", "Print the current table."))
        self.action_print.setShortcut(_translate("main_window", "Ctrl+P"))
        self.action_cut.setText(_translate("main_window", "C&ut"))
        self.action_cut.setStatusTip(_translate("main_window", "Cut the current selection content to the clipboard."))
        self.action_cut.setShortcut(_translate("main_window", "Ctrl+X"))
        self.action_copy.setText(_translate("main_window", "&Copy"))
        self.action_copy.setStatusTip(_translate("main_window", "Copy the current selection content to the clipboard."))
        self.action_copy.setShortcut(_translate("main_window", "Ctrl+C"))
        self.action_paste.setText(_translate("main_window", "&Paste"))
        self.action_paste.setStatusTip(_translate("main_window", "Paste the clipboard content into the current selection."))
        self.action_paste.setShortcut(_translate("main_window", "Ctrl+V"))
        self.action_help.setText(_translate("main_window", "&Help"))
        self.action_help.setShortcut(_translate("main_window", "F1"))
        self.action_about.setText(_translate("main_window", "About &Sequence-ToolKit"))
        self.action_delete.setText(_translate("main_window", "&Delete"))
        self.action_delete.setStatusTip(_translate("main_window", "Remove the current selection."))
        self.action_delete.setShortcut(_translate("main_window", "Del"))
        self.action_quit.setText(_translate("main_window", "&Quit"))
        self.action_quit.setStatusTip(_translate("main_window", "Close all tabs and quit the application."))
        self.action_quit.setShortcut(_translate("main_window", "Ctrl+Q"))
        self.action_close.setText(_translate("main_window", "&Close"))
        self.action_close.setStatusTip(_translate("main_window", "Close the current tab."))
        self.action_close.setShortcut(_translate("main_window", "Ctrl+W"))
        self.action_clear_all.setText(_translate("main_window", "C&lear All"))
        self.action_clear_all.setStatusTip(_translate("main_window", "Delete all the content of the table."))
        self.action_clear_all.setShortcut(_translate("main_window", "Shift+Del"))
        self.action_about_genvis.setText(_translate("main_window", "About &GenVis"))
        self.action_about_genvis.setToolTip(_translate("main_window", "About GenVis"))
        self.action_settings.setText(_translate("main_window", "&Settings"))
        self.action_exec_genrep.setText(_translate("main_window", "GenRep"))
        self.action_exec_genrep.setToolTip(_translate("main_window", "Open Report Generator"))
        self.action_undo.setText(_translate("main_window", "Undo"))
        self.action_undo.setShortcut(_translate("main_window", "Ctrl+Z"))
        self.action_redo.setText(_translate("main_window", "Redo"))
        self.action_redo.setShortcut(_translate("main_window", "Ctrl+Shift+Z"))
        self.action_exec_gensec.setText(_translate("main_window", "GenSec"))
        self.action_exec_gensec.setToolTip(_translate("main_window", "Open Sequence Generator"))

import img_rc
