# 2. Software design

## 2.1 Architecture
The software consists of four layers: `Presentation Layer`, `Business Logic Layer`, `Data Layer` and `Infrastructure Layer`.

The main purpose `Presentation Layer` is the UI interface that used to interact with users who will use this system, mainly game players and game publishers.
The `Business Logic Layer` is the layer that consists of main functions of this system, and these functions is split into five different sets according to their purposes. These five sets are `User Management`, `Publisher Management`, `Game Transaction`, 'Community Management' and `Game Management`.
The `Data Layer` uses MySQL, and have four main functions, `Data Transaction`, `Data Analysis`, `Data Storage` and `Database Operation`. 
The last layer `Infrastructure Layer` is the most basic layer. It contains the `OS (Operating System)`, `Server`, `Network`, `Cloud Storage` and `Backup`.

Users can use `Presentation Layer` to interact with the system, the action is then passed through the layers in an orderly fashion until the action is complete.

![](https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/software_design/ArchitectureDesign.jpg "software architecture") 

## 2.2 Component functionality
### 2.2.1 Presentation Layer
In `Presentation Layer`, mainly uses `HTML`, `CSS` and `Vue.JS`. Users interact with the system through this layer. `Presentation Layer` will pass the information to `Business Layer`, then `Business Layer` will call the related functions to finish the action includes exchange information with `Data Layer`.

Here are some examples that how users interact with the system. 

![](https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/software_design/jpgForPresentationLayer/login.jpg "The action login") 

In this example, the user inputs his userID and password, and then choose the `login` button in the page. `login` function will be called. The information will be sent to the `data layer` to be checked whether it is already stored in the database. If the answer is yes, the system will jump to the homepage. If the answer is no, the system will give the user a register option, after user input information that needed to do the register work, the information will be added in to the database, and then jump to the homepage.

![](https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/software_design/jpgForPresentationLayer/recommendGame.jpg "The action recommendation")

In this example,  the user first need to finish the login work, then the system will jump to the homepage. At the same time, the function `recommendByRate` will be called. The system will query the private rating information of the user to see what types of game the user likes and the games that the user already have. Then the database will give the weight of the same type of games. Then the rating will be calculated by the weight. The result will be showed in the sidebar of the homepage.



### 2.2.2 Business Logic Layer (BLL)
`Business Logic layer` has five main subsystems, which are `User Management`, `Publisher Management`, `Game Transaction`, 'Community Management' and `Game Management`. `Game Management` has three subsystems, `Rating Management`, `Review Manegement` and `Expansion Management` To realize all the requirements, there are eight classes in BLL, `userService`, `User`, `userCommunity`, `Publisher`, `Game`, `ratingService`, `reviewService` and `gameExpansion`. Some functions of a system can be included in another system, for example, there is not a class for `Game Transaction` but its related function can be acessed in `User` class.

The `user` class has four attributes, `userID`, `userName`, `password` and `email`. User class also has seven functions, `updateGame` update the game collection, `add` add game to game collection, `remove` remove the chosen game from his game collection, `postReview` post new review for chosen game, `postRules` post new rules to the chosen game (the rules also need to be checked by publisher), `updatePersonFile` update his own personal details, `sellgame` user also have the role seller, he can sell his game to others and decide the price of the game so that other user can decide whether to buy the game. 

The `User` can use `userService` class to finish three steps, register, login and logout.

The `Publisher` class is similar to the `User` class. The differences are that `Publisher` can publish rules, clarification and errata documents. 

The `userCommunity` class has four attributes. `communityID` is the identification of the community. `communityGame` indicates which game this community belongs to. `peopleNumber` is the number of people in this community (including players and publishers). `Review` stores all reviews in this community. Apart from that, three methods are provided for this class. `postReviews` returns all the reviews in the community. `addPlayer` and `removePlayer` are methods that change the members of the community.

The `Game` class has attributes that help the player to manage their game collection and buy new games. `gameId`, `gameName` and `type` help players to search games. The `price` is the money paid when buying the game. The `Status` indicates whether this game is available or there is a new version. The `rate` allows players to search the highest rating or most popular games. Besides, there are four methods, to change the state of games(`changePrice, updateStatus` and `changeRules`) and recommand the game (`recommandByType`). 

The `ratingService` class provides several methods to modified game's rate and recommend by rate. These services can be invoked when players give feedback to games or the system recommend popular games for players.

The `reviewService` class has methods for players to post their review (`postReview`) and read others' reviews (`orderByGame` and `orderByUser`). There is also a weight system that can filter certain review sources (`orderByWeight`).

The `gameExpansion` class have attributes, `expansionID`, `expansionName` and `expansionPrice` and two main functions, (`addExpansion`) and (`deleteExpansion`). This class can be used to manage expansions of games.

![](https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/software_design/businessLogicLayer.jpg "business layer") 


### 2.2.3 Data Layer

There are 8 tables in the database. The `User` Table and `Publisher` Table store the personal information of game player and publisher, including userid, password, name and email. The `Community` table stores the data of the user community where users can read other's review or add their own review. The `Game` Table stores information of all published games. The `Rules` Table stores games' rules and clarifications. The `Rate` Table stores the user's private rate to a game and corresponding weight. The `Docs` Table stores publisher's FAQs and errata documents to the game. The `Review` Table stores all the reviews from players, including review id, post date and content.

Relationship between tables is also important for data layer. Firstly, each user can own several games and several players can all play a same game, so that there is a many-to-many relationship between `User` Table and `Game` Table. For publishers, they can publish several rules, FAQs and errata documents for games, which means that the relationships between `Publisher` Table and `Docs` Table (and `Rules` Table) are both one to many. Also, one rule might contain several FAQs and documents to be explained, so that the relationship between `Docs` Table and `Rules` Table is many to one. For the games, one game always has more than one rules (many-to-one relationship between `Rules` Table and `Game` Table) and there is one community for each game (one to one relationship between `Game` Table and `Community` Table). Players could share their rating and review to a game so that one game could have more than one rates and reviews. (Why one:one on diagram?)

![](https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/software_design/database%20layer%20ER.jpg "database layer") 

### 2.2.4 Infrastructure Layer
`Infrastructure Layer` is basic but also the most important. This layer has five fundamental parts, `Network`, `Server`, `OS`, `Cloud Storage` and `Backup`. First, all the service need to be based on a valid server cluster. Second, the network need to have adequate bandwidth to accommodate numerous user accesses. Third, there should be enough cloud space to store all the information that produced by the users and the games. Fourth, the operating system should be strong enough to keep the whole system running. Last, there should be a backup version of the system that can be used to recall, which will reduce some avoidable problems.

## 2.3 Implementation path
At first, the `Infrastructure Layer` should be decided. The operating system should be open enough for most of the requirements to be implemented. The network and server can have enough load to support the operation of the entire system, and the storage space should be large enough. The second step is to collect and organize the data and realize the UI interface. It is also clear that the interface between the front end and the back end should keep matching. The database should match the tables in the component design. Next, different subsystems of the business layer are developed by stages, and each subsystem is carried out on the basis of meeting the project requirements. In the process of each stage, the progress is recorded in the development log, and the project is regularly backed up. 