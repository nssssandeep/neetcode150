# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTreeHelper(self):
        pass

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        stack = [root]
        while stack:
            ele = stack.pop()
            ele.left, ele.right = ele.right, ele.left
            if ele.left: stack.append(ele.left)
            if ele.right: stack.append(ele.right)
        return root
"""
Recursive Solution
        if not root:
            return root
        left = root.left
        right = root.right
        root.left = right
        root.right = left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
"""
