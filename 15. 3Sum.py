# Solution to this problem is similar to brute force approach from Two-sum problem. Understand the algorithm of
# Two-sum problem and then check below code. We can then understand how the original creator must have come up with
# this solution. Understanding thinking process is necessary.

# The idea is to sort an input array and then run through all indices of a possible first element of a triplet. For
# each possible first element we make a standard bi-directional 2Sum sweep of the remaining part of the array. Also
# we want to skip equal elements to avoid duplicates in the answer without making a set. The basic idea is whether
# its 3sum or 4sum we try to reduce the problem to a 2sum problem. For 2sum problem we apply a 2 pointers (left &
# right) approach and solve it. This solution is O(n*n) time.

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the numbers, since we are using left and right pointers, left pointing to start and right pointing to
        # the end element and if the addition of numbers is GREATER than zero then we will decrement right pointer
        # because last pointer is pointing to biggest number and decrementing it will point to second biggest number
        # and we will get closer to zero. Repeat this till we get zero. Note: Since this problem is not focused
        # towards how you are sorting, hence using the inbuilt function, else would have implemented mergesort/quicksort

        result = []
        nums.sort()

        length = len(nums)
        # To avoid the out of range error and also since we want 3 numbers in total,
        # so we won't calculate sum when only 2 or 1 number is remaining. Hence length-2
        for i in range(length - 2):
            # Small but important trick to improve performance: Since we SORTED the list, hence if the first number
            # itself is greater than zero that is nums[i] > 0, then break because, In sorted list, if first number is
            # positive, remaining numbers will also always be positive, which means it will never have sum of zero,
            # due to the missing negative numbers in the array. So in such cases use the technique called 'Early Exit'

            if nums[i] > 0:
                break
            # If Condition to avoid duplicates except at index zero since we wont have i-1 at first position.
            if i == 0 or nums[i] != nums[i - 1]:
                left = i + 1
                right = length - 1
                complement = 0 - nums[i]  # We learned complement in 2 sum problem

                while left < right:
                    if nums[left] + nums[right] == complement:  # If addition of triplet is EQUAL TO ZERO
                        result.append([nums[i], nums[left], nums[right]])
                        # Now after adding the triplet, we again need to check whether the next numbers are duplicate of
                        # current number, if yes we need to skip them hence the following while loops. And this needs to
                        # be done from both sides, left and right.

                        while left < right and nums[left] == nums[left + 1]: left += 1
                        while left < right and nums[right] == nums[right - 1]: right -= 1

                        # Finally we need to move the pointers ahead from both sides, so increment them.
                        left += 1
                        right -= 1

                    # If addition is LESS THAN ZERO, than increment left, because since array is sorted, incremented
                    # node will be greater than the current node and hence will get closer to ZERO
                    elif nums[left] + nums[right] < complement:
                        left += 1

                    # If addition is GREATER THAN ZERO, than decrement right, because since array is sorted, decremented
                    # node will be less than the current node and hence will get closer to ZERO
                    else:  # nums[left] + nums[right] > complement:
                        right -= 1

        return result


sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(sol.threeSum(nums))
