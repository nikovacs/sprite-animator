# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_sprite_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 532)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.new_sprite_image_combobox = QtWidgets.QComboBox(Dialog)
        self.new_sprite_image_combobox.setObjectName("new_sprite_image_combobox")
        self.new_sprite_image_combobox.addItem("")
        self.new_sprite_image_combobox.addItem("")
        self.new_sprite_image_combobox.addItem("")
        self.new_sprite_image_combobox.addItem("")
        self.new_sprite_image_combobox.addItem("")
        self.new_sprite_image_combobox.addItem("")
        self.new_sprite_image_combobox.addItem("")
        self.new_sprite_image_combobox.addItem("")
        self.new_sprite_image_combobox.addItem("")
        self.new_sprite_image_combobox.addItem("")
        self.new_sprite_image_combobox.addItem("")
        self.new_sprite_image_combobox.addItem("")
        self.new_sprite_image_combobox.addItem("")
        self.new_sprite_image_combobox.addItem("")
        self.horizontalLayout.addWidget(self.new_sprite_image_combobox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.new_sprite_custom_img_textbox = QtWidgets.QLineEdit(Dialog)
        self.new_sprite_custom_img_textbox.setObjectName("new_sprite_custom_img_textbox")
        self.horizontalLayout_2.addWidget(self.new_sprite_custom_img_textbox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.new_sprite_description_textbox = QtWidgets.QLineEdit(Dialog)
        self.new_sprite_description_textbox.setObjectName("new_sprite_description_textbox")
        self.horizontalLayout_3.addWidget(self.new_sprite_description_textbox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.new_sprite_x_coord_textbox = QtWidgets.QLineEdit(Dialog)
        self.new_sprite_x_coord_textbox.setObjectName("new_sprite_x_coord_textbox")
        self.horizontalLayout_4.addWidget(self.new_sprite_x_coord_textbox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.new_sprite_y_coord_textbox = QtWidgets.QLineEdit(Dialog)
        self.new_sprite_y_coord_textbox.setObjectName("new_sprite_y_coord_textbox")
        self.horizontalLayout_4.addWidget(self.new_sprite_y_coord_textbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.new_sprite_width_textbox = QtWidgets.QLineEdit(Dialog)
        self.new_sprite_width_textbox.setObjectName("new_sprite_width_textbox")
        self.horizontalLayout_5.addWidget(self.new_sprite_width_textbox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.new_sprite_height_textbox = QtWidgets.QLineEdit(Dialog)
        self.new_sprite_height_textbox.setObjectName("new_sprite_height_textbox")
        self.horizontalLayout_5.addWidget(self.new_sprite_height_textbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.openGLWidget = QtWidgets.QOpenGLWidget(Dialog)
        self.openGLWidget.setObjectName("openGLWidget")
        self.verticalLayout_3.addWidget(self.openGLWidget)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.add_sprite_btn = QtWidgets.QPushButton(Dialog)
        self.add_sprite_btn.setObjectName("add_sprite_btn")
        self.horizontalLayout_7.addWidget(self.add_sprite_btn)
        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_7.addWidget(self.cancel_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 4)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Image:"))
        self.new_sprite_image_combobox.setItemText(0, _translate("Dialog", "Custom"))
        self.new_sprite_image_combobox.setItemText(1, _translate("Dialog", "SPRITES"))
        self.new_sprite_image_combobox.setItemText(2, _translate("Dialog", "BODY"))
        self.new_sprite_image_combobox.setItemText(3, _translate("Dialog", "HEAD"))
        self.new_sprite_image_combobox.setItemText(4, _translate("Dialog", "SWORD"))
        self.new_sprite_image_combobox.setItemText(5, _translate("Dialog", "SHIELD"))
        self.new_sprite_image_combobox.setItemText(6, _translate("Dialog", "HORSE"))
        self.new_sprite_image_combobox.setItemText(7, _translate("Dialog", "ATTR1"))
        self.new_sprite_image_combobox.setItemText(8, _translate("Dialog", "ATTR2"))
        self.new_sprite_image_combobox.setItemText(9, _translate("Dialog", "ATTR3"))
        self.new_sprite_image_combobox.setItemText(10, _translate("Dialog", "ATTR12"))
        self.new_sprite_image_combobox.setItemText(11, _translate("Dialog", "PARAM1"))
        self.new_sprite_image_combobox.setItemText(12, _translate("Dialog", "PARAM2"))
        self.new_sprite_image_combobox.setItemText(13, _translate("Dialog", "PARAM3"))
        self.label_2.setText(_translate("Dialog", "Custom Image:"))
        self.label_3.setText(_translate("Dialog", "Description:"))
        self.new_sprite_description_textbox.setText(_translate("Dialog", "sprite"))
        self.label_4.setText(_translate("Dialog", "X:"))
        self.label_5.setText(_translate("Dialog", "Y:"))
        self.label_6.setText(_translate("Dialog", "Width:"))
        self.label_7.setText(_translate("Dialog", "Height:"))
        self.add_sprite_btn.setText(_translate("Dialog", "Add Sprite"))
        self.cancel_btn.setText(_translate("Dialog", "Cancel"))
