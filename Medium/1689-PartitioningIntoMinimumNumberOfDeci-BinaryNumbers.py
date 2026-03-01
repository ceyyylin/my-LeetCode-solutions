# runtime: 15 ms, beats 79.74%
# returns the minimum number of positive deci-binary numbers needed so that they sum up to n

class Solution:
    def minPartitions(self, n: str) -> int:
        # the biggest num in n gives the number of deci-binary numbers needed
        return int(max(n))