class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 這不是最佳解
        # 不過是邏輯較基礎、運用 Python 技巧較少的解法

        # self.direction: 1 right, 2 down, 3 left, 4 up
        self.matrix = [[None for _ in range(n)] for _ in range(n)]
        self.height = n
        self.width = n
        self.dire = 1

        i = j = 0
        for now in range(1, n * n + 1):
            self.matrix[i][j] = now

            temp = self.move(i, j)
            if temp == -1:
                self.dire += 1
                if self.dire == 5:
                    self.dire = 1
                temp = self.move(i, j)

            if now != n * n:
                i, j = temp

        return self.matrix

    def move(self, i, j):
        # 針對每個方向，確認 1. 該方向不會越界 2. 該方向為空格
        if self.dire == 1     and j < self.width - 1 and self.matrix[i][j + 1] == None:
                j += 1
        elif self.dire == 2   and i < self.height - 1 and self.matrix[i + 1][j] == None:
                i += 1
        elif self.dire == 3   and j > 0 and self.matrix[i][j - 1] == None:
                j -= 1
        elif self.dire == 4   and i > 0 and self.matrix[i - 1][j] == None:
                i -= 1
        else:
            return -1

        return (i, j)


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3))
