# runtime: 0 ms, beats 100.00%
# gets the length of the last word of the input

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # .strip() removes the leading and trailing spaces
        # .split() splits the string by any whitespace (spaces, tabs, multiple spaces)
        # [-1] gets the last word
        return len(s.strip().split(' ')[-1])