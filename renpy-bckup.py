import os,shutil
from pathlib import Path
from distutils.dir_util import copy_tree
from pip._vendor.colorama import Fore, Style

# Global Vars
base_dir = "C:/_share/_game/VN/" # folder where your games are, change to your directory
backup_folder = "_backup" #backup folder !! NO SLASHES !! make shure it exists inside base_dir

###### dont change save_folder and dest_dir
save_folder = "/game/saves/" # default folder for most ren'py games
dest_dir = base_dir + backup_folder + "/" # combine folders and add slash at end

# Call function per folder with name
def copysaves(game):
    dest = dest_dir + game #set path to dest per game
    src = base_dir + game + save_folder # set path to source per game
    print("Source: " + src)
    if game != '_backup': # Skip backup folder
        if os.path.isdir(Path(src)): #Check if Games folder exists in source, else its likly not renpy
            if os.path.isdir(Path(dest)): # Check is target folder exists else make one
                print("Copying game: " + game)
                copy_tree(src,dest)
            else:
                print("Create dest dir")
                os.mkdir(Path(dest)) # make destination folder in backup target
                print("Copying game: " + game)
                copy_tree(src,dest)
        else:
            print(Fore.RED + game + " is problably not an Ren'py Game, Skipping" + Style.RESET_ALL)
            
    else:
        print(Fore.RED + "Skipping backup folder" + Style.RESET_ALL)
        
    return

# start of program
# check if backup destination exists
if os.path.isdir(Path(dest_dir)):
    print(Fore.GREEN + "backup folder exist" + Style.RESET_ALL)
    # then start backup
    gamelist = next(os.walk(Path(base_dir)))[1]
    for game in gamelist: #loop through list of folders
        copysaves(game)
        
else:
    print(Fore.RED + "backup folder is not there" + Style.RESET_ALL)

foldercount = "total of {0} ".format(len(gamelist))
print(Fore.GREEN + foldercount + "Folders checked" + Style.RESET_ALL)
print(Fore.GREEN + "Backup Script Finished"  + Style.RESET_ALL)
    


