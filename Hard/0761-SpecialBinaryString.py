# runtime: 0 ms, beats 100.00%
# recursively splits the string into top-level special substrings, optimizes inner parts,
# then sorts them in descending lexicographical order to construct the largest possible special binary string.

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return ""

        bubbles = []  # store the result
        count = 0  # +1 for 1s, -1 for 0s
        i = 0  # the start of the current part

        for j, char in enumerate(s):
            # count until the value of inner part is 0, then create a new one
            if char == "1":
                count += 1
            else:
                count -= 1
            if count == 0:
                # calls the main function again for bubble (creates the same variables, loops etc.)
                # explanation of s[i+1:j]:
                # i is constant, it's the first index at first and increases later on, depending on our bubbles
                # j increases as the loop continues, representing the current index
                inner_part = self.makeLargestSpecial(s[i + 1: j])
                bubbles.append(f"1{inner_part}0")
                # give i a new value to continue creating bubbles (j+1 not to capture an existing bubble)
                i = j + 1

        # sorts the bubbles from largest to smallest lexicographically
        bubbles.sort(reverse=True)
        # returns the bubbles as a string
        return "".join(bubbles)