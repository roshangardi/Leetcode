# Implement Quicksort for lists/arrays
# Algo from: https://www.youtube.com/watch?v=7h1s2SojIRw&t=431s&ab_channel=AbdulBari
# also read, https://github.com/lkesteloot/qsort/blob/master/qsort.py
# Uncomment all the "print" functions to see more data.

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, low, high):
        initial_low = low
        initial_high = high
        # print("Initial low and high values are Low:{} High:{}".format(initial_low, initial_high))
        # Pivot should be median/centre value of the list or atleast random value rather than the first elem of the list
        pivot = self.mainlist[low]  # In this case, pivot is the first element, not efficient in case of
                                    # already sorted list, and can lead to O(n^2) time complexity
        while low < high:
            while True:
                if low >= initial_high: # Should not increment low beyond the actual high value, else index out of range
                    break
                if mainlist[low] <= pivot:  # Left of pivot is smaller than pivot, so increment low else break.
                    low += 1
                else:
                    break
            # print(low, high)
            while True:
                if high <= initial_low: # Should not decrement high beyond the actual low value, else index out of range
                    break
                if mainlist[high] >= pivot: # Right of pivot is greater than pivot, so increment high else break.
                    high -= 1
                else:
                    break

            # print("Current Low and high values are Low:{} High:{}".format(low, high))
            if low < high:  # After Increment/Decrement if low&high didn't intersect yet, then swap
                # print("Yes Low is less than High")
                self.mainlist[low], self.mainlist[high] = self.mainlist[high], self.mainlist[low]
        # print("Before Swapping: Low:{} High:{}".format(self.mainlist[initial_low], self.mainlist[high]))
        self.mainlist[initial_low], self.mainlist[high] = self.mainlist[high], self.mainlist[initial_low] # Finally swap the pivot with the high
        # print("After Swapping: Low:{} High:{}".format(self.mainlist[initial_low], self.mainlist[high]))
        # print()
        return high

    def quicksortutil(self, low, high):
        if low < high:
            newhigh = self.partition(low, high)
            self.quicksortutil(low, newhigh)    # Till newhigh, because it now acts as an maxvalue for the 'low'.
            self.quicksortutil(newhigh + 1, high)

    def quicksort(self, mainlist):
        if len(mainlist) < 2:   # If mainlist contain only one element than return that element | Base Case.
            return mainlist

        self.mainlist = mainlist
        self.mainlist.append(float('inf'))  # Required to stop the 'low' from incrementing infinitely

        low, high = 0, len(self.mainlist) - 1   # Initially low is pointing to first ele and high to last elem.
        self.quicksortutil(low, high)

        return self.mainlist[:len(mainlist) - 1]    # Returning main list without the "inf" value


if __name__ == "__main__":

    mainlist = [33, 12, 99, 67, 87, 44]
    # mainlist = [5,4,3,2,1]
    # mainlist = [45, 2]
    sol = Solution()
    solnode = sol.quicksort(mainlist)

    for num in solnode:
        print(num)
