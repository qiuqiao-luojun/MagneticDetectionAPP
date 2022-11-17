# -*-coding:utf-8-*-
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication, QSpinBox

from WaveAdjustDialog import Ui_Dialog


class QmyWaveAdjust(QDialog):

    def __init__(self, gaindata = [1]*32, XAxisLength=1000, CompressRatio=1, AlarmThreshold1=70, AlarmThreshold2=80, BlindHeadData = 600, BlindTailData = 600,parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_Dialog()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.initPictureSetting(gaindata, XAxisLength, CompressRatio, AlarmThreshold1, AlarmThreshold2, BlindHeadData, BlindTailData)


    def initPictureSetting(self, gaindata, XAxisLength, CompressRatio, AlarmThreshold1, AlarmThreshold2, BlindHeadData, BlindTailData):
        list = self.ui.frame1.findChildren(QSpinBox)
        n = 0
        for controlSpinBox in list:
            controlSpinBox.setValue(gaindata[(n)])
            n = n+1
        AlarmThreshold1 = int(AlarmThreshold1)
        AlarmThreshold2 = int(AlarmThreshold2)
        self.ui.XAxisLengthComboBox.setCurrentText('%s' % XAxisLength)  # 显示步长
        self.ui.CompressRatioComboBox.setCurrentText('%s' % CompressRatio)  # 显示步长
        self.ui.AlarmThresholdspinBox1.setValue(AlarmThreshold1) # 报警线1
        self.ui.AlarmThresholdspinBox2.setValue(AlarmThreshold2) # 报警线2
        self.ui.BlindHeadDataComboBox.setCurrentText('%s' % BlindHeadData) #端头盲区
        self.ui.BlindTailDataComboBox.setCurrentText('%s' % BlindTailData) #端尾盲区

    @pyqtSlot()
    def on_SoftNormalizationpushButton1_clicked(self):
        SoftGain1 = self.ui.SoftGain1.value()
        list = self.ui.frame1.findChildren(QSpinBox)
        for controlSpinBox in list[1:8]:
            controlSpinBox.setValue(SoftGain1)

    @pyqtSlot()
    def on_SoftNormalizationpushButton2_clicked(self):
        SoftGain9 = self.ui.SoftGain9.value()
        list = self.ui.frame1.findChildren(QSpinBox)
        for controlSpinBox in list[9:16]:
            controlSpinBox.setValue(SoftGain9)


    @pyqtSlot()
    def on_SoftNormalizationpushButton3_clicked(self):
        SoftGain17 = self.ui.SoftGain17.value()
        list = self.ui.frame1.findChildren(QSpinBox)
        for controlSpinBox in list[17:24]:
            controlSpinBox.setValue(SoftGain17)

    @pyqtSlot()
    def on_SoftNormalizationpushButton4_clicked(self):
        SoftGain25 = self.ui.SoftGain25.value()
        list = self.ui.frame1.findChildren(QSpinBox)
        for controlSpinBox in list[25:32]:
            controlSpinBox.setValue(SoftGain25)


    def getWaveAdujustParameters(self):
        list = self.ui.frame1.findChildren(QSpinBox)
        gaindata = [1]*32
        i = 0
        for controlSpinBox in list:
            gaindata[i] = controlSpinBox.value()
            i = i +1
        XAxisLength = self.ui.XAxisLengthComboBox.currentText()
        CompressRatio = self.ui.CompressRatioComboBox.currentText()
        AlarmThreshold1 = self.ui.AlarmThresholdspinBox1.value()
        AlarmThreshold2 = self.ui.AlarmThresholdspinBox2.value()
        BlindHeadData = self.ui.BlindHeadDataComboBox.currentText()
        BlindTailData = self.ui.BlindTailDataComboBox.currentText()

        XAxisLength = int(XAxisLength)
        CompressRatio = int(CompressRatio)
        BlindHeadData = int(BlindHeadData)
        BlindTailData = int(BlindTailData)
        return gaindata, XAxisLength, CompressRatio, AlarmThreshold1, AlarmThreshold2, BlindHeadData, BlindTailData


if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyWaveAdjust()  # 创建窗体
    form.show()
    sys.exit(app.exec_())