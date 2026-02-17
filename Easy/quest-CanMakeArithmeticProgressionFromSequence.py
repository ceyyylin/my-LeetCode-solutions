# runtime: 0 ms, beats 100.00%
# checks arithmetic progression of an array
# formula: an = a1 + (n - 1)d
# an for the nth value of the array
# a1 for the first value of the array
# d for the common difference

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        maximum = max(arr)
        minimum = min(arr)
        d = (maximum - minimum) / (n - 1)
        if (maximum - minimum) % (n - 1) != 0: # check if d is an integer
            return False
        if minimum + (n - 1) * d == maximum: # check if the other values have the same common difference
            arr_set = set(arr) # create a set to fasten up
            for i in range(n):
                expected = minimum + i * d
                if not expected in arr_set: # check if the expected value is in our array
                    return False

            return True