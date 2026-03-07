# runtime: 3 ms, beats 80.49%
# finds the smallest pair of distinct numbers [x, y] (where x < y) in the given list that have different occurrence frequencies
# returns [-1, -1] if no such pair exists

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        # create a dict
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # sort the keys (given nums)
        unique_nums = sorted(freq.keys())

        n = len(unique_nums)
        # pick x
        for i in range(n):
            # pick y, (i + 1) because x is always smaller than y
            for j in range(i + 1, n):
                x = unique_nums[i]
                y = unique_nums[j]

                if freq[x] != freq[y]:
                    return [x, y]

        return [-1, -1]