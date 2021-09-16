import json
import os
from Game import Game

class Player():
    """
    This is the game player class. Players can manage their games.
    """

    def __init__(self, name, games):
        self.name = name
        self.games = games


    def addGame(self, gameName):
        """
        Add a specific game to player's collection
        """
        if gameName in self.games:
            print("You already have this game!\n")
        else:
            self.games[gameName] = {}  
            self.games[gameName]['extensions'] = {} 
            print("Add game {} successfully.\n".format(gameName))


    def removeGame(self, gameName):
        """
        Remove a specific game from player's collection
        """
        if gameName in self.games:
            self.games.pop(gameName)
            print("Remove game {} successful!\n".format(gameName))
        else:
            print("You don't have this game!\n")



    def viewPersonalGames(self):
        """
        Player views all games he current has.
        """
        if len(self.games) == 0:
            print("{}, you don't have any game now!\n".format(self.name))
        else:
            print("{}'s game:".format(self.name))
            for g in self.games:
                print(g)
