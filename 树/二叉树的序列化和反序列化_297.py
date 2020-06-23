# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def __init__(self):
        self.idx = 0

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        p = root
        stack, nodes = [], []
        while stack or p:
            if p:
                nodes.append(str(p.val))
                stack.append(p)
                p = p.left
            else:
                nodes.append('None')
                p = stack.pop()
                p = p.right
        nodes.append('None')
        return ' '.join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        list1 = data.split(' ')
        self.idx = 0
        return self.constructTree(list1)

    def constructTree(self, list1):
        if self.idx >= len(list1) or list1[self.idx] == 'None':
            self.idx += 1
            return None
        val = int(list1[self.idx])
        self.idx += 1
        node = TreeNode(val)
        node.left = self.constructTree(list1)
        node.right = self.constructTree(list1)
        return node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__ == '__main__':
    codec = Codec()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    str1 = codec.serialize(node1)
    root = codec.deserialize(str1)
    print(str1)
