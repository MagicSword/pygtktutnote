.. _07adjustments:
.. vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

.. module:: Adjustments
    :synopsis: Adjustments for transfer date between widgets


7. Adjustments
==============

GTK有一些元件可以用來控制大小。像range widgets的捲軸。
另一些元件用來顯示內容，如果內容太多，就只會顯示其中的一些。
像 text,viewport widgets。要怎麼讓這兩者間互動？大概有兩個方法：

 * 當元件大小改變的時候，丟出自已狀態改變的signal
 * 丟出新值給signal function
 * 查widgets內部的屬性，以確定是不是有狀態改變


常見的例子就是 scrollbar和viewport或是text area連接。
如果每個元件都有不同的設定方式，那互動工作可能要得要程式設計師自己動手作。

貼心的(?)GTK都幫你搞定了。你只要用 ``Adjustment`` , 它不是widget，有點像中間人的角色，負責在元件間存值、傳值。
最常見的例子是用 ``Adjustment`` 存scrollbar的狀態。
不過因為 ``Adjustment`` 是從 ``Object``  繼承來的，使得它更威。
更重要的是它可以發送signals，讓signals在其他可調整的元件間傳送。

其他例子，像是 ProgressBars,ViewPorts,Scrolled Window...

7.1. Creating an Adjustment
---------------------------

新增 Adjustment::

    adjustment = gtk.Adjustment(value=0, lower=0, upper=0, 
                        step_incr=0, page_incr=0, page_size=0)


 * value: 初始值
 * lower,upper: 最大值、最小值
 * step_incr: 每次遞增多少
 * page_incr: 比較大的遞增
 * page_size: 通常對應的是文件的大小，通常是 non-zero

因為upper代表的是可見區的最大值，並不是整份文件大小

7.2. Using Adjustments the Easy Way
-----------------------------------

調整型(?)元件有兩種
 * 沒有特定單位的，例：Scrollbars,Scales, ProgressBar, and SpinButton
    這些元件用的是相對的單位，可以直接用mouse,keyboard改變大小

 * 有固定單位的，例: text,viewport,CompoundList,scrolled window
    這些元件都用固定單位：pixel，這些元件也可以用scrollbar間接的改變大小
     
現在來試試用scrollbar控制text,viewports    
::

  # creates its own adjustments
  viewport = gtk.Viewport()
  # uses the newly-created adjustment for the scrollbar as well
  vscrollbar = gtk.VScrollbar(viewport.get_vadjustment())


7.3. Adjustment Internals
-------------------------

如果要建立一個自己的對應到Adjustment的函式，要怎麼讀出Adjustment的值？
在這用例子來說明 ``gtk.Adjustment()`` 

改變 Adjustment的值::

    adjustment.set_value(value)

之前提過 ``Adjustment`` 也可以送出 signals，所以可以設定 ``Adjustment`` 內部
數值改變，送出signal到與它連接的widgets，對應的callback應該會是這樣::

    def value_changed(adjustment):

和 ``Adjustment`` 連接的元件在 ``Adjustment`` 值變更時，也會發出signals。

例：有一個 scale widget，會依數值變更而改變圖片的方向，對應的callback應該會是::

    def cb_rotate_picture(adj, picture):
        set_picture_rotation (picture, adj.value)



``Adjustment`` 連接到scale widget::

    dj.connect("value_changed", cb_rotate_picture, picture)

最大值、最小值(upper,lower)改變的情形，例:使用者新增或刪除text widget的文字。
定義 text widget狀態變成changed的signal::

    def changed(adjustment):

Range widgets通常會有一個handler和 changed連接。

一般來說，如果你是自已寫widget，如果你直接改變 ``Adjustment`` 的值，你可能要手動送出重新設定的signal::

    adjustment.emit("changed")

------------------------------------

.. seealso::

Range widgets typically connect a handler to this signal, which changes their appearance to reflect the change - for example, the size of the slider in a scrollbar will grow or shrink in inverse proportion to the difference between the lower and upper values of its adjustment.

You probably won't ever need to attach a handler to this signal, unless you're writing a new type of range widget. However, if you change any of the values in a Adjustment directly, you should emit this signal on it to reconfigure whatever widgets are using it, like this:


.. vim: ts=4
