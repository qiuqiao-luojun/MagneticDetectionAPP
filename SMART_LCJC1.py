# -*-coding:utf-8-*-
# -*- coding: utf-8 -*-
import csv
import os
import struct
import sys
import time

import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, QFileDialog, QMessageBox, QDialog, QLabel

from PyQt5.QtCore import pyqtSlot, Qt, QDir

import numpy as np

import socket

import threading

from multiprocessing import Process, Queue, freeze_support

import math

import traceback

import matplotlib as mpl

from matplotlib.figure import Figure

from matplotlib.backends.backend_qt5agg import (FigureCanvas,
                 NavigationToolbar2QT as NavigationToolbar)

from mainwindow import Ui_MainWindow

from MyNewDetection import QmyNewDetection

from MyPictureSetting import QmyPictureSetting

from MyHardwareParamters import QmyHardwareParamter

from MyWaveAdjustDialog import QmyWaveAdjust

## FigureCanvas 的父类是QWidget，是Figure的容器类
## NavigationToolbar 是图表上的工具栏

#多继承
# class QmyWidget(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__() #用函数获取父类，并执行父类的构造函数，使用super()得到的是第一个基类，在这里就是QMainWindow。在执行完这个语句后，self就是QMainWindow对象
#         self.setupUi(self)#QmyWidget的基类包括Ui_MainWindow类，所以可以 调用Ui_MainWindow类的setupUi()函数。同时经过前面调用了父类的构造函数，self代表的是QMainWindow对象，可以作为参数传递给setupUi()函数

def JudgeBool(A):
    if A[0] == 'F':
        return False
    else:
        return True


ylim_min = 0
SoftWareGain = [1]*32
localport = 2020;  # 本地端口
SendIP = "192.168.2.100";  #发送端IP
SendPort = 2021;  # 发送端口

# 参数初始化
CalibrationThreshold = 2048  # 标定线
DataSizePerPag = 680
filename = None
OilPipeType = None
OilPipeThickness = None
OilPipeSpecification = None
Operator = None
DetectionData = None
PulseDuration = '0.5s'
FourAxis = True  # 四屏显示
TwoAxis = False  # 双屏显示
OneAxis = False  # 单屏显示
HalfAxis = False  # 半屏显示
AbsoluteAxis = False  # 绝对坐标显示
RelativeAxis = True  # 相对坐标显示
axis_one_start = 1  # 第一屏起始通道
axis_one_end = 8  # 第一屏结束通道
axis_two_start = 9  # 第二屏起始通道
axis_two_end = 16  # 第二屏结束通道
axis_three_start = 17  # 第三屏起始通道
axis_three_end = 24  # 第三屏结束通道
axis_four_start = 1  # 第四屏起始通道
axis_four_end = 24  # 第四屏结束通道
XAxisLength = 4000  # 每屏横坐标最多的点数
CompressRatio = 1  # 数据压缩比
AlarmThreshold1 = 70  # 报警线1
AlarmThreshold2 = 80  # 报警线2
BlindHeadData = 600  # 端头盲区数据
BlindTailData = 600  # 端尾盲区数据
XAxisBagNum = int(XAxisLength / 20)  # 每屏横坐标最多的包数
DataSizePerPag = 680  # 每个包转化成十进制后的每个包数量的多少

SpaceMode = True  # 等空间采样
TimeMode = False  # 等时间采样
SpaceAccuracy = '0.5mm'  # 空间采样精度
TimeAccuracy = '1000点/s'  # 时间采样精度
OpenAlarm = True  # 报警打开
CloseAlarm = False  # 报警关闭
ProbeOneGain = 0  # 探头1增益
ProbeTwoGain = 0  # 探头2增益
ProbeThreeGain = 0  # 探头3增益
ProbeFourGain = 0  # 探头4增益
TimingXAxisLength = 1000
Mode = int("67", 16)  # 等时采样
ylim_min = 2048
SoftWareGain = [1] * 32
HardwareGainOrder = [(i * 5 ) for i in range(0, 40)]
colorlist = ['blue', 'orange', 'forestgreen', 'red', 'purple', 'brown', 'pink', 'navy']


if os.path.exists('data_storage_location\\' + 'TotalInformation.csv'):
    total = sum(1 for line in open('data_storage_location\\' + 'TotalInformation.csv'))
    if total > 150:
        df = pd.read_csv('data_storage_location\\' + 'TotalInformation.csv')
        df.drop(df.index[0:50], inplace=True)
        df.to_csv('data_storage_location\\' + 'TotalInformation.csv', index=False)
    with open('data_storage_location' + '\\TotalInformation.csv', 'r') as csvfile:
        [Newfilename, OilPipeType, OilPipeThickness, OilPipeSpecification, Operator, DetectionData,
         PulseDuration] = csvfile.readlines()[-1].split(',')
        if os.path.isfile('data_storage_location\\' + Newfilename + '\\parameters.bin'):
            with open('data_storage_location\\' + Newfilename + '\\parameters.bin', 'r') as f:
                [Newfilename, OilPipeType, OilPipeThickness, OilPipeSpecification, Operator, DetectionData,
                 PulseDuration, FourAxis, TwoAxis, OneAxis, HalfAxis, AbsoluteAxis, RelativeAxis, axis_one_start,
                 axis_one_end, axis_two_start, axis_two_end, axis_three_start, axis_three_end, axis_four_start,
                 axis_four_end, XAxisLength, CompressRatio, AlarmThreshold1, AlarmThreshold2, BlindHeadData,
                 BlindTailData, XAxisBagNum, SpaceMode, TimeMode, SpaceAccuracy, TimeAccuracy, OpenAlarm,
                 CloseAlarm,
                 ProbeOneGain, ProbeTwoGain, ProbeThreeGain, ProbeFourGain, Mode, kong] = f.read().split(',')
                FourAxis = JudgeBool(FourAxis)
                TwoAxis = JudgeBool(TwoAxis)
                OneAxis = JudgeBool(OneAxis)
                HalfAxis = JudgeBool(HalfAxis)
                AbsoluteAxis = JudgeBool(AbsoluteAxis)
                RelativeAxis = JudgeBool(RelativeAxis)
                SpaceMode = JudgeBool(SpaceMode)  # 等空间采样
                TimeMode = JudgeBool(TimeMode)  # 等时间采样
                OpenAlarm = JudgeBool(OpenAlarm)  # 报警打开
                CloseAlarm = JudgeBool(CloseAlarm)  # 报警关闭
                axis_one_start = int(axis_one_start)
                axis_one_end = int(axis_one_end)
                axis_two_start = int(axis_two_start)
                axis_two_end = int(axis_two_end)
                axis_three_start = int(axis_three_start)
                axis_three_end = int(axis_three_end)
                axis_four_start = int(axis_four_start)
                axis_four_end = int(axis_four_end)
                XAxisLength = int(XAxisLength)
                CompressRatio = int(CompressRatio)
                AlarmThreshold1 = int(AlarmThreshold1)
                AlarmThreshold2 = int(AlarmThreshold2)
                BlindHeadData = int(BlindHeadData)
                BlindTailData = int(BlindTailData)
                XAxisBagNum = int(XAxisLength / 20)  # 每屏横坐标最多的包数
                ProbeOneGain = int(ProbeOneGain)  # 探头1增益
                ProbeTwoGain = int(ProbeTwoGain)  # 探头2增益
                ProbeThreeGain = int(ProbeThreeGain)  # 探头3增益
                ProbeFourGain = int(ProbeFourGain)  # 探头4增益
                if TimeMode == True:
                    Mode = int("47", 16)  # 等时间采样
                # if SpaceMode == True:
                else:
                    Mode = int("67", 16)  # 等空间采样

x_encode_array = np.load('x_encode_array.npy')
x_encode_top = np.load('x_encode_top.npy')
channel_choice = np.load('channel_choice.npy')    # 通道对应位置坐标 实际的1-8通道对应硬件数据的1，5，9等等
Synthetic_location_array = np.load('Synthetic_location_array.npy')  # 采集数据的坐标位置

def recieve_data(q,localport,SendIP,SendPort,deliverBytes,filename):
    """
    确认UDP客户端的ip及地址
    q：多进程队列传递数据
    localport:本地端口
    SendIP：目标端口IP；SendPort：目标端口
    deliverBytes：发送指令；
    filename：保存文件的名字
    """
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        port = int(localport)
        address = ('', port)
        udp_socket.bind(address) # 绑定套接字
        send_address = (str(SendIP), int(SendPort))
        udp_socket.sendto(deliverBytes, send_address)  # 发送指令
        while True:
            if os.path.isfile('有缺陷出现.bin'):  # 有缺陷出现，发送警报指令
                udp_socket.sendto(bytes.fromhex('88 04 09 00 00 00 00 10'), send_address)
            if os.path.isfile('stop.txt'):  # 停止按钮触发，发送停止指令
                udp_socket.sendto(bytes.fromhex('12 04 09 00 00 00 00 18'), send_address)
                break;
            else:
                recv_data = udp_socket.recvfrom(65536)
                send_addr = recv_data[0]  # 接收数据
                q.put(send_addr)  # 多进程队列传递数据
                # 判断字节个数，符合一定大小的字节才能被写入文件中去
        udp_socket.close()
    except Exception as err:
        print(traceback.format_exc())


class QmyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("管道漏磁检测软件系统")

        self.__labMove = QLabel("坐标值:")
        self.__labMove.setMinimumWidth(400)
        self.ui.statusbar.addWidget(self.__labMove)

        self.__labPick = QLabel("提示信息栏")
        self.__labPick.setMinimumWidth(1200)
        self.ui.statusbar.addWidget(self.__labPick)

        ## rcParams[]参数设置，以正确显示汉字
        mpl.rcParams['font.sans-serif'] = ['KaiTi', 'Times New Roman']  # 汉字字体
        ##                                       'Times New Roman']
        mpl.rcParams['font.size'] = 12  # 字体大小
        ##  华文宋体：STSong 华文仿宋：STFangsong 华文黑体：STHeiti
        ##      黑体：SimHei 仿宋：FangSong 楷体：KaiTi
        mpl.rcParams['axes.unicode_minus'] = False  # 正常显示符号

        self.x_encode_data = np.array([0] * XAxisLength * CompressRatio)

        # self.eachchannel_show = self.ui.ChannelChoiceComboBox
        self.__fig = None  # Figue对象
        self.__ax1 = None  # 1-8通道
        self.__ax2 = None  # 9-16通道
        self.__ax3 = None  # 17-24通道
        self.__ax4 = None  # 25-32通道
        if FourAxis is True:
            self.AxisNum = 4
            self.Axis_list = [self.__ax1, self.__ax2, self.__ax3, self.__ax4]
        if TwoAxis is True:
            self.AxisNum = 2
            self.Axis_list = [self.__ax1, self.__ax2]
        if OneAxis is True:
            self.AxisNum = 1
            self.Axis_list = [self.__ax1]

        self.__filename = None  # 文件名字

          # 屏幕数目
        if AbsoluteAxis == True:
            self.__AbsoluteYAxisShow = True  # 标识符：是否是绝对坐标显示
        else:
            self.__AbsoluteYAxisShow = False

        self.__datacollection = False  # 标识符：是否在接收数据

        self.countfilepage = 1
        self.cache_data = None  # 缓存处理的数据
        self.plot_timing_data = np.array([]) # 实时处理的转化为2^16的数据
        self.plot_historical_data = np.array([])
        self.historical_original_data = None
        self.historical_data = None  # 打开历史数据的时候，存取的数据
        # self.deliverBytes = bytes.fromhex(str())
        self.deliverBytes = bytes([Mode,int(float(SpaceAccuracy[0:-2])*10-1),int(10000/int(TimeAccuracy[0:-3])-1),HardwareGainOrder[ProbeOneGain],HardwareGainOrder[ProbeTwoGain],HardwareGainOrder[ProbeThreeGain],HardwareGainOrder[ProbeFourGain],18]) # 初始化要发送的字节指令
        self.RecieveDataProcess = None # 对子进程提前进行设置
        self.__iniFigure()  # 创建绘图系统，初始化窗口
        self.__drawFigure()  # 绘图


    ##==========自定义函数=================
    def __iniFigure(self):  ##创建绘图系统，初始化窗口
        self.ui.frame.setFixedWidth(150)
        self.ui.frame_2.setFixedHeight(48)
        self.ui.statusbar.setFixedHeight(30)
        self.__fig = Figure(figsize=(30,800))  # 单位英寸 ,facecolor="lightgray"
        figCanvas = FigureCanvas(self.__fig)  # 创建FigureCanvas对象，必须传递一个Figure对象


        splitter_2 = QSplitter(self)
        splitter_2.setOrientation(Qt.Vertical)
        splitter_2.addWidget(figCanvas)
        splitter_2.addWidget(self.ui.frame_2)

        splitter_1 = QSplitter(self)
        splitter_1.setOrientation(Qt.Horizontal)
        splitter_1.addWidget(self.ui.frame)
        splitter_1.addWidget(splitter_2)

        self.setCentralWidget(splitter_1)
        self.setWindowState(Qt.WindowMaximized)

        if self.__datacollection is False:
            self._cid1 = figCanvas.mpl_connect("motion_notify_event", self.do_canvas_mouseMove)
            self._cid2 = figCanvas.mpl_connect("axes_enter_event", self.do_axes_mouseEnter)
            self._cid3 = figCanvas.mpl_connect("axes_leave_event", self.do_axes_mouseLeave)

        ##  =================自定义槽函数==========
        # event类型 matplotlib.backend_bases.MouseEvent

    def do_canvas_mouseMove(self, event):
        if event.inaxes == None:
            return
        info = "%s 横坐标=%.3f 米, 纵坐标=%.3f (占屏比:%f%%) " % (event.inaxes.get_label(), self.x_encode_data[int(event.xdata)], event.ydata, (event.ydata - ylim_min) / (4096 - ylim_min) * 100)
        self.__labMove.setText(info)

        ## event类型：matplotlib.backend_bases.LocationEvent

    def do_axes_mouseEnter(self, event):
        event.inaxes.patch.set_facecolor('black')  # 设置背景颜色
        event.inaxes.patch.set_alpha(0.1)  # 透明度
        event.canvas.draw()

    def do_axes_mouseLeave(self, event):
        event.inaxes.patch.set_facecolor('w')  # 设置背景颜色
        event.canvas.draw()
        ##event 类型： matplotlib.backend_bases.PickEvent


    def __drawFigure(self):  ## 绘图
        global ylim_min
        if HalfAxis is True:
            ylim_min = 2048
        else:
            ylim_min = 0
        ylim_max = 4096
        if self.AxisNum == 4:
            self.__ax1 = self.__fig.add_axes([0.05, 0.77, 0.87, 0.2]) # 添加子图，ax1是 matplotlib.axes.Axes 类对象
            self.__ax2 = self.__fig.add_axes([0.05, 0.53, 0.87, 0.2])
            self.__ax3 = self.__fig.add_axes([0.05, 0.29, 0.87, 0.2])
            self.__ax4 = self.__fig.add_axes([0.05, 0.05, 0.87, 0.2])
            self.Axis_list = [self.__ax1,self.__ax2,self.__ax3,self.__ax4]
            # self.__ax2.set_title("9-16通道")  # 子图标题

        if self.AxisNum == 2:
            self.__ax1 = self.__fig.add_axes([0.05, 0.53, 0.87, 0.4])  # 添加子图，ax1是 matplotlib.axes.Axes 类对象
            self.__ax2 = self.__fig.add_axes([0.05, 0.05, 0.87, 0.4])
            self.__ax3 = None
            self.__ax4 = None
            self.Axis_list = [self.__ax1, self.__ax2]

        if self.AxisNum == 1:
            self.__ax1 = self.__fig.add_axes([0.05, 0.05, 0.87, 0.87])  # 添加子图，ax1是 matplotlib.axes.Axes 类对象
            self.__ax2 = None
            self.__ax3 = None
            self.__ax4 = None
            self.Axis_list = [self.__ax1]
        self.__data_init()


        for ax in self.Axis_list:
            # ax.patch.set_facecolor('black')
            ax.plot([CalibrationThreshold]*XAxisLength, '--', linewidth=1.5, color='darkred')
            if OpenAlarm is True:
                ax.plot([AlarmThreshold1 * (4096 - ylim_min) / 100 + ylim_min] * XAxisLength, '--', linewidth=1.5,
                        color='green')
                ax.plot([AlarmThreshold2 * (4096 - ylim_min) / 100 + ylim_min] * XAxisLength, '--', linewidth=1.5,
                        color='green')
            ax.set_xlim([0, XAxisLength])  # X轴范围
            if self.__AbsoluteYAxisShow is True:
                ax.set_ylim([ylim_min, ylim_max])
            ax.grid(b=False)
            for label in ax.xaxis.get_majorticklabels():  # x轴刻度不可见
                label.set_visible(False)
            for label in ax.yaxis.get_majorticklabels():  # y轴刻度不可见
                label.set_visible(False)
            # for tick in ax.xaxis.get_major_ticks():  # 设置上面的刻度尺
            #     tick.tick2On = True
            #     tick.tick1On = False

    def __data_init(self):
        self.data = []  # 32个通道的数据
        for i in range(0, 8):
            channel_data = {'x': [], 'y': [], 'angle': []}
            self.data.append(channel_data)
        for i in range(0, 8):
            self.__ax1.plot(self.data[i]['x'], self.data[i]['y'], label=("通道" + str(i + 1)), color=colorlist[i])
        leg = self.__ax1.legend(bbox_to_anchor=(1.02, 0), loc=3, borderaxespad=0, markerscale=1.5, frameon=False)
        for i in leg.legendHandles:
            i.set_linewidth(12)


    # 开始检测过程中除了停止按钮，其他都不能点击
    def Button_close(self):
        self.ui.HardwareCalibration.setEnabled(False)
        self.ui.StopDataCalibration.setEnabled(True)
        self.ui.HardwareParametersSetting.setEnabled(False)
        self.ui.PictureSetting.setEnabled(False)
        self.ui.NewDetection.setEnabled(False)
        self.ui.StopDataCollection.setEnabled(True)
        self.ui.GoOnDetection.setEnabled(False)
        self.ui.HistoricalData.setEnabled(False)
        self.ui.WaveAdjust.setEnabled(False)
        self.ui.ChannelPlayback.setEnabled(False)
        self.ui.DataSave.setEnabled(False)


    # 结束检测后打开所有按钮
    def Button_start(self):
        self.ui.HardwareCalibration.setEnabled(True)
        self.ui.StopDataCalibration.setEnabled(True)
        self.ui.HardwareParametersSetting.setEnabled(True)
        self.ui.PictureSetting.setEnabled(True)
        self.ui.NewDetection.setEnabled(True)
        self.ui.StopDataCollection.setEnabled(True)
        self.ui.GoOnDetection.setEnabled(True)
        self.ui.HistoricalData.setEnabled(True)
        self.ui.WaveAdjust.setEnabled(True)
        self.ui.ChannelPlayback.setEnabled(True)
        self.ui.DataSave.setEnabled(True)
        self.ui.firstpage.setEnabled(True)
        self.ui.previouspage.setEnabled(True)
        self.ui.nextpage.setEnabled(True)
        self.ui.lastpage.setEnabled(True)
        self.ui.previousfile.setEnabled(True)
        self.ui.nextfile.setEnabled(True)


    def parameters_initial(self): # 初始化一些变量与数据
        global axis_one_start, axis_one_end, axis_two_start, axis_two_end, axis_three_start, axis_three_end,axis_four_start, axis_four_end, OneAxisStart, OneAxisEnd, XAxisLength, XAxisBagNum, CompressRatio, AlarmThreshold1, AlarmThreshold2, SoftWareGain
        self.cache_data = None
        self.plot_timing_data = np.array([])
        self.plot_historical_data = np.array([])
        SoftWareGain = [1] * 32
        if self.__datacollection is True:
            self.historical_original_data = None
            self.historical_data = None
            # 按钮设置
            self.Button_close()
            self.ui.firstpage.setEnabled(False)
            self.ui.previouspage.setEnabled(False)
            self.ui.nextpage.setEnabled(False)
            self.ui.lastpage.setEnabled(False)
            self.ui.previousfile.setEnabled(False)
            self.ui.nextfile.setEnabled(False)
            self.ui.TotalPageNumberlineEdit.setText('1')
            self.ui.CurrentPageNumberlineEdit.setText('1')
            # 文件清除
            if os.path.isfile('硬件标定文件.txt'):  # 以stop.txt文件作为收数据进程的循环的标志位
                os.remove('硬件标定文件.txt')
            if os.path.isfile('stop.txt'):  # 以stop.txt文件作为收数据进程的循环的标志位
                os.remove('stop.txt')
            if os.path.isfile('有缺陷出现.bin'):  # 以有缺陷出现文件作为收数据进程的循环的标志位
                os.remove('有缺陷出现.bin')


    def filenumcount(self):
        # 文件页数计算
        filecount = 0
        for root, dir, files in os.walk(self.__filename):
            filecount += len(files)
        if self.__datacollection is True:
            self.countfilepage = filecount
            totalfilenum = filecount
        else:
            totalfilenum = filecount-1
        self.ui.TotalFileNumberlineEdit.setText('%s' % totalfilenum)
        self.ui.CurrentFileNumberlineEdit.setText('%s' % self.countfilepage)


    def childprocessbegin(self):
        q = Queue()  # 以队列的形式进行数据传输
        # 开启接收数据的进程
        self.RecieveDataProcess = Process(target=recieve_data,
                                          args=(q, localport, SendIP, SendPort, self.deliverBytes, self.__filename))
        self.RecieveDataProcess.start()
        # 开线程进行数据处理与页面显示
        self.timing_data_process = threading.Thread(target=self.timing_data_read, args=(q,))
        self.timing_data_process.setDaemon(True)
        self.timing_data_process.start()


    def closeEvent(self, event) :
        try:
            with open('stop.txt', 'ab') as f:
                f.write(b'0')
            self.__datacollection = False
            if self.RecieveDataProcess is not None:
                self.RecieveDataProcess.terminate()
                self.RecieveDataProcess = None
            os.remove('stop.txt')
        except Exception as err:
            print(traceback.format_exc())


    # 实时显示时数据的接收
    def timing_data_read(self,q):
        try:
            if self.__filename == '硬件标定文件.txt':
                f = open(self.__filename,'ab')
            else:
                childfile = str(self.countfilepage) + '.txt'
                f = open(os.path.join(self.__filename, childfile), 'ab')
            count = 0
            while self.__datacollection:
                if not q.empty():
                    data = q.get()
                    if len(data) == 1360:
                        f.write(data)
                        count += 1
                        # 数据报警信号的判断
                        if OpenAlarm is True:
                            self.AlarmJudge= threading.Thread(target=self.judgeThreshold,args=(data,))
                            self.AlarmJudge.setDaemon(True)
                            self.AlarmJudge.start()
                        if (count % 2 == 0):
                            X = np.array(struct.unpack('H' * int(len(data) / 2), data))
                            self.plot_timing_data = np.append(self.plot_timing_data, X[:32])
                            if len(self.plot_timing_data) > 0 and (len(self.plot_timing_data) % (32*50) == 0):
                                # 图像的实时显示
                                self.timing_picture = threading.Thread(target=self.TimedispalyFigure)
                                self.timing_picture.setDaemon(True)
                                self.timing_picture.start()
                                if (len(self.plot_timing_data) == 32*TimingXAxisLength):
                                    timing_page = 1 + int(self.ui.CurrentPageNumberlineEdit.text())
                                    self.ui.CurrentPageNumberlineEdit.setText(str(timing_page))
                                    self.ui.TotalPageNumberlineEdit.setText(str(timing_page))
                                    self.plot_timing_data = np.array([])
                                    if (self.__filename != '硬件标定文件.txt' and timing_page > 2 and (timing_page-1) * TimingXAxisLength % 4000 == 0):
                                        self.countfilepage += 1
                                        childfile = str(self.countfilepage) + '.txt'
                                        f = open(os.path.join(self.__filename, childfile), 'ab')
                                        self.ui.CurrentFileNumberlineEdit.setText('%s'%self.countfilepage)
                                        self.ui.TotalFileNumberlineEdit.setText('%s'%self.countfilepage)
                    else:
                        # self.ui.statusbar.showMessage("硬件返回值：" + data.hex())
                        self.__labPick.setText("硬件返回值：" + data.hex())
        except Exception as err:
            print(traceback.format_exc())


    def judgeThreshold(self, data):
        try:
            X = np.array(struct.unpack('H' * int(len(data) / 2), data))
            MaxSignal = np.max(X[:640])
            MinSignal = np.min(X[:640])
            if MaxSignal > (AlarmThreshold1 * (4096 - ylim_min) / 100 + ylim_min) or MinSignal < (4096 - (AlarmThreshold1 * (4096 - ylim_min) / 100 + ylim_min)):
                with open('有缺陷出现.bin', 'ab') as f:
                    f.write(b'0')
                time.sleep(0.01)
                os.remove('有缺陷出现.bin')
        except Exception as err:
            print(traceback.format_exc())


    def PictureDraw(self, X):
        # 历史数据显示的时候 报警线的绘制 横坐标的显示等等
        if self.__datacollection is not True:
            # 是否半屏显示
            if HalfAxis is True:
                ylim_min = 2048
            else:
                ylim_min = 0
            Pag_num = int(X.shape[0] / DataSizePerPag)
            AxisShowLength = XAxisLength
            show_location_array = Synthetic_location_array[:(20 * Pag_num)]


            xdata = X[x_encode_array[:(20 * Pag_num)]].flatten()[::CompressRatio]
            xdata_top = X[x_encode_top[:(20 * Pag_num)]].flatten()[::CompressRatio]
            distance_toplabel = xdata_top.copy()
            for i in range(distance_toplabel.shape[0]):
                if distance_toplabel[i] <= 32768:
                    distance_toplabel[i] = 0
                else:
                    distance_toplabel[i] = -1
                    xdata_top[i] = xdata_top[i] - 65535
            self.x_encode_data = xdata * 0.025 * 0.001 + distance_toplabel + xdata_top
            if self.x_encode_data.shape[0] < XAxisLength:
                a = np.array([0] * (XAxisLength - self.x_encode_data.shape[0]))
                self.x_encode_data = np.append(self.x_encode_data, a, 0)

            # 横坐标的显示情况
            for axis in self.Axis_list:
                axis.set_xlim([0, AxisShowLength])
                if self.__AbsoluteYAxisShow is True:
                    axis.set_ylim([ylim_min, 4096])
                axis.plot([CalibrationThreshold] * AxisShowLength, '--', linewidth=1.5, color='darkred')
                if OpenAlarm is True:
                    axis.plot([AlarmThreshold1 * (4096 - ylim_min) / 100 + ylim_min] * XAxisLength, '--',
                              linewidth=1.5,
                              color='green')
                    axis.plot([AlarmThreshold2 * (4096 - ylim_min) / 100 + ylim_min] * XAxisLength, '--',
                              linewidth=1.5,
                              color='green')
            if axis == self.Axis_list[-1]:
                axis.set_xticks(np.linspace(0, AxisShowLength, 11))
                self.xlabeldata = self.x_encode_data[::int(XAxisLength / 10)]
                axis.set_xticklabels(round(float(i), 3) for i in self.xlabeldata)


        def lineplot(axis, a, b):
            for j in range(a, b):
                if self.__datacollection is not True:
                    if HalfAxis is True : # 半屏显示设置
                        y = np.max(np.array([(abs(i-2048)*math.pow(10,float(SoftWareGain[j]/20))+2048) for i in X[show_location_array + channel_choice[j]]]).reshape(-1,CompressRatio), axis=1)
                    else:
                        y = np.max(np.array([((i - 2048) * math.pow(10,float(SoftWareGain[j]/20)) + 2048) for i in
                                             X[show_location_array + channel_choice[j]]]).reshape(-1, CompressRatio),
                                   axis=1)
                else:
                    if HalfAxis is True:
                        y = np.array([(abs(i - 2048) + 2048) for i in X[int(channel_choice[j])::32]])
                    else:
                        y = X[int(channel_choice[j])::32]
                linewidth = '1.5'
                channel_num = j % 8
                axis.plot(y, label=("通道" + str(channel_num + 1)), linewidth=linewidth, color=colorlist[channel_num])

            axis.grid(b=False)

        for axis in self.Axis_list[:-1:1]:
            for label in axis.xaxis.get_majorticklabels():
                label.set_visible(False)
            for label in axis.yaxis.get_majorticklabels():
                label.set_visible(False)

        if self.__filename != '硬件标定文件.txt':
            for axis in self.Axis_list:
                if axis == self.__ax1:
                    axis.set_title("%s-%s通道" % (axis_one_start, axis_one_end))
                if axis == self.__ax2:
                    axis.set_title("%s-%s通道" % (axis_two_start, axis_two_end))  # 子图标题
                if axis == self.__ax3:
                    axis.set_title("%s-%s通道" % (axis_three_start, axis_three_end))  # 子图标题
                if axis == self.__ax4:
                    axis.set_title("%s-%s通道" % (axis_four_start, axis_four_end))  # 子图标题
        else:
            channel_mean = []
            for j in range(32):
                if self.__datacollection is not True:
                    channel_mean.append(int(np.mean(X[show_location_array + channel_choice[j]])))
                else:
                    channel_mean.append(int(np.mean(X[int(channel_choice[j])::32])))
            for axis in self.Axis_list:
                if axis == self.__ax1:
                    axis.set_title("%s|%s|%s|%s|%s|%s|%s|%s" % (
                    channel_mean[0], channel_mean[1], channel_mean[2], channel_mean[3], channel_mean[4],
                    channel_mean[5], channel_mean[6], channel_mean[7]))
                if axis == self.__ax2:
                    axis.set_title("%s|%s|%s|%s|%s|%s|%s|%s" % (
                    channel_mean[8], channel_mean[9], channel_mean[10], channel_mean[11], channel_mean[12],
                    channel_mean[13], channel_mean[14], channel_mean[15]))
                if axis == self.__ax3:
                    axis.set_title("%s|%s|%s|%s|%s|%s|%s|%s" % (
                    channel_mean[16], channel_mean[17], channel_mean[18], channel_mean[19], channel_mean[20],
                    channel_mean[21], channel_mean[22], channel_mean[23]))
                if axis == self.__ax4:
                    axis.set_title("%s|%s|%s|%s|%s|%s|%s|%s" % (
                    channel_mean[24], channel_mean[25], channel_mean[26], channel_mean[27], channel_mean[28],
                    channel_mean[29], channel_mean[30], channel_mean[31]))


        for axis in self.Axis_list:
            if axis == self.__ax1:
                a = axis_one_start - 1
                b = axis_one_end
                lineplot(axis, a, b)

            if axis == self.__ax2:
                a = axis_two_start - 1
                b = axis_two_end
                lineplot(axis, a, b)

            if axis == self.__ax3:
                a = axis_three_start - 1
                b = axis_three_end
                lineplot(axis, a, b)

            if axis == self.__ax4:
                a = axis_four_start - 1
                b = axis_four_end
                lineplot(axis, a, b)


    def TimedispalyFigure(self):  ## 绘图
        try:
            # 数据达到一定数量，清屏、画报警线
            if (len(self.plot_timing_data) % 32 * TimingXAxisLength == 0):
                for ax in self.Axis_list:
                    ax.cla()
                    ax.set_xlim([0, TimingXAxisLength])
                    if self.__AbsoluteYAxisShow is True:
                        ax.set_ylim([ylim_min, 4096])
                    ax.plot([CalibrationThreshold] * TimingXAxisLength, '--', linewidth=1.5, color='darkred')
                    if OpenAlarm is True:
                        ax.plot([AlarmThreshold1 * (4096 - ylim_min) / 100 + ylim_min] * TimingXAxisLength, '--',
                                  linewidth=1.5, color='green')
                        ax.plot([AlarmThreshold2 * (4096 - ylim_min) / 100 + ylim_min] * TimingXAxisLength, '--',
                                  linewidth=1.5, color='green')
            X = self.plot_timing_data
            self.PictureDraw(X)
            leg = self.__ax1.legend(bbox_to_anchor=(1.02, 0), loc=3, borderaxespad=0, markerscale=1.5, frameon=False)
            for i in leg.legendHandles:
                i.set_linewidth(12)
            self.__fig.canvas.draw()  # 重绘
        except Exception as err:
            print(traceback.format_exc())


    def __dispalyFigure(self):  ## 绘图
        try:
            # self.ui.statusbar.showMessage("正在加载数据，请等待...")
            self.__labPick.setText("正在加载数据，请等待...")
            # 图像清屏
            for ax in self.Axis_list:
                ax.cla()
            X = self.plot_historical_data
            self.PictureDraw(X)
            leg = self.__ax1.legend(bbox_to_anchor=(1.02, 0), loc=3, borderaxespad=0, markerscale=1.5, frameon=False)
            for i in leg.legendHandles:
                i.set_linewidth(12)
            self.__fig.canvas.draw()  # 重绘
            self.__labPick.setText("数据加载完毕!" + " "*25 + "文件打开地址：" + self.__filename)
        except Exception as err:
            print(traceback.format_exc())


    # 硬件标定
    @pyqtSlot()
    def on_HardwareCalibration_clicked(self):
        try:
            self.__iniFigure()  # 创建绘图系统，初始化窗口
            self.__drawFigure()  # 绘图
            self.__filename = '硬件标定文件.txt'
            self.__datacollection = True  # 检测开始的标志位
            self.parameters_initial()
            self.countfilepage = 1

            self.ui.TotalFileNumberlineEdit.setText('1')
            self.ui.CurrentFileNumberlineEdit.setText('1')
            self.deliverBytes = bytes.fromhex('47 04 06 10 10 10 10 18')  # 标定时发送的字节是定时采样
            self.childprocessbegin()
        except Exception as err:
            print(traceback.format_exc())


    def StopDetction(self):
        global DataSizePerPag, XAxisBagNum, CompressRatio
        with open('stop.txt', 'ab') as f:
            f.write(b'0')
        self.__datacollection = False
        time.sleep(1)
        if self.RecieveDataProcess is not None:
            self.RecieveDataProcess.terminate()
            self.RecieveDataProcess = None
            self.__labPick.setText("检测结束")
            QMessageBox.information(None,'检测状态框','检测结束')
        os.remove('stop.txt')
        self.Button_start()


    @pyqtSlot()
    def on_StopDataCalibration_clicked(self):  # 停止数据检测
        try:
            self.StopDetction()
        except Exception as err:
            print(traceback.format_exc())


    @pyqtSlot()
    def on_HardwareParametersSetting_clicked(self): # 新建数据检测
        try:
            global SpaceMode, TimeMode, SpaceAccuracy, TimeAccuracy, OpenAlarm, CloseAlarm, AlarmThreshold1, AlarmThreshold2, ProbeOneGain, ProbeTwoGain, ProbeThreeGain, ProbeFourGain, Mode
            Dialog_HardwareParameter = QmyHardwareParamter()
            Dialog_HardwareParameter.initHardwareParamter(SpaceMode,TimeMode,  SpaceAccuracy, TimeAccuracy, OpenAlarm, CloseAlarm, AlarmThreshold1, AlarmThreshold2, ProbeOneGain, ProbeTwoGain, ProbeThreeGain, ProbeFourGain)
            ret = Dialog_HardwareParameter.exec()  # 模态方式运行对话框
            if (ret == QDialog.Accepted):
                SpaceMode, TimeMode, SpaceAccuracy, TimeAccuracy, OpenAlarm, CloseAlarm, AlarmThreshold1, AlarmThreshold2, ProbeOneGain, ProbeTwoGain, ProbeThreeGain, ProbeFourGain = Dialog_HardwareParameter.get_HardwareParameters()
                if TimeMode == True:
                    Mode = int("47",16)  # 等时间采样
                # if SpaceMode == True:
                if SpaceMode == True:
                    Mode = int("67",16)  # 等空间采样
                self.__labPick.setText("报警阈值1："+str(AlarmThreshold1) + "%("+str(AlarmThreshold1*4096/100)+")"+" "*5+"报警阈值2："+str(AlarmThreshold1) + "%("+str(AlarmThreshold2*4096/100)+")"+" "*5+"探头1增益："+str(ProbeOneGain)+" "*3+"探头2增益："+str(ProbeTwoGain)+" "*3+"探头3增益："+str(ProbeThreeGain)+" "*3+"探头4增益："+str(ProbeFourGain))
                # self.ui.statusbar.showMessage("报警阈值1："+str(AlarmThreshold1) + "%("+str(AlarmThreshold1*4096/100)+")"+" "*5+"报警阈值2："+str(AlarmThreshold1) + "%("+str(AlarmThreshold2*4096/100)+")"+" "*5+"探头1增益："+str(ProbeOneGain)+" "*3+"探头2增益："+str(ProbeTwoGain)+" "*3+"探头3增益："+str(ProbeThreeGain)+" "*3+"探头4增益："+str(ProbeFourGain))
                self.deliverBytes = bytes([Mode,int(float(SpaceAccuracy[0:-2])*10-1),int(10000/int(TimeAccuracy[0:-3])-1),HardwareGainOrder[ProbeOneGain],HardwareGainOrder[ProbeTwoGain],HardwareGainOrder[ProbeThreeGain],HardwareGainOrder[ProbeFourGain],18])
                print([Mode,int(float(SpaceAccuracy[0:-2])*10-1),int(10000/int(TimeAccuracy[0:-3])-1),HardwareGainOrder[ProbeOneGain],HardwareGainOrder[ProbeTwoGain],HardwareGainOrder[ProbeThreeGain],HardwareGainOrder[ProbeFourGain],18])
        except Exception as err:
            print(traceback.format_exc())


    @pyqtSlot()
    def on_NewDetection_clicked(self): # 新建数据检测
        try:
            Dialog_NewDetection = QmyNewDetection()
            global localport, SendIP, SendPort, Newfilename, OilPipeType,OilPipeThickness,OilPipeSpecification,Operator,DetectionData, PulseDuration, SoftWareGain, Mode, SpaceAccuracy, TimeAccuracy, HardwareGainOrder
            print([Mode, int(float(SpaceAccuracy[0:-2]) * 10 - 1), int(10000 / int(TimeAccuracy[0:-3]) - 1),
                   HardwareGainOrder[ProbeOneGain], HardwareGainOrder[ProbeTwoGain], HardwareGainOrder[ProbeThreeGain],
                   HardwareGainOrder[ProbeFourGain], 18])
            Newfilename = None
            Dialog_NewDetection.initNewDetection(PulseDuration)
            ret = Dialog_NewDetection.exec()  # 模态方式运行对话框
            if (ret == QDialog.Accepted):
                Newfilename,OilPipeType,OilPipeThickness,OilPipeSpecification,Operator,DetectionData, PulseDuration = Dialog_NewDetection.get_NewDetectionParameters()
                # 创建
                if Newfilename != '':
                    self.deliverBytes = bytes(
                        [Mode, int(float(SpaceAccuracy[0:-2]) * 10 - 1), int(10000 / int(TimeAccuracy[0:-3]) - 1),
                         HardwareGainOrder[ProbeOneGain], HardwareGainOrder[ProbeTwoGain],
                         HardwareGainOrder[ProbeThreeGain], HardwareGainOrder[ProbeFourGain], 18])
                    self.__iniFigure()  # 创建绘图系统，初始化窗口
                    self.__drawFigure()  # 绘图
                    self.__datacollection = True
                    self.parameters_initial()
                    curPath = QDir.currentPath()
                    title = Newfilename
                    full_path = curPath + '\\data_storage_location\\' + title + '/'
                    self.__filename = full_path
                    if not os.path.isdir(r'data_storage_location'):
                        os.mkdir(r'data_storage_location')
                    if not os.path.isdir(full_path):
                        os.mkdir(full_path)
                        self.countfilepage = 1
                    else:
                        self.filenumcount()
                    if not os.path.isfile(curPath + '\\data_storage_location\\' + title + '\\parameters.bin'):
                        with open(curPath + '\\data_storage_location\\' + title + '\\parameters.bin', 'a') as f:
                            f.write('%s,'*39%(Newfilename, OilPipeType,OilPipeThickness,OilPipeSpecification,Operator,DetectionData, PulseDuration, FourAxis,TwoAxis,OneAxis,HalfAxis,AbsoluteAxis,RelativeAxis,axis_one_start,axis_one_end,axis_two_start,axis_two_end,axis_three_start,axis_three_end,axis_four_start,axis_four_end,XAxisLength,CompressRatio,AlarmThreshold1,AlarmThreshold2,BlindHeadData,BlindTailData,XAxisBagNum,SpaceMode,TimeMode,SpaceAccuracy,TimeAccuracy,OpenAlarm,CloseAlarm,ProbeOneGain,ProbeTwoGain,ProbeThreeGain,ProbeFourGain,Mode))
                            with open(curPath + '\\data_storage_location\\' + 'TotalInformation.csv', 'a', newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow([Newfilename, OilPipeType,OilPipeThickness,OilPipeSpecification,Operator,DetectionData, PulseDuration])
                    self.ui.TotalFileNumberlineEdit.setText('1')
                    self.ui.CurrentFileNumberlineEdit.setText('1')
                    self.childprocessbegin()
            else:
                pass
        except Exception as err:
            print(traceback.format_exc())


    @pyqtSlot()
    def on_GoOnDetection_clicked(self):  # 继续进行数据检测
        try:
            if self.__filename != '':
                if self.__filename == '硬件标定文件.txt':
                    QMessageBox.critical(self, "错误", "刚刚进行的是硬件标定，没有新建文件，不能继续检测")
                else:
                    self.__iniFigure()  # 创建绘图系统，初始化窗口
                    self.__drawFigure()  # 绘图
                    self.__datacollection = True
                    self.parameters_initial()
                    self.filenumcount()
                    self.childprocessbegin()
            else:
                QMessageBox.critical(self, "错误", "没有已执行的文件存在")
        except Exception as err:
            print(traceback.format_exc())


    @pyqtSlot()
    def on_StopDataCollection_clicked(self): # 新建数据检测
        try:
            self.StopDetction()
        except Exception as err:
            print(traceback.format_exc())


    # 历史数据显示
    def historical_data_read(self):
        try:
            childfile = str(self.countfilepage) + '.txt'
            with open(os.path.join(self.__filename, childfile), 'rb') as f:
                text = f.read()
                count = len(text) / 2
                if (count == 0):
                    QMessageBox.critical(self, "错误", "文件中不存在数据")
                else:
                    self.__labPick.setText("正在加载数据，请等待...")
                    self.historical_original_data = np.array(struct.unpack('H' * int(count), text))
                    if (BlindHeadData != 0):
                        self.historical_data = np.delete(self.historical_original_data,
                                                         np.s_[0:int(BlindHeadData / 20 * 680)], 0)
                    if (BlindTailData != 0):
                        self.historical_data = np.delete(self.historical_data,
                                                         np.s_[-1:-int(BlindTailData / 20 * 680):-1], 0)
                    Page_num = math.ceil(self.historical_data.shape[0] / DataSizePerPag / XAxisBagNum / CompressRatio)
                    self.ui.TotalPageNumberlineEdit.setText("%s" % Page_num)
                    historic_page = int(self.ui.CurrentPageNumberlineEdit.text())-1
                    self.plot_historical_data = self.historical_data[historic_page * CompressRatio * XAxisBagNum * DataSizePerPag : DataSizePerPag * XAxisBagNum * (
                                historic_page + 1) * CompressRatio]
                    self.__iniFigure()  # 创建绘图系统，初始化窗口
                    self.__drawFigure()  # 绘图
                    self.dispalyFigure = threading.Thread(target=self.__dispalyFigure)
                    self.dispalyFigure.start()
        except Exception as err:
            print(traceback.format_exc())


    def HistoricalParameters_initial(self):
        global Newfilename, OilPipeType, OilPipeThickness, OilPipeSpecification, Operator, DetectionData, PulseDuration, FourAxis, TwoAxis, OneAxis, HalfAxis, AbsoluteAxis, RelativeAxis, axis_one_start, axis_one_end, axis_two_start, axis_two_end, axis_three_start, axis_three_end, axis_four_start, axis_four_end, XAxisLength, CompressRatio, AlarmThreshold1, AlarmThreshold2, BlindHeadData, BlindTailData, XAxisBagNum, SpaceMode, TimeMode, SpaceAccuracy, TimeAccuracy, OpenAlarm, CloseAlarm, ProbeOneGain, ProbeTwoGain, ProbeThreeGain, ProbeFourGain, Mode
        parameter_name = os.path.join(self.__filename , 'parameters.bin')
        if os.path.exists(parameter_name):
            with open(parameter_name, 'r') as f:
                [Newfilename, OilPipeType, OilPipeThickness, OilPipeSpecification, Operator, DetectionData,
                 PulseDuration, FourAxis, TwoAxis, OneAxis, HalfAxis, AbsoluteAxis, RelativeAxis, axis_one_start,
                 axis_one_end, axis_two_start, axis_two_end, axis_three_start, axis_three_end, axis_four_start,
                 axis_four_end, XAxisLength, CompressRatio, AlarmThreshold1, AlarmThreshold2, BlindHeadData,
                 BlindTailData, XAxisBagNum, SpaceMode, TimeMode, SpaceAccuracy, TimeAccuracy, OpenAlarm, CloseAlarm,
                 ProbeOneGain, ProbeTwoGain, ProbeThreeGain, ProbeFourGain, Mode, kong] = f.read().split(',')
                FourAxis = JudgeBool(FourAxis)
                TwoAxis = JudgeBool(TwoAxis)
                OneAxis = JudgeBool(OneAxis)
                HalfAxis = JudgeBool(HalfAxis)
                AbsoluteAxis = JudgeBool(AbsoluteAxis)
                RelativeAxis = JudgeBool(RelativeAxis)
                SpaceMode = JudgeBool(SpaceMode)  # 等空间采样
                TimeMode = JudgeBool(TimeMode)  # 等时间采样
                OpenAlarm = JudgeBool(OpenAlarm)  # 报警打开
                CloseAlarm = JudgeBool(CloseAlarm)  # 报警关闭
                axis_one_start = int(axis_one_start)
                axis_one_end = int(axis_one_end)
                axis_two_start = int(axis_two_start)
                axis_two_end = int(axis_two_end)
                axis_three_start = int(axis_three_start)
                axis_three_end = int(axis_three_end)
                axis_four_start = int(axis_four_start)
                axis_four_end = int(axis_four_end)
                XAxisLength = int(XAxisLength)
                CompressRatio = int(CompressRatio)
                AlarmThreshold1 = int(AlarmThreshold1)
                AlarmThreshold2 = int(AlarmThreshold2)
                BlindHeadData = int(BlindHeadData)
                BlindTailData = int(BlindTailData)
                XAxisBagNum = int(XAxisLength / 20)  # 每屏横坐标最多的包数
                ProbeOneGain = int(ProbeOneGain)  # 探头1增益
                ProbeTwoGain = int(ProbeTwoGain)  # 探头2增益
                ProbeThreeGain = int(ProbeThreeGain)  # 探头3增益
                ProbeFourGain = int(ProbeFourGain)  # 探头4增益
                Mode = int(Mode)
                if FourAxis is True:
                    self.AxisNum = 4
                    self.Axis_list = [self.__ax1, self.__ax2, self.__ax3, self.__ax4]
                if TwoAxis is True:
                    self.AxisNum = 2
                    self.Axis_list = [self.__ax1, self.__ax2]
                if OneAxis is True:
                    self.AxisNum = 1
                    self.Axis_list = [self.__ax1]
                # 屏幕数目
                if AbsoluteAxis == True:
                    self.__AbsoluteYAxisShow = True  # 标识符：是否是绝对坐标显示
                else:
                    self.__AbsoluteYAxisShow = False


    @pyqtSlot()
    def on_HistoricalData_clicked(self):# 打开文件
        try:
            curPath = QDir.currentPath() + '\\data_storage_location'  # 获取系统当前目录
            dlgTitle = "选择一个文件"  # 对话框标题
            filt = "所有文件(*.*);;文本文件(*.txt);;图片文件(*.jpg *.gif *.png)"  # 文件过滤器
            filename, filtUsed = QFileDialog.getOpenFileName(self, dlgTitle, curPath, filt)
            if filename != '':
                tem_filename = filename.split('/')
                self.__filename = '/'.join(tem_filename[:-1]) + '/'
                # 文件名字
                self.countfilepage = tem_filename[-1][:-4]
                self.HistoricalParameters_initial()
                self.ui.CurrentPageNumberlineEdit.setText("1")
                self.historical_data_read()
                self.filenumcount()
        except Exception as err:
            print(traceback.format_exc())


    @pyqtSlot()
    def on_PictureSetting_clicked(self):
        try:
            global FourAxis, TwoAxis, OneAxis, HalfAxis, AbsoluteAxis, RelativeAxis, axis_one_start, axis_one_end, axis_two_start, axis_two_end, axis_three_start, axis_three_end, axis_four_start, axis_four_end
            Dialog_PictureSetting = QmyPictureSetting()
            Dialog_PictureSetting.initPictureSetting(FourAxis, TwoAxis, OneAxis, HalfAxis, AbsoluteAxis, RelativeAxis, axis_one_start,axis_one_end,axis_two_start,axis_two_end,axis_three_start,axis_three_end,axis_four_start,axis_four_end)
            ret = Dialog_PictureSetting.exec()  # 模态方式运行对话框
            if (ret == QDialog.Accepted):
                FourAxis, TwoAxis, OneAxis, HalfAxis, AbsoluteAxis, RelativeAxis, axis_one_start, axis_one_end, axis_two_start, axis_two_end, axis_three_start, axis_three_end, axis_four_start, axis_four_end = Dialog_PictureSetting.get_PictureSettingParameters()
                if FourAxis is True:
                    self.AxisNum = 4
                if TwoAxis is True:
                    self.AxisNum = 2
                if OneAxis is True:
                    self.AxisNum = 1
                if AbsoluteAxis is True:
                    self.__AbsoluteYAxisShow = True
                if RelativeAxis is True:
                    self.__AbsoluteYAxisShow = False
                self.__iniFigure()
                self.__drawFigure()  # 绘图
                if self.__filename is not None:
                    if self.historical_original_data is None:
                        pass
                    else:
                        self.dispalyFigure = threading.Thread(target=self.__dispalyFigure)
                        self.dispalyFigure.start()
        except Exception as err:
            print(traceback.format_exc())


    @pyqtSlot()
    def on_WaveAdjust_clicked(self):
        try:
            global SoftWareGain, XAxisLength, CompressRatio, AlarmThreshold1, AlarmThreshold2, BlindHeadData, BlindTailData, XAxisBagNum
            Dialog_WaveAdjust = QmyWaveAdjust()
            Dialog_WaveAdjust.initPictureSetting(SoftWareGain, XAxisLength, CompressRatio, AlarmThreshold1, AlarmThreshold2, BlindHeadData, BlindTailData)
            OrignialCompressRatio = CompressRatio
            ret = Dialog_WaveAdjust.exec()  # 模态方式运行对话框
            if (ret == QDialog.Accepted):
                SoftWareGain, XAxisLength, CompressRatio, AlarmThreshold1, AlarmThreshold2, BlindHeadData, BlindTailData = Dialog_WaveAdjust.getWaveAdujustParameters()
                OriginalXAxisBagNum = XAxisBagNum
                XAxisBagNum = int(XAxisLength / 20)
                # 端头端尾去除
                if (BlindHeadData != 0):
                    self.historical_data = np.delete(self.historical_original_data,
                                                     np.s_[0:int(BlindHeadData / 20 * 680)], 0)
                if (BlindTailData != 0):
                    self.historical_data = np.delete(self.historical_data,
                                                     np.s_[-1:-int(BlindTailData / 20 * 680):-1], 0)
                # 页码数据信息
                Page_num = math.ceil(self.historical_data.shape[0] / (DataSizePerPag * XAxisBagNum * CompressRatio))
                self.ui.TotalPageNumberlineEdit.setText("%s" % Page_num)
                if OrignialCompressRatio == CompressRatio and OriginalXAxisBagNum == XAxisBagNum:
                    CurrentPage = int(self.ui.CurrentPageNumberlineEdit.text())
                else:
                    CurrentPage = 1
                if CurrentPage > Page_num:
                    CurrentPage = Page_num
                self.ui.CurrentPageNumberlineEdit.setText("%s" % CurrentPage)
                historic_page = CurrentPage - 1
                # 相应页码的数据提取
                self.plot_historical_data = self.historical_data[
                                            historic_page * XAxisBagNum * CompressRatio * DataSizePerPag:DataSizePerPag * XAxisBagNum * CompressRatio * (
                                                        historic_page + 1)]
                # 如何数据个数不够一页
                if (self.plot_historical_data.shape[0] / DataSizePerPag * 20 % CompressRatio) != 0:
                    self.plot_historical_data = self.historical_data[
                                                historic_page * XAxisBagNum * CompressRatio * DataSizePerPag:-1]
                self.__iniFigure()
                self.__drawFigure()  # 绘图
                if self.__filename is not None:
                    if self.historical_original_data is None:
                        QMessageBox.critical(self, "错误", "请点击历史数据后再点击波形调整")
                    else:
                        self.dispalyFigure = threading.Thread(target=self.__dispalyFigure)
                        self.dispalyFigure.start()
        except Exception as err:
            print(traceback.format_exc())


    @pyqtSlot()
    def on_ChannelPlayback_clicked(self):
        try:
            global CompressRatio, XAxisLength, XAxisBagNum
            if self.__filename != '':
                self.HistoricalParameters_initial()
                self.ui.CurrentPageNumberlineEdit.setText("1")
                CompressRatio = 20
                XAxisLength = 2000
                XAxisBagNum = int(XAxisLength / 20)
                self.plot_historical_data = self.historical_data[
                                            0 * XAxisBagNum * CompressRatio * DataSizePerPag:DataSizePerPag * XAxisBagNum * CompressRatio]
                # 如何数据个数不够一页
                if (self.plot_historical_data.shape[0] / DataSizePerPag * 20 % CompressRatio) != 0:
                    self.plot_historical_data = self.historical_data[:-1]

                Page_num = math.ceil(self.historical_data.shape[0] / DataSizePerPag / XAxisBagNum / CompressRatio)
                self.ui.TotalPageNumberlineEdit.setText("%s" % Page_num)
                self.Button_close()
                self.__iniFigure()
                self.__drawFigure()  # 绘图
                # 相应页码的数据提取
                if self.historical_original_data is None:
                    QMessageBox.critical(self, "错误", "请点击历史数据后再进行通道回放")
                else:

                    self.dispalyFigure = threading.Thread(target=self.__dispalyFigure)
                    self.dispalyFigure.start()
            else:
                QMessageBox.critical(self, "错误", "没有已执行的文件存在")
        except Exception as err:
            print(traceback.format_exc())


    @pyqtSlot()
    def on_DataSave_clicked(self):
        try:
            curPath = QDir.currentPath()  # 获取系统当前目录
            title = "另存为一个文件"  # 对话框标题
            filt = "图片格式(*.png);;图片文件(*.jpeg);;图片格式(*.bmp);;图片格式(*.tiff);;文本文件(*.txt);;所有文件(*.*)"  # 文件过滤器
            fileName, flt = QFileDialog.getSaveFileName(self, title, curPath, filt)
            if fileName == "":
                return
            if fileName is not None:
                self.__fig.savefig(fileName)
                self.__labPick.setText('图片保存为：' + fileName)
                # self.ui.statusbar.showMessage('图片保存为：' + fileName)
            else:
                QMessageBox.critical(self, "错误", "保存文件失败")
        except Exception as err:
            print(traceback.format_exc())


    @pyqtSlot()
    def on_firstpage_clicked(self):
        if self.__filename is None:
            QMessageBox.critical(self, "错误", "没有数据")
        else:
            if self.historical_original_data is None:
                QMessageBox.critical(self, "错误", "请点击历史数据后再点击此按钮")
            else:
                self.ui.CurrentPageNumberlineEdit.setText("1")
                self.plot_historical_data = self.historical_data[0 * XAxisBagNum * CompressRatio * DataSizePerPag:DataSizePerPag * XAxisBagNum * 1* CompressRatio]
                if (self.plot_historical_data.shape[0] / DataSizePerPag * 20 % CompressRatio) != 0:
                    self.plot_historical_data = self.historical_data[0:-1]
                self.dispalyFigure = threading.Thread(target=self.__dispalyFigure)
                self.dispalyFigure.start()



    @pyqtSlot()
    def on_lastpage_clicked(self):
        if self.__filename is None:
            QMessageBox.critical(self, "错误", "没有数据")
        else:
            if self.historical_original_data is None:
                QMessageBox.critical(self, "错误", "请点击历史数据后再点击此按钮")
            else:
                lastpage = int(self.ui.TotalPageNumberlineEdit.text())
                self.ui.CurrentPageNumberlineEdit.setText("%s" % lastpage)
                self.plot_historical_data = self.historical_data[(lastpage-1) * XAxisBagNum * DataSizePerPag* CompressRatio:DataSizePerPag * XAxisBagNum * lastpage* CompressRatio]
                if (self.plot_historical_data.shape[0] / DataSizePerPag * 20 % CompressRatio) != 0:
                    self.plot_historical_data = self.historical_data[
                                            (lastpage-1) * XAxisBagNum * DataSizePerPag* CompressRatio:-1]
                self.dispalyFigure = threading.Thread(target=self.__dispalyFigure)
                self.dispalyFigure.start()


    @pyqtSlot()
    def on_previouspage_clicked(self):
        if self.__filename is None:
            QMessageBox.critical(self, "错误", "没有数据")
        else:
            if self.historical_original_data is None:
                QMessageBox.critical(self, "错误", "请点击历史数据后再点击此按钮")
            else:
                current = int(self.ui.CurrentPageNumberlineEdit.text())
                if current == 1:
                    dlgTitle = "加载失败"
                    strInfo = "当前为第一页"
                    QMessageBox.warning(self, dlgTitle, strInfo)
                else:
                   current = current - 1
                   self.ui.CurrentPageNumberlineEdit.setText("%s" % current)
                   self.plot_historical_data = self.historical_data[(current - 1) * XAxisBagNum * DataSizePerPag* CompressRatio:DataSizePerPag * XAxisBagNum * current* CompressRatio]
                   if (self.plot_historical_data.shape[0] / DataSizePerPag * 20 % CompressRatio) != 0:
                       self.plot_historical_data = self.historical_data[(current - 1) * XAxisBagNum * DataSizePerPag * CompressRatio:-1]
                   self.dispalyFigure = threading.Thread(target=self.__dispalyFigure)
                   self.dispalyFigure.start()


    @pyqtSlot()
    def on_nextpage_clicked(self):
        if self.__filename is None:
            QMessageBox.critical(self, "错误", "没有数据")
        else:
            if self.historical_original_data is None:
                QMessageBox.critical(self, "错误", "请点击历史数据后再点击此按钮")
            else:
                nextpage = int(self.ui.CurrentPageNumberlineEdit.text())
                lastpage = int(self.ui.TotalPageNumberlineEdit.text())
                if nextpage == (lastpage):
                    dlgTitle = "加载失败"
                    strInfo = "当前为最后一页"
                    QMessageBox.warning(self, dlgTitle, strInfo)
                else:
                    nextpage = nextpage + 1
                    self.ui.CurrentPageNumberlineEdit.setText("%s" % nextpage)
                    self.plot_historical_data = self.historical_data[(nextpage-1)*XAxisBagNum*DataSizePerPag* CompressRatio:DataSizePerPag*XAxisBagNum*nextpage* CompressRatio]
                    if (self.plot_historical_data.shape[0] / DataSizePerPag * 20 % CompressRatio) != 0:
                        self.plot_historical_data = self.historical_data[(nextpage - 1) * XAxisBagNum * DataSizePerPag * CompressRatio:-1]
                    self.dispalyFigure = threading.Thread(target=self.__dispalyFigure)
                    self.dispalyFigure.start()


    @pyqtSlot()
    def on_previousfile_clicked(self):
        if self.__filename is None:
            QMessageBox.critical(self, "错误", "没有数据")
        else:
            if self.historical_original_data is None:
                QMessageBox.critical(self, "错误", "请点击历史数据后再点击此按钮")
            else:
                currentfile = int(self.ui.CurrentFileNumberlineEdit.text())
                if currentfile == 1:
                    dlgTitle = "加载失败"
                    strInfo = "当前为第一个文件"
                    QMessageBox.warning(self, dlgTitle, strInfo)
                else:
                    currentfile = currentfile - 1
                    self.countfilepage = currentfile
                    self.ui.CurrentFileNumberlineEdit.setText("%s" % self.countfilepage)
                    self.ui.CurrentPageNumberlineEdit.setText("1")
                    childfile = str(self.countfilepage) + '.txt'
                    if os.path.isfile(os.path.join(self.__filename, childfile)):
                        self.historical_data_read()
                    else:
                        QMessageBox.critical(self, "错误", "文件不存在")


    @pyqtSlot()
    def on_nextfile_clicked(self):
        if self.__filename is None:
            QMessageBox.critical(self, "错误", "没有数据")
        else:
            if self.historical_original_data is None:
                QMessageBox.critical(self, "错误", "请点击历史数据后再点击此按钮")
            else:
                nextfile = int(self.ui.CurrentFileNumberlineEdit.text())
                lastfile = int(self.ui.TotalFileNumberlineEdit.text())
                if nextfile == (lastfile):
                    dlgTitle = "加载失败"
                    strInfo = "当前为最后一个文件"
                    QMessageBox.warning(self, dlgTitle, strInfo)
                else:
                    nextfile = nextfile + 1
                    self.countfilepage = nextfile
                    self.ui.CurrentFileNumberlineEdit.setText("%s" % self.countfilepage)
                    self.ui.CurrentPageNumberlineEdit.setText("1")
                    childfile = str(self.countfilepage) + '.txt'
                    if os.path.isfile(os.path.join(self.__filename , childfile)):
                        self.historical_data_read()
                    else:
                        QMessageBox.critical(self, "错误", "文件不存在")



if __name__ == "__main__":  # 用于当前窗体测试
    freeze_support()
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyMainWindow()  # 创建窗体
    form.show()
    sys.exit(app.exec_())