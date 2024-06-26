# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anasayfa.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1120, 632)
        Form.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 50, 1021, 531))
        self.label.setStyleSheet("background-color: rgb(12, 49, 97);\n"
"border-radius: 20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_ikugames = QtWidgets.QLabel(Form)
        self.label_ikugames.setGeometry(QtCore.QRect(70, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_ikugames.setFont(font)
        self.label_ikugames.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border-radius: 10px;")
        self.label_ikugames.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ikugames.setObjectName("label_ikugames")
        self.pushButton_onerial = QtWidgets.QPushButton(Form)
        self.pushButton_onerial.setGeometry(QtCore.QRect(660, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_onerial.setFont(font)
        self.pushButton_onerial.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(216, 216, 216);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(163, 163, 163);\n"
"}")
        self.pushButton_onerial.setObjectName("pushButton_onerial")
        self.pushButton_cikis = QtWidgets.QPushButton(Form)
        self.pushButton_cikis.setGeometry(QtCore.QRect(970, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cikis.setFont(font)
        self.pushButton_cikis.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(168, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(176, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_cikis.setObjectName("pushButton_cikis")
        self.lineEdit_arama = QtWidgets.QLineEdit(Form)
        self.lineEdit_arama.setGeometry(QtCore.QRect(250, 60, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_arama.setFont(font)
        self.lineEdit_arama.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_arama.setText("")
        self.lineEdit_arama.setObjectName("lineEdit_arama")
        self.tableWidget_oyun = QtWidgets.QTableWidget(Form)
        self.tableWidget_oyun.setGeometry(QtCore.QRect(80, 160, 471, 361))
        self.tableWidget_oyun.setStyleSheet("border-radius: 10px;")
        self.tableWidget_oyun.setObjectName("tableWidget_oyun")
        self.tableWidget_oyun.setColumnCount(5)
        self.tableWidget_oyun.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_oyun.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_oyun.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_oyun.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_oyun.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_oyun.setHorizontalHeaderItem(4, item)
        self.tableWidget_koleksiyon = QtWidgets.QTableWidget(Form)
        self.tableWidget_koleksiyon.setGeometry(QtCore.QRect(570, 160, 471, 161))
        self.tableWidget_koleksiyon.setStyleSheet("border-radius: 10px;")
        self.tableWidget_koleksiyon.setObjectName("tableWidget_koleksiyon")
        self.tableWidget_koleksiyon.setColumnCount(4)
        self.tableWidget_koleksiyon.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_koleksiyon.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_koleksiyon.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_koleksiyon.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_koleksiyon.setHorizontalHeaderItem(3, item)
        self.tableWidget_favori = QtWidgets.QTableWidget(Form)
        self.tableWidget_favori.setGeometry(QtCore.QRect(570, 360, 471, 161))
        self.tableWidget_favori.setStyleSheet("border-radius: 10px;")
        self.tableWidget_favori.setObjectName("tableWidget_favori")
        self.tableWidget_favori.setColumnCount(4)
        self.tableWidget_favori.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_favori.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_favori.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_favori.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_favori.setHorizontalHeaderItem(3, item)
        self.label_oyunlar = QtWidgets.QLabel(Form)
        self.label_oyunlar.setGeometry(QtCore.QRect(80, 120, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_oyunlar.setFont(font)
        self.label_oyunlar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border-radius: 10px;")
        self.label_oyunlar.setAlignment(QtCore.Qt.AlignCenter)
        self.label_oyunlar.setObjectName("label_oyunlar")
        self.label_koleksiyonum = QtWidgets.QLabel(Form)
        self.label_koleksiyonum.setGeometry(QtCore.QRect(570, 120, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_koleksiyonum.setFont(font)
        self.label_koleksiyonum.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border-radius: 10px;")
        self.label_koleksiyonum.setAlignment(QtCore.Qt.AlignCenter)
        self.label_koleksiyonum.setObjectName("label_koleksiyonum")
        self.label_favorioyunlarim = QtWidgets.QLabel(Form)
        self.label_favorioyunlarim.setGeometry(QtCore.QRect(570, 320, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_favorioyunlarim.setFont(font)
        self.label_favorioyunlarim.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border-radius: 10px;")
        self.label_favorioyunlarim.setAlignment(QtCore.Qt.AlignCenter)
        self.label_favorioyunlarim.setObjectName("label_favorioyunlarim")
        self.pushButton_koleksiyonekle = QtWidgets.QPushButton(Form)
        self.pushButton_koleksiyonekle.setGeometry(QtCore.QRect(90, 530, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_koleksiyonekle.setFont(font)
        self.pushButton_koleksiyonekle.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(216, 216, 216);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(163, 163, 163);\n"
"}")
        self.pushButton_koleksiyonekle.setObjectName("pushButton_koleksiyonekle")
        self.pushButton_favoriekle = QtWidgets.QPushButton(Form)
        self.pushButton_favoriekle.setGeometry(QtCore.QRect(580, 530, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_favoriekle.setFont(font)
        self.pushButton_favoriekle.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(216, 216, 216);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(163, 163, 163);\n"
"}")
        self.pushButton_favoriekle.setObjectName("pushButton_favoriekle")
        self.pushButton_favorisil = QtWidgets.QPushButton(Form)
        self.pushButton_favorisil.setGeometry(QtCore.QRect(830, 530, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_favorisil.setFont(font)
        self.pushButton_favorisil.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(168, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(176, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_favorisil.setObjectName("pushButton_favorisil")
        self.pushButton_begen = QtWidgets.QPushButton(Form)
        self.pushButton_begen.setGeometry(QtCore.QRect(260, 530, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_begen.setFont(font)
        self.pushButton_begen.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(216, 216, 216);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(163, 163, 163);\n"
"}")
        self.pushButton_begen.setObjectName("pushButton_begen")
        self.pushButton_begenme = QtWidgets.QPushButton(Form)
        self.pushButton_begenme.setGeometry(QtCore.QRect(410, 530, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_begenme.setFont(font)
        self.pushButton_begenme.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(216, 216, 216);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(163, 163, 163);\n"
"}")
        self.pushButton_begenme.setObjectName("pushButton_begenme")
        self.pushButton_oyunekle = QtWidgets.QPushButton(Form)
        self.pushButton_oyunekle.setGeometry(QtCore.QRect(850, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_oyunekle.setFont(font)
        self.pushButton_oyunekle.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(216, 216, 216);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(163, 163, 163);\n"
"}")
        self.pushButton_oyunekle.setObjectName("pushButton_oyunekle")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_ikugames.setText(_translate("Form", "İKU GAMES"))
        self.pushButton_onerial.setText(_translate("Form", "Oyun Önerisi Al"))
        self.pushButton_cikis.setText(_translate("Form", "Çıkış Yap"))
        self.lineEdit_arama.setPlaceholderText(_translate("Form", "Oyun"))
        item = self.tableWidget_oyun.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Ad"))
        item = self.tableWidget_oyun.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Tür"))
        item = self.tableWidget_oyun.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Yapımcı"))
        item = self.tableWidget_oyun.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Platform"))
        item = self.tableWidget_oyun.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Puan"))
        item = self.tableWidget_koleksiyon.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Ad"))
        item = self.tableWidget_koleksiyon.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Tür"))
        item = self.tableWidget_koleksiyon.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Yapımcı"))
        item = self.tableWidget_koleksiyon.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Platform"))
        item = self.tableWidget_favori.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Ad"))
        item = self.tableWidget_favori.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Tür"))
        item = self.tableWidget_favori.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Yapımcı"))
        item = self.tableWidget_favori.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Platform"))
        self.label_oyunlar.setText(_translate("Form", "Oyunlar"))
        self.label_koleksiyonum.setText(_translate("Form", "Koleksiyonum"))
        self.label_favorioyunlarim.setText(_translate("Form", "Favori Oyunlarım"))
        self.pushButton_koleksiyonekle.setText(_translate("Form", "Koleksiyona Ekle"))
        self.pushButton_favoriekle.setText(_translate("Form", "Favori listesine ekle"))
        self.pushButton_favorisil.setText(_translate("Form", "Favori listesinden kaldır"))
        self.pushButton_begen.setText(_translate("Form", "Beğen"))
        self.pushButton_begenme.setText(_translate("Form", "Beğenme"))
        self.pushButton_oyunekle.setText(_translate("Form", "Oyun Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
