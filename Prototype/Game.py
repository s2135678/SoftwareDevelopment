import json
import System

class Game():

    def __init__(self, name, username,expansions):
        """
        need three parameter?
        """
        self.name = ""
        self.reviews = set()
        self.rating = 0
        self.expansions=list()

    def viewAllReviews(self):
        print(self.reviews)


    def addReview(self, player, review):
        self.reviews.add(review)

    def viewRating(self):
        pass

    def add(self, game):
        pass