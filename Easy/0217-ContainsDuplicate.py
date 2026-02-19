# runtime: 7 ms, beats 88.38%
# checks the array and returns true if 1 or more ints repeat
# return len(set(nums)) != len(nums) used daily but it could be risky for LeetCode
# set() saves the num only once, if there's repetition, it'll be smaller than the length of the array

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                # if a num is seen twice, immediately return true
                return True
            seen.add(num)
        return False