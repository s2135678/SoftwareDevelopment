# Risk Analysis

## Risk assessment method
A qualitative risk assessment strategy was applied to the project, with the risks identified. For every risk, the probability and impact were evaluated using categories shown below: <br> 
* **Probability of risk**: Unlikely, Possible, Probable, Certain <br>
* **Impact of risk**: Negligible, Moderate, Severe, Catastrophic <br>

After assessing the risk probability and impact, risk priority was determined using the risk matrix below:
<p float="left">
  <img src="https://git.ecdf.ed.ac.uk/sd202021groups/group_10/raw/master/Risk%20Analysis/Slide1.png" width="70%" />
</p>

## Risk control method
We identified 7 ways of risk control: <br>
1. **Avoid** the risk by not accepting any situation that carry risk 
2. **Transfer** the risk from one part of a system to another to reduce the risk
3. **Buy** information about the risk  
4. **Eliminate** the risk by removing any exposure
5. **Assume** that the risk can happen and be ready to handle it
6. **Publicise** the risk to customers to minimise the shock when it occurs 
7. **Control** the risk by altering the schedule to minise its effect

## Risk categories 
Risks are categorised into 4 groups:
1. **Scheduling**: risks associated with project planning, estimation and team performance
2. **Operational**: risks associated with implementation of prototype 
3. **Technical**: risks associated with software performance and function 
4. **Programmatic**: risks from external sources 

### Scheduling Risks 
| **Risk** | **Probability of risk** | **Impact** | **Risk Priority** | **Resolution Method** | **Resolution Strategy**|
| ------ | ------ | ------ | ------ | ------ | ------ |
|Uneven workload split between team members|Possible|Negligible - easily resolved and minimal impact on the final prototype's quality|Low|Control|Split workload broadly between sub teams so team members stay focussed on their area and from here split workload based on time as opposed to number of tasks|
|Individual falling behind on workload|Probable|Severe - can cause changes to the time and effort estimate for prototype development, resulting in unfinished prototype or submission|High|Control|Project Manager individually check in with team members. Internal deadlines set before final deadline. Collaborative sub-teams to encourage participation and help pick up slack if necessary|
|Lack of communication between different sub teams resulting in an incoherent prototype|Unlikely|Moderate - could result in a prototype which does not function properly because different areas have not been consolidated|Medium|Control|Regular (every 3-4 das) whole-team meetings to present progress and ask questions|
|Poor effort and time estimate for prototype development| Possible | Severe - fail to produce a functioning prototype in time. Tasks that depend on completion of other tasks are not accomplished|High|Control|Discuss the appropriate time and effort estimate for tasks familiar to team members. For unfamiliar tasks, consult with experts or obtain information from International Software Benchmarking Standards Group|
|Disputes among team members|Unlikely|Moderate - disputes on project decisions can be resolved by the group, personal disputes cause a bigger problem as it may impact on the quality and timeliness of the prototype|Low|Avoid|Democtratic vote for disagreements on project decisions (since 5 members a majority rules), for personal disputes, have to prevent with open communication lines and honesty|
|Time difference in working hours|Certain|Negligible - the work will still get done, just with more asynchronous communication at times|Trivial|Control|Ensure group meetings are at a social time for everyone in the group (10am - 2pm UK time)|
|Team member unable to continue|Unlikely|Moderate - would require a reallocation of the tasks with potentially minimal notice and would put a strain on the rest of the team. The prototype may be incomplete with components missing and low-quality|Low|Assume|It is out of our control, but would require fast action to ensure all areas required for the project can still be completed|

### Operational Risks 
| **Risk** | **Probability of risk** | **Impact** | **Risk Priority** | **Resolution Method** | **Resolution Strategy**|
| ------ | ------ | ------ | ------ | ------ | ------ |
|Technology required to develop prototype is not available on all team members' personal machines e.g. mixture of windows and mac|Probable|Moderate - may cause uneven distribution of tasks as only those with compatible PC can complete the tasks. If this is the case for majority of tasks, it may result in unfinished prototype with partially completed tasks|Medium|Control|Discuss personal computer models before technology is chosen and research technology compatible with all if they are different|
|No team member has sufficient skills in implementing a specific area of the prototype|Possible|Severe - If the component is core to the software, the product may not address core functionalities. Else, the quality may be poor|High|Eliminate|Remove this specific area from the prototpe as there is not sufficient time to train individuals within the schedule|
|Faulty development tools|Possible|Severe - If the development tool breaks down in the midst of development, moderate-to-severe changes could be made to the prototype to finish in time. Fixing the issue or switching to a different tool may take time, causing changes to the time and effort estimate|High|Avoid| Assess the reliability of development tools before choosing|
|Version control system breaks down|Unlikely|Moderate - Unable to track changes and work together on the prototype. May cause disruptions to time and effort estimate as switching to a different version control system takes time|Low|Assume|Be aware of the possibility and have an alternative version control system in mind to switch to when this happens. Communicate through other methods to notify team members about changes made to the code|
|Usability testing failure|Possible|Severe - unable to evaluate the prototype and identify issues with the design. The quality of final product is low and difficult to use|High|Eliminate|Careful testing design, taking account of the current pandemic|

### Technical Risks 
| **Risk** | **Probability of risk** | **Impact** | **Risk Priority** | **Resolution Method** | **Resolution Strategy**|
| ------ | ------ | ------ | ------ | ------ | ------ |
|Unexpected changes to design|Unlikely|Severe - causes major changes to architecture, UI, and prototype. Impacts all tasks associated with the UI, Operation & Maintenance and Development components|High|Avoid|If the changes are severe and cannot be implemented in time, reject the change. If achievable, re-evaluate the time and effort estimate and follow swiftly|
|Extra functionality|Unlikely|Moderate - If the functionality is core to the software, it may cause severe changes to the architecture, UI and prototype. All core components (UI, Operation/Maintenance and Development) are affected. If the functionality is trivial, may have local impacts on the components|Low|Eliminate|Assess the requirements of the new functionality and remove if the task is unfamiliar and time consuming|
|Final product fails to perform core functionalities|Possible|Catastrophic - project failure|High|Eliminate|Prioritise tasks to ensure core functionalities are addressed and tested first. Use prototypes to identify potential issues that may rise during final product development|
|Low quality of final product|Possible|Moderate - Non-funtional requirements are not addressed and customers are dissatisfied with the product|Low|Avoid|Good project planning and estimation to ensure non-functional requirements are also addressed in the time given|

### Programmatic Risks 
| **Risk** | **Probability of risk** | **Impact** | **Risk Priority** | **Resolution Method** | **Resolution Strategy**|
| ------ | ------ | ------ | ------ | ------ | ------ |
|Changes to data protection policy|Possible|Moderate - may require changes made to the Operation & Maintenance component|Low|Assume|Changes in data protection policy cannot be predicted, but if changes are required, the team is prepared to modify the design and architecture|
|New functionality suggestion from customer|Unlikely|Moderate - may cause moderate-to-severe changes to the architecture and design. Depending on the functionality, all core components are affected|Low|Avoid|Dependent on the new functionality. If the risk is too high, remove. If moderate, renegotiate with the customer|