import heapq
from collections import defaultdict
from typing import List

class Node:
    def __init__(self, val: int, time: int):
        self.val = val
        self.time = time    
        self.next = None   
    
    def __lt__(self, other):
        # Max heap behavior (latest first)
        return self.time > other.time

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def exists(self):
        return self.head is not None

    def appendleft(self, val: int, time: int) -> None:
        new_node = Node(val,time)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node 

class Twitter:
    def __init__(self):
        self.follower_map = defaultdict(set)   # user -> set of followees
        self.tweets = {}                       # user -> LinkedList of tweets
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer += 1
        if userId not in self.tweets:
            self.tweets[userId] = LinkedList()
        self.tweets[userId].appendleft(tweetId, self.timer)

        # user should always follow themselves
        self.follower_map[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        queue = []
        result = []

        # ensure self-follow
        self.follower_map[userId].add(userId)

        for followee in self.follower_map[userId]:
            tweets = self.tweets.get(followee)
            if tweets and tweets.exists():
                heapq.heappush(queue, tweets.head)
        
        while queue and len(result) < 10:            
            top: Node = heapq.heappop(queue)
            result.append(top.val)
            if top.next:
                heapq.heappush(queue, top.next) 

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].add(followeeId)
        self.follower_map[followerId].add(followerId)  # ensure self-follow

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.follower_map[followerId].discard(followeeId)
