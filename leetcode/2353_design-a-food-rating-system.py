import collections
import heapq
from typing import List

from sortedcontainers import SortedSet


class Food:
    def __init__(self, food_rating, food_name):
        self.food_rating = food_rating
        self.food_name = food_name

    def __lt__(self, other):
        if self.food_rating == other.food_rating:
            return self.food_name < other.food_name

        return self.food_rating > other.food_rating


class FoodRatingsV1:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating_map = {}
        self.food_cuisine_map = {}
        self.cuisine_food_map = collections.defaultdict(list)

        for i in range(len(foods)):
            self.food_rating_map[foods[i]] = ratings[i]
            self.food_cuisine_map[foods[i]] = cuisines[i]
            heapq.heappush(self.cuisine_food_map[cuisines[i]], Food(ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating_map[food] = newRating
        cuisine_name = self.food_cuisine_map[food]
        heapq.heappush(self.cuisine_food_map[cuisine_name], Food(newRating, food))

    def highestRated(self, cuisine: str) -> str:
        highest_rated = self.cuisine_food_map[cuisine][0]
        while self.food_rating_map[highest_rated.food_name] != highest_rated.food_rating:
            heapq.heappop(self.cuisine_food_map[cuisine])
            highest_rated = self.cuisine_food_map[cuisine][0]

        return highest_rated.food_name


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating_map = {}
        self.food_cuisine_map = {}
        self.cuisine_food_map = collections.defaultdict(SortedSet)

        for i in range(len(foods)):
            self.food_rating_map[foods[i]] = ratings[i]
            self.food_cuisine_map[foods[i]] = cuisines[i]
            self.cuisine_food_map[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine_name = self.food_cuisine_map[food]
        old_elt = (-self.food_rating_map[food], food)
        self.cuisine_food_map[cuisine_name].remove(old_elt)

        self.food_rating_map[food] = newRating
        self.cuisine_food_map[cuisine_name].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        highest_rated = self.cuisine_food_map[cuisine][0]
        return highest_rated[1]


fr = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                 ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7])
assert fr.highestRated("korean") == "kimchi"
assert fr.highestRated("japanese") == "ramen"
fr.changeRating("sushi", 16)
assert fr.highestRated("japanese") == "sushi"
fr.changeRating("ramen", 16)
assert fr.highestRated("japanese") == "ramen"
