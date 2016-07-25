# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
    	res = []
    	if root:
    		children = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
    		if children:
    			res.extend(map(lambda x: str(root.val) + "->" + x, children))
    		else:
    			res.append(str(root.val))
    	return res
        