# fhlbc-collaboration
This repo gives our Code Warrior group a place to practice concepts and best practices.

---

### Steps to complete before March 10, 2023 

- Send a message to @Sarah in our Code Warriors teams channel with your GitHub Username

**NOTE** _Your username is what you are 'Signed in as' and not the name you enter in your profile_
- Once I confirm you have been added to the list of Collaborators in GitHub, clone a local copy of this repo
- Change directories into the repo (you should see branch name `main` added in the terminal)
- Create a new branch from `main` to one called `merges`
  - run `git checkout -b merges`
  - run `git pull origin merges` to get the latest changes on this branch
- Create a text file with your name in the following format: `first_last.txt`
- Push your new file to the `merges` branch 
  - run `git add .` OR `git add <filename>`
  - run `git commit -m '<commit message here>'`
  - run `git push origin merges`

**NOTE** _Read the terminal output to be sure your code is in the repo!_
  - Your push will fail if you are on the `main` branch 
  - Your push could also fail if someone else has pushed a change between your cloning the repo and your push of code
  - If your push fails, check the branch, try running `git pull origin merges`, and then run the push code again

If everything worked as expected, the `merges` branch in the GitHub GUI should now contain your text file.
