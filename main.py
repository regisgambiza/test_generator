import sqlite3
import sys
import time
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplashScreen

from mainwindow import Ui_Baddaz_code

# Connect to database and get all data
db = sqlite3.connect("my_db.db")
cursor = db.cursor()
command = """SELECT * from questions"""
result = cursor.execute(command)


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_Baddaz_code()
        self.ui.setupUi(self.main_win)

        self.ui.pushButton.clicked.connect(self.show_next)
        self.ui.pushButton_3.clicked.connect(self.cancel)

        self.ui.stackedWidget.setCurrentIndex(0)



    def show(self):
        self.main_win.show()

    def show_next(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.get_data()

    def cancel(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def get_data(self):
        for value, data in enumerate(result):
            self.ui.textBrowser.setText(str(data[0]))
            self.ui.radioButton.setText(str(data[1]))
            self.ui.radioButton_4.setText(str(data[2]))
            self.ui.radioButton_2.setText(str(data[3]))
            self.ui.radioButton_3.setText(str(data[4]))



if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Creating the splash screen
    splash = QSplashScreen(QPixmap('picture.png'))
    splash.show()
    QTimer.singleShot(2000, splash.close)

    # Pretend to do something
    time.sleep(3)

    # Display main app
    main_win = MainWindow()

    # Apply qt-material stylesheet
    # apply_stylesheet(app, theme='dark_amber.xml')
    main_win.show()

    sys.exit(app.exec())
