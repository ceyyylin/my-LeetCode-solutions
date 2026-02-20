# runtime: 55 ms, beats 72.04% (find a faster solution)
# returns the number of non-empty substrings that have the same number of 0's and 1's and all the 0's and all the 1's in these substrings are grouped consecutively
# uses run-length encoding and state tracking

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0 # total count of valid groups
        prev = 0 # length of the previous group of identical characters
        strk = 1 # length of the current group of identical characters

        # start from 1 because it always does comparison with (i - 1)
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                strk += 1
            else:
                # save the current streak as previous to prev and reset strk
                prev = strk
                strk = 1

            # if current group size is within the previous group's capacity, a valid pair is found
            if strk <= prev:
                res += 1

        return res