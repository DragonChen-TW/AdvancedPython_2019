class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # # v1.1 72ms
        # colors = [0, 0, 0] # count 0's, 1's, 2's
        # for n in nums:
        #     colors[n] += 1
        # now = 0
        # for i, count in enumerate(colors):
        #     for _ in range(count):
        #         nums[now] = i
        #         now += 1

        # # v1.2 52ms
        # colors = [0, 0, 0] # count 0's, 1's, 2's
        # for n in nums:
        #     colors[n] += 1
        # now = 0
        # for i, count in enumerate(colors):
        #     nums[now:now + count] = [i] * count
        #     now += count

        # v2 56 ms
        l = len(nums)
        ans = [1] * l
        i0, i2 = 0, 0

        for n in nums:
            if n == 0:
                i0 += 1
            elif n == 2:
                i2 += 1

        ans[:i0] = [0] * i0
        if i2:
            ans[-i2:] = [2] * i2

        nums[:] = ans[:]

        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.sortColors([2,0,2,1,1,0]))
    print(s.sortColors([0, 0]))
