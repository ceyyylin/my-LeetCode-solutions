# runtime: 31 ms, beats 87.74% (find a faster solution)
# precomputes prime set-bit counts as a bitmask for O(1) lookup.

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # since right <= 10^6 (~2^20), a number can have at most 20 set bits
        # precompute prime set-bit counts as a bitmask for O(1) lookup
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        mask = 0
        # build the mask dynamically
        for p in primes:
            # shift 1 to left by p and perform a bitwise OR operation
            mask |= (1 << p)

        count = 0

        for num in range(left, right + 1):
            bit_count = num.bit_count()  # count of 1s in binary
            # shift mask to right by bit_count and perform AND operation with 1
            if (mask >> bit_count) & 1:
                count += 1

        return count