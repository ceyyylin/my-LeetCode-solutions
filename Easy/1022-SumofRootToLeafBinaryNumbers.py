# runtime: 0 ms, beats 100.00%
# returns the sum of numbers represented by the path from the root to leaf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if node == None: return 0

            # perform bitwise addition
            # could use | instead of + since << 1 guarantees the least significant bit is 0
            # could use * 2 instead of << 1 but shifting is faster and safer
            current_sum = (current_sum << 1) + node.val

            if node.left == None and node.right == None: return current_sum

            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        # starts from the root and sets the initial value of current_sum to 0
        return dfs(root,0)