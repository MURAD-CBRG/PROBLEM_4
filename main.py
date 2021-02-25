import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic
import sqlite3


class DataBase(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('main.ui', self)

        self.initUI()

    def initUI(self):
        data_base = sqlite3.connect('coffee.sqlite')

        cursor = data_base.cursor()

        query = "SELECT * FROM MainTable"
        res = cursor.execute(query).fetchall()

        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)

        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

        self.tableWidget.setHorizontalHeaderLabels(
            [
                'ID',
                'Название сорта',
                'Степень обжарки',
                'Молотый/в зернах',
                'Описание вкуса',
                'Цена',
                'Объем упаковки'
            ]
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataBase()
    window.show()
    sys.exit(app.exec())
