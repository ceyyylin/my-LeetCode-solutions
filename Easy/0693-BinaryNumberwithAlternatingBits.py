# runtime: 0 ms, beats 100.00%
# checks whether the given int has alternating bits

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1) # shift right by 1 bit and perform XOR
        # if the 1s align perfectly the & will be 0
        return x & (x + 1) == 0