class SnapshotArray:

    # O(L) O(L)
    def __init__(self, length: int):
        # snap_id, value
        self.record = [[[0, 0]] for _ in range(length)]
        self.id = 0

    # O(1) O(1)
    def set(self, index: int, val: int) -> None:
        if self.record[index][-1][0] == self.id:
            self.record[index][-1][1] = val
        else:
            self.record[index].append([self.id, val])

    # O(1) O(1)
    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    # O(logN) O(1)
    def get(self, index: int, snap_id: int) -> int:
        idx = self.bisect_left(self.record[index], [snap_id + 1, -float('inf')]) - 1
        return self.record[index][idx][1]

    def bisect_left(self, nums, num):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < num:
                l = m + 1
            else:
                r = m - 1

        return l

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)