# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:  
            return False
            
        if sum == root.val and not root.left and not root.right:
            return True
        
        subsum = sum - root.val
        if root.left and self.hasPathSum(root.left, subsum):
            return True
        elif root.right and self.hasPathSum(root.right, subsum):
            return True
        else:
            return False