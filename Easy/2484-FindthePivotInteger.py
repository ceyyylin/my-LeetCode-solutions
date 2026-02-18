# runtime: 2 ms, beats 69.10% (create a better one asap, the loop slows it down)
# returns the pivot integer x, if no such integer exists, returns -1.

class Solution:
    def pivotInteger(self, n: int) -> int:
        # get all the numbers from 1 to n (n + 1 because python starts counting from 0)
        for x in range(1, n + 1):
            # apply the Gauss' Law to find x
            if (x + 1) * x == (x + n) * (n - x + 1):
                return x
        # if there's no x return -1
        return -1