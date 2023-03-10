# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stock_items.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StockItemsDialog(object):
    def setupUi(self, StockItemsDialog):
        StockItemsDialog.setObjectName("StockItemsDialog")
        StockItemsDialog.resize(498, 349)
        self.stockItemsLabel = QtWidgets.QLabel(StockItemsDialog)
        self.stockItemsLabel.setGeometry(QtCore.QRect(200, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.stockItemsLabel.setFont(font)
        self.stockItemsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stockItemsLabel.setObjectName("stockItemsLabel")
        self.idDisplay = QtWidgets.QTextEdit(StockItemsDialog)
        self.idDisplay.setGeometry(QtCore.QRect(30, 230, 31, 21))
        self.idDisplay.setObjectName("idDisplay")
        self.itemNameDisplay = QtWidgets.QTextEdit(StockItemsDialog)
        self.itemNameDisplay.setGeometry(QtCore.QRect(80, 230, 171, 21))
        self.itemNameDisplay.setObjectName("itemNameDisplay")
        self.itemUnitDisplay = QtWidgets.QTextEdit(StockItemsDialog)
        self.itemUnitDisplay.setGeometry(QtCore.QRect(270, 230, 121, 21))
        self.itemUnitDisplay.setObjectName("itemUnitDisplay")
        self.categoryDisplay = QtWidgets.QTextEdit(StockItemsDialog)
        self.categoryDisplay.setGeometry(QtCore.QRect(410, 230, 51, 21))
        self.categoryDisplay.setObjectName("categoryDisplay")
        self.leftComboBox = QtWidgets.QComboBox(StockItemsDialog)
        self.leftComboBox.setGeometry(QtCore.QRect(30, 260, 31, 22))
        self.leftComboBox.setObjectName("leftComboBox")
        self.textEdit_2 = QtWidgets.QTextEdit(StockItemsDialog)
        self.textEdit_2.setGeometry(QtCore.QRect(80, 260, 281, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.rightComboBox = QtWidgets.QComboBox(StockItemsDialog)
        self.rightComboBox.setGeometry(QtCore.QRect(370, 260, 91, 22))
        self.rightComboBox.setObjectName("rightComboBox")
        self.addStockItemsButton = QtWidgets.QPushButton(StockItemsDialog)
        self.addStockItemsButton.setGeometry(QtCore.QRect(30, 320, 62, 19))
        self.addStockItemsButton.setObjectName("addStockItemsButton")
        self.updateStockItemsButton = QtWidgets.QPushButton(StockItemsDialog)
        self.updateStockItemsButton.setGeometry(QtCore.QRect(180, 320, 62, 19))
        self.updateStockItemsButton.setObjectName("updateStockItemsButton")
        self.deleteStockItemsButton = QtWidgets.QPushButton(StockItemsDialog)
        self.deleteStockItemsButton.setGeometry(QtCore.QRect(260, 320, 62, 19))
        self.deleteStockItemsButton.setObjectName("deleteStockItemsButton")
        self.cancelStockItensButton = QtWidgets.QPushButton(StockItemsDialog)
        self.cancelStockItensButton.setGeometry(QtCore.QRect(370, 320, 62, 19))
        self.cancelStockItensButton.setObjectName("cancelStockItensButton")
        self.stockItemsTableView = QtWidgets.QTableView(StockItemsDialog)
        self.stockItemsTableView.setGeometry(QtCore.QRect(30, 40, 431, 181))
        self.stockItemsTableView.setObjectName("stockItemsTableView")

        self.retranslateUi(StockItemsDialog)
        self.cancelStockItensButton.clicked.connect(StockItemsDialog.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(StockItemsDialog)

    def retranslateUi(self, StockItemsDialog):
        _translate = QtCore.QCoreApplication.translate
        StockItemsDialog.setWindowTitle(_translate("StockItemsDialog", "Stock Items"))
        self.stockItemsLabel.setText(_translate("StockItemsDialog", "Stock Items"))
        self.addStockItemsButton.setText(_translate("StockItemsDialog", "Add"))
        self.updateStockItemsButton.setText(_translate("StockItemsDialog", "Update"))
        self.deleteStockItemsButton.setText(_translate("StockItemsDialog", "Delete"))
        self.cancelStockItensButton.setText(_translate("StockItemsDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StockItemsDialog = QtWidgets.QDialog()
    ui = Ui_StockItemsDialog()
    ui.setupUi(StockItemsDialog)
    StockItemsDialog.show()
    sys.exit(app.exec_())
