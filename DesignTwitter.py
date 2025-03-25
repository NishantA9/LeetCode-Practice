from collections import defaultdict
from typing import List
import heapq

class Twitter:
    def __init__(self):
        self.count = 0  # Acts as a timestamp counter (newest tweet has smallest count)
        self.tweetMap = defaultdict(list)  # Maps userId to list of [count, tweetId]
        self.followMap = defaultdict(set)  # Maps userId to set of followees

    def postTweet(self, userId: int, tweetId: int) -> None: # Add tweet with decreasing count (like a timestamp)
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []  # To hold the final 10 most recent tweetIds
        minHeap = []  # Min-heap to track the top 10 recent tweets
        self.followMap[userId].add(userId)  # User should follow themself
        for followeeId in self.followMap[userId]: # Go through all followees
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1  # Start from their latest tweet
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1]) # Store count to compare recency, along with tweetId, followeeId, and index
        heapq.heapify(minHeap)  # Convert list to min-heap
        while minHeap and len(res) < 10: # Extract 10 most recent tweets
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0: # Push the next older tweet from the same user if it exists
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)  # Add followee to follower's set

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId] and followeeId != followerId: # Remove only if it exists (and cannot unfollow self)
            self.followMap[followerId].remove(followeeId)