from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(word):
            l = 0
            r = len(word) - 1

            while l <= r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1

            return True

        for word in words:
            if isPalindrome(word):
                return word

        return ""


assert Solution().firstPalindrome(["knywrurkwbrtpalvuuzbczcwzpdqibcwwyflwiddixemsrwblupyerjgvcpavdjfhmujitcsmdbvhxw",
                                   "ovkeowhqvwlndtpxdnimgietvjsqydbuuwmxkfxxgn", "damomwtjugmsrfyvytaheg",
                                   "bngqatscosdakdwjz",
                                   "jwzcowuantgqlzjrzgpapcugxvviltrhmcwijtpqapmxjfcilrsmsbeffphcxmaozlczncoxxjmuqijhidxqinhywrtah",
                                   "ujvoejixvaioikkwzxgtmkchckrigfejjpheiiehpjjefgirkchckmtgxzwkkioiavxijeovju",
                                   "kacjvcouuigbhydrryaperxvjetwsycmnlkxujaqngjhhotqskclquklxsozfryfxwiksstmropcdvhgsnosgvltqo",
                                   "qrbsdxxolwzmyltproznfgyydxkkejwdiwpvfzvjoxqvwguoerhclytzvolymbxummwsoqtttyttik",
                                   "tkekt", "esrshrlfoihhjrouleucwpeubygivoatrfraphgwpvtkanwu",
                                   "kwzrfelynncvsrwvaukiinhjdydmlimggjldhflygemzwnjizzlsuqwahsufwmwhfjkjpngdfsudyavtogoaqzknpew",
                                   "sdgpcnvsbzxhyjt"]) == "ujvoejixvaioikkwzxgtmkchckrigfejjpheiiehpjjefgirkchckmtgxzwkkioiavxijeovju"
assert Solution().firstPalindrome(["po", "zsz"]) == "zsz"
assert Solution().firstPalindrome(["abc", "car", "ada", "racecar", "cool"]) == "ada"
assert Solution().firstPalindrome(["notapalindrome", "racecar"]) == "racecar"
assert Solution().firstPalindrome(["def", "ghi"]) == ""
