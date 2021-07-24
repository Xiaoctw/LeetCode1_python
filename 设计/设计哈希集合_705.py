class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._len = 1007
        self.arr = [[] for _ in range(self._len)]

    def add(self, key: int) -> None:
        idx = key % self._len
        if key not in self.arr[idx]:
            self.arr[idx].append(key)

    def remove(self, key: int) -> None:
        idx = key % self._len
        if key in self.arr[idx]:
            self.arr[idx].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = key % self._len
        if key in self.arr[idx]:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
