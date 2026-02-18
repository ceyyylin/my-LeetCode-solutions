# runtime: 0 ms, beats 100.00%
# returns the pivot integer x, if no such integer exists, returns -1.

class Solution:
    def pivotInteger(self, n: int) -> int:
        # calculate the summation using Gauss' Law
        sum = n * (n + 1) // 2
        # if sqrt of the result is an integer, it's 100% a pivot int
        x = sum ** 0.5
        if x == int(x):
            return int(x)

        return -1