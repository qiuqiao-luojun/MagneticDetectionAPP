# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewDetectionClickedDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewDetection(object):
    def setupUi(self, NewDetection):
        NewDetection.setObjectName("NewDetection")
        NewDetection.resize(922, 467)
        NewDetection.setStyleSheet("QDialog{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 255));font: 12pt \"黑体\";}\n"
"\n"
"\n"
"")
        self.buttonBox = QtWidgets.QDialogButtonBox(NewDetection)
        self.buttonBox.setGeometry(QtCore.QRect(700, 410, 171, 32))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.SelectRowParameterPushButton = QtWidgets.QPushButton(NewDetection)
        self.SelectRowParameterPushButton.setGeometry(QtCore.QRect(20, 410, 131, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.SelectRowParameterPushButton.setFont(font)
        self.SelectRowParameterPushButton.setObjectName("SelectRowParameterPushButton")
        self.splitter = QtWidgets.QSplitter(NewDetection)
        self.splitter.setGeometry(QtCore.QRect(20, 8, 841, 381))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("QFrame{font: 12pt \"黑体\";}\n"
"QLineEdit{font: 12pt \"Times New Roman\";}\n"
"QRadioButton{font: 12pt \"黑体\";}\n"
"\n"
"\n"
"")
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.FileNameLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.FileNameLabel.setFont(font)
        self.FileNameLabel.setObjectName("FileNameLabel")
        self.gridLayout.addWidget(self.FileNameLabel, 1, 0, 1, 1)
        self.OilPipeTypeLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.OilPipeTypeLabel.setFont(font)
        self.OilPipeTypeLabel.setObjectName("OilPipeTypeLabel")
        self.gridLayout.addWidget(self.OilPipeTypeLabel, 2, 0, 1, 1)
        self.OilPipeTypeEdit = QtWidgets.QLineEdit(self.frame)
        self.OilPipeTypeEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.OilPipeTypeEdit.setFont(font)
        self.OilPipeTypeEdit.setObjectName("OilPipeTypeEdit")
        self.gridLayout.addWidget(self.OilPipeTypeEdit, 2, 1, 1, 1)
        self.OilPipeThicknessLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.OilPipeThicknessLabel.setFont(font)
        self.OilPipeThicknessLabel.setObjectName("OilPipeThicknessLabel")
        self.gridLayout.addWidget(self.OilPipeThicknessLabel, 2, 2, 1, 1)
        self.OilPipeThicknessEdit = QtWidgets.QLineEdit(self.frame)
        self.OilPipeThicknessEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OilPipeThicknessEdit.sizePolicy().hasHeightForWidth())
        self.OilPipeThicknessEdit.setSizePolicy(sizePolicy)
        self.OilPipeThicknessEdit.setObjectName("OilPipeThicknessEdit")
        self.gridLayout.addWidget(self.OilPipeThicknessEdit, 2, 3, 1, 1)
        self.OilPipeSpecificationLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.OilPipeSpecificationLabel.setFont(font)
        self.OilPipeSpecificationLabel.setObjectName("OilPipeSpecificationLabel")
        self.gridLayout.addWidget(self.OilPipeSpecificationLabel, 2, 4, 1, 1)
        self.OilPipeSpecificationEdit = QtWidgets.QLineEdit(self.frame)
        self.OilPipeSpecificationEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.OilPipeSpecificationEdit.setFont(font)
        self.OilPipeSpecificationEdit.setObjectName("OilPipeSpecificationEdit")
        self.gridLayout.addWidget(self.OilPipeSpecificationEdit, 2, 5, 1, 1)
        self.OperatorLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.OperatorLabel.setFont(font)
        self.OperatorLabel.setObjectName("OperatorLabel")
        self.gridLayout.addWidget(self.OperatorLabel, 3, 0, 1, 1)
        self.OperatorEdit = QtWidgets.QLineEdit(self.frame)
        self.OperatorEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.OperatorEdit.setFont(font)
        self.OperatorEdit.setObjectName("OperatorEdit")
        self.gridLayout.addWidget(self.OperatorEdit, 3, 1, 1, 1)
        self.DetectionDateLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DetectionDateLabel.setFont(font)
        self.DetectionDateLabel.setObjectName("DetectionDateLabel")
        self.gridLayout.addWidget(self.DetectionDateLabel, 3, 2, 1, 1)
        self.DetectionDateEdit = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DetectionDateEdit.setFont(font)
        self.DetectionDateEdit.setObjectName("DetectionDateEdit")
        self.gridLayout.addWidget(self.DetectionDateEdit, 3, 3, 1, 1)
        self.PulseDurationLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PulseDurationLabel.setFont(font)
        self.PulseDurationLabel.setObjectName("PulseDurationLabel")
        self.gridLayout.addWidget(self.PulseDurationLabel, 3, 4, 1, 1)
        self.PulseDurationcomboBox = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.PulseDurationcomboBox.setFont(font)
        self.PulseDurationcomboBox.setObjectName("PulseDurationcomboBox")
        self.PulseDurationcomboBox.addItem("")
        self.PulseDurationcomboBox.addItem("")
        self.PulseDurationcomboBox.addItem("")
        self.PulseDurationcomboBox.addItem("")
        self.PulseDurationcomboBox.addItem("")
        self.PulseDurationcomboBox.addItem("")
        self.gridLayout.addWidget(self.PulseDurationcomboBox, 3, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("QLabel{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0152284 rgba(51, 102, 153, 255));color: rgb(255, 255, 255);font: 16pt \"黑体\";}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 6)
        self.FileNameEdit = QtWidgets.QLineEdit(self.frame)
        self.FileNameEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.FileNameEdit.setFont(font)
        self.FileNameEdit.setDragEnabled(False)
        self.FileNameEdit.setReadOnly(False)
        self.FileNameEdit.setObjectName("FileNameEdit")
        self.gridLayout.addWidget(self.FileNameEdit, 1, 1, 1, 5)
        self.InformationtableWidget = QtWidgets.QTableWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.InformationtableWidget.sizePolicy().hasHeightForWidth())
        self.InformationtableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.InformationtableWidget.setFont(font)
        self.InformationtableWidget.setShowGrid(False)
        self.InformationtableWidget.setRowCount(20)
        self.InformationtableWidget.setObjectName("InformationtableWidget")
        self.InformationtableWidget.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.InformationtableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.InformationtableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.InformationtableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.InformationtableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.InformationtableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.InformationtableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.InformationtableWidget.setHorizontalHeaderItem(6, item)

        self.retranslateUi(NewDetection)
        self.buttonBox.accepted.connect(NewDetection.accept)
        self.buttonBox.rejected.connect(NewDetection.reject)
        QtCore.QMetaObject.connectSlotsByName(NewDetection)

    def retranslateUi(self, NewDetection):
        _translate = QtCore.QCoreApplication.translate
        NewDetection.setWindowTitle(_translate("NewDetection", "新建检测设置"))
        self.SelectRowParameterPushButton.setText(_translate("NewDetection", "选择该行数据"))
        self.FileNameLabel.setText(_translate("NewDetection", "*文件名称："))
        self.OilPipeTypeLabel.setText(_translate("NewDetection", "油管类型："))
        self.OilPipeThicknessLabel.setText(_translate("NewDetection", "钢管壁厚"))
        self.OilPipeSpecificationLabel.setText(_translate("NewDetection", "钢管规格"))
        self.OperatorLabel.setText(_translate("NewDetection", "操作员："))
        self.DetectionDateLabel.setText(_translate("NewDetection", "检测日期："))
        self.PulseDurationLabel.setText(_translate("NewDetection", "报警时长："))
        self.PulseDurationcomboBox.setItemText(0, _translate("NewDetection", "0.5s"))
        self.PulseDurationcomboBox.setItemText(1, _translate("NewDetection", "0.1s"))
        self.PulseDurationcomboBox.setItemText(2, _translate("NewDetection", "0.2s"))
        self.PulseDurationcomboBox.setItemText(3, _translate("NewDetection", "1.0s"))
        self.PulseDurationcomboBox.setItemText(4, _translate("NewDetection", "2.0s"))
        self.PulseDurationcomboBox.setItemText(5, _translate("NewDetection", "5.0s"))
        self.label.setText(_translate("NewDetection", "新建参数设置"))
        item = self.InformationtableWidget.horizontalHeaderItem(0)
        item.setText(_translate("NewDetection", "文件名称"))
        item = self.InformationtableWidget.horizontalHeaderItem(1)
        item.setText(_translate("NewDetection", "钢管类型"))
        item = self.InformationtableWidget.horizontalHeaderItem(2)
        item.setText(_translate("NewDetection", "钢管壁厚"))
        item = self.InformationtableWidget.horizontalHeaderItem(3)
        item.setText(_translate("NewDetection", "钢管规格"))
        item = self.InformationtableWidget.horizontalHeaderItem(4)
        item.setText(_translate("NewDetection", "操作员"))
        item = self.InformationtableWidget.horizontalHeaderItem(5)
        item.setText(_translate("NewDetection", "检测日期"))
        item = self.InformationtableWidget.horizontalHeaderItem(6)
        item.setText(_translate("NewDetection", "报警时长"))
