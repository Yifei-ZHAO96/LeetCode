from typing import List


class Solution:
    # O(MN) O(1)
    # checking if all other rows are the same/inverse of the 1st row
    def removeOnes(self, grid: List[List[int]]):
        first_row = grid[0]
        
        def is_row_valid(row, first_row):
            # all the same
            if row == first_row:
                return True
            
            # all are different
            for j in range(len(row)):
                if row[j] == first_row[j]:
                    return False
            
            return True
        
        for i in range(1, len(grid)):
            if not is_row_valid(grid[i], first_row):
                return False

        return True


# 示例输入
grid1 = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]
print(Solution().removeOnes(grid1))  # 输出应为 True


grid = [[1,1,0],[0,0,0],[0,0,0]]
print(Solution().removeOnes(grid))  # 输出应为 False