# -*- coding: utf-8 -*-
#!/usr/bin/python

print("Hello, World!")

# 输出
# ➜  learning_of_python3 python \ hello.py
# Hello, World!
# ➜  learning_of_python3 python3 \ hello.py
# Hello, World!
# ➜  learning_of_python3

# 关于python的解释介绍
# https://www.runoob.com/python3/python3-intro.html

# 优点
#  简单 -- Python 是一种代表简单主义思想的语言。阅读一个良好的 Python 程序就感觉像是在读英语一样，尽管这个英语的要求非常严格！Python 的这种伪代码本质是它最大的优点之一。它使你能够专注于解决问题而不是去搞明白语言本身。
#  易学 -- 就如同你即将看到的一样，Python 极其容易上手。前面已经提到了，Python 有极其简单的语法。
#  免费、开源 -- Python 是 FLOSS（自由/开放源码软件）之一。简单地说，你可以自由地发布这个软件的拷贝、阅读它的源代码、对它做改动、把它的一部分用于新的自由软件中。FLOSS 是基于一个团体分享知识的概念。这是为什么 Python 如此优秀的原因之一——它是由一群希望看到一个更加优秀的 Python 的人创造并经常改进着的。
#  高层语言 -- 当你用 Python 语言编写程序的时候，你无需考虑诸如如何管理你的程序使用的内存一类的底层细节。
#  可移植性 -- 由于它的开源本质，Python 已经被移植在许多平台上（经过改动使它能够工作在不同平台上）。如果你小心地避免使用依赖于系统的特性，那么你的所有 Python 程序无需修改就可以在下述任何平台上面运行。这些平台包括 Linux、Windows、FreeBSD、Macintosh、Solaris、OS/2、Amiga、AROS、AS/400、BeOS、OS/390、z/OS、Palm OS、QNX、VMS、Psion、Acom RISC OS、VxWorks、PlayStation、Sharp Zaurus、Windows CE 甚至还有 PocketPC、Symbian 以及 Google 基于 Linux 开发的 Android 平台！
#  解释性 -- 这一点需要一些解释。一个用编译性语言比如 C 或 C++ 写的程序可以从源文件（即 C 或 C++ 语言）转换到一个你的计算机使用的语言（二进制代码，即0和1）。这个过程通过编译器和不同的标记、选项完成。当你运行你的程序的时候，连接/转载器软件把你的程序从硬盘复制到内存中并且运行。而 Python 语言写的程序不需要编译成二进制代码。你可以直接从源代码运行程序。在计算机内部，Python 解释器把源代码转换成称为字节码的中间形式，然后再把它翻译成计算机使用的机器语言并运行。事实上，由于你不再需要担心如何编译程序，如何确保连接转载正确的库等等，所有这一切使得使用 Python 更加简单。由于你只需要把你的 Python 程序拷贝到另外一台计算机上，它就可以工作了，这也使得你的 Python 程序更加易于移植。
#  面向对象 -- Python 既支持面向过程的编程也支持面向对象的编程。在“面向过程”的语言中，程序是由过程或仅仅是可重用代码的函数构建起来的。在“面向对象”的语言中，程序是由数据和功能组合而成的对象构建起来的。与其他主要的语言如 C++ 和 Java 相比，Python 以一种非常强大又简单的方式实现面向对象编程。
#  可扩展性 -- 如果你需要你的一段关键代码运行得更快或者希望某些算法不公开，你可以把你的部分程序用 C 或 C++ 编写，然后在你的 Python 程序中使用它们。
#  丰富的库 -- Python 标准库确实很庞大。它可以帮助你处理各种工作，包括正则表达式、文档生成、单元测试、线程、数据库、网页浏览器、CGI、FTP、电子邮件、XML、XML-RPC、HTML、WAV 文件、密码系统、GUI（图形用户界面）、Tk 和其他与系统有关的操作。记住，只要安装了 Python，所有这些功能都是可用的。这被称作 Python 的“功能齐全”理念。除了标准库以外，还有许多其他高质量的库，如 wxPython、Twisted 和 Python 图像库等等。
#  规范的代码 -- Python 采用强制缩进的方式使得代码具有极佳的可读性。
# 缺点

#  运行速度，有速度要求的话，用 C++ 改写关键部分吧。
#  国内市场较小（国内以 Python 来做主要开发的，目前只有一些 web2.0 公司）。但时间推移，目前很多国内软件公司，尤其是游戏公司，也开始规模使用他。
#  中文资料匮乏（好的 Python 中文资料屈指可数，现在应该变多了）。托社区的福，有几本优秀的教材已经被翻译了，但入门级教材多，高级内容还是只能看英语版。
#  构架选择太多（没有像 C# 这样的官方 .net 构架，也没有像 ruby 由于历史较短，构架开发的相对集中。Ruby on Rails 构架开发中小型web程序天下无敌）。不过这也从另一个侧面说明，python比较优秀，吸引的人才多，项目也多。


# Python 的主要运用领域有:

#  云计算：云计算最热的语言，典型的应用OpenStack
#  WEB开发：许多优秀的 WEB 框架，许多大型网站是Python开发、YouTube、Dropbox、Douban……典型的Web框架包括Django
#  科学计算和人工智能：典型的图书馆NumPy、SciPy、Matplotlib、Enided图书馆、熊猫
#  系统操作和维护：操作和维护人员的基本语言
#  金融：定量交易、金融分析，在金融工程领域，Python 不仅使用最多，而且其重要性逐年增加。
#  图形 GUI：PyQT，WXPython，TkInter
# Python 在一些公司的运用有:

#  谷歌：谷歌应用程序引擎，代码。Google.com、 Google 爬虫、Google 广告和其他项目正在广泛使用 Python。
#  CIA：美国中情局网站是用 Python 开发的。
#  NASA：美国航天局广泛使用 Python 进行数据分析和计算。
#  YouTube：世界上最大的视频网站 YouTube 是用 Python 开发的。
#  Dropbox：美国最大的在线云存储网站，全部用 Python 实现，每天处理 10 亿的文件上传和下载。
#  Instagram：美国最大的照片共享社交网站，每天有 3000 多万张照片被共享，所有这些都是用 Python 开发的。
#  Facebook：大量的基本库是通过 Python 实现的
#  Red Hat/Centos：世界上最流行的 Linux 发行版中的 Yum 包管理工具是用 Python 开发的
#  Douban：几乎所有公司的业务都是通过 Python 开发的。
#  知乎：中国最大的 Q＆A 社区，通过 Python 开发（国外 Quora）
# 除此之外，还有搜狐、金山、腾讯、盛大、网易、百度、阿里、淘宝、土豆、新浪、果壳等公司正在使用 Python 来完成各种任务。