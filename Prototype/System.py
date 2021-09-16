from Player import Player
import json
import os 

class System():
    """
    The software platform. System can encode / decode data and interact with players
    """
    def __init__(self):
        self.players = dict() # store players' data
        self.games = dict() # store games' data
        self.activePlayer = None # current active player

        

    ##################################
    # following methods are related to read/write files.
    ################################################

    def load(self):
        """
        Load information from file system
        """
        def helper(fileName):
            if os.path.exists(fileName):
                with open(fileName, 'r') as f:
                    return json.load(f)
            else: # create an empty players collection
                return dict()

        print("Loading ......")
        self.players = helper("./players.json")
        self.games = helper("./game.json")

    def save(self):
        """
        Save information to file system
        """
        def helper(fileName, data):
            with open(fileName, 'w') as f:
                json.dump(data, f) 

        print("Saving data ......")
        helper("./players.json", self.players)
        helper("./game.json", self.games)
        
    #######################
    # following methods are related to players.
    ####################################
    def createSpaceForNewPlayer(self, playerName):
        """
        Create record for a new player's information
        """
        assert playerName not in self.players

        self.players[playerName] = {}
        self.players[playerName]["password"] = ""
        self.players[playerName]["games"] = {}


    def welcome(self):
        """
        Welcome page of the software, where players can log in an account
        or sign up a new account.
        """

        while self.activePlayer == None:

            print("-------------------- Welcome Page ----------------------")
            choice = input("0 to sign up, 1 to log in: ")
            if choice == '0':
                self.signUp()
            elif choice == '1':
                self.login()
            else:
                print("invalid input")

        self.jumpToProfile()


    def viewAllgames(self):
        """
        Print names of all games on system.
        """
        print("All games in this software:")
        for name in self.games.keys():
            print(name)


    def jumpToProfile(self):
        """
        Jump to active player's profile
        """
        while True:
            print("-------------------- {}'s  Profile ----------------------\n".format(self.activePlayer.name))
            self.viewAllgames()
            self.activePlayer.viewPersonalGames()

            cmd = input("input 0 to exit, 1 to manage your game collection: ")
            if cmd == '0':
                self.exit()
            elif cmd == '1':
                self.manageGame()
            else:
                print("invalid command\n")



    def manageGame(self):
        """
        Player can manage his/her game collection here.
        Such as adding, removing, viewing ...
        """

        player = self.activePlayer
        while True:
            print("-------------------- {}'s Game Collection ----------------------\n".format(self.activePlayer.name))
            print("input 0 to return to your profile.")
            print("input 1 to add a game.")
            print("input 2 to remove a game.")
            print("input 3 to add a review.")
            print("input 4 to view reviews.")
            cmd = input()

            if cmd == '0':
                return

            elif cmd == '1':
                print("--------------------Adding game----------------------\n")
                gameName = input("input the name of game you want to add:")
                if gameName in self.games:
                    player.addGame(gameName)
                else:
                    print("Sorry our software doesn't have this game now.\n")

            elif cmd=='2':
                print("--------------------Removinging game----------------------\n")
                gameName = input("input the name of game you want to remove:")
                player.removeGame(gameName)

            elif cmd == '3':
                print("--------------------Adding reviews----------------------\n")
                self.addReview()

            elif cmd == '4':
                print("--------------------Viewing reviews----------------------\n")
                self.viewReview()
            else:
                print("invalid input")
            """
            elif cmd=='5':
                gamename = input("Select the game name that you want to see expansions:\n")
                tmpExpansions = list()
                fileName = "./expansions.json"
                if os.path.exists(fileName):
                    with open(fileName, 'r') as f:
                        allExpansions = json.load(f)
                for item in allExpansions["expansions"]:
                    if (gamename in item["gamename"]) & (self.name in item["username"]):
                        tmpExpansions.append(item["exname"])
                if len(tmpExpansions) == 0:
                    print("You do not have {}'s expansions\n".format(gamename))
                else:
                    print("the expansions of {} that you already have".format(gamename))
                    for item in tmpExpansions:
                        print(item)

                print("Do you want to operate expansions")
                cmd = input("input 1 to add a expansion, 2 to delete a expansion:\n")
                if cmd == '1':
                    gamename = input("Select the game name that you want to add its expansions:\n")
                    if os.path.exists(fileName):
                        with open(fileName, 'r') as f:
                            allExpansions = json.load(f)

                    print("Expansions that you do not have:")
                    for item in allExpansions["expansions"]:
                        if (gamename in item["gamename"]) & (self.name not in item["username"]):
                            print(item["exname"])
                    expansionName= input("Select the expansion name to add it:\n")

                    for item in allExpansions["expansions"]:
                        if expansionName == item["exname"]:
                            item["username"].append(self.name)

                    with open(fileName, 'w') as f:
                        json.dump(allExpansions, f)
                    print("Add successfully!\n")

                if cmd == '2':
                    gamename = input("Select the game name that you want to delete its expansions:\n")
                    if os.path.exists(fileName):
                        with open(fileName, 'r') as f:
                            allExpansions = json.load(f)

                    print("Expansions that you have:")
                    for item in allExpansions["expansions"]:
                        if (gamename in item["gamename"]) & (self.name in item["username"]):
                            print(item["exname"])
                    expansionName = input("Select the expansion name to delete it:\n")

                    for item in allExpansions["expansions"]:
                        if expansionName == item["exname"]:
                            item["username"].remove(self.name)

                    with open(fileName, 'w') as f:
                        json.dump(allExpansions, f)
                    print("Delete successfully!\n")
                """

    def addReview(self):
        """
        Add a review to a game in active player's collection
        """
        gameName = input("input the name of game to which you want to add review:")
        playerName = self.activePlayer.name

        if gameName in self.players[playerName]['games']:
            review = input("input your review to {}:".format(gameName))
            self.games[gameName]["reviews"].append(playerName+': '+review)
        else:
            print("Cannot add review, because you don't have this game")

        self.save()



    def viewReview(self):
        """
        Print all reviews of a game.
        """
        gameName = input("input the name of game to which you want to view review:")
        if gameName in self.games:
            for r in self.games[gameName]["reviews"]:
                print('    ' + r)
        else:
            print("invalid game name")

    #######################
    # following methods are related to login / logout.
    ############################################

    def login(self):
        """
        Login to an existing account
        modified the activePlayer to the login player
        """
        print("-------------------- Log In Page ----------------------")

        userName = input("input user name: ")
        if userName not in self.players:
            print("user name does not exit.\n")
            return None

        passWord = input("input password: ")
        if passWord != self.players[userName]['password']:
            print("wrong password.\n")
            return None

        self.activePlayer = Player(userName, self.players[userName]['games'])


    def signUp(self):
        """
        Sign up a new account
        """
        print("-------------------- Sign Up Page ----------------------")
        playerName = input("Signup: input player name: ")
        if playerName in self.players:
            print("name {} has existed\n". format(playerName))
            return 
        
        password =  input("Signup: input password: ")
        
        self.createSpaceForNewPlayer(playerName)
        self.players[playerName]["password"] = password

        self.save()


    def exit(self):
        """
        Exit the software
        """
        self.save()
        self.activePlayer = None
        print("-------------------- Exit ----------------------")
        exit()