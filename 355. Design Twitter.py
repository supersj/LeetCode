from collections import deque
import queue as q
class User(object):
    def __init__(self, userId):
        self.id = userId
        self.followee = set([])
        self.tweet = deque([])

    def addfollowee(self, followeeId):
        self.followee.add(followeeId)

    def unfollow(self, followeeId):
        if followeeId in self.followee:
            self.followee.remove(followeeId)

    def postTweet(self, timeId, tweetId):
        self.tweet.appendleft([timeId, tweetId])


class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cnt = 0
        self.Users = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.cnt += 1
        if self.Users.has_key(userId):
            self.Users[userId].postTweet(self.cnt, tweetId)
        else:
            self.Users[userId] = User(userId)
            self.Users[userId].postTweet(self.cnt, tweetId)

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        result = []
        r = q.PriorityQueue(10)
        if not self.Users.has_key(userId):
            return []
        else:
            for i in range(min(10,len(self.Users[userId].tweet))):
                r.put([-self.Users[userId].tweet[i][0],self.Users[userId].tweet[i][1]])
            for user in self.Users[userId].followee:
                for i in range(min(10, len(self.Users[user].tweet))):
                    r.put([-self.Users[user].tweet[i][0], self.Users[user].tweet[i][1]])
        while not r.empty():
            result.append(r.get()[1])
        return result

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        if not self.Users.has_key(followerId):
            self.Users[followerId] = User(followerId)
        if not self.Users.has_key(followeeId):
            self.Users[followeeId] = User(followeeId)
        self.Users[followerId].addfollowee(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        if self.Users.has_key(followerId):
            if not self.Users.has_key(followeeId):
                return
            self.Users[followerId].unfollow(followeeId)