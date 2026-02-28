# runtime: 584 ms, beats 86.79%
# returns the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, mod (10**9 + 7)

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = 0
        for i in range(1, n + 1):
            # get the binary lengths from 1 to n and add the binary representation of i, then perform modulo
            bits = i.bit_length()
            result = ((result << bits) + i) % (10**9 + 7)

        return result