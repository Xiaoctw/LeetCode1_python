from 搜索_回溯.TreeNode import TreeNode


class Solution:
    """
    判断一棵树是否为二叉搜索树
    这是自己写的狗屎算法
    """

    def isValidBST(self, root):
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if root.left == None:
            return root.val < self.find_min(root.right) and self.isValidBST(root.right)
        if root.right == None:
            return root.val > self.find_max(root.left) and self.isValidBST(root.left)
        return self.find_max(root.left) < root.val < self.find_min(root.right) and self.isValidBST(
            root.left) and self.isValidBST(root.right)

    def find_min(self, node):
        while node.left != None:
            node = node.left
        return node.val

    def find_max(self, node):
        while node.right != None:
            node = node.right
        return node.val


class Solution1:
    """
    大佬写的算法
    利用了中序遍历的思想,二叉搜索树中序遍历是一个递增的序列
    遍历过程当中前一个肯定回比后一个要大,因此初始化last(上一个)
    为负无穷
    以后出现二叉搜索树首先思考以下中序遍历
    """

    def isValidBST(self, root: 'TreeNode') -> 'bool':
        last = float('-inf')

        def checkValid(root):  # 新的命名方式,不要老用judge了,用check
            nonlocal last  # nonlocal用于在函数内部使用外层非全局变量
            if root is None:
                return True
            if not checkValid(root.left) or last >= root.val:
                return False
            last = root.val
            return checkValid(root.right)

        return checkValid(root)
