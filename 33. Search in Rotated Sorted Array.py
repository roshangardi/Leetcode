# Solution here takes advantage of the solution of similar problem Find minimum in the sorted rotated array,
# similar to current problem. We used that solution and found the smallest element and then used normal binary search
# on the subset of array. First starting for first node till smallest node - 1. And second starting from smallest
# node till the last node. For example in [4, 5, 6, 7, 0, 1, 2]. We found smallest element i.e. 0. Then we did normal
# binary search from 4 to 7 (since now all elements are sorted (4,5,6,7) so binary search is possible) and if target
# not found then we again did normal binary search from 0 to 2.


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        location = self.findmin(nums)
        left = 0
        right = location

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            return left

        left = location + 1
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            return left
        else:
            return -1

    def findmin(self, nums):
        if not nums:
            return
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left - 1


sol = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
print(sol.search(nums, 7))

# Very CLEVER SOLUTION. Read comments to understand

class Solution_two:
    def search_two(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        pivot = nums[0]
        comparator = 0

        while left < right:
            mid = (left + right) // 2

            #  Checking if both target and nums[mid] are on same side.
            if ((nums[mid] > pivot) and (target > pivot)) or ((nums[mid] <= pivot) and (target <= pivot)):
                # Can also be written as: if ((target > nums[0]) == (nums[mid] > nums[0]))
                comparator = nums[mid]
            else:
                if target < pivot:
                    comparator = float("-inf")
                else:
                    comparator = float("inf")

            if comparator < target:
                left = mid + 1
            elif comparator > target:
                right = mid
            else:
                return mid
        return -1

"""
Explanation
Think of the problem in this. We cannot do regular binary search because of the rotation.

Example: nums: [12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7]
Ideally this would have looked as [0, 1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17]
But it is rotated at a pivot number: 12. This is nums[0]. Let's call it pivot number i.e nums[0] for this explanation.
Let's call the left increasing sub sequence as left half(12 to 17) & right increasing subsequence as right half(0 to 7)

HERE'S THE GIST OF THE SOLUTION LOGIC: THE PROBLEM IN NOT BEING ABLE TO DO REGULAR BINARY SEARCH IS: WHEN YOUR MID 
POINT AND TARGET END UP BEING IN DIFFERENT HALVES (ONE IS IN LEFT AND OTHER IN RIGHT OR VICE VERSA). IF THEY ARE BOTH 
IN SAME HALF, IT'S JUST LIKE REGULAR BINARY SEARCH BECAUSE YOU WILL CONVERGE TOWARDS THE TARGET ON THAT STEP OF THE 
BINARY SEARCH. IF YOU ENDED UP IN SEPARATE HALVES, WE CAN CONVERGE TOWARDS THE TARGET BY MAKING IT -INF OR INF LIKE 
SHOWN BELOW. Here's the trick: 

If target is say in the left half, then when searching we need to make the numbers as [12, 13, 14, 15, 16, 17, inf, 
inf, inf, inf, inf, inf, inf, inf] if target is in right half then we need to make it as [-inf, -inf, -inf, -inf, 
-inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7] We don't need to edit the actual array like that, we just need to make the 
comparator number i.e. comparator variable (in regular case, the mid point that we select) to INF or -INF based on which 
side the target is and which side the mid point number is. 

Okay, but we don't need to always use the comparator as -inf or inf. Think of the case when that is possible? That's 
when your target and nums[mid] are on the same half side (left or right half). THis means that your mid point and 
target are on the same half and you are converging towards the target. So then just keep doing regular binary for 
that step and let the comparator be nums[mid]. 

How do we check if they both (nums[mid] and target) are on the same half? We have to check if they are both greater 
than the pivot number or both smaller than pivot number i.e. nums[0] 
if (((nums[mid] > nums[0]) && (target > nums[0])) || ((nums[ mid] <= nums[0]) && (target <= nums[0]))). 
This can also be done as if ((target > nums[0]) == (nums[mid] > nums[0])). 
Ok, so if they both are on the same half let our comparator be nums[mid], because we are converging 
towards the target and are on the same half at the moment of comparision. comparator = nums[mid] proceed with 
comparing how you do regular binary search comparision. But, what if nums[mid] and target are on different halves? 
Then we have to not use the nums[mid] as comparator. We have to use -INF or INF. How can we decide whether to make 
comparator as -INF or INF instead of nums[mid]? 

target and nums[mid] are on different halves. we have to change nums[mid] to -INF or INF. Let's find out which side 
nums[mid] is. If we know which half (left or right) it is in, we know whether to select -INF or INF. Compare target 
to nums[0]. (Why compare target and not nums[mid] because we want to make the numbers on nums[mid] 's side as -INF or 
INF when comparing, not on target's side, so we use target as the reference) if target is greater than nums[0], 
target is on the left half. Look at the example above and you can see this. For example: target is 14, it is greater 
than 12 so it belongs in left half This means that nums[mid] is on the other half: right half. Make comparator as 
INF. if target is less than nums[0], target is on the right half. Look at the example above: For example if target is 
5, it is less than 12 so it belongs in right half This means that nums[mid] is on the other half. left half. make 
comparator as -INF.
Now you can go ahead and do binary search """