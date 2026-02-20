# runtime: 0 ms, beats 100.00%
# calculates the absolute difference between the ASCII values of adjacent characters

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        # using len(s)-1, otherwise it could possibly end up getting a syntax error
        # it uses i and i + 1, if the last char of the string is i, it would throw an error
        for i in range(len(s) - 1):
            # calculate subtraction of ASCII values and get the absolute value
            abs_diff = abs(ord(s[i]) - ord(s[i + 1]))
            # add the result to the score
            score += abs_diff
        return score