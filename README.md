# gitgoing

[![Build Status](https://travis-ci.org/CodeNeuro/gitgoing.png?branch=master)](https://travis-ci.org/CodeNeuro/gitgoing) 
[![Join the chat at https://gitter.im/CodeNeuro/gitgoing](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/CodeNeuro/gitgoing?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Get going with contributing to open-source software

* Free software: BSD license
* Documentation: https://gitgoing.readthedocs.org.

## Prerequisistes: Installing Git and Python

1. Make a github account
2. Create a folder for all your code.
  * Mac: 
2. Install git on your computer
  * Mac - Comes with git but you can update it if you want via `homebrew`.
    1. Create a folder `~/code` by typing into the terminal `mkdir ~/code`
      * (feel free to use your own code folder if you already have one that you like)
    2. OPTIONAL: Use homebrew http://brew.sh (it's a great package manager for installing command line apps!)
      * Install by pasting this into your terminal: `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
      * If you don't have `git` installed, type `brew install git` to install it!
  * Windows
    1. Install gitextensions here: http://sourceforge.net/projects/gitextensions/
    2. Create a folder `C:\code` by typing into powershell `mkdir C:\code`
      * (feel free to use your own code folder if you already have one that you like)
3. Install Anaconda Python distribution found here: http://continuum.io/downloads
  * Make sure to use the Python 2.7 version. You can verify that your computer has Python 2.7 by typing `python --version` into your terminal.

## Setting up your environment

"Environments" are sandboxes where you can install python package of specific versions, and then they don't conflict with other versions. They're very helpful if you're testing your software package with different versions of programs like `numpy` or `scipy` but don't want to mess up your own installation.

1. Create a gitgoing-specific `conda` environment by typing at the Terminal (for Mac and Linux) or Anaconda Terminal (for Windows). We'll install `pip` (package to install python packages - yes it's very meta) and `numpy` (matrices in python).

```
conda create --yes --name gitgoing pip numpy pytest
```
You should get output that looks like this:
```
Fetching package metadata: ....
Solving package specifications: ................
Package plan for installation in environment /Users/olga/anaconda/envs/gitgoing:

The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    pytest-2.8.1               |           py27_0         219 KB

The following NEW packages will be INSTALLED:

    numpy:      1.10.1-py27_0
    openssl:    1.0.2d-0     
    pip:        7.1.2-py27_0 
    py:         1.4.30-py27_0
    pytest:     2.8.1-py27_0 
    python:     2.7.10-2     
    readline:   6.2-2        
    setuptools: 18.4-py27_0  
    sqlite:     3.8.4.1-1    
    tk:         8.5.18-0     
    wheel:      0.26.0-py27_1
    zlib:       1.2.8-0      

Fetching packages ...
pytest-2.8.1-p 100% |################################################################################################################################| Time: 0:00:00 639.21 kB/s
Extracting packages ...
[      COMPLETE      ]|###################################################################################################################################################| 100%
Linking packages ...
[      COMPLETE      ]|###################################################################################################################################################| 100%
#
# To activate this environment, use:
# $ source activate gitgoing
#
# To deactivate this environment, use:
# $ source deactivate
#

```

2. Let's activate the environment with the instructions above.
3. Now that we have our environment setup, fork this repo by clicking the `Fork` button in the top right corner on the github page for this repo: https://github.com/CodeNeuro/gitgoing
4. Clone the fork that you just made by clicking the url to clone on the right side of the github page of your fork. Then browse in your terminal to your code folder `cd ~/code` and then type in the clone command: `git clone https://github.com/yourgithubname/gitgoing`
5. Move into the folder via `cd gitgoing`, then make sure the clone worked by typing `git status`, and you should see:

```
On branch master
Your branch is up-to-date with 'origin/master'.
```


## Let's learn Git

1. Make a change (aka edit) to a file in your cloned repo and save the change locally. Try making a change to this README.md file by adding content to the bottom of it.
2. Type `git status` in the terminal to see what's up. Type `git diff` to get a detailed list of differences. Use `j` and `k` to navigate up and down the diff, and `q` to end the diff.
3. Type `git commit -am "message for the commit"` to create a new commit
  - Look, `git` is teaching you life lessons like overcoming fear of commitment :)
4. Type `git status` to see what's up.
5. Type `git push` to push your changes up to the github server.
6. If you made a change to the README.md file, you should see it changed on your fork's github page.
7. Type `git branch` to list out the current local branches
8. Type `git checkout -b newbranch` to create a new branch
9. Make a commit onto the branch, and push the changes up to github.
   Note: You will need to use the branch name in the push, e.g. if my branch is called `smallchange`, I would push via `git push origin smallchange`
  - BONUS: Make a merge conflict! Make *another* branch and edit the `README.md` file. Now make **another** branch and edit the `README.md` file *on the same line*. Try to push both branches. You should get a merge conflict. This is good. See, git is teaching you yet another life lesson: dealing with conflict!
10. You should see your new branch up on your fork's github page.

## Let's make a real contribution
1. You can run the test suite by typing `py.test` (pronounced "pie test") in the repo's root directory. This is a python package that will execute the tests and print out the results.
2. Open up the test file `tests/test_gitgoing.py` in your favorite editor
3. Comment out the test named `test_cv_broken` by removing the # characters at the beginning of each line of the test in the `test_gitgoing.py` file.
4. Run the tests again and watch it fail. You should see this kind of message:

```
============================================================================= test session starts ==============================================================================
platform darwin -- Python 2.7.9 -- py-1.4.25 -- pytest-2.6.3
plugins: cov
collected 8 items 

tests/test_gitgoing.py ..F....X

=================================================================================== FAILURES ===================================================================================
___________________________________________________________________________________ test_cv ____________________________________________________________________________________

x_norm = array([[ -3.78944360e-01,   1.02198073e+00,  -1.18127826e+00,
         -2.7882...2.19688063e+00,   1.71670354e-01,  -1.37347439e+00,
          5.33478606e-01]])

    def test_cv(x_norm):
        from gitgoing.gitgoing import std, mean, cv
    
        test_cv = cv(x_norm)
        true_cv = std(x_norm)/mean(x_norm)
    
        # This test will fail
>       assert test_cv == true_cv
E       assert 0.51026948757496537 == 1.9597487687387671

tests/test_gitgoing.py:47: AssertionError
================================================================ 1 failed, 6 passed, 1 xpassed in 0.23 seconds =================================================================
```
  - BONUS: Notice the `@pytest.fixture` "decorator" on the function `x_norm` (in Python, these things above functions are called decorators. If you're familiar with lambda calculus, they are closures). What does this do to the function?
4. Use your new knowledge of `git` to fix the test!
  1. Create a branch `git checkout -b myfixbringsalltheboystotheyard` 
  2. Fix the test by editing files, using Sublime text
  3. Add and commit the changes `git commit -am "fixed test_cv_broken"`
  4. Push to your new branch `git push origin myfixbringsalltheboystotheyard`
5.  Run the tests again and watch it succeed.
6. Create a pull request back to the original repo that you forked by going to 
   your `gitgoing` repo website (`github.com/yourgithubusername/gitgoing`),
   and pressing the green "compare" button next to the branches, which looks 
   like this: ![](http://i.imgur.com/xKzb8v7.png)
7. And that's how you contribute to open source software!

## Build the documentation
A key part of any open source project is documenting it! The [sphinx](link) library makes it really easy to add documentation to a project, which you can then host for free on [github pages](link).

We're currently doing that for this repository, you can see the documentation page [here](http://codeneuro.org/gitgoing)

To see where the documentation comes from, you can build it yourself locally. If you've cloned this repository, just navigate to the `docs` folder, and then enter

```
sphinx-build -a . build
```

This creates a set of `.html` files in the folder `build`. If you go into that folder and double-click `index.html`, it should open in a web browser, and you'll see something that looks just like the webpage mentioned above.

Sphinx takes a little bit of configuration, but can automatically generate a page directly from your Python package, including the documentation you provide for your classes and methods. And you can regenerate the documentation whenever you change the code. This makes it easy to automatically document your project and keep the documentation up to date.

## You're done!

Awesome job! If you want to learn more about 

### Github links

- [Understanding Git Conceptually](http://www.sbf5.com/~cduan/technical/git/)
- [Think like (a) git](http://think-like-a-git.net/)

### Python packaging

- [Python Packaging User Guide](https://python-packaging-user-guide.readthedocs.org/en/latest/) (crowdsourced, more authoratative)
- [How to package your Python Code](http://python-packaging.readthedocs.org/en/latest/)

### Pytest links

- [Introduction to Pytest](http://pythontesting.net/framework/pytest/pytest-introduction/)
- [Official Documentation](http://pytest.org/latest/)
