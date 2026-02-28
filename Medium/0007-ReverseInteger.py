# runtime: 41 ms, beats 78.41%
# returns the reversed version of the given integer

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            # getting the absolute val and putting the "-" front of the reversed number to keep it negative
            result = int("-" + str(abs(x))[::-1])
            # only checking if the number is bigger than the smallest value given since it can't be positive
            if result < -2 ** 31:
                return 0
        else:
            result = int(str(x)[::-1])
            # only checking if the number is smaller than the biggest value given since it can't be negative
            if result > (2 ** 31) - 1:
                return 0

        return result