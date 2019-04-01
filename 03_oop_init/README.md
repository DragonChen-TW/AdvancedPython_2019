# Lesson 03 - 物件導向（一）初始化

## 資訊

- Date: 03/20
- 主題: 物件導向（一）初始化

## 內容

<!-- TOC -->
- [物件導向是什麼？](#%E7%89%A9%E4%BB%B6%E5%B0%8E%E5%90%91%E6%98%AF%E4%BB%80%E9%BA%BC)
- [LeetCode](#leetcode)
  - [解題要點](#%E8%A7%A3%E9%A1%8C%E8%A6%81%E9%BB%9E)
- [Homework](#homework)
  - [Stack(Linked-list)](#stacklinked-list)
<!-- /TOC -->

### 物件導向是什麼？

什麼是物件導向？中文全稱是「物件導向程式設計」，英文叫做 Object-Oriented Programming（簡稱 OOP）

不過中文翻譯裡「Programming」的語意比較弱，**我會稱他為「物件導向程式設計法」或「物件導向設計法」，重點在於，OOP 是一種程式設計的思維與方法**

程式設計經歷過許多演進，語言、效率還有設計思維都有許多的變動，設計思維大概經歷過三個世代：
1. 指令式程式設計（組合語言） Imperative programming
定義清楚每個動作的資料處理與狀態，每個呼叫都對應到一個動作
2. 程序式程式設計 （C 語言） Procedural programming
用函式來切割一個程式，定義清楚輸入、格式、計算流程，之後透過呼叫函式的方法來編寫程式
3. 物件導向程式設計（Python、C++） Object-Oriented programming
用物件當作一個單位，裡面放入函式與資料，物件裡的函式可以存取及修改物件內的資料

此外還有一種函數式程式設計（Functional programming，如：R 語言、Haskell），概念是使用 Immutable Data、Pure Function 來串接、設計程式，也有一定的使用量。

雖然物件導向的說明有點少，不過後面我們會慢慢看到

### LeetCode

LeetCode 0001
https://leetcode.com/problems/two-sum/
- Script: [there](leetcode_0001.py)

#### 解題要點
1. O(n^2) 基礎解法
2. O(1/2 * n^2) 剪枝、降低係數
3. O(n) 改進資料結構，大幅提升演算法
dict、set 利用 hash 儲存資料  
使用 in 運算子時，時間複雜度只需要 O(1)  

### Homework
#### Stack(Linked-list)

利用 Linked-list 改寫 [OOP_02.py](OOP_02.py) 的 Stack

實現 push、pop、is_empty
[hw1.py](hw1.py)內有提供 Node class（linked-list 的最小單位）、print_linked_list
