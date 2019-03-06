# Lesson 01 - 簡介與基礎

<!-- TOC -->

- [資訊](#%E8%B3%87%E8%A8%8A)
- [內容](#%E5%85%A7%E5%AE%B9)
	- [介紹](#%E4%BB%8B%E7%B4%B9)
	- [環境](#%E7%92%B0%E5%A2%83)
		- [Atom](#atom)

<!-- /TOC -->

## 資訊

- Date: 03/06
- 主題: Python 現況、Python技巧、pip 教學

## 內容

### 介紹

從 TIOBE index 排名或資訊公司的職缺來看，Python 是近期非常受歡迎的程式語言之一，尤其是在以合作為基礎的開源社群中（另一個新星是 Javascript）

儘管如此，台灣仍是老牌的 JAVA、C/C++ 為主，資訊科系也很少談到這個新崛起的語言

![2019_03_tiobe_index](/images/2019_03_tiobe_index.png)

特別是在深度學習領域中，Python 目前扮演了無可取代的角色，著名的框架如 Tensorflow、Kersa、PyTorch，都是默認甚至唯一支援 Python 語言的。學校教得不多（甚至不會教），出社會又用得到怎麼辦？

**想進一步知道有關 Python 用途，可以[看看我的文章](https://www.smalldragon.tw/python37-0-5-locate/)**

接著要談到這門課，這堂課的目的是什麼？因為 Python 的快速崛起，很多人都學過課，卻沒有了後續，遇到不限語言的作業、只支援 Python 的套件時，卻發現 Python 沒有想像中簡單，要用好它有很多的訣竅

這堂課希望能培養學生以 Python 為主要開發語言，熟悉 Python、習慣 Python，**了解開發技巧、Python 技巧，還有相當重要的開源社群，目的成為專業的 Python 開發者、軟體工程師**


### 環境

#### Atom

相較 Java，沒有對特定 IDE 的強烈需要，相較 R 語言，沒有像是 R studio 大多數人使用的最佳解，Python 可以選擇任意 IDE、Text Editor

我個人偏好使用 Atom，~~不推薦使用 Sublime Text~~，Atom 是一款開源軟體由 Github 維護，用 Electron 開發的編輯器。你也可以選擇 VS code、PyCharm 甚至是 Jupyter 來開發

![Atom Offical Website](/images/atom_offical.png)

Atom 在官網有各個平台的下載點
https://atom.io

詳細教學後面課程會慢慢介紹

#### Python 和 pip

不論是哪種方法寫程式，都是透過 command line 執行，接著要安裝主角 Python 和 套件管理器 pip

2.x.x 和 3.x.x 是 Python 的兩個大版本（沒有 Python1，放心），但兩者差別不小，現在開發者預設使用 Python3，有非常特別的目的才會考慮 Python2

**有興趣可以[看看我有關py2和py3的文章](https://www.smalldragon.tw/python37-0-intro/)**

現在 Python2 最新版本: 2.7.16（已停止更新功能，2020停止支援）
現在 Python3 最新版本: 3.7.2

##### Mac or Linux
~~如果你是 mac 或是 linux 系統，其實你的電腦裡面已經內建 Python，不過我們要使用的是Python3所以還是需要下載安裝

[Python 3.7.2下載](https://www.python.org/downloads/release/python-372/)
<img src="/images/Python3.7.2_download.png" style="width:70%;margin: 0 15%;">

拉到最下面

![](https://i.imgur.com/RGChKbT.png)

挑你Mac OS版本符合的下載

點點點就裝好了（懶）

##### Windows
一樣這裡，[Python 3.7.2下載](https://www.python.org/downloads/release/python-372/)

最下面

![](https://i.imgur.com/eaosboF.png)

x64系統載上面那三個其中一個，x32系統載下面那三個其中一個

![](https://i.imgur.com/TwdiIBV.png)

勾選 Install Now 然後一直下一步
<font color="red">記得「Add Python 3.6 to PATH」一定要勾起來</font>
現在好像沒有這個選項了？

##### 確認

安裝完之後，在terminal（Mac or Linux）或是在 cmd（Windows）輸入

```shell
python3 --version
```
會看到它顯示版本號碼，類似這樣的畫面

![](https://i.imgur.com/g1wlSnS.png)


恭喜！你的 Python 已經安裝成功了！




2019 Advanced Python course  in NSYSU mis by Small Dragon Chen
