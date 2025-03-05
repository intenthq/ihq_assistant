Definition of done

These are a list of requirements that the story must adhere to in order for the sprint team to consider it complete or done. The team can use this as a check list.

This is the state we want to achieve.

## Progression of ticket in each column of Jira Board
| Column 1 | Column 2 | Column 3 |
| --- | --- | --- |
| **State Activity** | **State Activity** |  |
| New | Definition of ready met<br/>Relevant documentation / diagrams produced and/or updated<br/>Stories (or Epic) with High Privacy Risk implications have been raised with the DPO, Security and a high level discussion has been had. |  |
| Ready/ To Do | Prioritised by the PO (Refined and agreed by the team) |  |
| In Dev  | Code produced (all “sub-task“ items against the story are completed). Unit tests written and passing.<br/><br/>Code quality gates passed  <br/>Pull Request Quality Gate Setup |  |
| Code Review | 1 PR reviewer<br/>Code commented, checked in and run against current version in source control. Pipeline has been setup and all the variable dependencies have been resolved. Builds generated without failures<br/>Test scripts |  |
| Ready for Testing | Passes all testing per acceptance criteria<br/><br/>Testing automation: script of testing automation must be updated for sprint user stories.  <br/>No P1 or P2 defects. |  |
| Testing | Passes all testing per acceptance criteria<br/><br/>Testing automation: script of testing automation must be updated for sprint user stories.  <br/>No P1 or P2 defects. |  |
| PO Review | Passes all testing per acceptance criteria<br/>P3 bugs can remain open with resolution plan approved by PO<br/>P4 bugs can remain open without resolution plan. |  |
| Ready for Release  | Merge to develop  <br/>Passed regression |  |
| Completed  | Story has been accepted by PO and meets Definition of Done and is able to be shown in Sprint Review. |  |