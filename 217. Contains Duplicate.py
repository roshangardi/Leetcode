from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = set()
        for num in nums:
            if num in distinct:
                return True
            else:
                distinct.add(num)
        return False

    """ Most pythonic solution would be as follows:
    But be cautious since interviewer might be looking for different/harder way of solving the problem.

    def containsDuplicate(self, nums: List[int]) -> bool:
        len_array = len(nums)
        new_len_array = len(set(nums))
        return len_array != new_len_array
    """


sol = Solution()
list_with_duplicates = [7, 1, 5, 3, 6, 4, 4]
print(sol.containsDuplicate(list_with_duplicates))
