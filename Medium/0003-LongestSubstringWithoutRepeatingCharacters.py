# runtime: 1183 ms, beats 5.02% (learn sliding window method asap)
# find the length of the longest substring without duplicate characters using brute force

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_val = 0

        # checks the longest substring for each char and updates the max value
        for i in range(len(s)):
            seen = []
            counter = 0

            for j in range(i, len(s)):
                char = s[j]

                if char not in seen:
                    seen.append(char)
                    counter += 1
                else:
                    break

            if counter > max_val:
                max_val = counter

        return max_val