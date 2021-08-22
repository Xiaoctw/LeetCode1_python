
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.num_node=0
        self.head=LinkNode(-1,-1)
        self.tail=LinkNode(-1,-1)
        self.head.right=self.tail
        self.tail.left=self.head
        self.key2node={}


    def get(self, key: int) -> int:
        if key in self.key2node:
            node=self.key2node[key]
            node.left.right=node.right
            node.right.left=node.left
            node.right=self.head.right
            node.left=self.head
            node.right.left=node
            self.head.right=node
            return node.val
        else:
            return -1


    def delete(self):
        node=self.tail.left
        key=node.key
        del self.key2node[key]
        node.left.right=node.right
        node.right.left=node.left
        self.num_node-=1



    def put(self, key: int, value: int) -> None:
        if key in self.key2node:
            node=self.key2node[key]
            node.left.right=node.right
            node.right.left=node.left
            new_node = LinkNode(key, value)
            # self.key2node[key] = new_node
            # new_node.right = self.head.right
            # new_node.left = self.head
            # self.head.right = new_node
            # new_node.right.left = new_node
            self.add(key,value)
            return
        if self.num_node==self.cap:
            self.delete()
        # new_node=LinkNode(key,value)
        # self.key2node[key] = new_node
        # new_node.right=self.head.right
        # new_node.left=self.head
        # self.head.right=new_node
        # new_node.right.left=new_node
        self.add(key,value)
        self.num_node+=1

    def add(self,key,value):
        new_node = LinkNode(key, value)
        self.key2node[key] = new_node
        new_node.right = self.head.right
        new_node.left = self.head
        self.head.right = new_node
        new_node.right.left = new_node




class LinkNode:
    def __init__(self,key,value):
        self.key=key
        self.val=value
        self.left=None
        self.right=None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == '__main__':
    cache=LRUCache(2)
    cache.put(1,1)
    cache.put(2,2)
    print(cache.get(1))
    cache.put(3,3)
    print(cache.get(2))
    cache.put(4,4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
