class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
                    
        if root:
            if root.left == None and root.right == None:
                return 1
            else:
                return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)
        else:
            return 0
