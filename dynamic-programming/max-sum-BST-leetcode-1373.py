# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def remove_none(arr):
    return [x for x in arr if x is not None]


class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = 0

        def is_bst(node):
            if node is None:
                return True, None, None, 0
            
            is_bst_l, min_l, max_l, sum_l = is_bst(node.left)
            is_bst_r, min_r, max_r, sum_r = is_bst(node.right)
            
            is_bst_node = (is_bst_l and is_bst_r and 
                    (max_l is None or node.val > max_l) and 
                    (min_r is None or node.val < min_r))
            if is_bst_node:
                total_sum = node.val + sum_l + sum_r
                self.max_sum = max(self.max_sum, total_sum)
            else:
                total_sum = 0

            min_key = min(remove_none([min_l, node.val, min_r]))
            max_key = max(remove_none([max_l, node.val, max_r]))
                
            return is_bst_node, min_key, max_key, total_sum
        
        is_bst(root)
        return self.max_sum
