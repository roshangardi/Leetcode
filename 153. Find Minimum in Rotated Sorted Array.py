# Classic binary search problem.
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return

        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        # left and right both converge to the minimum index;
        # DO NOT use left <= right because that would loop forever
        while left < right:
            # find the middle value between the left and right bounds (their average);
            # can equivalently do: mid = left + (right - left) // 2,
            # if we are concerned left + right would cause overflow (which would occur
            # if we are searching a massive array using a language like Java or C that has
            # fixed size integer types)

            mid = (left + right) // 2

            # in normal binary search, we have a target to match exactly,
            # and would have a specific branch for if nums[mid] == target.
            # we do not have a specific target here, so we just have simple if/else.

            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]

            if nums[mid] > nums[right]:
                # we KNOW the pivot must be to the right of the middle:
                # if nums[mid] > nums[right], we KNOW that the
                # pivot/minimum value must have occurred somewhere to the right
                # of mid, which is why the values wrapped around and became smaller.

                # example:  [3,4,5,6,7,8,9,1,2]
                # in the first iteration, when we start with mid index = 4, right index = 9.
                # if nums[mid] > nums[right], we know that at some point to the right of mid,
                # the pivot must have occurred, which is why the values wrapped around
                # so that nums[right] is less then nums[mid]

                # we know that the number at mid is greater than at least
                # one number to the right, so we can use mid + 1 and
                # never consider mid again; we know there is at least
                # one value smaller than it on the right
                left = mid + 1
            else:
                # here, nums[mid] <= nums[right]:
                # we KNOW the pivot must be at mid or to the left of mid:
                # if nums[mid] <= nums[right], we KNOW that the pivot was not encountered
                # to the right of middle, because that means the values would wrap around
                # and become smaller (which is caught in the above if statement).
                # this leaves the possible pivot point to be at index <= mid.

                # example: [8,9,1,2,3,4,5,6,7]
                # in the first iteration, when we start with mid index = 4, right index = 9.
                # if nums[mid] <= nums[right], we know the numbers continued increasing to
                # the right of mid, so they never reached the pivot and wrapped around.
                # therefore, we know the pivot must be at index <= mid.

                # we know that nums[mid] <= nums[right].
                # therefore, we know it is possible for the mid index to store a smaller
                # value than at least one other index in the list (at right), so we do
                # not discard it by doing right = mid - 1. it still might have the minimum value.
                right = mid
                # at this point, left and right converge to a single index (for minimum value) since
                # our if/else forces the bounds of left/right to shrink each iteration:

                # when left bound increases, it does not disqualify a value
                # that could be smaller than something else (we know nums[mid] > nums[right],
                # so nums[right] wins and we ignore mid and everything to the left of mid).

                # when right bound decreases, it also does not disqualify a
                # value that could be smaller than something else (we know nums[mid] <= nums[right],
                # so nums[mid] wins and we keep it for now).

                # so we shrink the left/right bounds to one value,
                # without ever disqualifying a possible minimum
        return nums[left]


sol = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
print(sol.findMin(nums))

"""
Just think of it in general for a binary search, you have an array and you do two steps. First you see if what you're looking at now is the answer. In this case we want to see if start is less than end. Ok now if that's not true then you go on to the second step, which is to divide the array into two parts. From start to mid, and mid + 1 to end. Now you chose which side of the array brings your closer to the solution and go back to step 1.

The point is, if we do as you say, which is to say end = mid - 1, then you are always leaving out an element when you divide the array in half. So therefore you aren't dividing it into two contiguous halves.

Here's an example to prove the point.
Line 1 [4, 7, 8, 9, 13, 14, 18, 1, 2, 3]
Line 2 [4, 7, 8, 9, 13] [14, 18, 1, 2, 3]
Line 3 [14, 18, 1, 2, 3]
Line 4[14, 18 , 1]
Line 5 [18, 1]
Line 6 [1]
Line 7 return start (1)

If we had said end = mid - 1, then line 4 would have excluded the 1, which is the answer.
"""
