# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_path(node):
            # nonlocal to access the diameter when doing recursion
            nonlocal diameter
            # if no child
            if not node:
                return 0

            # calculate the longest path for left and right
            left_longest = longest_path(node.left)
            right_longest = longest_path(node.right)

            # check if its bigger than diameter
            diameter = max(diameter, left_longest + right_longest)

            # add the edge to parent while returning
            return max(left_longest, right_longest) + 1

        # do post-tree traversal
        longest_path(root)
        return diameter
