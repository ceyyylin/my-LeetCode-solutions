# runtime: 0 ms, beats 100.00%
# calculates the approximate value of sqrt using the number line
# used binary search

class Solution:
    def mySqrt(self, x: int) -> int:
        lowest = 0 # sqrt of a number can't be < 0
        highest = x # creating the number line
        ans = -1  # placeholder (this value will change later, wrote -1 for readability)

        while lowest <= highest:
            middle = (lowest + highest) // 2 # finding the approximate middle point using //
            middle_sq = middle * middle # get the square of the middle

            if middle_sq == x:
                return middle
            elif middle_sq > x:
                highest = middle - 1 # look for smaller, new number line -> 0, middle - 1
            else:
                ans = middle
                lowest = middle + 1 # look for bigger, new number line -> middle + 1, highest

        return ans