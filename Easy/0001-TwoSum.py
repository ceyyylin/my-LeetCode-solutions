# runtime: 0 ms, beats 100.00%
# sums up two numbers to reach the target value and returns the indexes

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # store the numbers seen
        for i in range(len(nums)):
            complement = target - nums[i] # target - known value to find the missing
            if complement in seen: # check if the missing value is stored in the list
                return [seen[complement], i] # return [x,y]

            seen[nums[i]] = i # add the number to the list