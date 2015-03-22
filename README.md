# gitgoing
Learn to use and contribute to open source software

## Setting up your environment
1. Make a github account
2. Install git on your computer
  * Mac (NOTE: doesn't it come with git? What do we need homebrew for?)
    1. Use homebrew http://brew.sh
    2. Install by pasting this into your terminal: `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
    3. Create a folder `~/code` by typing into the terminal `mkdir ~/code`
      * (feel free to use your own code folder if you already have one that you like)
  * Windows
    1. Install gitextensions here: http://sourceforge.net/projects/gitextensions/
    2. Create a folder `C:\code` by timping into powershell `mkdir C:\code`
      * (feel free to use your own code folder if you already have one that you like)
3. Install Anaconda Python distribution found here: http://continuum.io/downloads
  * NOTE: We should be explicit about what version of python we ask them to use
  * Make sure to use the Python 2.7 version. You can verify that your computer has Python 2.7 by typing `python --version` into your terminal.
4. Fork this repo by clicking the `Fork` button in the top right corner on the github page for this repo: https://github.com/CodeNeuro/gitgoing
5. Clone the fork that you just made by clicking the url to clone on the right side of the github page of your fork. Then browse in your terminal to your code folder `cd ~/code` and then type in the clone command: `git clone {url_of_your_fork}`

## Let's learn Git
1. Make a change (aka edit) to a file in your cloned repo and save the change locally. Try making a change to this README.md file by adding content to the bottom of it.
2. Type `git status` in the terminal to see what's up. Type `git diff` to get a detailed list of differences. Use `j` and `k` to navigate up and down the diff, and `q` to end the diff.
3. Type `git commit -am "{message for the commit}"` to create a new commit
4. Type `git status` to see what's up.
5. Type `git push` to push your changes up to the github server.
6. If you made a change to the README.md file, you should see it changed on your fork's github page.
7. Type `git branch` to list out the current local branches
8. Type `git checkout -b {branch_name}` to create a new branch
9. Make a commit onto the branch, and push the changes up to github.
10. You should see your new branch up on your fork's github page.

## Let's make a real contribution
1. You can run the test suite by `HOW?`
2. Comment out the test named `BrokenTest1` by removing the # characters at the beginning of each line in the `BrokenTestCases` file.
3. Run the tests again and watch it fail.
4. Fix the test! Run the tests again and watch it succeed.
5. Create a pull request back to the original repo that you forked by `HOW?`
6. And that's how you contribute to open source software!

## Additional useful links
http://www.sbf5.com/~cduan/technical/git/
