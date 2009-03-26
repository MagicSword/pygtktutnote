#!/usr/bin/env python
# encoding: utf-8
# example helloworld2.py

import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld2:

    # 新版的helloworld。傳入callback的data會被印到stdou
    # 
    def callback(self, widget, data):
        print "Hello again - %s was pressed" % data

    # another callback
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        # 新的函數。用來設定windows 的title
        # 
        self.window.set_title("Hello Buttons!")

        # Here we just set a handler for delete_event that immediately
        # exits GTK.
        self.window.connect("delete_event", self.delete_event)

        # Sets the border width of the window.
        self.window.set_border_width(10)

        # 新建了一個box用來當成其他widget的容器。
        # 在 "packing section"還會再詳述。
        # HBox基本上是看不到的，大多是用來排列widget
        self.box1 = gtk.HBox(False, 0)

        # Put the box into the main window.
        self.window.add(self.box1)

        # Creates a new button with the label "Button 1".
        self.button1 = gtk.Button("Button 1")

        # button1被按下的時候，程式會呼叫callback()
        # 並傳出 "button 1"
        self.button1.connect("clicked", self.callback, "button 1")

        # 上次用add()，這次改用pack_start()
        # 
        self.box1.pack_start(self.button1, True, True, 0)

        # 記得這個步驟，秀出 button1
        #
        self.button1.show()

        # Do these same steps again to create a second button
        self.button2 = gtk.Button("Button 2")

        # Call the same callback method with a different argument,
        # passing a pointer to "button 2" instead.
        self.button2.connect("clicked", self.callback, "button 2")

        self.box1.pack_start(self.button2, True, True, 0)

        # 在這個例子中，button的順序不重要，所以隨便
        # 但 box1,windows還是最後秀，這樣所有widgets可以一起顯示 
        self.button2.show()
        self.box1.show()
        self.window.show()

def main():
    gtk.main()

if __name__ == "__main__":
    hello = HelloWorld2()
    main()
