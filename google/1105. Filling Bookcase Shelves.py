from typing import List

class Solution:
    # O(N** 2) O(N)
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] + [float('inf')] * n # minimum height after placing i books

        for i in range(1, n + 1):
            # assume we opened up a new row for book i - 1
            curr_width = 0
            j = i - 1
            curr_height = 0
            # what if we move previous books one by one to current row, while there's space, will it produce smaller height overall?
            # stop when the row is full, or no more books left
            while j >= 0:
                # put book j into current row & update info
                # curr_width: remaining space in current row after putting in book j                         
                # curr_height: height of the tallest book in current row
                curr_width += books[j][0]
                if curr_width > shelfWidth:
                    break
                curr_height = max(curr_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + curr_height) # suppose j+1 th book is at the final layer
                j -= 1
        
        return dp[-1]
