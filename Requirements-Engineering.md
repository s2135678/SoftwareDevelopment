# 1. Requirements
This section presents both functional and non-functional requirements of the game collection management and sourcing system. It includes methods of requirements capture used and other alternatives we considered. The functional and non-functional requirements were prioritised used MOSCOW method. The overall aim of the project is to create an online space for players to manage, explore, and find communities for all types of games.

## 1.1 Functional Requirements 
The requirements are prioritised using the MOSCOW method. 
The requirements are grouped into one of:
* Must have (M)
* Should have (S)
* Could have (C) 
* Won't have (W)

### Must have
* Must allow a user to register for an account.
* Must allow a user to login to their account.
* Must allow a user to logout from their account.
* Must allow a user to search their collection.
* Must allow a user to add/remove items from their collection.
* Must ensure that a username is unique.
* Must ensure that a username is case sensitive.

### Should have
* Should allow a user to search for games they do not own.
* Should allow a user to read reviews for games posted by user communities and websites.
* Should allow a user to post a review of a game.
* Should allow a user to post house rules for games.
* Should allow a user to post clarifications of rules for games.
* Should allow a user to read FAQs and errata documents from publishers.
* Should recommend new games to users.
* Should allow users to search for other players to play with.
* Should allow users to search for clubs/communities in a given geographical area.
* Should allow users to share their geographical location.
* Should allow users to view properties of games, such as price, game type, status (whether the game is available or there is a new version), average rating, etc.
* Should allow users to search for sellers of games.
* Should allow the properties of games to be updated/changed.
* Should check if a user already holds an account.
* Should recommend new games to users.
* Should provide alternative methods of accessing the system for users with visual and hearing impairments.
* Should allow a user to search for games using specific keywords.

### Could have
* Could allow a user to provide contact info.
* Could allow publishers to register for a publisher account.
* Could allow publishers to post rules for games.
* Could allow publishers to provide contact info.
* Could allow publishers to provide errata documents for games.
* Could allow a community to post comments.
* Could allow a user to join a community.
* Could allow a user to sell a game.
* Could allow a publisher to add/remove an expansion to a game.
* Could filter reviews of games.
* Could allow a user to search for games by rating.
* Could ensure that a username contains only numbers and letters.
* Could allow a user to compare prices of games.
* Could allow a user to submit feedback to publishers if they encounter a bug or issue with a game.
* Could allow a user to post a comment to a community when they encounter an bug or issue with a game.
* Could allow a user to view the order in which expansion packs for games have been released.
* Could allow a publisher to specify the date at which an expansion pack was released.
* Could allow a user to gather a game and its related titles together.
* Could highlight key features of expansion packs.
* Could allow users to discuss games in a forum within community pages.
* Could allow reporting of inappropriate behaviour within discussion areas of communities within the system.
* Could allow a user to reply to comments or questions posed in community forums on the system.
* Could notify a user when a question or comment has been replied to.

### Won't have
* Won't have information packed densely and inaccessibly.
* Won't have confusing paths of buttons and systems to navigate the system.

## 1.2 Non-functional Requirements 
The requirements are prioritised using the MOSCOW method. 
The requirements are grouped into one of:
* Must have (M)
* Should have (S)
* Could have (C) 
* Won't have (W)

### Must have
* Must allow a user to search their collection via a search bar.
* Must allow a user to add/remove games from their collection via buttons on their personal page.


### Should have
* Should allow a user to search for games they don't own via a search bar.
* Should allow a user to post a review of a game in a text field on the game page.
* Should allow a user to include a rating of a game in their review using a 5-point/star rating scale.
* Should allow a user to navigate the system without confusion.
* Should provide detailed descriptions of games.
* Should run efficiently on multiple operating systems without vast differences.
* Should allow a user to access a navigation bar on every page of the system in an obvious location.
* Should display information in a dark colour palette to reduce strain on users' eyes.
* Should provide alternative colour palettes for those with colour impairments, such as colour blindness.
* Should provide closed captions on all videos to provide accessibility to those with hearing impairments.
* Should provide text to speech for users with visual impairments.
* Should provide the ability to enlarge font size for users with visual impairments.
* Should have a logical interface layout.
* Should include detailed information on games in a single place.
* Should provide a logical control structure to allow users to interact with the system in an intuitive manner.
* Should have self-documenting control structures, such as buttons on the system labelled with their purpose.

### Could have
* Could allow games to have properties such as type (board game or card game etc), price, status (available, new version available, etc), average rating and rules.
* Could display similar related games a user might be interested in.
* Could allow a user to search by selecting genres and types of games they are interested in.
* Could allow a user to gather different games and their sequels and expansions under a common heading.
* Could allow a user to view key features of expansion packs in a bulleted list on the page for the expansion pack.
* Could allow a user to report other users if they are behaving inappropriately in discussion areas of the communities on the system.
* Could implement a forum or chat room system within communities on the system, allowing discussion of games of interest within the community.
* Could implement an notification inbox for users to quickly and simply access and view responses to their comments in communities.

### Won't have


## 1.3 Prioritisation 
Requirements were grouped into four categories: 
* Must have (M)
* Should have (S)
* Could have (C) 
* Won't have (W) 

Requirements were categorised as 'Must' if the functionality is core to the game collection management and sourcing.

Requirements that have high risk (i.e. we are unfamiliar with methods to achieve the functionality) were also placed into 'Must'. 

## 1.4 Capture Methodology 
A number of different capture methodologies were employed in extracting the requirements for this project, specifically:
* Reading the Product Description.
* A questionnaire given to gamers.
* Questions sent to Alistair Grant for clarification.

Each will be discussed in detail below.

### Reading the Product Description
Requirements capture began by reading the product brief explaining the purpose of the project and what was expected of it. This provided a wealth of information, allowing a large number of functional requirements to be established, for example it was simple to extrapolate the need for user accounts within the game management system, to allow individual users to manage their collections. Further it was simple to establish the requirement for manipulation of games within a users' collection, to allow the addition and removal of games. Additionally the product description allowed for the consideration of different types of users within the system, such as publishers and communities and the allowance of different privileges and characteristics.

The functional requirements derived from the product description allowed the non-functional requirements to be extrapolated using common sense to dictate how the functional requirements should be implemented, given that functional requirements are what the system should do and non-functional requirements are how it should be done.

### Questionnaire
Moving on from the product description a questionnaire was devised to be given to gamers to determine the sort of requirements they would like to see in a game management system, considering those already on the market.

The responses to the questionnaire were extremely informative as they identified a number of requirements both functional and non-functional which had not been considered by the development team or elucidated in the product description.

When asked whether they used game management/collection sites, 66.7% said they did, a further 27.8% said they did but not really and a final 5.6%  said they never used game management/collection sites.

<p float="left">
  <img src="https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/Project Requirements/do_you_use_game_collection_sites.png" width="49%"/>
</p>

Those who said they used game management/collection sites, were asked what they used it for and gave a number of responses, such as:
* To find new games to play.
* To manage multiple games.
* To find game communities and players to play with.
* To compare game prices and look up reviews.

Most gamers who answered the questionnaire said they used game management/collection sites to find new games to play, closely followed by using them to manage multiple games.

Gamers were also asked if there was anything they liked/didn't like about the Steam user interface. This was extremely helpful in considering the UI design of the game management product as it was apparent that navigation was often not straightforward and many found the Steam user interface to be very cluttered and displayed large amounts of superfluous and irrelevant information.

Gamers were then asked whether they had ever joined a game club or community. There was a fairly even split between those who had and had not, as shown in the pie chard below.

<p float="left">
  <img src="https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/Project Requirements/joined_game_club_or_community.png" width="49%"/>
</p>

### Questions asked of Alistair Grant