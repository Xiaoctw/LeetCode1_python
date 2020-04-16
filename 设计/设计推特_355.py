import itertools
from collections import defaultdict,deque
import heapq
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #创建一个迭代的工具，每次递减1
        self.timer=itertools.count(step=-1)
        self.tweets=defaultdict(deque)
        self.followees=defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets[userId].appendleft((next(self.timer),tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        #heapq.merge用于合并有序的序列，这也是为什么把时间放在第一个位置
        #这个可能tweets长度不固定
        tweets=heapq.merge(*(self.tweets[u] for u in self.followees[userId]|{userId}))
        #对迭代器进行切片操作
        return [t for _,t in itertools.islice(tweets,10)]
    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        #删除
        self.followees[followerId].discard(followeeId)