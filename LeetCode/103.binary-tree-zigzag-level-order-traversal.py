#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
# @lc code=end

def sum_of_values(root):
  if root is None:
    return 0
  else:
    return root.val + sum_of_values(root.left) + sum_of_values(root.right)


print(sum_of_values([3,9,20,0,0,15,7]))