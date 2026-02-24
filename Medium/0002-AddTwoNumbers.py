# runtime: 6 ms, beats 29.81% (learn carry asap)
# add the two numbers and returns the sum as a linked list using brute force

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # convert the values into array until l1 turns None
        val1 = []
        current1 = l1
        while current1:
            val1.append(current1.val)
            current1 = current1.next

        # reversing the array to get the correct result when summing up
        num_str1 = ""
        for digits in reversed(val1):
            num_str1 += str(digits)

        # convert into int for summation
        num1 = int(num_str1)

        val2 = []
        current2 = l2
        while current2:
            val2.append(current2.val)
            current2 = current2.next

        num_str2 = ""
        for digits in reversed(val2):
            num_str2 += str(digits)

        num2 = int(num_str2)

        sum_all = num1 + num2

        # convert the result into linked list
        dummy = ListNode(0)
        new_current = dummy
        # reverse the summation so the linked list has the order needed
        for digit in str(sum_all)[::-1]:
            new_current.next = ListNode(int(digit))
            new_current = new_current.next

        return dummy.next