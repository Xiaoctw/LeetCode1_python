from collections import defaultdict
import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val2idx = defaultdict(lambda: set())
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.nums.append(val)
        size = len(self.nums)
        self.val2idx[val].add(size - 1)
        return len(self.val2idx[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if len(self.val2idx[val]) == 0:
            return False
        idx1 = self.val2idx[val].pop()
        size = len(self.nums)
        if size != idx1 + 1:
            last_val = self.nums[size - 1]
            self.nums[idx1], self.nums[size - 1] = self.nums[size - 1], self.nums[idx1]
            self.nums.pop()
            self.val2idx[last_val].remove(size - 1)
            self.val2idx[last_val].add(idx1)
        else:
            self.nums.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
    set1 = {1, 2, 3, 4, 5}
    print(set1)
    print(set1.pop())
    print(set1)
