import sys

from PyQt5.QtWidgets import QDialog, QApplication

from PictureSettingDialog import Ui_Dialog

class QmyPictureSetting(QDialog):

    def __init__(self, FourAxis = True, TwoAxis = False, OneAxis=False, HalfAxis = True, AbsoluteAxis = True, RelativeAxis = False, axis_one_start= 1,axis_one_end= 8,axis_two_start= 9,axis_two_end= 16,axis_three_start= 17,axis_three_end= 24,axis_four_start= 25,axis_four_end= 32, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_Dialog()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.initPictureSetting(FourAxis, TwoAxis, OneAxis, HalfAxis, AbsoluteAxis, RelativeAxis, axis_one_start,axis_one_end,axis_two_start,axis_two_end,axis_three_start,axis_three_end,axis_four_start,axis_four_end)


    def initPictureSetting(self, FourAxis, TwoAxis, OneAxis, HalfAxis, AbsoluteAxis, RelativeAxis, axis_one_start,axis_one_end,axis_two_start,axis_two_end,axis_three_start,axis_three_end,axis_four_start,axis_four_end):
        axis_one_start = int(axis_one_start)
        axis_one_end = int(axis_one_end)
        axis_two_start = int(axis_two_start)
        axis_two_end = int(axis_two_end)
        axis_three_start = int(axis_three_start)
        axis_three_end = int(axis_three_end)
        axis_four_start = int(axis_four_start)
        axis_four_end = int(axis_four_end)
        self.ui.FourAxisRadioButton.setChecked(FourAxis)
        self.ui.TwoAxisRadioButton.setChecked(TwoAxis)
        self.ui.OneAxisRadioButton.setChecked(OneAxis)
        self.ui.HalfAxischeckBox.setChecked(HalfAxis)
        self.ui.AbsoluteAxisRadioButton.setChecked(AbsoluteAxis)
        self.ui.RelativeAxisRadioButton.setChecked(RelativeAxis)
        self.ui.axis_1_begin.setValue(axis_one_start)  # 第一个轴的初始通道
        self.ui.axis_1_end.setValue(axis_one_end)  # 第一个轴的结束通道
        self.ui.axis_2_begin.setValue(axis_two_start)  # 第二个轴的初始通道
        self.ui.axis_2_end.setValue(axis_two_end)  # 第二个轴的结束通道
        self.ui.axis_3_begin.setValue(axis_three_start)  # 第三个轴的初始通道
        self.ui.axis_3_end.setValue(axis_three_end)  # 第三个轴的结束通道
        self.ui.axis_4_begin.setValue(axis_four_start)  # 第四个轴的初始通道
        self.ui.axis_4_end.setValue(axis_four_end)  # 第四个轴的结束通道
        self.ui.FourAxisRadioButton.toggled.connect(self.buttonState)  # 状态被切换
        self.ui.TwoAxisRadioButton.toggled.connect(self.buttonState)  # 状态被切换
        self.ui.OneAxisRadioButton.toggled.connect(self.buttonState)  # 状态被切换


    def buttonState(self):
        radioButton = self.sender()
        if radioButton.text() == '四屏显示':
            if radioButton.isChecked() == True:
                # print('四轴显示')
                self.ui.axis_1_begin.setEnabled(True)
                self.ui.axis_1_end.setEnabled(True)
                self.ui.axis_2_begin.setEnabled(True)
                self.ui.axis_2_end.setEnabled(True)
                self.ui.axis_3_begin.setEnabled(True)
                self.ui.axis_3_end.setEnabled(True)
                self.ui.axis_4_begin.setEnabled(True)
                self.ui.axis_4_end.setEnabled(True)
        if radioButton.text() == '双屏显示':
            if radioButton.isChecked() == True:
                # print('四轴显示')
                self.ui.axis_1_begin.setEnabled(True)
                self.ui.axis_1_end.setEnabled(True)
                self.ui.axis_2_begin.setEnabled(True)
                self.ui.axis_2_end.setEnabled(True)
                self.ui.axis_3_begin.setEnabled(False)
                self.ui.axis_3_end.setEnabled(False)
                self.ui.axis_4_begin.setEnabled(False)
                self.ui.axis_4_end.setEnabled(False)
        if radioButton.text() == '单屏显示':
            if radioButton.isChecked() == True:
                # print('单轴显示')
                self.ui.axis_1_begin.setEnabled(True)
                self.ui.axis_1_end.setEnabled(True)
                self.ui.axis_2_begin.setEnabled(False)
                self.ui.axis_2_end.setEnabled(False)
                self.ui.axis_3_begin.setEnabled(False)
                self.ui.axis_3_end.setEnabled(False)
                self.ui.axis_4_begin.setEnabled(False)
                self.ui.axis_4_end.setEnabled(False)


    def get_PictureSettingParameters(self):
        if self.ui.FourAxisRadioButton.isChecked() == True:
            FourAxis = True
            TwoAxis = False
            OneAxis = False
        if self.ui.TwoAxisRadioButton.isChecked() == True:
            FourAxis = False
            TwoAxis = True
            OneAxis = False
        if self.ui.OneAxisRadioButton.isChecked() == True:
            FourAxis = False
            TwoAxis = False
            OneAxis = True
        if self.ui.HalfAxischeckBox.isChecked() == True:
            HalfAxis = True
        else:
            HalfAxis = False
        if self.ui.AbsoluteAxisRadioButton.isChecked() == True:
            AbsoluteAxis = True
            RelativeAxis = False
        if self.ui.RelativeAxisRadioButton.isChecked() == True:
            AbsoluteAxis = False
            RelativeAxis = True


        axis_one_start = self.ui.axis_1_begin.value()
        axis_one_end = self.ui.axis_1_end.value()
        axis_two_start = self.ui.axis_2_begin.value()
        axis_two_end = self.ui.axis_2_end.value()
        axis_three_start = self.ui.axis_3_begin.value()
        axis_three_end = self.ui.axis_3_end.value()
        axis_four_start = self.ui.axis_4_begin.value()
        axis_four_end = self.ui.axis_4_end.value()
        return FourAxis, TwoAxis, OneAxis, HalfAxis, AbsoluteAxis, RelativeAxis, axis_one_start, axis_one_end, axis_two_start, axis_two_end, axis_three_start,axis_three_end, axis_four_start, axis_four_end



if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyPictureSetting()  # 创建窗体
    form.show()
    sys.exit(app.exec_())