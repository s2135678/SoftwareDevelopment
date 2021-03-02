# Planning and Scheduling   
## 1. The Development Model

   Based on the main purpose of this mission, we chose Evolutionary Prototyping development model. In the entire development process, first determine the overall architecture of the system and the specific technologies to be used in each part. Effectively dock the interface between the front and back ends and the interface between the back end and the database. Then develop the project prototype according to the UI design -> development mode. The development sequence is: main interface, login interface, community interface, game management interface, rules interface, comment interface, developer interface. After the development of each component is completed, add it to the project prototype, and then continue the development of the next component.

   ![](https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/planning_and_scheduling/Evolutionary.png "Developmemnt Model") 

   

## 2. Work Break Structure

   As we already have the architecture in submission 1, we can split the whole task to small tasks (Product Hierarchy).
     ![](https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/planning_and_scheduling/Hierachy.png "WBS") 

   There are three main parts when we develop the system:

   *  UI. Simple interface 
      
      UI design is singled out as a large subtask, and then classified according to the different components designed, mainly divided into 6 categories. Because the development model of our choice is Evolutionary Prototyping, we take the completion of small components as the primary goal. On the basis of the smooth operation of the small components, all the components are spliced together to complete the development of the entire prototype. In the UI design part, first design the layout of each page, as well as the main buttons to be included and their corresponding functions. On this basis, front-end developers implement the entire layout and button functions.
   

   * Operation & Maintenance

     * Database
     
        In this task, we will compare different kinds of databases (such as relational model, graph like model and document model) and select the suitable one. The evaluation conditions include relationships between objects (such one-to-many, many-to-one and many-to-many), read and write rate (such as the rate of querying and updating), reliability, scalability and maintainability.
        

     
     * Version Control & Recall(unnecessary)
     
        Version Control will be throughout the whole process of software development. The prototype, risk analysis, software structure and requirements engineering all need version control. Because software usually needs to roll back to old versions. Also, a software commonly provides several versions to users, such as a stable version (or long time support version LTS) and a preview version.
        
     * Release Product
     
     After the entire system design is completed, how to publish the system to a suitable platform will be the next key issue. The platform on which this system relies must have sufficient bandwidth and storage space, while at the same time satisfying data security and system robustness
     

   * Development
   
     For Web software development, the client-server is commonly used. In this model, the program runing on the server is often called the back-end, and the program running on clients is often called the front-end. It is straight forward to break the software into these two parts.

     * The front end 
    
        The responsibility of front end is accepting inputs from users, converting them to "valid" commands and sending them to the back-end server. Then the server returns some message to front-end, and the front-end renders the message so that users can see software's reponse on their screens. The program of the front-end should handle events occuring on GUI. For example, if a user clicks a button using the mouse or does a gesture on their smart phone, the front-end should start using corresponded control-flow. 
        
        Sub-tasks of the front-end are based on both the GUI design and the control flow.
        
        
     * The back end
     
        The program deployed on back-end (or server) involves all functionality implementations of the software. Some frameworks (such as Spring Boot and Flask) can be used here to make the software structure more clear. Also, the interface between back-end and front-end is very important. 
        
        Sub-tasks in back-end are based on the software's functionality and control flow. 
        
        
       There are more details about the little tasks of the three main parts.
         ![](https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/planning_and_scheduling/Product.png "Little Tasks") 

## 3. Tasks Dependencies

Before writing the prototype, all team members should get familiar with the software architecture and learn the techniques which will be used, including Python, Flask, CSS and so on. At the same time, the GUI designing can start, because there is not so much technical demand for this task.
    
At the second stage, functionalities of the software will be implemented one by one, which includes login/logout, player's homepage, game community, publisher's homepage, game rules and reviews. For each sub-task, we should firstly design the GUI and then implement the frontend and backend. At the same time, database designing can start.
    
At the third stage, after all GUIs have been implemented, we can start the GUI optimization. Also, components optimization will start after all tasks of frontend/backend have been finished.
    
At the final stage, the software will be deployed and released.
    
Also, software testing runs through all stages because we will use Test Driven Development (TDD).

## 4. Gantt Chart

   ![](https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/planning_and_scheduling/Task_Dependencies.png "Gantt Chart")

# Team Structure
Changes to the team structure are as follows:

## Project Manager: Milly
Milly will continue as our project manager as Milly has experience of working with this team from the previous assignment.

## Risk Analysis Team: Sera, Milly, Gregor

## Planning and Development Team: Hao, Xiaoyu
In the previous assignment, Hao and Xiaoyu were responsible for the software architecture. 
As Hao and Xiaoyu have knowledge of inner workings of the software, and have experience of working together, they were allocated to the 'Planning and Development' section of the project.    
