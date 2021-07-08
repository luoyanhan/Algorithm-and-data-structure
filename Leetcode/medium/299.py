from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        length = len(secret)
        a = 0
        b = 0
        rest_secret = defaultdict(int)
        rest_guess = defaultdict(int)
        for idx in range(length):
            if secret[idx] == guess[idx]:
                a += 1
            else:
                rest_secret[secret[idx]] += 1
                rest_guess[guess[idx]] += 1
        for word in rest_guess:
            if word in rest_secret:
                b += min(rest_secret[word], rest_guess[word])
        return '{}A{}B'.format(a, b)


from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        length = len(secret)
        a = 0
        b = 0
        counter = defaultdict(int)
        for idx in range(length):
            if secret[idx] == guess[idx]:
                a += 1
            else:
                if counter[guess[idx]] > 0:
                    b += 1
                counter[guess[idx]] -= 1
                if counter[secret[idx]] < 0:
                    b += 1
                counter[secret[idx]] += 1
        return '{}A{}B'.format(a, b)