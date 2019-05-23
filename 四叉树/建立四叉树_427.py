class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    """
    建立一颗四叉树
    """
    def construct(self, grid):
        def make_tree(beg1, end1, beg2, end2):
            if beg1 == end1:
                node = Node(grid[beg1][beg2] == 1, True, None, None, None, None)
                return node
            else:
                node1 = make_tree(beg1, beg1 + (end1 - beg1) // 2, beg2, (end2 - beg2) // 2 + beg2)
                node2 = make_tree(beg1, beg1 + (end1 - beg1) // 2, (end2 - beg2) // 2 + 1 + beg2, end2)
                node3 = make_tree(beg1 + (end1 - beg1) // 2 + 1, end1, beg2, (end2 - beg2) // 2 + beg2)
                node4 = make_tree(beg1 + (end1 - beg1) // 2 + 1, end1, (end2 - beg2) // 2 + 1 + beg2, end2)
                if node1.isLeaf and node2.isLeaf and node3.isLeaf and node4.isLeaf and node1.val == node2.val and node2.val == node3.val and node3.val == node4.val:
                    node = Node(node4.val, True, None, None, None, None)
                    return node
                return Node(None, False, node1, node2, node3, node4)

        return make_tree(0, len(grid) - 1, 0, len(grid) - 1)


if __name__ == '__main__':
    grid = [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]
    obj = Solution()
    node = obj.construct(grid)
    print(node)
