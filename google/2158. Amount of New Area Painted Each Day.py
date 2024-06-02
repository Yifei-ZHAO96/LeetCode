import collections
import heapq

class Solution(object):
    # O(N logN) O(N)
    def amountPainted(self, paint):
        """
        :type paint: List[List[int]]
        :rtype: List[int]
        """
        # Dictionary to store start and end points with their corresponding interval indices and flags
        points = collections.defaultdict(list)
        
        # Populate the points dictionary with start and end events
        # O(N) O(N)
        for i, (s, e) in enumerate(paint):
            points[s].append((True, i))  # (True, i) indicates the start of the interval with index i
            points[e].append((False, i))  # (False, i) indicates the end of the interval with index i
        
        # Min-heap to track the currently active intervals
        min_heap = []
        # Lookup array to mark intervals that have ended
        lookup = [False] * len(paint)
        # Result array to store the amount of new area painted for each interval
        result = [0] * len(paint)
        # Variable to keep track of the previous position processed
        prev = -1
        
        # Iterate over each unique position in sorted order
        # O(N logN)
        for pos in sorted(points.keys()):
            # Remove intervals from the heap that have ended
            while min_heap and lookup[min_heap[0]]:
                heapq.heappop(min_heap)
            
            # If there are active intervals, calculate the new painted area
            if min_heap:
                result[min_heap[0]] += pos - prev
            
            # Update the previous position
            prev = pos
            
            # Process each event at the current position
            for t, i in points[pos]:
                if t:
                    # If it's a start event, add the interval index to the heap
                    heapq.heappush(min_heap, i)
                else:
                    # If it's an end event, mark the interval as ended
                    lookup[i] = True
        
        return result

# Test case
paint = [[1, 4], [4, 7], [5, 8]]
solution = Solution()
print(solution.amountPainted(paint))  # Output: [3, 3, 1]