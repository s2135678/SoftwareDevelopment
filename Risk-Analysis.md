# Risk Analysis

## Risk assessment method
The process of analysing risks to the project starts with identifying any and all risks which pose a threat to the development of the prototype. In order to determine these risks, a qualitative risk assessment strategy was applied. This was chosen in favour of a quantative approach because the project did not have any monetary motivation i.e. there was no financial cost assosiated with delays or number of working hours like there would be for a real software development project. This means that all the risks identified impact on the quality of the prototype and the timeliness of it's development only. In addition, although a quantative approach would make it easier to categorise and prioritise the mitigatin of risks (as they can be easily ranked against each other), there are very few ways to assign a value to the different elements of this specific project, and so a qualitative, but detailed method is preferred. For every risk, the probability and impact were evaluated using categories shown below: <br> 
* **Probability of risk**: Unlikely, Possible, Probable, Certain <br>
* **Impact of risk**: Negligible, Moderate, Severe, Catastrophic <br>

After assessing the risk probability and impact, risk priority was determined using the risk matrix below:
<p float="left">
  <img src="https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/Risk%20Analysis/Slide1.png" width="70%" />
</p>

## Risk control method
In order to mitigate the risks, a strucured response is required. The goal is to address the risks now so they don't happen (or we are at least prepared for them) as opposed to waiting for something to go wrong during the development stage when there is more to lose if time is spent solving problems that could be avoided or solved earlier.
The 7 was identified to control risk were: <br>
1. **Avoid** the risk by not accepting any situation that carry risk 
2. **Transfer** the risk from one part of a system to another to reduce the risk
3. **Buy** information about the risk  
4. **Eliminate** the risk by removing any exposure
5. **Assume** that the risk can happen and be ready to handle it
6. **Publicise** the risk to customers to minimise the shock when it occurs 
7. **Control** the risk by altering the schedule to minimise its effect

## Risk categories 
Risks are categorised into 4 groups:
1. **Scheduling**: risks associated with project planning, estimation and team performance
2. **Operational**: risks associated with implementation of prototype 
3. **Technical**: risks associated with software performance and function 
4. **Programmatic**: risks from external sources 

### Scheduling Risks 
| **Risk** | **Probability of risk** | **Impact** | **Risk Priority** | **Resolution Method** | **Resolution Strategy**|
| ------ | ------ | ------ | ------ | ------ | ------ |
|Uneven workload split between team members|Possible|Negligible - easily resolved and minimal impact on the final prototype's quality. Affects overall project, not task specific.|Low|Control|Split workload broadly between sub teams so team members stay focussed on their area and from here split workload based on time as opposed to number of tasks|
|Individual falling behind on workload|Probable|Severe - can cause changes to the time and effort estimate for prototype development, resulting in unfinished prototype or submission. Affects overall project, not task specific.|High|Control|Project Manager individually check in with team members. Internal deadlines set before final deadline. Collaborative sub-teams to encourage participation and help pick up slack if necessary|
|Lack of communication between different sub teams resulting in an incoherent prototype|Unlikely|Moderate - could result in a prototype which does not function properly because different areas have not been consolidated, Affects overall project, not task specific.|Medium|Control|Regular (every 3-4 das) whole-team meetings to present progress and ask questions|
|Poor effort and time estimate for prototype development| Possible | Severe - fail to produce a functioning prototype in time. Tasks that depend on completion of other tasks are not accomplished. Affects overall project, not task specific.|High|Control|Discuss the appropriate time and effort estimate for tasks familiar to team members. For unfamiliar tasks, consult with experts or obtain information from International Software Benchmarking Standards Group|
|Disputes among team members|Unlikely|Moderate - disputes on project decisions can be resolved by the group, personal disputes cause a bigger problem as it may impact on the quality and timeliness of the prototype. Affects overall project, not task specific.|Low|Avoid|Democtratic vote for disagreements on project decisions (since 5 members a majority rules), for personal disputes, have to prevent with open communication lines and honesty|
|Time difference in working hours|Certain|Negligible - the work will still get done, just with more asynchronous communication at times. Affects overall project, not task specific.|Trivial|Control|Ensure group meetings are at a social time for everyone in the group (10am - 2pm UK time)|
|Team member unable to continue|Unlikely|Moderate - would require a reallocation of the tasks with potentially minimal notice and would put a strain on the rest of the team. The prototype may be incomplete with components missing and low-quality. Affects overall project, not task specific.|Low|Assume|It is out of our control, but would require fast action to ensure all areas required for the project can still be completed|

### Operational Risks 
| **Risk** | **Probability of risk** | **Impact** | **Risk Priority** | **Resolution Method** | **Resolution Strategy**|
| ------ | ------ | ------ | ------ | ------ | ------ |
|Technology required to develop prototype is not available on all team members' personal machines e.g. mixture of windows and mac|Probable|Moderate - may cause uneven distribution of tasks as only those with compatible PC can complete the tasks. If this is the case for majority of tasks, it may result in unfinished prototype with partially completed tasks. Affects tasks involving interface as the formatting may be different. |Medium|Control|Discuss personal computer models before technology is chosen and research technology compatible with all if they are different|
|No team member has sufficient skills in implementing a specific area of the prototype|Possible|Severe - If the component is core to the software, the product may not address core functionalities. Else, the quality may be poor. Affects the specifc tasks for which we are lacking in skill.|High|Eliminate|Remove this specific area from the prototpe as there is not sufficient time to train individuals within the schedule|
|Faulty development tools|Possible|Severe - If the development tool breaks down in the midst of development, moderate-to-severe changes could be made to the prototype to finish in time. Fixing the issue or switching to a different tool may take time, causing changes to the time and effort estimate. Affects overall project, not task specific.|High|Avoid| Assess the reliability of development tools before choosing|
|Version control system breaks down|Unlikely|Moderate - Unable to track changes and work together on the prototype. May cause disruptions to time and effort estimate as switching to a different version control system takes time. Affects project as a whole- spcifically tasks which are split between team members.|Low|Assume|Be aware of the possibility and have an alternative version control system in mind to switch to when this happens. Communicate through other methods to notify team members about changes made to the code|
|Usability testing failure|Possible|Severe - unable to evaluate the prototype and identify issues with the design. The quality of final product is low and difficult to use. Affects overall project, encompassed in the "Testing" task which runs throughout.|High|Eliminate|Careful testing design, taking account of the current pandemic|

### Technical Risks 
| **Risk** | **Probability of risk** | **Impact** | **Risk Priority** | **Resolution Method** | **Resolution Strategy**|
| ------ | ------ | ------ | ------ | ------ | ------ |
|Unexpected changes to design|Unlikely|Severe - causes major changes to architecture, UI, and prototype. Impacts all tasks associated with the UI, Operation & Maintenance and Development components.|High|Avoid|If the changes are severe and cannot be implemented in time, reject the change. If achievable, re-evaluate the time and effort estimate and follow swiftly|
|Extra functionality|Unlikely|Moderate - If the functionality is core to the software, it may cause severe changes to the architecture, UI and prototype. All core components (UI, Operation/Maintenance and Development) are affected. If the functionality is trivial, may have local impacts on the components|Low|Eliminate|Assess the requirements of the new functionality and remove if the task is unfamiliar and time consuming|
|Final product fails to perform core functionalities|Possible|Catastrophic - project failure|High|Eliminate|Prioritise tasks to ensure core functionalities are addressed and tested first. Use prototypes to identify potential issues that may rise during final product development. Affects overall project, not task specific.|
|Low quality of final product|Possible|Moderate - Non-funtional requirements are not addressed and customers are dissatisfied with the product|Low|Avoid|Good project planning and estimation to ensure non-functional requirements are also addressed in the time given|

### Programmatic Risks 
| **Risk** | **Probability of risk** | **Impact** | **Risk Priority** | **Resolution Method** | **Resolution Strategy**|
| ------ | ------ | ------ | ------ | ------ | ------ |
|Changes to data protection policy|Possible|Moderate - may require changes made to the Operation & Maintenance component|Low|Assume|Changes in data protection policy cannot be predicted, but if changes are required, the team is prepared to modify the design and architecture|
|New functionality suggestion from customer|Unlikely|Moderate - may cause moderate-to-severe changes to the architecture and design. Depending on the functionality, all core components are affected|Low|Avoid|Dependent on the new functionality. If the risk is too high, remove. If moderate, renegotiate with the customer|
| Competitor software grows rapidly to threaten our userbase|Possible|Moderate- may cause some users to leave but most will stay with the software they are used to and comfortable with. More likely to impact new user sign-ups. Affects database as the potential capactity for users will not be used and may need to be scaled down.|Low|Buy|Get information about the competitor in question and investage the reason for their relative success in order to improve our own software.|
|Deadline for assignment is changed/brought forward.|Unlikely|Severe- the entire schedule will have to be restructured to accomodate the new end date. Affects all core components of the system, but particularly tasks scheduled towards the end e.g.Component optimisation, GUI optimisation, and database design.|High|Assume|Stay vigilant and up to date with the course announcements and be ready to adjust the schedule if it needs to be.|