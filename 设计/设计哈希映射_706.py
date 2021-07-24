class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._len = 1007
        self.hash_arr = [[] for _ in range(self._len)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self._len
        for i in range(len(self.hash_arr[idx])):
            if self.hash_arr[idx][i][0] == key:
                self.hash_arr[idx][i][1] = value
                return
        self.hash_arr[idx].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx=key%self._len
        for i in range(len(self.hash_arr[idx])):
            if self.hash_arr[idx][i][0]==key:
                return self.hash_arr[idx][i][1]
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        tem_list=[]
        idx=key%self._len
        for i in range(len(self.hash_arr[idx])):
            if self.hash_arr[idx][i][0]==key:
                tem_list=self.hash_arr[idx][i]
        if tem_list:
            self.hash_arr[idx].remove(tem_list)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
