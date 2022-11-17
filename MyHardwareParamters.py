# -*- coding: utf-8 -*-
import sys
import traceback

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication

from HardwareParametersDialog import Ui_Dialog

class QmyHardwareParamter(QDialog):

    def __init__(self,SpaceMode= False,TimeMode=True, SpaceAccuracy='0.5mm',TimeAccuracy='1000点/s',  OpenAlarm = True, CloseAlarm = False, AlarmThreshold1 = 70, AlarmThreshold2 = 80, ProbeOneGain=6, ProbeTwoGain=6, ProbeThreeGain=6, ProbeFourGain=6,parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_Dialog()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面

        self.initHardwareParamter(SpaceMode,TimeMode, SpaceAccuracy,TimeAccuracy, OpenAlarm, CloseAlarm, AlarmThreshold1, AlarmThreshold2, ProbeOneGain, ProbeTwoGain, ProbeThreeGain, ProbeFourGain)


    def initHardwareParamter(self, SpaceMode,TimeMode, SpaceAccuracy,TimeAccuracy, OpenAlarm, CloseAlarm, AlarmThreshold1, AlarmThreshold2, ProbeOneGain, ProbeTwoGain, ProbeThreeGain, ProbeFourGain):
        self.ui.SpaceModeradioButton.setChecked(SpaceMode)
        self.ui.TimeModeradioButton.setChecked(TimeMode)
        if SpaceMode == True:
            self.ui.SpaceAccuracyComboBox.setEnabled(True)
            self.ui.TimeAccuracyComboBox.setEnabled(False)
        if TimeMode == True:
            self.ui.SpaceAccuracyComboBox.setEnabled(False)
            self.ui.TimeAccuracyComboBox.setEnabled(True)
        self.ui.SpaceModeradioButton.toggled.connect(self.ModebuttonState)  # 状态被切换
        self.ui.TimeModeradioButton.toggled.connect(self.ModebuttonState)  # 状态被切换
        self.ui.OpenAlarmstartradioButton.setChecked(OpenAlarm)
        self.ui.CloseAlarmstartradioButton.setChecked(CloseAlarm)
        if OpenAlarm == True:
            self.ui.AlarmThresholdspinBox1.setEnabled(True)
            self.ui.AlarmThresholdspinBox2.setEnabled(True)
        if CloseAlarm == True:
            self.ui.AlarmThresholdspinBox1.setEnabled(False)
            self.ui.AlarmThresholdspinBox2.setEnabled(False)
        self.ui.OpenAlarmstartradioButton.toggled.connect(self.AlarmbuttonState)  # 状态被切换
        self.ui.CloseAlarmstartradioButton.toggled.connect(self.AlarmbuttonState)  # 状态被切换
        AlarmThreshold1 = int(AlarmThreshold1)
        AlarmThreshold2 = int(AlarmThreshold2)
        ProbeOneGain = int(ProbeOneGain)
        ProbeTwoGain = int(ProbeTwoGain)
        ProbeThreeGain = int(ProbeThreeGain)
        ProbeFourGain = int(ProbeFourGain)
        self.ui.SpaceAccuracyComboBox.setCurrentText(SpaceAccuracy)
        self.ui.TimeAccuracyComboBox.setCurrentText(TimeAccuracy)
        self.ui.AlarmThresholdspinBox1.setValue(AlarmThreshold1)
        self.ui.AlarmThresholdspinBox2.setValue(AlarmThreshold2)
        self.ui.GainProbeOnespinBox.setValue(ProbeOneGain)
        self.ui.GainProbeTwospinBox.setValue(ProbeTwoGain)
        self.ui.GainProbeThreespinBox.setValue(ProbeThreeGain)
        self.ui.GainProbeFourspinBox.setValue(ProbeFourGain)



    def ModebuttonState(self):
        radioButton = self.sender()
        if radioButton.text() == '等空间采样':
            if radioButton.isChecked() == True:
                self.ui.SpaceAccuracyComboBox.setEnabled(True)
                self.ui.TimeAccuracyComboBox.setEnabled(False)
        if radioButton.text() == '等时间采样':
            if radioButton.isChecked() == True:
                # print('单轴显示')
                self.ui.SpaceAccuracyComboBox.setEnabled(False)
                self.ui.TimeAccuracyComboBox.setEnabled(True)


    def AlarmbuttonState(self):
        radioButton = self.sender()
        if radioButton.text() == '开':
            if radioButton.isChecked() == True:
                self.ui.AlarmThresholdspinBox1.setEnabled(True)
                self.ui.AlarmThresholdspinBox2.setEnabled(True)
        if radioButton.text() == '关':
            if radioButton.isChecked() == True:
                self.ui.AlarmThresholdspinBox1.setEnabled(False)
                self.ui.AlarmThresholdspinBox2.setEnabled(False)


    @pyqtSlot()
    def on_NormalizationpushButton_clicked(self):
        try:
            ProbeOneGain = int(self.ui.GainProbeOnespinBox.text())
            ProbeTwoGain = ProbeOneGain
            ProbeThreeGain = ProbeOneGain
            ProbeFourGain = ProbeOneGain
            self.ui.GainProbeTwospinBox.setValue(ProbeTwoGain)
            self.ui.GainProbeThreespinBox.setValue(ProbeThreeGain)
            self.ui.GainProbeFourspinBox.setValue(ProbeFourGain)
        except Exception as err:
            print(traceback.format_exc())


    def get_HardwareParameters(self):
        if self.ui.TimeModeradioButton.isChecked() == True:
            TimeMode = True
        else:
            TimeMode = False
        if self.ui.SpaceModeradioButton.isChecked() == True:
            SpaceMode = True
        else:
            SpaceMode = False
        if self.ui.OpenAlarmstartradioButton.isChecked() == True:
            OpenAlarm = True
        else:
            OpenAlarm = False
        if self.ui.CloseAlarmstartradioButton.isChecked() == True:
            CloseAlarm = True
        else:
            CloseAlarm = False

        TimeAccuracy = self.ui.TimeAccuracyComboBox.currentText()
        SpaceAccuracy = self.ui.SpaceAccuracyComboBox.currentText()
        AlarmThreshold1 = self.ui.AlarmThresholdspinBox1.text()
        AlarmThreshold2 = self.ui.AlarmThresholdspinBox2.text()
        ProbeOneGain = self.ui.GainProbeOnespinBox.text()
        ProbeTwoGain = self.ui.GainProbeTwospinBox.text()
        ProbeThreeGain = self.ui.GainProbeThreespinBox.text()
        ProbeFourGain = self.ui.GainProbeFourspinBox.text()

        AlarmThreshold1 = int(AlarmThreshold1)
        AlarmThreshold2 = int(AlarmThreshold2)
        ProbeOneGain = int(ProbeOneGain)
        ProbeTwoGain = int(ProbeTwoGain)
        ProbeThreeGain = int(ProbeThreeGain)
        ProbeFourGain = int(ProbeFourGain)
        return SpaceMode,TimeMode,  SpaceAccuracy, TimeAccuracy, OpenAlarm, CloseAlarm, AlarmThreshold1, AlarmThreshold2, ProbeOneGain, ProbeTwoGain, ProbeThreeGain, ProbeFourGain


if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyHardwareParamter()  # 创建窗体
    form.show()
    sys.exit(app.exec_())