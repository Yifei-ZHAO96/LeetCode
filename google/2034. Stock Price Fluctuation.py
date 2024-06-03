import heapq

class StockPrice:

    def __init__(self):
        self.record = {}
        self.min_heap = []
        self.max_heap = []
        self.time = 0

    # O(logN)
    def update(self, timestamp: int, price: int) -> None:
        self.record[timestamp] = price
        self.time = max(self.time, timestamp)
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    # O(1)
    def current(self) -> int:
        return self.record[self.time]

    # O(NlogN)
    def maximum(self) -> int:
        while self.max_heap and self.record[self.max_heap[0][1]] != -self.max_heap[0][0]:
            heapq.heappop(self.max_heap)
        
        return -self.max_heap[0][0]

    # O(NlogN)
    def minimum(self) -> int:
        while self.min_heap and self.record[self.min_heap[0][1]] != self.min_heap[0][0]:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()