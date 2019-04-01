# Lesson 03 - 物件導向（二）Magic Method

## 資訊

- Date: 03/27
- 主題: 物件導向（二）Magic Method

## 內容

<!-- TOC -->
- [Homework 解析](#homework-%E8%A7%A3%E6%9E%90)
  - [Stack(Linked-list)](#stacklinked-list)
- [LeetCode](#leetcode)
  - [題目](#%E9%A1%8C%E7%9B%AE)
  - [解題重點](#%E8%A7%A3%E9%A1%8C%E9%87%8D%E9%BB%9E)
  - [參考解答](#%E5%8F%83%E8%80%83%E8%A7%A3%E7%AD%94)
- [Magic Method](#magic-method)
<!-- /TOC -->

### Homework 解析
#### Stack(Linked-list)
**解題要點**：
- 考慮題目在選用資料結構中的狀態，確保不會出錯（Line 21 預防了非法存取 self.head）
- 總是確認初始化、過程、終止條件，以防任何例外（Line 30）

### LeetCode
#### 題目
- 基礎題  
LeetCode 0059 Spiral Matrix II  
https://leetcode.com/problems/spiral-matrix-ii/  
LeetCode 0075 Sort Color  
https://leetcode.com/problems/sort-colors/  

- 小組討論  
LeetCode 0078（Recursive）  
https://leetcode.com/problems/subsets/  
LeetCode 0020（Stack）  
https://leetcode.com/problems/valid-parentheses/  
LeetCode 0021（Linked List）  
https://leetcode.com/problems/merge-two-sorted-lists/

#### 解題重點
- 0059 Spiral Matrix II  
如何初始二維陣列?  
可以用 list coprehension `[[None for _ in range(n)] for _ in range(n)]`
- 0075 Sort Color  
只能用 in-place 修改，如何最快？  
Python 的 `arr[0:3] = [3, 4, 5]` 是記憶體區間取代，算是比較快速的方法
- 0078 Subsets  
這類問題通常能用遞迴、DP（Dynamic Programming 動態規劃）解決  
這邊選用遞迴，因為高中數學有這類排列組合  
我們知道，所有的可能性為 [每個位置取數字 or not] ** [位置數]  
用遞迴寫出來，完成
- 0020 Valid Parentheses  
用 Stack 存前半段的括號，遇到後半段括號時，從 Stack pop 出來比較是否是一對  
額外還有幾個例外狀況，在 code 裡面都有列出來
- 0021 Merge Two Sorted Lists  
思考最慢方法 >> 合併兩個 list，再做一次 sort >> O(N logN)  
因為是「已排序陣列」，所以比較兩個 list 的所有元素，按照大小塞到新陣列 >> O(N)

#### 參考解答
- [0059 Spiral Matrix II](leet_code/0059.py)
- [0075 Sort Color](leet_code/0075.py)
- [0078 Subsets](leet_code/0078.py)
- [0020 Valid Parentheses](leet_code/0020.py)
- [0021 Merge Two Sorted Lists](leet_code/0021.py)

### Magic Method
Magic Method（中文翻為魔術方法）是一類特別的功能，很多是跳脫普通程式邏輯，Python 獨特的方法  

Magic Method 在物件導向中更是如虎添翼，透過命名為 Magic Method，Python 會自動偵測你對預設功能做出的調整，幫你綁定上去，例如設定`__add__`，你的物件就能調整 + 的操作方法

**參考資料**
- A Guide to Python's Magic Methods  
https://rszalski.github.io/magicmethods/
