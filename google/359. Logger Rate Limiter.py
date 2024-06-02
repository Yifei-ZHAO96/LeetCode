import heapq


class Logger:
    def __init__(self) -> None:
        self.startTime_map = {}
        self.q_logs = []
    
    # O(1) O(1)
    def start(self, processId: str, startTime: int) -> None:
        self.startTime_map[processId] = startTime
    
    # O(logN) O(1)
    def end(self, processId: str, endTime: int) -> None:
        if processId in self.startTime_map:
            heapq.heappush(self.q_logs,
                (self.startTime_map[processId], processId, endTime))
            del self.startTime_map[processId]
    
    # O(N logN) O(N)
    def print(self) -> None:
        temp = self.q_logs[:]
        
        while temp:
            start, pid, end = heapq.heappop(temp)
            print("{} started at {} and ended at {}".format(
                pid, start, end
            ))

log = Logger()
log.start("1", 100)
log.start("2", 101)
log.end("2", 102)
log.start("3", 103)
log.end("1", 104)
log.end("3", 105)
log.print();