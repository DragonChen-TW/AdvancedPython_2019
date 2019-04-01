class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # init
        self.ans = []
        self.nums = nums

        # start recurive
        self.recur(0, [])

        return self.ans

    def recur(self, i, token):
        if i == len(self.nums):
            self.ans.append(token)
            return # You'll get infinite loop if you forget it

        # everytime pick up (or not pick up) a item in index i
        # and go next index
        # append answer in the end (line 17)

        self.recur(i + 1, token)
        self.recur(i + 1, token + [self.nums[i]])

if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3]))
