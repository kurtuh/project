import sys
import datetime
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QDialog, QMessageBox
from MainWindow import Ui_MainWindow
from MainWindow1 import Ui_Dialog


class menu1(QDialog):
    def __init__(self):
        super(menu1, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.remove)
    def remove(self):
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        self.ui.lineEdit.setText('')
        self.ui.lineEdit_2.setText('')
        self.ui.label.setText('Вы зарегистрировались!')
        with open('order.txt', 'r') as file:
            content = file.read()
        with open('order.txt', 'a') as file:
            file.write(login + '\n')

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_10.clicked.connect(self.pizza)
        self.ui.pushButton_11.clicked.connect(self.toast)
        self.ui.pushButton_12.clicked.connect(self.tartar)
        self.ui.pushButton_13.clicked.connect(self.sushi)
        self.ui.pushButton_14.clicked.connect(self.burger)
        self.ui.pushButton_15.clicked.connect(self.cola)
        self.ui.pushButton_16.clicked.connect(self.pasta)
        self.ui.pushButton_17.clicked.connect(self.milkshake)
        self.ui.pushButton_18.clicked.connect(self.order)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.pushButton.clicked.connect(self.up_window)

    def up_window(self):
        self.new_window = menu1()
        self.new_window.show()
    def pizza(self):
        current_value = self.ui.label_2.text()
        new_value = int(current_value) + 400
        self.ui.label_2.setText(str(new_value))
        name = 'Пицца чоризо фреш'
        found = False
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 0)
            if item and item.text() == name:
                quantity_item = self.ui.tableWidget.item(row, 1)
                if quantity_item:
                    quantity_item.setText(str(int(quantity_item.text()) + 1))
                found = True
                break
        if not found:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            x = QTableWidgetItem(name)
            self.ui.tableWidget.setItem(row, 0, x)
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem('1'))
        file = open('order.txt', 'r')
        with open('order.txt', 'a') as file:
            file.write(name + ' \n')

    def toast(self):
        current_value = self.ui.label_2.text()
        new_value = int(current_value) + 300
        self.ui.label_2.setText(str(new_value))
        name = 'Тост с авокадо и яйцом'
        found = False
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 0)
            if item and item.text() == name:
                quantity_item = self.ui.tableWidget.item(row, 1)
                if quantity_item:
                    quantity_item.setText(str(int(quantity_item.text()) + 1))
                found = True
                break
        if not found:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            x = QTableWidgetItem(name)
            self.ui.tableWidget.setItem(row, 0, x)
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem('1'))
        file = open('order.txt', 'r')
        with open('order.txt', 'a') as file:
            file.write(name + ' \n')
    def tartar(self):
        current_value = self.ui.label_2.text()
        new_value = int(current_value) + 500
        self.ui.label_2.setText(str(new_value))
        name = 'Тар тар с говядиной'
        found = False
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 0)
            if item and item.text() == name:
                quantity_item = self.ui.tableWidget.item(row, 1)
                if quantity_item:
                    quantity_item.setText(str(int(quantity_item.text()) + 1))
                found = True
                break
        if not found:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            x = QTableWidgetItem(name)
            self.ui.tableWidget.setItem(row, 0, x)
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem('1'))
        file = open('order.txt', 'r')
        with open('order.txt', 'a') as file:
            file.write(name + ' \n')
    def sushi(self):
        current_value = self.ui.label_2.text()
        new_value = int(current_value) + 450
        self.ui.label_2.setText(str(new_value))
        name = 'Суши Филадельфия'
        found = False
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 0)
            if item and item.text() == name:
                quantity_item = self.ui.tableWidget.item(row, 1)
                if quantity_item:
                    quantity_item.setText(str(int(quantity_item.text()) + 1))
                found = True
                break
        if not found:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            x = QTableWidgetItem(name)
            self.ui.tableWidget.setItem(row, 0, x)
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem('1'))
        file = open('order.txt', 'r')
        with open('order.txt', 'a') as file:
            file.write(name + ' \n')
    def burger(self):
        current_value = self.ui.label_2.text()
        new_value = int(current_value) + 520
        self.ui.label_2.setText(str(new_value))
        name = 'Бургер с мраморной говядиной'
        found = False
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 0)
            if item and item.text() == name:
                quantity_item = self.ui.tableWidget.item(row, 1)
                if quantity_item:
                    quantity_item.setText(str(int(quantity_item.text()) + 1))
                found = True
                break
        if not found:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            x = QTableWidgetItem(name)
            self.ui.tableWidget.setItem(row, 0, x)
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem('1'))
        file = open('order.txt', 'r')
        with open('order.txt', 'a') as file:
            file.write(name + ' \n')
    def cola(self):
        current_value = self.ui.label_2.text()
        new_value = int(current_value) + 200
        self.ui.label_2.setText(str(new_value))
        name = 'Кока кола)'
        found = False
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 0)
            if item and item.text() == name:
                quantity_item = self.ui.tableWidget.item(row, 1)
                if quantity_item:
                    quantity_item.setText(str(int(quantity_item.text()) + 1))
                found = True
                break
        if not found:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            x = QTableWidgetItem(name)
            self.ui.tableWidget.setItem(row, 0, x)
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem('1'))
        file = open('order.txt', 'r')
        with open('order.txt', 'a') as file:
            file.write(name + ' \n')
    def pasta(self):
        current_value = self.ui.label_2.text()
        new_value = int(current_value) + 420
        self.ui.label_2.setText(str(new_value))
        name = 'Паста карбонара'
        found = False
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 0)
            if item and item.text() == name:
                quantity_item = self.ui.tableWidget.item(row, 1)
                if quantity_item:
                    quantity_item.setText(str(int(quantity_item.text()) + 1))
                found = True
                break
        if not found:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            x = QTableWidgetItem(name)
            self.ui.tableWidget.setItem(row, 0, x)
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem('1'))
        file = open('order.txt', 'r')
        with open('order.txt', 'a') as file:
            file.write(name + ' \n')
    def milkshake(self):
        current_value = self.ui.label_2.text()
        new_value = int(current_value) + 300
        self.ui.label_2.setText(str(new_value))
        name = 'Молочный коктейль'
        found = False
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 0)
            if item and item.text() == name:
                quantity_item = self.ui.tableWidget.item(row, 1)
                if quantity_item:
                    quantity_item.setText(str(int(quantity_item.text()) + 1))
                found = True
                break
        if not found:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            x = QTableWidgetItem(name)
            self.ui.tableWidget.setItem(row, 0, x)
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem('1'))
        file = open('order.txt', 'r')
        with open('order.txt', 'a') as file:
            file.write(name + ' \n')
    def order(self):
        self.ui.label_2.setText('0')
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        current_value = self.ui.label_2.text()
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        x = QTableWidgetItem('Ваш заказ принят')
        self.ui.tableWidget.setItem(row, 0, x)
        quantity_item = self.ui.tableWidget.item(row, 0)
        file = open('order.txt', 'r')
        with open('order.txt', 'a') as file:
            file.write('Ваш заказ принят' + ' \n')
        with open('order.txt', 'a') as file:
            file.write(str(datetime.datetime.now()) + '\n' + '\n')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())