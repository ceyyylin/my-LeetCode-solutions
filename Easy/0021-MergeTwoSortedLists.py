# runtime: 0 ms, beats 100.00%
# merges two linked lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create nodes with val = 0
        dummy = temp = ListNode(0)
        # make sure none of l1 and l2 are empty
        while list1 != None and list2 != None:
            # compare the values and add the smaller one to the result linked list
            if list1.val < list2.val:
                # connect the pointer of temp to the current node l1
                temp.next = list1
                # move to the next node of l1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            # move to the next node to prevent from overwriting the same spot
            temp = temp.next

        # connect the leftovers to temp after while ends
        temp.next = list1 or list2
        # since the val of dummy is 0, return the actual list using .next
        # not using temp because it's moving while dummy is fixed at the startup
        return dummy.next