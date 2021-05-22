# rviz_qt_embedder tutorial
An example for using a rviz config file in your custom PyQt UI.

This is a useful example describing how to use rviz functionalities in your custom PyQt based UI. Basically you would first need to create a .ui file in Designer for your UI. I have just created a Simple Window with one GridLayout to hold my rviz widget. Then go ahead and open rviz and create a .rviz file. In my project, I have used the map display in my custom UI, so first I created the appropriate .rviz file in rviz.

Note: The map display created above is not a static image, whatever rosmsgs are published on the topics during the run, the rviz widget gets updated accordingly, as it would on a separate rviz window. Therefore, this provides a way for you to visualise rostopics on rviz along with your other Qt Widgets.
