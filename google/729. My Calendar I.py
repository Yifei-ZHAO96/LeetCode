class MyCalendar:

    def __init__(self):
        self.records = []

    # O(logN + N)
    def book(self, start: int, end: int) -> bool:
        s = self.bisect_right(self.records, start)
        e = self.bisect_left(self.records, end)
    
        if s % 2 == 0 and e % 2 == 0 and s == e:
            self.records[s:e] = [start, end]
            return True
        
        return False

    def bisect_left(self, nums, num):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < num:
                l = m + 1
            else:
                r = m - 1
        
        return l

    def bisect_right(self, nums, num):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] <= num:
                l = m + 1
            else:
                r = m - 1
        
        return l

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)