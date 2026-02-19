# runtime: 3 ms, beats 80.62%
# reads the roman number from right to left and converts it into int

class Solution:
    def romanToInt(self, s: str) -> int:
        # create dict
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0 # will be the output at the end
        prev = 0 # value of the last processed character (right side)
        for char in reversed(s): # reverse the input
            value = roman[char] # get the value from dict

            if value < prev:
                # if value of current is < than previous perform subtraction
                total -= value
            else:
                # if >= perform summation
                total += value

            # store the current as previous to continue comparing
            prev = value

        return total