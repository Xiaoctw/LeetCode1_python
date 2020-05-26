class LRUCache:

    def __init__(self, capacity: int):
        '''
        字典结构能够快速定位到对应节点，对应节点
        为双向链表，适合删除添加操作
        :param capacity:
        '''
        self.cap=capacity
        self.head,self.tail=LinkNode(-1,-1),LinkNode(-1,-1)
        self.head.right=self.tail
        self.tail.left=self.head
        self.dic1={}#保存值到对应节点的映射
        self.num_node=0

    def get(self, key: int) -> int:
        if key in self.dic1:
            node=self.dic1[key]
            val=self.dic1[key].val
            pre=node.left
            next=node.right
            pre.right=next
            next.left=pre
            node.right=self.head.right
            self.head.right.left=node
            node.left=self.head
            self.head.right=node
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic1:
            node=self.dic1[key]
            node.val=value
            node.left.right=node.right
            node.right.left=node.left
            node.right=self.head.right
            node.left=self.head
            self.head.right.left=node
            self.head.right=node
            return
        if self.num_node==self.cap:
            delete_node=self.tail.left
            self.tail.left=delete_node.left
            delete_node.left.right=self.tail
            k=delete_node.key
            del self.dic1[k]
            self.num_node-=1
        node=LinkNode(key,value)
        self.dic1[key]=node
        node.right=self.head.right
        self.head.right.left=node
        self.head.right=node
        node.left=self.head
        self.num_node+=1




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
