# runtime: 0 ms, beats 100.00%
# returns true if s contains at most one contiguous segment of ones

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # 01 could stand for both leading zeros and a second segment, for example:
        # 0011 and 101101 -> both contain "01" so only checking this
        return "01" not in s