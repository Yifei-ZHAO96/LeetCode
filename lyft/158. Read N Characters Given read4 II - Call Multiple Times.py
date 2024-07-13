from typing import List

def read4(buf) -> int:
    pass


class Solution:
    def __init__(self):
        # Initialize buffer buf4 as an array of size 4 to store characters read by read4
        self.buf4 = [None] * 4
        # i points to the current position in buf4, size is the number of characters read in the last call to read4
        self.i = self.size = 0

    def read(self, buf: List[str], n: int) -> int:
        j = 0  # j keeps track of the number of characters read so far
        while j < n:
            if self.i == self.size:
                # If the buffer has no available characters, call read4 to read new characters
                self.size = read4(self.buf4)
                self.i = 0  # Reset the position pointer in the buffer
                if self.size == 0:
                    # If read4 reads no characters, it means the end of the file has been reached, exit the loop
                    break
            while j < n and self.i < self.size:
                # Copy characters from buf4 to the target buffer buf one by one
                buf[j] = self.buf4[self.i]
                self.i += 1  # Move the position pointer in buf4 forward
                j += 1  # Move the position pointer in the target buffer buf forward
        return j  # Return the actual number of characters read
