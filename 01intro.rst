.. _01intro:
.. vim: ts=4


Forward
=======

    雖然覺得PyGTK的語法太雜，不過因為目前主要用的是Gnome，還是看一下好了。
    雖說是筆記，不過好像快作成翻譯了

Document Formation
------------------

 * 章名依英文PyGTK tutorial 原版，code、圖檔名都依英文原版，可能會作些修改
 * 翻譯的話，術語不強制一定都要翻成中文，以看的懂為主
 * 因為是筆記，所以可能會省略我覺得不重要的地方，會加一些東西，重排版
 * ReST原始碼一行不超過 80 chars
 * Source code 都用 include進來的，註解重要的會翻譯，加行號
 * 圖片用 figure tag
 * ReST一章節一份文件，檔名用 01intro.rst 的格式
 * 元件的中譯名參考 glade-2
 * 在文間的程式碼用 ``gtk.sample()``

 

1. Introduction
===============

    * GTK原來是GIMP所發展出來的GUI Toolkit
    * this tutorial based on GTK+ 2.0~2.4,Python 2.2,PyGTK 2.0~2.4
    * :download:`pygtkconsole <examples/pygtkconsole.py>`:一個小程式，可以用來和pygtk互動
    * ipython: 記得也有和pygtk,pyqt 互動的功能

Brief
-----------------

這邊簡述一下這份教學文件各章節內容：

介紹

 * `1. Introduction`_ 
 * :ref:`02start`
 * :ref:`03moveon`
 * :ref:`04packing`
 * :ref:`05widget`

基本元件：

 * :ref:`06button`
 * :ref:`07adjustments`
 * :ref:`08range`
 * :ref:`09misc`
 * :ref:`10container`
 * :ref:`11menu`
 * :ref:`12drawingaera`


進階元件
 * :ref:`13texview`
 * :ref:`14treeview`
 * :ref:`15new2.2`
 * :ref:`16new2.4`
 * :ref:`17undocumented`


進階功能設定
 * :ref:`18setAttrib`
 * :ref:`19timeouts`
 * :ref:`20advSignal`
 * :ref:`21selection`
 * :ref:`22dragdrop`
 * :ref:`23gtkrc`


範例、其他

 * :ref:`24scribble`
 * :ref:`25tips`
 * :ref:`26contributing`
 * :ref:`27credits`
 * :ref:`28copyright`



.. _`1. Introduction`: 01intro_



