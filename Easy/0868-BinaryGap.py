# runtime: 0 ms, beats 100.00%
# returns the biggest distance between two 1s

class Solution:
    def binaryGap(self, n: int) -> int:
        max_dist = 0
        current_dist = 0
        found_first_one = False # prevents from counting dist until the first 1 is found

        # n = 2 * (n // 2) + (n % 2) -> this works for all ints, repeat this until there's no int left
        while n > 0:
            bit = n % 2

            if bit == 1:
                if found_first_one:
                    # compare current and max distances and set max as the biggest one
                    max_dist = max(max_dist, current_dist)

                current_dist = 1
                found_first_one = True
            else:
                if found_first_one:
                    current_dist += 1

            n //= 2

        return max_dist