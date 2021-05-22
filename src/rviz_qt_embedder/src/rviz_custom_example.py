#!/usr/bin/env python

import rviz
import rospy
import sys
from PyQt5 import QtGui, QtCore, uic, QtWidgets

# from PyQt4 import *   
# from PyQt4.Qt import *
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *

# from python_qt_binding.QtGui import *
# from python_qt_binding.QtCore import *
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseWithCovarianceStamped
import rviz





class MyWindow(QtWidgets.QMainWindow):
	def __init__(self):

		#Qt Stuff..
		super(MyWindow, self).__init__()
		uic.loadUi('/home/rajendra/rqtGUI_ws/src/rviz_qt_embedder/ui/designer_file.ui', self)		#load the .ui file made from Qt designer -- you can also use pyside-uic -o outpit.py input.ui on terminal to see your .ui file converted to python objects.

		#initialise your rviz widget
		self.map_widget = MyViz()
		#add the widget to a layout present in the main window.(This will depend on the name of your layout defined by you in the designer file)
		self.gridLayout.addWidget(self.map_widget)




#follow this : http://docs.ros.org/hydro/api/rviz_python_tutorial/html/  for more information and  my comments.
class MyViz(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.frame = rviz.VisualizationFrame()
        self.frame.setSplashPath( "" )
        self.frame.initialize()
        reader = rviz.YamlConfigReader()
        config = rviz.Config()

        #you will need a rviz config file. This config file basically has the information about what all from the rviz you want to display on your custom UI.
   
        reader.readFile( config, "/home/rajendra/rqtGUI_ws/src/rviz_qt_embedder/rviz/my_rviz_file.rviz" ) #my_rviz_file.rviz
        self.frame.load( config )

        #some settings for how you want your rviz screen to look like.
        self.setWindowTitle( config.mapGetChild( "Title" ).getValue() )
        self.frame.setMenuBar( None )
        self.frame.setStatusBar( None )
        self.frame.setHideButtonVisibility( False )
        self.manager = self.frame.getManager()
        self.grid_display = self.manager.getRootDisplayGroup().getDisplayAt( 0 )
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget( self.frame )
        self.setLayout( layout )



if __name__ == '__main__':
	rospy.init_node('talker')
	rospy.loginfo("Node initialised")
	app = QtWidgets.QApplication(sys.argv)
	myWindow = MyWindow()
	myWindow.show()
	app.exec_()