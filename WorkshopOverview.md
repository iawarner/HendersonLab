# Delta Workshop for Lab Retreat 2022
# Author: Isabel Warner
# Date: 29May2022

## Goals 
1. Familiarize with terminal window & scripting programs 
2. Download scripts from git 
3. Sign in to the cluster 
4. Upload scripts and data to the cluster
5. Look at data 
6. Unpack scripts 
7. Load modules and run scripts 
8. Download data
9. Visualize data 
10. Basic unix commands 

## Prerequisites 
1. Delta account
2. Terminal program (terminal or windows terminal; powershell as a last resort)
3. Text editor (Sublime suggested, but VSC and atom work too, text wrangler as a last resort)
4. Administrator control of your laptop (if things need to be installed, hopefully won't need this)

## Resources
1. Delta wiki: 
2. The difference between powershell and windows terminal: https://www.makeuseof.com/windows-terminal-vs-powershell/
3. 

## Part 1: Open this file 
Congrats! You've opened this file in a text editor! 

## Part 2: Github  
Go to this git page: https://github.com/iawarner/HendersonLab 
First we'll page around. 
The first page you should look at in a github repository is the README.md file, which will usually be on the first page. 
It'll explain what the software is doing, and what it needs in order to run correctly. 
Open the link in our README.md in a new tab, and check out the README.md file for BioTraDIS
If you go over to the WorkshopOverview.md file, you'll see _this_ file! You can follow along there or continue reading in your text editor. 

## Part 3: Command line 
Open your terminal window. 
You should get a > prompt where you can type commands (sometimes it looks like $ instead)

A few quick unix commands and terms:
`directory` a folder 

- press tab to auto-complete 

_of note: avoid putting spaces in the names of files, they require a special character to denote the space that bugs up code.
it's why you'll see a lot of programmers writing files with underscores i.e. file_name.txt_

`ls` or list 
lets you see what's in the directory (folder)

`ls -a` list all
shows you everything in a folder (including hidden scripts) 

`cd` change directory
lets you change the folder you're working in 

`cd ..` go back one
lets you go back one level of directories 

`cd ~/path/to/directory` takes you straight to the specified directory 

`pwd` print working directory 
outputs (prints) the path to the directory you are currently in
ex: `path/to/directory` 

`mv` move
moves OR RENAMES files 

`cp` copy
copies files 

`scp` copy to a second device 
we'll be using this to copy our folders onto climb 

`-` flag, usually written with a letter to denote an action 
examples: 
`-f` force
will override any safety controls and force an operation to complete 
`-r` recursive
goes down every level, i.e. recursively copying a folder will copy everything _within_ the folder 
`-o` output file
lets you name the output file 

`rm` remove
removes files
**note: literally never type `rm -rf` it will wipe your entire hard drive, even the operating system, off your computer**

`rmdir` removes directories

`touch` makes files 
ex: `touch filename.txt`

`mkdir` makes directories
ex: `mkdir directory_name`

you can use these commands to get around, make files, delete them, and rename them 

once you've gotten your command line up, we're going to make a directory for this project
decide where you want that directory to be, and navigate there using `cd` 
then, make your directory using
`mkdir DeltaWorkshop`
and navigate there using
`cd DeltaWorkshop`

congrats you've made a folder! now let's populate it with some files 

## Downloading from git 
This is a public repository, so you shouldn't need a git account to download from it. 
To download the files we'll do 
`git clone https://github.com/iawarner/HendersonLab`
you can also individually download the files using the user interface from the website, but... don't do that. 

Scripts that are real packages will be available for install using tools like bioconda, or they'll have explicit `make` and install instructions in their README files. 

For our purpose we're just trying to get the files, so `clone` is fine 
`git clone` will just copy the entire directory that's available on git into the folder (it will also enable you to edit and upload your edits to the github page, but for that you need get set up and it's beyond the scope of this workshop)

## Look at your files
The next step is going to be looking at your files in your terminal window 
There's a few commands you can use to do this
First, go to the directory using `cd HendersonLab` 
Then, check out the python script (the .py file) using
`head figure_BW.py` 
which will print the script into the terminal window
if you want to print more lines you can specify how many with a `-` flag 
so if we say 
`head -100 figure_BW.py` it'll print the first 100 lines 

if you want to look at the end of the file you can use `tail` in exactly the same way 

if you want to look at your script _without_ it printing in your terminal window, you can use
`nano figure_BW.py`
to open it in (effectively) another window, then use `ctrl X` to exit (and say N if you've made any changes)

have a look at some of your other files while you're here
what do they look like? what do you notice about the different file extensions and how the files look when you view them? 

## Uploading to Delta2 
You should have (and have activated) a delta2 account. If you haven't activated it, please log in before continuing. 

Log into delta using your uq username @delta2.imb.uq.edu.au 
You'll need to be on the VPN, and you sign in will look like
`uqiwarne@delta2.imb.uq.edu.au`
it'll prompt for your UQ password, and then you should be logged in 
go to your `90days` folder using
`cd 90days`
and then type `pwd` to get the path 
now type `exit` to leave delta2 and return to your local computer

To upload our files we'll use 
`scp -r /path/to/HendersonLab yourusername@delta2.imb.uq.edu.au:/home/uqusername/90days/`
note you will have to change your path to the file, your delta2 username, and your username on the delta2 path 
we are doing
`scp` to copy remotely 
`-r` to copy everything in the file
and then telling it a) where the file is b) what the file is and c) where we want the file to go 

you'll be asked to input your password, and then it should start uploading

## Running our scripts on Delta2 
Go ahead and log back onto delta2 using the above commands
Then we'll need a **pbs script**

Delta works on a queue system: you submit a script telling it what you would like to run and how much memory and time you expect it to need, and it puts it in the list of jobs 

To learn more about what delta expects, check out the wiki: http://delta-wiki.imb.uq.edu.au/igc/TitleIndex 

So we need to make our script with `touch testscript.pbs`
the .pbs extension is important! it tells the system what type of file it is, and the system only reads pbs files 

then we can use `nano testscript.pbs` 
(there are different editors, but I use nano)

and copy in:
```

```
