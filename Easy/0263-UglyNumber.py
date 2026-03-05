# runtime: 1 ms, beats 30.29%
# returns true if n is an ugly number
# an ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5

class Solution:
    def isUgly(self, n: int) -> bool:
        # an ugly number can't be negative or 0
        if n <= 0:
            return False

        # try dividing the number with the given values until the result is 1, if it fails return False
        while n > 1:
            if n % 5 == 0:
                n //= 5
                continue
            elif n % 3 == 0:
                n //= 3
                continue
            elif n % 2 == 0:
                n //= 2
                continue
            else:
                return False

        return True