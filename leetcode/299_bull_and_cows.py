import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cows = 0
        bulls = 0

        secret_dict = collections.Counter(secret)

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                cows += 1
                secret_dict[secret[i]] -= 1

        for i in range(len(secret)):
            if guess[i] != secret[i] and guess[i] in secret_dict.keys() and secret_dict[guess[i]] > 0:
                bulls += 1
                secret_dict[guess[i]] -= 1

        return f"{cows}A{bulls}B"


if __name__ == "__main__":
    assert Solution().getHint("1807", "7810") == "1A3B"
    assert Solution().getHint("1123", "0111") == "1A1B"
