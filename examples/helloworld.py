#!/usr/bin/env python
# encoding: utf-8

# example helloworld.py

import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld:

    # callback function. 省略了參數
    def hello(self, widget, data=None):
        print "Hello World"

    def delete_event(self, widget, event, data=None):
        # 傳回值:
        #        FALSE->GTK會送出destory
        #        TRUE->表示你不想關掉視窗
        # 這個常用在那些“是否確定要離開“之類的對語視窗滿有用
        # 
        print "delete event occurred"

        # Change FALSE to TRUE and the main window will not be destroyed
        # with a "delete_event".
        return False

    # 另一個 callback function
    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        # 建立一個新視窗
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        # 當這個視窗收到 "delete_event"的時候(通常是從WM的close button)
        # 程式會呼叫 上面定義的delete_event()這個function，
        # 傳到function的資料如果是 NULL，則會被忽略
        # 
        # 
        self.window.connect("delete_event", self.delete_event)

        # 把"destory"事件連接到self.destory()
        # 當destory事件發生的時候，程式就會去呼叫 self.destory()
        # destory事件發生：gtk_widget_destory(),或是callback的傳回值是FALS
        self.window.connect("destroy", self.destroy)

        # 設定視窗邊框寬度
        self.window.set_border_width(10)

        # 新建一個按鈕
        self.button = gtk.Button("Hello World")

        # When the button receives the "clicked" signal, it will call the
        # function hello() passing it None as its argument.  The hello()
        # function is defined above.
        self.button.connect("clicked", self.hello, None)

        # This will cause the window to be destroyed by calling
        # gtk_widget_destroy(window) when "clicked".  Again, the destroy
        # signal could come from here, or the window manager.
        self.button.connect_object("clicked", gtk.Widget.destroy, self.window)

        # 把button加到GTK 主視窗容器中
        self.window.add(self.button)

        # show button 
        self.button.show()

        # show windos
        self.window.show()

    def main(self):
        # 所有的PyGTK程式一定要有gtk.main()。會持續的執行程式、並等待事件發生。
        # 像是 key press , mouse event
        gtk.main()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    hello = HelloWorld()
    hello.main()


