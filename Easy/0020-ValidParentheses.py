# runtime: 0 ms, beats 100.00%
# checks if the parentheses are valid and returns True or False depending on that

class Solution:
    def isValid(self, s: str) -> bool:
        # create a dict
        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        # store the chars for LIFO
        stack = []

        for char in s:
            if char in brackets.values():
                # if opening parentheses, add it to the stack
                stack.append(char)
            elif char in brackets:
                # if the stack is empty or the opening and closing parentheses don't match return False
                if not stack or brackets[char] != stack.pop():
                    return False
        # if there's anything left in the stack, return False
        return not stack