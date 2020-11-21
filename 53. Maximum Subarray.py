from typing import List

# Watch: https://www.youtube.com/watch?v=2MmGzdiKR9Y (solved using Kadane's algorithm.)
# Analysis of the problem: https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts
# This problem uses KADANE'S ALGORITHM. (https://www.youtube.com/watch?v=86CQq3pKSUw)
# KADANE'S ALGORITHM is widely used for solving Max Sub array problem.
# This problem also uses the concepts of Dynamic Programming.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
        return max(nums)


array_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sol = Solution()
result = sol.maxSubArray(array_list)
print(result)
