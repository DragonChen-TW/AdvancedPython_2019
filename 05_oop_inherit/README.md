# Lesson 05 - 物件導向（三）繼承與多型

## 資訊

- Date: 04/10
- 主題: 物件導向（三）繼承與多型

## 內容

### Python TQC+ 競賽
宣傳個比賽  
https://www.tqcplus.org.tw/python/Index.aspx  
獎金給不少  
http://media.usc.edu.tw/media/1125

### 繼承與多型
#### 基本繼承
繼承與多型是物件導向的一個重要觀念。  

確保你的程式碼有將重複使用的變數、函式包裝成物件後，貪心的攻城獅想到進一步提高效率的方法，因為同類型物件會有類似的部分，包含標籤屬性、部分函式，乾脆進一步把同性質的物件也包裝起來，建立一個最基礎的類別。  

建立基礎類別後，所有子類別都繼承父類別，這些有個性(?)的物件再去詳細的設定他特別的部分，大量減少這些同性質物件的 code 數量。  

e.g. 建立基本類別-動物，貓、狗、小熊維尼各自繼承動物類別，設定自己的函式與屬性

#### 基本多型
多型也是合併的概念，多個類別被輸入到某個 code 內，code 內不論類別為何，都調度同一個介面（例如傳入 obj，統一呼叫 obj.show_result()），讓兩段 code 的接口改成由前半段的 obj 設計，後面只要用固定的方法呼叫即可  

wiki 上的說法蠻完整的，待會看完實際 code 之後，可以再體會一下  

> 指為不同資料類型的實體提供統一的介面。
> 電腦程式執行時，相同的訊息可能會送給多個不同的類別之物件，而系統可依據物件所屬類別，引發對應類別的方法，而有不同的行為。
> 簡單來說，所謂多型意指相同的訊息給予不同的物件會引發不同的動作。

現代的 Python 框架超過一半都會使用繼承與多型（其他語言我只知道 JavaScript 也很完整），例如繼承某個基本類別，編寫不同的邏輯、實現方法，然後調整好介面，用多型給框架呼叫。（很抽象我知道 QQ，我是去年用 Django 寫 case 才頓悟的）

## Zerojudge
- a059 完全數
https://zerojudge.tw/ShowProblem?problemid=a059

- Solution: [There](zerojudge_a059.py)
- Another:  [There](zerojudge_a059_2.py)

## 參考資料
- Object-Oriented Programming (OOP) in Python 3 (RealPython)  
https://realpython.com/python3-object-oriented-programming/
