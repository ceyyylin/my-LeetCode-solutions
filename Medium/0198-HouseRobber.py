# runtime: 0 ms, beats 100.00%
# returns the maximum amount of money that could be robbed

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0

        for num in nums:
            # comparing prev1 and (prev2 + num) guarantees that the police won't be alerted
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current

        return prev1