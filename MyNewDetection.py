# -*- coding: utf-8 -*-
import csv
import os
import sys
import traceback

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QAbstractItemView

from PyQt5.QtCore import QDateTime, pyqtSlot, Qt

from NewDetectionClickedDialog import Ui_NewDetection

def JudgeBool(A):
    if A[0] == 'F':
        return False
    else:
        return True

class QmyNewDetection(QDialog):

    def __init__(self, PulseDuration = '0.5s',parent=None):

        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_NewDetection()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.ui.InformationtableWidget.setRowCount(180)
        self.ui.InformationtableWidget.setAlternatingRowColors(True)
        headerText = ["文件名称", "钢管类型", "钢管壁厚", "钢管规格", "操作员", "检测日期", "报警时长"]
        self.ui.InformationtableWidget.setColumnCount(len(headerText))  # 列数
        ##        self.ui.tableInfo.setHorizontalHeaderLabels(headerText)   #简单的表头文字，无格式

        for i in range(len(headerText)):
            headerItem = QTableWidgetItem(headerText[i])
            headerItem.setFont(QFont('SimHei', 12))
            self.ui.InformationtableWidget.setHorizontalHeaderItem(i, headerItem)
        self.initNewDetection(PulseDuration)


    def initNewDetection(self,PulseDuration):
        self.ui.PulseDurationcomboBox.setCurrentText(PulseDuration)
        curDateTime = QDateTime.currentDateTime()
        self.ui.DetectionDateEdit.setText(curDateTime.toString("yyyy-MM-dd hh:mm:ss"))
        currenttime = QDateTime.currentDateTime()
        self.ui.FileNameEdit.setText(currenttime.toString("yyyy年MM月dd日hh时mm分ss秒"))
        if os.path.isfile('data_storage_location' + '\\TotalInformation.csv'):
            with open('data_storage_location' + '\\TotalInformation.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                i = 0
                for row in reader:
                    if row != []:
                        for j in range(7):
                            newItem = QTableWidgetItem(row[j])
                            newItem.setFont(QFont('Times', 10))
                            self.ui.InformationtableWidget.setItem(i, j, newItem)
                    i = i+1
        # 禁止编辑
        self.ui.InformationtableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 整行选择
        self.ui.InformationtableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 隐藏表格线
        self.ui.InformationtableWidget.setShowGrid(False)
        self.ui.InformationtableWidget.sortItems(5,Qt.DescendingOrder)


    @pyqtSlot()
    def on_SelectRowParameterPushButton_clicked(self):
        try:
            global Newfilename,OilPipeType,OilPipeThickness,OilPipeSpecification,Operator,DetectionData, PulseDuration
            curRow = self.ui.InformationtableWidget.currentRow()  # 当前行号
            Newfilename=self.ui.InformationtableWidget.item(curRow, 0).text()
            OilPipeType = self.ui.InformationtableWidget.item(curRow, 1).text()
            OilPipeThickness = self.ui.InformationtableWidget.item(curRow, 2).text()
            OilPipeSpecification = self.ui.InformationtableWidget.item(curRow, 3).text()
            Operator = self.ui.InformationtableWidget.item(curRow, 4).text()
            DetectionData = self.ui.InformationtableWidget.item(curRow, 5).text()
            PulseDuration  = self.ui.InformationtableWidget.item(curRow, 6).text()
            self.ui.FileNameEdit.setText('%s' % Newfilename)
            self.ui.OilPipeTypeEdit.setText('%s' % OilPipeType)
            self.ui.OilPipeThicknessEdit.setText('%s' % OilPipeThickness)
            self.ui.OilPipeSpecificationEdit.setText('%s' % OilPipeSpecification)
            self.ui.OperatorEdit.setText('%s' % Operator)
            self.ui.PulseDurationcomboBox.setCurrentText('%s' % PulseDuration)
        except Exception as err:
            print(traceback.format_exc())


    def get_NewDetectionParameters(self):
        global paremters
        Newfilename = self.ui.FileNameEdit.text()
        OilPipeType = self.ui.OilPipeTypeEdit.text()
        OilPipeThickness = self.ui.OilPipeThicknessEdit.text()
        OilPipeSpecification = self.ui.OilPipeSpecificationEdit.text()
        Operator = self.ui.OperatorEdit.text()
        DetectionData = self.ui.DetectionDateEdit.text()
        PulseDuration = self.ui.PulseDurationcomboBox.currentText()
        return Newfilename,OilPipeType,OilPipeThickness,OilPipeSpecification,Operator,DetectionData, PulseDuration


if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyNewDetection()  # 创建窗体
    form.show()
    sys.exit(app.exec_())