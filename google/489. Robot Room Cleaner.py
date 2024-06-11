# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot:
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """
       pass

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
       pass

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
       pass

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """
       pass


class Solution:
    def cleanRoom(self, robot: Robot):
        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def dfs(x, y, d):
            seen.add((x, y))
            
            for i in range(4):
                nd = (d + i) % 4
                nx = x + dirs[nd][0]
                ny = y + dirs[nd][1]
                
                if (nx, ny) not in seen and robot.move():
                    dfs(nx, ny, nd)
                    goBack()
            
                robot.turnRight()

        
        seen = set()
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        dfs(0, 0, 0)