from collections import defaultdict
class Twitter:

    def __init__(self):
        self.user_follow = defaultdict(set)
        self.tweets = list()


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        cnt = 0
        tweet_ids = list()
        for idx in range(len(self.tweets)-1, -1, -1):
            user_id, tweet_id = self.tweets[idx]
            if user_id not in self.user_follow[userId] and userId != user_id:
                continue
            cnt += 1
            tweet_ids.append(tweet_id)
            if cnt >= 10:
                break
        return tweet_ids



    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follow[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_follow[followerId]:
            self.user_follow[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)