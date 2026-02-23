# runtime: 268 ms, beats 42.00%
# returns true if every binary code of length k is a substring of s

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st = set() # gets only the unique chars

        # len(s) - k + 1 to prevent from "index out of bounds"
        for i in range(len(s) - k + 1):
            # using the s[] for slicing
            st.add(s[i: i + k])

        # if length of st is equal to 2^k return True
        return len(st) == 2**k