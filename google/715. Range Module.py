def bisect_left(nums, num):
    """
    bisect_left returns the index where x should be inserted in a such that 
    all elements before that index are less than x, and all elements after that 
    index are greater than or equal to x.
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] >= num:
            r = m - 1
        else:
            l = m + 1
    
    return l


def bisect_right(nums, num):
    """
        bisect_right returns the index where x should be inserted in a such that
        all elements before that index are less than or equal to x, and all 
        elements after that index are greater than x.
    """
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] <= num:
            l = m + 1
        else:
            r = m - 1
    
    return l

# example to test bisect
# nums = [0, 1, 2, 2, 2, 2, 4]
# num = 2
# print(bisect_left(nums, num))
# print(bisect_right(nums, num))


class RangeModule:

    def __init__(self):
        # Initialize an empty list to track the range boundaries
        self.tracker = []

    def addRange(self, left: int, right: int) -> None:
        # Find the position to insert the start of the new range
        start = self.bisect_left(self.tracker, left)
        # Find the position to insert the end of the new range
        end = self.bisect_right(self.tracker, right)

        # Prepare the subtrack to replace the range
        subtrack = []
        # If start is even, it means the new range starts outside an existing range
        if start % 2 == 0:
            subtrack.append(left)
        # If end is even, it means the new range ends outside an existing range
        if end % 2 == 0:
            subtrack.append(right)
        
        # Replace the range in tracker with the new subtrack
        # This effectively merges overlapping ranges or adds new ranges
        self.tracker[start: end] = subtrack

    def queryRange(self, left: int, right: int) -> bool:
        # Find the position where the left boundary would fit
        start = self.bisect_right(self.tracker, left)
        # Find the position where the right boundary would fit
        end = self.bisect_left(self.tracker, right)

        # Check if both boundaries fit within the same range
        # and if start is odd, indicating that the range is within an existing range
        return start == end and start % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        # Find the position to insert the start of the range to remove
        start = self.bisect_left(self.tracker, left)
        # Find the position to insert the end of the range to remove
        end = self.bisect_right(self.tracker, right)

        # Prepare the subtrack to replace the range
        subtrack = []
        # If start is odd, it means the range starts within an existing range
        if start % 2 == 1:
            subtrack.append(left)
        # If end is odd, it means the range ends within an existing range
        if end % 2 == 1:
            subtrack.append(right)
        
        # Replace the range in tracker with the new subtrack
        # This effectively removes the specified range
        self.tracker[start: end] = subtrack