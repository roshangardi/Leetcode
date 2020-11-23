# This is a variant of Kadane's Algorithm
# I tried to solve this problem on notebook until it made sense. I also traced this algorithm on notebook using example.

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:    # check the edge case of an empty array
            return 0
        # since the array can contain negative/positive integers
        # at each iteration, the max product could be obtained by
        # multiplying to a previous max or by multiplying prev min
        # (since even number of -ve integers will be a +ve product)
        # or by using the number itself

        local_max = local_min = global_max = nums[0]    # Initialize all values to first element

        for num in nums[1:]:
            prev_localmax = local_max   # Since 'local_max' is getting changed at below line, store it in some variable
            # because it needs to be used to calculate 'local_min'
            local_max = max(num, num * local_max, num * local_min)
            local_min = min(num, num * prev_localmax, num * local_min)
            global_max = max(global_max, local_max)
        return global_max


array_list = [-4, -3, -2]
sol = Solution()
result = sol.maxProduct(array_list)
print(result)

"""
https://medium.com/@aliasav/algorithms-maximum-product-subarray-b09e520b4baf:

Intuition:
This solution is similar to Kadane’s algorithm where we keep track of recent history and compute the latest 
solution in each iteration of the given array. Now since the array can contain positive or negative integers, 
keep in mind that a dynamic programming solution is required since we need to check all combinations and also have a 
‘look-ahead’ capability. We approach this problem bottom-up, such that at each iteration we will have the max 
possible subarray product. Consider this, at each iteration over the numbers array, the max product can be obtained: 
by multiplying nums[i] to a previous max product by multiplying nums[i] to a previous min product (since both these 
numbers might be negative, it’s worthwhile to compute this value) nums[i] might itself be the largest Hence, 
we use 3 variables to keep track of these values at each iteration. local_max = max(n * local_max, n * local_min, 
n) local_min = max(n * local_max, n * local_min, n) # keep in mind to use the previous and not the newly computed 
local max value global_max = max(local_max, global_max) After iterating over all the numbers, we will have computed 
the max product subarray. 

Conclusion: 
A few important concepts we touched: dynamic programming, arrays, Kadan’s algorithm. It takes practice to 
build up an intuition for solving dynamic programming problems. The trick I found is to: 1)master recursion 2)build 
an ability to form recursive solutions of given problems 3)practice top-down and bottom-up ways to solve a DP problem 
4)identify intermediate data structures to be used
"""