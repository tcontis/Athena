"""UI Layout"""
from PyQt5.QtCore import QObject
import sys
import pyqtgraph as pg
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QGridLayout, QMainWindow)
import socket

class UiMainWindow(QMainWindow):
    """The Main Window for the Athena Project"""

    def __init__(self):
        """Initialize Window"""
        super(UiMainWindow, self).__init__()
        self.setupUi()

    def setupUi(self):

        # Size window to default dimensions
        self.resize(1800, 900)
        self.setWindowTitle("Athena")
        self.showMaximized()

        # Create a central Widget and tabs
        self.central_tab_widget = QtWidgets.QTabWidget()
        self.tab_robot = QtWidgets.QWidget()

        self.tab_robot_master_grid_layout = QGridLayout()
        self.tab_robot_conn_box = QtWidgets.QGroupBox(self.central_tab_widget, title="Connect To Robot")
        self.tab_robot_conn_box.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_robot_conn_box_label = QtWidgets.QLabel("Enter IP or DNS:")
        self.tab_robot_conn_box_text_box = QtWidgets.QPlainTextEdit()
        self.tab_robot_conn_box_label_2 = QtWidgets.QLabel("")
        self.tab_robot_conn_box_button = QtWidgets.QPushButton("Connect!")
        self.tab_robot_conn_box_button.pressed.connect(self.connectButtonClicked)

        self.tab_robot_conn_box_vertical_layout = QtWidgets.QVBoxLayout(self.tab_robot_conn_box)
        self.tab_robot_conn_box_vertical_layout.addWidget(self.tab_robot_conn_box_label)
        self.tab_robot_conn_box_vertical_layout.addWidget(self.tab_robot_conn_box_text_box)
        self.tab_robot_conn_box_vertical_layout.addWidget(self.tab_robot_conn_box_label_2)
        self.tab_robot_conn_box_vertical_layout.addWidget(self.tab_robot_conn_box_button)

        self.tab_robot_master_grid_layout.addWidget(self.tab_robot_conn_box, 0, 0, 1, 1)
        self.tab_robot.setLayout(self.tab_robot_master_grid_layout)

        self.tab_control = QtWidgets.QWidget()
        self.central_tab_widget.addTab(self.tab_robot, "Robot")
        self.central_tab_widget.addTab(self.tab_control, "Control System")
        self.setCentralWidget(self.central_tab_widget)

        menubar = self.menuBar()

        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setWeight(50)
        menubar.setFont(font)
        menu_file = QtWidgets.QMenu(menubar)
        menu_file.setObjectName("menuFile")

        menu_file.setTitle("File")
        menubar.addAction(menu_file.menuAction())

        actionExit = QtWidgets.QAction(self)
        actionExit.setShortcut('Ctrl+Q')
        actionExit.triggered.connect(self.close)
        menubar.addAction(actionExit)
        self.setWindowFlags(
            QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMaximizeButtonHint)
        QtCore.QMetaObject.connectSlotsByName(self)

    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.question(self, 'Exit', "Are you sure you want to quit?",
                                               QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
            sys.exit()
        else:
            event.ignore()

    def connectButtonClicked(self):
        text = self.tab_robot_conn_box_text_box.toPlainText()
        if len(text.split(".")) == 4:
            try:
                data = socket.gethostbyaddr(text)
                self.tab_robot_conn_box_label_2.setText("Connected.")
            except socket.gaierror:
                self.tab_robot_conn_box_label_2.setText("Invalid or Unacceptable IPv4 Address: Could Not Get Address Info")
            except socket.herror:
                self.tab_robot_conn_box_label_2.setText("Invalid or Unacceptable IPv4 Address: Refused To Handshake")

        else:
            try:
                data = socket.gethostbyname(text)
                self.tab_robot_conn_box_label_2.setText("Connected.")
            except socket.gaierror:
                self.tab_robot_conn_box_label_2.setText("Invalid or Unacceptable DNS: Does Not Exist")
            except UnicodeError:
                self.tab_robot_conn_box_label_2.setText("Invalid or Unacceptable DNS: Invalid Characters")
            except Exception as e:
                print(type(e),'a')

