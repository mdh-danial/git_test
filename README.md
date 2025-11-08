# Using Git 
Using common git commands to publish project on GitHub. A basic Python program that asks for user's name.

## About / Overview
Get to know how to use git commands, what they do, and when to call it
1. git add
    - stages a chosen file, allows git to keep track of file (e.g. for updates)
    - files that have been staged then committed will no longer be staged, and can straight away run git commit without needing to stage it again

2. git commit -m "message"
    - Saves updates to a staged file and provides a message to help user keep track
    - requires file to be staged or have previously been committed

3. git clone 
    - allows user to clone / copy a repo from github to their computer
    - repo can be edited without affecting original copy

4. git status
    - check tracking status of files in repo
    - check which branch user is currently on
    - check commits 

5. git branch
    - shows all branches of the repo
    - adding branch name after git branch creates a new branch
    - allows user to make updates to code without affecting the original code. 

6. git checkout
    - allows user to switch to a different branch
    - requires name of branch to move to

7. git merge
    - once edits have been made on a different branch, user can choose to merge the edit to the main branch
    - checkout to branch you want the edit to be merged to
    - run git merge branch name

8. git push
    - once you have done all the commits, run git push to update the repo on Github
    - include name of branch you want to update on github

9. git pull
    - similar to git push except you receive updates of repo from github to your local computer

10. Merge conflicts
    - when two different commits conflict with eachother
    - requires user to manually resolve the conflict




## Features
- Ask for user's name
- Greet user by their name 
- Spell the user's name letter by letter
- Create a pyramid based on the number of letters in user's name

## Installation
```bash
git clone https://github.com/mdh-danial/git_test.git
cd git_test
python hello.py

