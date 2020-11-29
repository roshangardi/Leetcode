from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))  # Here (right-left) is width
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


sol = Solution()
nums = [1,2,100,1,1,1,1,1,2]
print(sol.maxArea(nums))

# Important concept or trick to understand in this algorithm is why we are incrementing the shorter line and not the
# larger one. I found a lot of the discussion and proof about this quite opaque, but one thing helped it finally
# clicked for me (which is sort of proof by contradiction i guess)
# You have two heights H_left and H_right, and H_right < H_left, then we know we have two choices, we want to move
# one of them. If we move the larger one, we cannot increase the height for the simple reason that we are always
# limited by the shortest, and we would be decreasing j-i, the width as well.
# To clarify: let's say we kept the shortest forever, what would happen? Well, j-i would decrease, and either we come
# across a taller block, which doesn't matter because our shorter one we kept only mattered, or we find a shorter
# one, in which case that one matters.
# Either way we end up with a smaller area, so we must move the shorter one because moving the larger one cannot give
# an increase in area.
# You only move the index inwards for the shorter height because:
# As we are decreasing the width by moving inwards, to counter that for getting a possibly larger area:
# we would need to increase the minimum of the height of the new left and right walls we consider.
# For a better minimum, we move away from the current minimum.
