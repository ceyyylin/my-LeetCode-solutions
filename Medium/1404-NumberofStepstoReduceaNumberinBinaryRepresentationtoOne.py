# runtime: 3 ms, beats 40.39%
# returns the number of steps to reduce the binary representation of an integer as a string s to 1

class Solution:
    def numSteps(self, s: str) -> int:
        # convert binary to decimal
        number = int(s, 2)
        counter = 0
        # break the loop when the number is equal to 1
        while number != 1:
            # if the number is odd add 1 and count the step
            if number % 2 == 1:
                number += 1
                counter += 1
            # if even perform int division to avoid getting the result as a float and count the step
            else:
                number //= 2
                counter += 1

        return counter