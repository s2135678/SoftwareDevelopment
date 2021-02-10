# 3. User Interface Design
This section presents the graphical user interface (GUI) for the game collection management and sourcing system, which will be implemented as a web application. This was decided following our survey, which showed that majority of players use personal computers to play games. We also considered designing a mobile application, as mobile phones were second preferred device after personal computers. Our web application addresses accessibility criteria for users with disabilities and offers different language options to provide access to users from all around the world.   

## 3.1 Accessibility
We plan to implement following features to address accessibility criteria for users with different disabilities. Accessibility settings can be adjusted in the Account Settings.

| **Disability** | **Accessibility Feature** |
| ------ | ------ |
| Visual Impairment  | Text to Speech <br> Option to enlarge font size |
| Color Impairment | Different color palettes offered. These include: Blue/Orange, Blue/Red and White/Black | 
| Hearing Impairment | Closed captions available on all videos |

## 3.2 Design Goals and Features 
Our primary goal is to allow users to accomplish tasks in fast, easy and logical manner. To address this, we identified 3 key features, which we implemented into our UI design.

### 3.2.1 Minimalistic Design

Results from the survey suggest that most players find current game management and sourcing systems (e.g. Steam) disorganised and difficult to navigate, often displaying too much irrelevant information. Thus, we have focused on creating a minimalistic design by implementing 4 features. 

Firstly, core functionalities are organised into visible and logical units and sub-units. In this way, fewer options are displayed and users can choose which options to expand depending on their goal. For example, rather than having two separate ‘My Profile’ and ‘Account Settings’ buttons on the navigation bar, ‘Account Settings’ is placed under ‘My Profile’ option to reduce overcrowding.

Secondly, these functionality options are all presented to the user in one page, to reduce the time spent scrolling to find the functionality. This was implemented using dropdown selections. For example, rather than displaying lists of games and communities on Player Profile page, these are organised into two separate dropdown selections (‘My Games’ and ‘My Communities’), which users can click to view the lists in each section.   

Thirdly, only one navigation bar is located at the top of each page. Many game collection and sourcing websites have 3 – 4 navigation bars placed on all sides of the page, overcrowding the screen. Our web application will have one main bar at the top, which will be present in all pages. 

Lastly, our web application will use dark color palette (navy, black and dark grey) to contrast with vibrant colors of games and to reduce strains to eyes. However, other color options will also be available to take account of those with color disabilities (See 3.1 Accessibility). 

### 3.2.2 Consistent Layout

Similar layout will be maintained for all pages of the web application. This increases user’s familiarity with the application and ensures easy navigation around the website. Some consistent features include: 
* Information displayed in grey containers
* Options to edit/add/remove/submit in black buttons
* Dropdown menu options shown in grey buttons

### 3.2.3 Other features
* Texts and terminologies will use words familiar to players.
* System status messages such as ‘Game added’ or ‘Searching…’ will be displayed to help users understand the outcome of their actions and determine next tasks. 
* Options to undo or redo actions will be implemented with features such as ‘cancel’ or ‘edit’. This provides users with freedom to control their own actions and prevent errors. 
* Error messages and confirmation messages such as ‘Are you sure you want to remove this game?’ will be displayed. This ensures that irreversible errors are prevented from taking place.  

## 3.3 UI Prototype and Control Flow 
### 3.3.1 Homepage (navigation bar)

<p float="left">
  <img src="https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/UI_design/UI_prototype/HomePage1.jpg" width="49%" />
  <img src="https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/UI_design/UI_prototype/HomePage2.jpg" width="49%" /> 
</p>

#### Purpose
* To attract and encourage users to create an account 
* To suggest games and communities 
* To display recent news, updates and feeds

#### User Interaction 
* Users can browse through game and community suggestions and feeds using image carousel. Click on the arrows to view previous or next suggestion/feed.
* Selecting an image directs users to corresponding game and community pages.

**Navigation bar**
* Navigation bar is located at the top of every page, allowing easy navigation between different pages.
* Before signing in, users have three options in the navigation bar:
    * Home icon: directs users to homepage
    * Search icon: search tool with filters (more information below)
    * Sign-up / Log-in : a pop-up requiring users to enter valid credentials

* After signing in, users have four options in the navigation bar:
    * Home icon: directs users to homepage
    * Search icon: search tool with filters (more information below)
    * My Profile: directs users to either the player page or account settings 
    * My Communities: directs users to the community page

**Search Tool**
* Search tool has filters for the game type, rating and community.
* Filters can be expanded and selection can be made with tick boxes.
* Click 'GO' to make the search. 


#### Control Flow
![Homepage_](uploads/bf3a397103b095767cff20d2bf9f7be9/Homepage_.jpg)

##### Overview
The homepage is the first thing seen by the user whether they have created an account or are just browsing. There is a navigation bar with search functionality (games, players or communities), a button which redirects the user back to this homepage, and either the option to login/sign up if they have  not already, or access their own profile and communities directly.

##### Searching
The search bar executes searches for game titles, other publicly viewable players, or communities for games. The search results can be filtered by type of result (game, player, community), rating (for games), or source of ratings e.g. our own users, website affiliated ratings.

##### Suggestions
Suggested communities and games are displayed in the main feed in a scrolling format. These are determined from the games and communities the user already engages with on their profile and games which other users of similar tastes play. 

##### Feeds
Publisher updates of the games, including new versions, expansion packs, convention information, or new threads from communities the user is a part of are displayed here.

##### Sign up/Log in
The sign up/log in option prompts users to enter their email address and password. Once these are verified as either an existing account or a new one has been made, the user is granted access to their own profile.

### 3.3.2 Player page

<p float="left">
  <img src="https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/UI_design/UI_prototype/PlayerPage1.jpg" width="49%" />
  <img src="https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/UI_design/UI_prototype/PlayerPage2.jpg" width="49%" /> 
</p>

#### Purpose
* To manage user's games and communities
* To display user's personal information, games and communities to other players 

#### User Interaction 
* Click on ‘Edit’ to change personal information, which is displayed for other players visiting user’s player profile.  
* For other players visiting user’s player page, personal information, games and communities are displayed without the option to edit. 
* Click on ‘My Games’ and ‘My Communities’ dropdown options to display user’s current games and communities. 

**My Games dropdown**
* Games are listed and expansion packs can be displayed by expanding the list. 
* Expansion packs are selected and unselected using tick boxes. 
* Click ‘Add’ or ‘Remove’ to edit games.

**My Communities dropdown**
* User’s game communities are listed, which can be expanded to display previews of most recent feed from the community. Click ‘Expand’ to display rest of the feed.
* Clicking on the community name directs users to the corresponding community page. Click ‘Add’ or ‘Remove’ to edit communities. 

#### Control Flow
![Player](uploads/d34a39dfee3feb04b8368609afe1235a/Player.jpg)

##### Overview
The player page displays information on the user including a small "about" section, their games, expansions, and communities. The same UI is used for viewing your own page as when looking at someone else's, with the addition of editing functionality.

##### Your profile
With your own profile, the about section can be edited, and games/communities can be added in order to personalize suggestions, and so other users can find you. The latter is only enabled if privacy settings are set to "public" in the account settings. The account settings page is accessible from your own profile only.

##### Other user's profile
When viewing other user's profile, you can see games and communities they have added to their profile, and can access the associated pages directly through these links.

### 3.3.3 Game page
<p float="left">
  <img src="https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/UI_design/UI_prototype/GamePage1.jpg" width="49%" />
  <img src="https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/UI_design/UI_prototype/GamePage2.jpg" width="49%" /> 
</p>

#### Purpose
* To provide basic information about the game, including ratings
* To read and write reviews from other users and from external sources
* To read and suggest rules 
* To submit questions on the game
* To provide pricing of the game from different retailers

#### User Interaction
* Click on dropdown options to view each section 

**Review dropdown**
* Users can submit their review of the game using text fields. Click ‘Submit’ to add reviews 
* Users can scroll down to see preview of reviews and ratings from other users and from external sources. Click ‘Expand’ to view the rest of reviews. 

**Community dropdown**
* Shows preview of recent posts from the game community. 
* ‘Go To Community Page’ button directs user to the corresponding community page.  

**Rules dropdown**
* Preview of official rules are displayed. Click ‘Expand’ to view all rules. 
* Users can add rules using text fields. This will be sent to the game publisher for approval. Click ‘Submit’ to add a rule. 
* Users can scroll down to preview recent updates from publishers. Click ‘Expand’ to view all updates. 

**FAQ dropdown**
* Users can post questions using text fields. Click ‘Submit’ to add a question. 
* Questions are sent to game publishers and answers are posted below the question. 
* Users can scroll down to preview FAQs from other players. Click ‘Expand’ to view the full FAQ.  

**Buy dropdown**
* Displays game price from different retailers 
* Click ‘Go To Website’ to redirect to retailer’s website
* Filters for ‘Used’ and ‘New’ can be selected using tick boxes.  

#### Control Flow
![Game](uploads/cbdc2debb7a133ddc2ad06ce401e1a28/Game.jpg)

##### Overview
The game page holds information for each game including the rating (from our users), title, description, and images. From the game page, the user is able to access a variety of functions from the drop down menu.

##### FAQ
This section holds frequently asked questions the game publisher has decided to publish. Users can ask the publisher any other queries they have directly with the submit function.

##### Community
This previews a few of the most recent threads of discussion from the community page associated with the game. There is also a link which redirects the user directly to the community page for the game.

##### Buy Now
Retailers (online or in person) are listed here with their price(s) and a link to their website. Since there is no platform to buy goods in our product, the users are free to investigate the retailers themselves which are helpfully managed in one section of this page.

##### Rules
Similar to the FAQ section, this details publisher-approved rules for the game but allows users/players to submit rules or corrections of the game to be considered by the publisher.

##### Ratings/Reviews
Ratings/reviews allow the user to see what others think of the game and also add their own review. The ratings can be filtered using the same method as in the search filters of the homepage- by source.

### 3.3.4 Community page
<p float="middle">
  <img src="https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/UI_design/UI_prototype/CommunityPage1.jpg" width="50%" />
</p>

#### Purpose
* To suggest communities and events near the user
* To find new communities and events using search tool

#### User Interaction
* Users can browse through community and event suggestions using image carousel. Click on the arrows to view previous or next suggestion/feed.
* Users can use search bar to find communities and events. Click ‘GO’ to make the search. 
* If user’s location is not specified, a prompt is displayed, redirecting users to account settings 

#### Control Flow
![Community](uploads/b941d6b2f17b47589096e3abe7f50525/Community.jpg)

##### Overview
There are two distinct layers to the community page- the first later is a homepage-like interface which displays suggested discussion threads (based on your games/communities) and allows users to search for communities. The layer below this, is the game-specific community page. 

##### Community home
The page serves the purpose of helping users navigate the communities. It is accessed from the home page by clicking on the "my communities" page. All pages are accessible through the search function and the suggested communities allows users to discover new games and conversations that similar users enjoyed.

##### Game specific community
This page hosts the discussion threads relating to specific threads, and also local clubs/events for that game. The local clubs and events are only displayed if location services have been allowed in the account settings and are displayed on an interactive map interface. The events are displayed in a calendar view. Users can comment on discussion threads for games regardless of whether they have added the game to their profile or not. This is the page users are directed to if they access a game specific community through another user's profile, or through the "suggested communities" links.

### 3.3.5 Account Settings page
<p float="middle">
  <img src="https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/UI_design/UI_prototype/AccountSetPage-1.jpg" width="50%" />
</p>

#### Purpose
* To set location settings, privacy and accessibility features.

#### User Interaction 
* ‘Location Sharing’, ‘Privacy’, ‘Text to Speech’ and ‘Closed Captions’ can be switched on/off using toggles
* Pop-up confirmation messages are displayed to confirm user’s action. 
* ‘Colour Theme’, ‘Text Size’ and ‘Languages’ options can be expanded and selections can be made using tick boxes. 

#### Control Flow
![Settings](uploads/c427847d2de286e0ae0a53842d9580d7/Settings.jpg)

##### Overview
The account settings are accessed through your own profile and detail the privacy, location, and accessibility settings which personalise the user's experience using the software.

##### Location Sharing
Location is only used to determine local clubs and events relating to games the user has searched for or is a player of. In particular, on the game-specific community page, the location is used to generate a map of the in-person clubs/meetups that are in the area.

##### Privacy
This allows the user to decide whether their own profile is publicly viewable or not. If set to private, users can still comment on community discussion threads, but other users cannot view the games or communities they play. If set to public, they can appear in general searches and their information is able to be viewed by any player.

##### Accessibility
Users can personalise their UI according to their personal needs in a variety of ways. these include text-to-speech, colour theme choice, and adjustable text size for users who are visually impaired and closed captions on video elements for users who are hearing impaired.

##### Language
Language settings are included to ensure users from all countries and backgrounds are able to use the software. This is particularly important as the larger the user base, the more information can be obtained to use to suggest relevant games/communities, and the more engagement there is with the discussion threads.

### 3.3.6 Publisher Interface
The idea of a separate interface for game publishers was explored, but when the technology required was discussed we concluded that we would focus on creating a slick and ergonomic interface for the players and focus our time on the one task. 

The idea was that publishers have a completely separate interface where they can read reviews posted on the website, review suggested rules or questions asked by players on the site, and choose whether to publish these on the game's page. In addition they could publish updates/bugfixes/new releases using the software which would be displayed on the main feed (homepage) of players who play that game.