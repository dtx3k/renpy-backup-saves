# renpy backup saves
## Python script to backup all your ren'py saves to a single location

This Script wil copy from every game folder the saves  and
copied them to a new folder in the root of the main directory. (you'll need all your games in the same folder though)

If your games are in c:\renpygames (c:\renpygames\game1, c:\renpygames\game2, etc)

you make a directory for example "_backup"  
```c:\renpygames\_backup ```


and edit the ```renpy-bckup.py``` to have your folder paths  
alwayy use forward slashes even on windows -> /  
when defining your path, the script will handle it ;)
it is intended to be OS independent thats why.
```
base_dir = "C:/_share/_game/VN/" # folder where your games are, change to your directory

backup_folder = "_backup" #backup folder !! NO SLASHES !! make shure it exists inside base_dir
```
run the script : ```python renpy-bckup.py```

this wil make a new folder for every game inside _backup with the name of the game,
inside there are the copies of all the saves for your save keeping
```
Example:  
c:\renpygames\_backup\game1\save1.save  
c:\renpygames\_backup\game2\save1.save
```
_I'm not a programmer so it's far from perfect...but it does the job_
