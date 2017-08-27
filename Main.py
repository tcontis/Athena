"""Class that runs entire Software project"""

import time
import datetime
import UI
from PyQt5.Qt import QApplication, QTimer
import numpy as np

#from DecisionNetwork import DecisionNetwork, DataProcessor


class Main(QApplication):
    """
    Main Class
    """

    def __init__(self, log_path):
        super(Main, self).__init__([])
        self.log_path = log_path

    def create_window(self):
        """Creates a window and application"""
        self.form = UI.UiMainWindow()
        self.form.show()
        self.form.update()
        self.start = time.time()

    def main_loop(self):
        self.processEvents()

if __name__ == '__main__':
    m = Main("logs/log.txt")
    m.create_window()
    while True:
        m.processEvents()
