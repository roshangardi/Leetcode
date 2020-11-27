from typing import List
import timeit

# Brute Force Solution with O(n^2) complexity. Not optimal solution BUT NECESSARY to understand because it's used by
# further COMPLEX problems like 3sum and 4sum:
"""
# Optimal solution for such problems is O(n) linear time

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):   # This is the crux of the problem.
                if nums[i] + nums[j] == target:
                    return [i, j]

# In the second for loop's condition, j start from i+1 position because there is no need to recalculate
# the addition till ith element since it will be already done by previous iterations.
"""
# Tip: We are using above brute force solution in 3sum & 4sum problem with a little extension of the logic.

# For bringing above solution in linear time, make use of HASHMAP/Dictionary(uses little extra space but that's okay)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage_dict = {}

        for i in range(len(nums)):
            complement = target - nums[i]  # Find complement and see if complement is present in dictionary.
            if complement in storage_dict:
                return [storage_dict[complement], i]
            storage_dict[nums[i]] = i
        return []  # If list is traversed completed and no complement found then return empty list.

# Un-comment the below code to check how much time the dictionary code is taking:

# def test():
#     nums = [11, 15, 2, 7, 6, 4]
#     target = 11
#     sol = Solution()
#
# if __name__ == '__main__':
#     import timeit
#     print(timeit.timeit("test()", setup="from __main__ import test"))


nums = [11, 15, 2, 7, 6, 4]
target = 11
sol = Solution()
print(sol.twoSum(nums, target))
