# runtime: 3 ms, beats 87.88%
# converts given decimals into binary and sorts them by the number of 1s

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # sorted(arr, ...) gets the numbers in arr and returns a new sorted list
        # key defines a custom sorting criterion
        # lambda is a practical function, names all the numbers x one by one and performs the key formula
        # x.bit_count() is the priority, this counts the number of 1s in x
        # the x [x.bit_count(), x] is used when two or more numbers have the same amount of 1s
        # so when the amount of 1s are equal, they get sorted from smallest to largest
        return sorted(arr, key = lambda x: [x.bit_count(), x])