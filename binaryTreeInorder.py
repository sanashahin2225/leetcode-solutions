class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        def inorder(root):
            if root != None:
                inorder(root.left)
                lst.append(root.val)
                inorder(root.right)
                
        inorder(root)
        return lst
