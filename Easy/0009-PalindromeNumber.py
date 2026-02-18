# runtime: 16 ms, beats 14.26% (need to find a faster algorithm)
# checks if a number is palindrome

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # negative numbers can't be palindrome
            return False
        num = x # store the number
        rev = 0 # store the reversed number
        while num != 0: # repeat until there's no number left
            # shift the number left by 1 (add a 0 to right) and add the last digit of the number
            rev = rev * 10 + num % 10
            # delete the last digit of the number
            num = num // 10

        return rev == x # update the reversed number