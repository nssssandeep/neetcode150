# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        max_dep = 0
        while stack:
            node, depth = stack.pop()
            max_dep = max(max_dep, depth)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        return max_dep
        #return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
        
