class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def searchTree(root,val):
            if root.val == val:
                return root
            elif root == None:
                return None
            elif root.val < val and root.right != None:
                return searchTree(root.right,val)
            elif root.val > val and root.left != None:
                return searchTree(root.left,val)
            else:
                return None
            
        if root:
            return searchTree(root,val)
        else:
            return None
