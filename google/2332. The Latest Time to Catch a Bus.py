from typing import List


class Solution:
    # O(NlogN) O(N)
    def latestTimeCatchTheBus(
        self, buses: List[int], passengers: List[int], capacity: int
    ) -> int:
        buses.sort()
        passengers.sort()
        j = 0

        for t in buses:
            c = capacity
            while c and j < len(passengers) and passengers[j] <= t:
                c, j = c - 1, j + 1
        j -= 1

        ans = buses[-1] if c else passengers[j]

        
        while 0 <= j and passengers[j] == ans:
            ans, j = ans - 1, j - 1
            
        return ans


buses = [10,20]
passengers = [2,17,18,19]
capacity = 2
print(Solution().latestTimeCatchTheBus(buses, passengers, capacity))
# Output: 16

buses = [20,30,10]
passengers = [19,13,26,4,25,11,21]
capacity = 2
print(Solution().latestTimeCatchTheBus(buses, passengers, capacity))
# Output: 20



for t in departs:
    k = capacity
    while k and people[j] <= t:
        k -= 1
        j += 1

j -= 1

if k:
    return departs[-1]

while j and 