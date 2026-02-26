# runtime: 1 ms, beats 59.33% (could use binary search for a faster algorithm)
# returns the median of the two sorted arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge the arrays and sort
        merged = nums1 + nums2
        merged.sort()

        # get the length of the new list
        n = len(merged)

        # if length is an odd number median is equal to the number in the middle
        if n % 2 == 1:
            # since the question asks for float convert the result into float
            return float(merged[n // 2])
        # if the length is an even number the median is the arithmetic mean of middle left and right nums
        else:
            mid_left = merged[n // 2 - 1]
            mid_right = merged[n // 2]

            return float((mid_left + mid_right) / 2)