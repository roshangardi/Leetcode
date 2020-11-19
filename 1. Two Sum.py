# Extremely simple problem
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):   # This is the crux of the problem.
                if nums[i] + nums[j] == target:
                    return [i, j]

# In the second for loop's condition, j start from i+1 position because there is no need to recalculate
# the addition till ith element since it will be already done by previous iterations.


nums = [11, 15, 2, 7, 6, 4]
target = 9

sol = Solution()
print(sol.twoSum(nums, target))
