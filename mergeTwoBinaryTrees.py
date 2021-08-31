class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root1 != None and root2 == None:
            return root1
        elif root1 == None and root2 != None:
            return root2
        elif root1 == None and root2 == None:
            return None
        else:
            temp = TreeNode(root1.val+root2.val)
            print(temp.val)
            temp.left = self.mergeTrees(root1.left,root2.left)
            temp.right = self.mergeTrees(root1.right,root2.right)
            return temp
