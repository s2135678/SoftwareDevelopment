# 4 Prototype Evolution

The prototype can be found here: [prototype source code](https://git.ecdf.ed.ac.uk/sd202021groups/group_10/tree/master/Prototype)

## 4.1 Original Criteria
The prototype implements the login/sign up process and the game management functionality for a user's profile, where users are able to add, remove, view, and rate games which are registered in the system.
This is implemented in a command line user interface with clear instructions on how to progress to the next page of the system, or return to a previous page at each stage.

 The current prototype has 4 main functions: 

* Sign up, log in and log out
* Add/remove a game to/from players' collection
* View/add to a game's reviews
* Store data on file system

## 4.2 Alterations
The original control flows for the homepage (which encompasses the login functionality) and the game management are shown here:
![](https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/UI_design/Homepage%20.jpg)
![](https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/UI_design/Player.jpg)

The control flow for the prototype is shown below. As you can see, both the login/sign up and game management funcionalities are combined into one diagram:
![](https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/Prototype/Prototype.png)

As you can see, the functionality employed in the prototype is the core game management functionality and the login/sign up process as these were identified as two of the highest priority core functionality features. There have been some changes, however, including the detail involved in the login process. There were few considerations made in the  initial design for how this would be implemented, and after consideration as a group, it was decided that the details of users would be stored in a json file. This storage format is also applied to the game data accessed through the player page (title and reviews).

Functionality was simplified in the player page as only the user's own page could be viewed/edited. In addition to this, the "about" section was removed as this was not a core component of the system and it's purpose was mostly for other user's benefit. For the same reason, the community functionality was not implemented. These decisions were made to streamline the prototype and to have a clear structure with all chosen functionalities implemented fully.

At present, users can view the games they already own after logging in, and select the games they like from the complete game collection to add them to their game collection. The part relating to the ranking of the game has not yet been developed. The part relating to the game community has not been developed. The trading part of the game has not yet been developed. Sorting and displaying game reviews according to a certain weight has not yet been developed. These functionalities are all goals for the full implementation should the project be extended.

Compared with the system architecture made before, the current reading and storing of data does not operate through a database, but simply reads and writes to corresponding json files. The original plan was to publish this project to a cloud server with sufficient load capacity to run. At the same time, there are good front-end pages for the user to interact with. But at present, only u has a prototype of a part of the back-end logic part, and realizes the most basic part.

## 4.3 Evaluation of planned schedule and tasks
The workplan set out in submission two was almost completely disregarded as, following communication with the client, it was made clear that the prototype required significantly fewer features than originally planned for. Although this meant that the planned schedule was not followed, it meant that the team could be split more appropriately between tasks as opposed to all members working on different elements of the prototype to then be combined, which could results in a less cohesive final prototype.

## 4.4 Future work
The plan, however, is still valid going forward if full functionality is to be implemented as an extension. The same main structure and separation of tasks could be applied to the process of expanding the prototype. The list of functionalities mentioned previously, which are yet to be implemented would be allocated between the using the same system.

The additional core functionalities which would be the priority to implement are:
* Expansion pack management
* Filtering of reviews by source (and a weighting function)

Once these core functionalities are implemented, further extensions could be made. The function of the comment section will be further improved. Next the development of the function of the game community, and compatibility with the game review function, so that the two can work alongside each other. Then would be the completion of the design of the front-end page, complete the front-end interaction through appropriate adjustments, and storage of the data on the database, and deployment of the database on the cloud server. Finally a game system would be built where users can interact with the system through the front end, manipulate data from the database at the back end, and effectively interact between the front and back ends. The development and optimisation of the publisher interface, and assoiated authority for this interface would be the final stage of production. 

## 4.5 Team structure evaluation

### 4.5.1 Submission 3:
### Project Manager: Milly Kinghorn
* Responsibilities as with previous submissions

### Protoype Team: Hao Yang, Xiaoyu Wei, Milly Kinghorn
* Responsible for the development of the prototype after group discussion of core functionality to be implemented
* Responsible for the testing of the prototype to ensure it fails gracefully and there are no bugs
* Responsible for evaluating the evolution of the prototype from previous submissions and planning how it could be taken forward to full-funcionality

### Usability Team: Sera Choi, Gregor Rowley
* Responsible for the planning and justification of usability testing methods
* Responsible for development and deployment of tests
* Responsible for the analysis of usability tests and presenting results

### 4.5.2 Evaluation
The original team structure plan was very clear in the flexibility that was expected throughout the project Each of the three submissions required a very different set of skills and so no particular roles were assigned. For example, it would have been inappropriate to have "software developer" and "UI designer" as these roles would only be relevant for one of the submission. There was however, an overlap in the knowledge of different areas of the software which made for a more natural fit to certain roles. For example, Hao and Xiaoyu were initially responsible for the software design in submission 1. This meant that, although everyone in the group understood the principles, they had a deeper knowledge of the technical details required. This  meant that when implementing the prototype, they took on the majority of responsibility with the programming involved in producing a viable and working product.

As part of the risk analysis, we identified a number of risks posed by issues in the team. These were all mitigated as detailed in the analysis and as a result the team structure had no negative impact on the subsequent submission.

In addition to this, Milly remained project manager throughout, as was stated in the original team structure plan.