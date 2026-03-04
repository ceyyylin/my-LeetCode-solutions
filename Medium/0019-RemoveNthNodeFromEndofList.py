# runtime: 0 ms, beats 100.00%
# removes the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # reverse the list
    def reverseList(self, head):
        curr = head
        prev = None

        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev

    # remove the nth node from the end
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use the reversed list for head
        head = self.reverseList(head)
        curr = head
        prev = None

        if n == 1:
            head = head.next
        else:
            # both range(1, n) and (n - 1) are correct, could use any of them
            for i in range(1, n):
                prev = curr
                curr = curr.next

            prev.next = curr.next

        # reverse the list once more
        return self.reverseList(head)