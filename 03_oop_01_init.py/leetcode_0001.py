from typing import List, Set

class Solution:
    def twoSum(self, nums, target):
        # # Solution 1 O(n^2)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # # Solution 2 O(1/2 * n^2)
        # for i in range(len(nums) - 1):
        #     # temp = nums[i]
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Solution 3 O(n)
        ans = {}

        for i in range(len(nums)):
            if nums[i] in ans and (target - nums[i]) in nums:
                return [nums.index(target - nums[i]), i]
            else:
                ans[nums[i]] = True
                ans[target - nums[i]] = True

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9)) # ans=[0,1]
print(s.twoSum([3, 2, 4], 7)) # ans=[0,2]
