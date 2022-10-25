# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1047, 934)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.new_btn = QtWidgets.QPushButton(self.centralwidget)
        self.new_btn.setObjectName("new_btn")
        self.horizontalLayout.addWidget(self.new_btn)
        self.open_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_btn.setObjectName("open_btn")
        self.horizontalLayout.addWidget(self.open_btn)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        self.saveas_btn = QtWidgets.QPushButton(self.centralwidget)
        self.saveas_btn.setObjectName("saveas_btn")
        self.horizontalLayout.addWidget(self.saveas_btn)
        self.undo_btn = QtWidgets.QPushButton(self.centralwidget)
        self.undo_btn.setObjectName("undo_btn")
        self.horizontalLayout.addWidget(self.undo_btn)
        self.redo_btn = QtWidgets.QPushButton(self.centralwidget)
        self.redo_btn.setObjectName("redo_btn")
        self.horizontalLayout.addWidget(self.redo_btn)
        self.plus_sprite_btn = QtWidgets.QPushButton(self.centralwidget)
        self.plus_sprite_btn.setObjectName("plus_sprite_btn")
        self.horizontalLayout.addWidget(self.plus_sprite_btn)
        self.minus_unused_btn = QtWidgets.QPushButton(self.centralwidget)
        self.minus_unused_btn.setObjectName("minus_unused_btn")
        self.horizontalLayout.addWidget(self.minus_unused_btn)
        self.import_btn = QtWidgets.QPushButton(self.centralwidget)
        self.import_btn.setObjectName("import_btn")
        self.horizontalLayout.addWidget(self.import_btn)
        self.reverse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reverse_btn.setObjectName("reverse_btn")
        self.horizontalLayout.addWidget(self.reverse_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bg_color_btn = QtWidgets.QPushButton(self.centralwidget)
        self.bg_color_btn.setObjectName("bg_color_btn")
        self.horizontalLayout.addWidget(self.bg_color_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sprite_scroll_area = QtWidgets.QScrollArea(self.centralwidget)
        self.sprite_scroll_area.setWidgetResizable(True)
        self.sprite_scroll_area.setObjectName("sprite_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 677, 796))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.sprite_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.sprite_scroll_area)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.dir_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.dir_combo_box.setObjectName("dir_combo_box")
        self.dir_combo_box.addItem("")
        self.dir_combo_box.addItem("")
        self.dir_combo_box.addItem("")
        self.dir_combo_box.addItem("")
        self.horizontalLayout_4.addWidget(self.dir_combo_box)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.selected_sprite_text = QtWidgets.QLineEdit(self.centralwidget)
        self.selected_sprite_text.setObjectName("selected_sprite_text")
        self.horizontalLayout_5.addWidget(self.selected_sprite_text)
        self.selected_sprite_combo = QtWidgets.QComboBox(self.centralwidget)
        self.selected_sprite_combo.setObjectName("selected_sprite_combo")
        self.horizontalLayout_5.addWidget(self.selected_sprite_combo)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.plus_layer_btn = QtWidgets.QPushButton(self.centralwidget)
        self.plus_layer_btn.setObjectName("plus_layer_btn")
        self.verticalLayout_6.addWidget(self.plus_layer_btn)
        self.minus_layer_btn = QtWidgets.QPushButton(self.centralwidget)
        self.minus_layer_btn.setObjectName("minus_layer_btn")
        self.verticalLayout_6.addWidget(self.minus_layer_btn)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.plus_x_btn = QtWidgets.QPushButton(self.centralwidget)
        self.plus_x_btn.setMinimumSize(QtCore.QSize(25, 0))
        self.plus_x_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.plus_x_btn.setObjectName("plus_x_btn")
        self.horizontalLayout_7.addWidget(self.plus_x_btn)
        self.minus_x_btn = QtWidgets.QPushButton(self.centralwidget)
        self.minus_x_btn.setMinimumSize(QtCore.QSize(25, 0))
        self.minus_x_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.minus_x_btn.setObjectName("minus_x_btn")
        self.horizontalLayout_7.addWidget(self.minus_x_btn)
        self.plus_y_btn = QtWidgets.QPushButton(self.centralwidget)
        self.plus_y_btn.setMinimumSize(QtCore.QSize(25, 0))
        self.plus_y_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.plus_y_btn.setObjectName("plus_y_btn")
        self.horizontalLayout_7.addWidget(self.plus_y_btn)
        self.minus_y_btn = QtWidgets.QPushButton(self.centralwidget)
        self.minus_y_btn.setMinimumSize(QtCore.QSize(25, 0))
        self.minus_y_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.minus_y_btn.setObjectName("minus_y_btn")
        self.horizontalLayout_7.addWidget(self.minus_y_btn)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.x_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.x_textbox.setMinimumSize(QtCore.QSize(35, 0))
        self.x_textbox.setMaximumSize(QtCore.QSize(25, 16777215))
        self.x_textbox.setObjectName("x_textbox")
        self.horizontalLayout_8.addWidget(self.x_textbox)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.y_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.y_textbox.setMinimumSize(QtCore.QSize(35, 0))
        self.y_textbox.setMaximumSize(QtCore.QSize(25, 16777215))
        self.y_textbox.setObjectName("y_textbox")
        self.horizontalLayout_8.addWidget(self.y_textbox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.length_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.length_textbox.setMaximumSize(QtCore.QSize(115, 16777215))
        self.length_textbox.setObjectName("length_textbox")
        self.horizontalLayout_9.addWidget(self.length_textbox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.loop_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.loop_checkbox.setObjectName("loop_checkbox")
        self.verticalLayout_9.addWidget(self.loop_checkbox)
        self.continuous_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.continuous_checkbox.setObjectName("continuous_checkbox")
        self.verticalLayout_9.addWidget(self.continuous_checkbox)
        self.singledir_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.singledir_checkbox.setObjectName("singledir_checkbox")
        self.verticalLayout_9.addWidget(self.singledir_checkbox)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.setbackto_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.setbackto_textbox.setObjectName("setbackto_textbox")
        self.horizontalLayout_10.addWidget(self.setbackto_textbox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.def_attr12_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.def_attr12_textbox.setObjectName("def_attr12_textbox")
        self.gridLayout.addWidget(self.def_attr12_textbox, 5, 1, 1, 1)
        self.def_attr1_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.def_attr1_textbox.setObjectName("def_attr1_textbox")
        self.gridLayout.addWidget(self.def_attr1_textbox, 2, 1, 1, 1)
        self.def_head_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.def_head_textbox.setObjectName("def_head_textbox")
        self.gridLayout.addWidget(self.def_head_textbox, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.param2_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.param2_textbox.setObjectName("param2_textbox")
        self.gridLayout.addWidget(self.param2_textbox, 7, 1, 1, 1)
        self.param1_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.param1_textbox.setObjectName("param1_textbox")
        self.gridLayout.addWidget(self.param1_textbox, 6, 1, 1, 1)
        self.def_attr3_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.def_attr3_textbox.setObjectName("def_attr3_textbox")
        self.gridLayout.addWidget(self.def_attr3_textbox, 4, 1, 1, 1)
        self.def_body_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.def_body_textbox.setObjectName("def_body_textbox")
        self.gridLayout.addWidget(self.def_body_textbox, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.def_attr2_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.def_attr2_textbox.setObjectName("def_attr2_textbox")
        self.gridLayout.addWidget(self.def_attr2_textbox, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)
        self.param3_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.param3_textbox.setObjectName("param3_textbox")
        self.gridLayout.addWidget(self.param3_textbox, 8, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 7, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 8, 0, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_4.addLayout(self.verticalLayout_8)
        self.edit_script_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_script_btn.setObjectName("edit_script_btn")
        self.verticalLayout_4.addWidget(self.edit_script_btn)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setMinimumSize(QtCore.QSize(100, 0))
        self.label_15.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_12.addWidget(self.label_15)
        self.frame_slider = QtWidgets.QSlider(self.centralwidget)
        self.frame_slider.setOrientation(QtCore.Qt.Horizontal)
        self.frame_slider.setObjectName("frame_slider")
        self.horizontalLayout_12.addWidget(self.frame_slider)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.horizontalLayout_12.setStretch(1, 3)
        self.horizontalLayout_12.setStretch(2, 1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_11.addWidget(self.time_label)
        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn.setObjectName("play_btn")
        self.horizontalLayout_11.addWidget(self.play_btn)
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout_11.addWidget(self.stop_btn)
        self.plus_frame_btn = QtWidgets.QPushButton(self.centralwidget)
        self.plus_frame_btn.setObjectName("plus_frame_btn")
        self.horizontalLayout_11.addWidget(self.plus_frame_btn)
        self.minus_frame_btn = QtWidgets.QPushButton(self.centralwidget)
        self.minus_frame_btn.setObjectName("minus_frame_btn")
        self.horizontalLayout_11.addWidget(self.minus_frame_btn)
        self.copy_btn = QtWidgets.QPushButton(self.centralwidget)
        self.copy_btn.setObjectName("copy_btn")
        self.horizontalLayout_11.addWidget(self.copy_btn)
        self.paste_left_btn = QtWidgets.QPushButton(self.centralwidget)
        self.paste_left_btn.setObjectName("paste_left_btn")
        self.horizontalLayout_11.addWidget(self.paste_left_btn)
        self.paste_right_btn = QtWidgets.QPushButton(self.centralwidget)
        self.paste_right_btn.setObjectName("paste_right_btn")
        self.horizontalLayout_11.addWidget(self.paste_right_btn)
        self.plus_sound_btn = QtWidgets.QPushButton(self.centralwidget)
        self.plus_sound_btn.setObjectName("plus_sound_btn")
        self.horizontalLayout_11.addWidget(self.plus_sound_btn)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.sound_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.sound_textbox.setObjectName("sound_textbox")
        self.horizontalLayout_11.addWidget(self.sound_textbox)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 1)
        self.horizontalLayout_11.setStretch(2, 1)
        self.horizontalLayout_11.setStretch(3, 1)
        self.horizontalLayout_11.setStretch(4, 1)
        self.horizontalLayout_11.setStretch(5, 1)
        self.horizontalLayout_11.setStretch(6, 1)
        self.horizontalLayout_11.setStretch(7, 1)
        self.horizontalLayout_11.setStretch(8, 1)
        self.horizontalLayout_11.setStretch(9, 1)
        self.horizontalLayout_11.setStretch(10, 3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_11)
        self.verticalLayout_2.addLayout(self.verticalLayout_10)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.new_btn, self.open_btn)
        MainWindow.setTabOrder(self.open_btn, self.save_btn)
        MainWindow.setTabOrder(self.save_btn, self.saveas_btn)
        MainWindow.setTabOrder(self.saveas_btn, self.undo_btn)
        MainWindow.setTabOrder(self.undo_btn, self.redo_btn)
        MainWindow.setTabOrder(self.redo_btn, self.plus_sprite_btn)
        MainWindow.setTabOrder(self.plus_sprite_btn, self.minus_unused_btn)
        MainWindow.setTabOrder(self.minus_unused_btn, self.import_btn)
        MainWindow.setTabOrder(self.import_btn, self.reverse_btn)
        MainWindow.setTabOrder(self.reverse_btn, self.bg_color_btn)
        MainWindow.setTabOrder(self.bg_color_btn, self.dir_combo_box)
        MainWindow.setTabOrder(self.dir_combo_box, self.selected_sprite_text)
        MainWindow.setTabOrder(self.selected_sprite_text, self.selected_sprite_combo)
        MainWindow.setTabOrder(self.selected_sprite_combo, self.plus_layer_btn)
        MainWindow.setTabOrder(self.plus_layer_btn, self.minus_layer_btn)
        MainWindow.setTabOrder(self.minus_layer_btn, self.plus_x_btn)
        MainWindow.setTabOrder(self.plus_x_btn, self.minus_x_btn)
        MainWindow.setTabOrder(self.minus_x_btn, self.plus_y_btn)
        MainWindow.setTabOrder(self.plus_y_btn, self.minus_y_btn)
        MainWindow.setTabOrder(self.minus_y_btn, self.x_textbox)
        MainWindow.setTabOrder(self.x_textbox, self.y_textbox)
        MainWindow.setTabOrder(self.y_textbox, self.length_textbox)
        MainWindow.setTabOrder(self.length_textbox, self.loop_checkbox)
        MainWindow.setTabOrder(self.loop_checkbox, self.continuous_checkbox)
        MainWindow.setTabOrder(self.continuous_checkbox, self.singledir_checkbox)
        MainWindow.setTabOrder(self.singledir_checkbox, self.setbackto_textbox)
        MainWindow.setTabOrder(self.setbackto_textbox, self.def_head_textbox)
        MainWindow.setTabOrder(self.def_head_textbox, self.def_body_textbox)
        MainWindow.setTabOrder(self.def_body_textbox, self.def_attr1_textbox)
        MainWindow.setTabOrder(self.def_attr1_textbox, self.def_attr2_textbox)
        MainWindow.setTabOrder(self.def_attr2_textbox, self.def_attr3_textbox)
        MainWindow.setTabOrder(self.def_attr3_textbox, self.def_attr12_textbox)
        MainWindow.setTabOrder(self.def_attr12_textbox, self.param1_textbox)
        MainWindow.setTabOrder(self.param1_textbox, self.param2_textbox)
        MainWindow.setTabOrder(self.param2_textbox, self.param3_textbox)
        MainWindow.setTabOrder(self.param3_textbox, self.edit_script_btn)
        MainWindow.setTabOrder(self.edit_script_btn, self.frame_slider)
        MainWindow.setTabOrder(self.frame_slider, self.play_btn)
        MainWindow.setTabOrder(self.play_btn, self.stop_btn)
        MainWindow.setTabOrder(self.stop_btn, self.plus_frame_btn)
        MainWindow.setTabOrder(self.plus_frame_btn, self.minus_frame_btn)
        MainWindow.setTabOrder(self.minus_frame_btn, self.copy_btn)
        MainWindow.setTabOrder(self.copy_btn, self.paste_left_btn)
        MainWindow.setTabOrder(self.paste_left_btn, self.paste_right_btn)
        MainWindow.setTabOrder(self.paste_right_btn, self.plus_sound_btn)
        MainWindow.setTabOrder(self.plus_sound_btn, self.sound_textbox)
        MainWindow.setTabOrder(self.sound_textbox, self.sprite_scroll_area)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.new_btn.setText(_translate("MainWindow", "New"))
        self.open_btn.setText(_translate("MainWindow", "Open"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.saveas_btn.setText(_translate("MainWindow", "Save As"))
        self.undo_btn.setText(_translate("MainWindow", "Undo"))
        self.redo_btn.setText(_translate("MainWindow", "Redo"))
        self.plus_sprite_btn.setText(_translate("MainWindow", "+ Sprite"))
        self.minus_unused_btn.setText(_translate("MainWindow", "- Unused"))
        self.import_btn.setText(_translate("MainWindow", "Import"))
        self.reverse_btn.setText(_translate("MainWindow", "Reverse"))
        self.bg_color_btn.setText(_translate("MainWindow", "BG Color"))
        self.label.setText(_translate("MainWindow", "Direction:"))
        self.dir_combo_box.setItemText(0, _translate("MainWindow", "Up"))
        self.dir_combo_box.setItemText(1, _translate("MainWindow", "Left"))
        self.dir_combo_box.setItemText(2, _translate("MainWindow", "Down"))
        self.dir_combo_box.setItemText(3, _translate("MainWindow", "Right"))
        self.label_2.setText(_translate("MainWindow", "Selected Sprite:"))
        self.plus_layer_btn.setText(_translate("MainWindow", "+L"))
        self.minus_layer_btn.setText(_translate("MainWindow", "-L"))
        self.plus_x_btn.setText(_translate("MainWindow", "+X"))
        self.minus_x_btn.setText(_translate("MainWindow", "-X"))
        self.plus_y_btn.setText(_translate("MainWindow", "+Y"))
        self.minus_y_btn.setText(_translate("MainWindow", "-Y"))
        self.label_3.setText(_translate("MainWindow", "X:"))
        self.label_4.setText(_translate("MainWindow", "Y:"))
        self.label_5.setText(_translate("MainWindow", "Length:"))
        self.loop_checkbox.setText(_translate("MainWindow", "Loop"))
        self.continuous_checkbox.setText(_translate("MainWindow", "Continuous"))
        self.singledir_checkbox.setText(_translate("MainWindow", "Single Dir"))
        self.label_6.setText(_translate("MainWindow", "Setbackto"))
        self.label_10.setText(_translate("MainWindow", "Def. attr2"))
        self.label_7.setText(_translate("MainWindow", "Def. Head"))
        self.label_8.setText(_translate("MainWindow", "Def. Body"))
        self.label_9.setText(_translate("MainWindow", "Def. attr1"))
        self.label_11.setText(_translate("MainWindow", "Def. attr3"))
        self.label_12.setText(_translate("MainWindow", "Def. ATTR12"))
        self.label_14.setText(_translate("MainWindow", "Def. param1"))
        self.label_16.setText(_translate("MainWindow", "Def. param2"))
        self.label_17.setText(_translate("MainWindow", "Def. param3"))
        self.edit_script_btn.setText(_translate("MainWindow", "Edit Script"))
        self.label_15.setText(_translate("MainWindow", "Time:"))
        self.time_label.setText(_translate("MainWindow", "PlaceHolder"))
        self.play_btn.setText(_translate("MainWindow", "Play"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.plus_frame_btn.setText(_translate("MainWindow", "+Frame"))
        self.minus_frame_btn.setText(_translate("MainWindow", "-Frame"))
        self.copy_btn.setText(_translate("MainWindow", "Copy"))
        self.paste_left_btn.setText(_translate("MainWindow", "<Paste"))
        self.paste_right_btn.setText(_translate("MainWindow", "Paste>"))
        self.plus_sound_btn.setText(_translate("MainWindow", "+Sound"))
        self.label_13.setText(_translate("MainWindow", "Sound:"))
