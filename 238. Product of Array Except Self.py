from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result_array = [1]
        # result_array[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the result_array[0] would be 1

        for i in range(1, len(nums)):
            # result_array[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            result_array.append(nums[i - 1] * result_array[i - 1])

        # left_right_total contains the product of all the elements to the right
        # Note: for the element at index 'len(nums) - 1', there are no elements to the right,
        # so the left_right_total would be 1
        left_right_total = 1
        for i in reversed(range(len(nums))):    # for i in range(len(nums) - 1, -1, -1), is the traditional way and is
                                                # more flexible because it doesn't restrict you to start only from last
                                                # element but can also start from second last etc.
            # For the index 'i', left_right_total would contain the
            # product of all elements to the right. We update left_right_total accordingly
            result_array[i] = result_array[i] * left_right_total
            left_right_total *= nums[i]

        return result_array


sol = Solution()
# hey = [2, 4, 1]
hey = [1, 2, 3, 4]
print(sol.productExceptSelf(hey))


"""
Thinking process for this problem:
There's only so many tools (DS&A) at your disposal to solve these problems. The trick is recognizing which tool to use. 
Often the instructions/rules of the problem are themselves hints. For example, this one says do it in O(N) time and 
ideally O(1) space. That tells us the optimal runtime is likely O(N), meaning we can rule out any algo that takes longer
than O(N), as well as any algo that runs faster than O(N). It's also effectively telling us we'll have to iterate 
through the entire array some constant number of times, at least once. Even without being told the optimal runtime 
ahead of time, we can still deduce that O(N) is the best we can possibly do since we have to do something for every 
element in the array.

So since we know we have to look at every element, now we have to ask ourselves what useful information can we glean 
during a pass through the array? After all, if we can't loop through the whole array for every element, that means we 
must be able to somehow build the solution for each array element using a partial solution. If we just simply get the 
product for the whole array, we'll notice that we actually get the solution for the last array element in the process. 
That makes sense, it's the last number, so the running product will be the answer for that cell before we multiply it 
by that element's value. And by that logic, if we go backwards through the array, we'll get the first cell's answer too.
Interesting...

What other information do we have after a pass through the array? Well, at every element we have the product of all 
elements before it but not including it. That's awfully similar to the question, isn't it? The only thing we're missing 
is the running product of the numbers after it, but as we just figured out, we can get that information with a second 
pass in the reverse direction. So on the first pass we record the running product for each element, then on the second 
pass do the same in the reverse direction and multiply the two products at that point for the solution. And there's 
our algorithm.
"""

