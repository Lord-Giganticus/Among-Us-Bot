import os

def run():
    run_choice = input("Complete. Do you wish to use the run.py file? If so enter 1, if not enter 2.")
    if run_choice == "1":
        os.system('cmd /c py -3 run.py')
        exit()
    if run_choice == "2":
        exit()

Download_Location = input("Enter where you want the repo to be cloned:")
os.chdir(Download_Location)
print(os.getcwd())
input("If this is not correct this WILL save somewhere you didn't want it. Press enter to continue")

git_location = input("Enter either your forked repo's .git link or the original repo's .git link:")

file = open('DL.bat','w')
file.write('git clone ')
file.write(git_location)
file.close()

os.system('cmd /c DL.bat')
os.system('cmd /c del /f DL.bat')

Bot_Choice = input("Enter a number for which bot you want to work on.\n[1] Normal Bot\n[2] Backup Bot\n[3] Both\n")
if Bot_Choice == "1":
    Repo_Folder = input("Enter the location of the cloned folder:")
    os.chdir(Repo_Folder)
    print(os.getcwd())
    input("If this is not correct this WILL NOT work. Press enter to continue.")
    os.chdir("nodejs")
    if os.path.isdir('node_modules') == True:
        os.system('cmd /c RD /S /Q node_modules')
    os.system('cmd /c npm install')
    run()
elif Bot_Choice == "2":
    Repo_Folder = input("Enter the location of the cloned folder:")
    os.chdir(Repo_Folder)
    print(os.getcwd())
    input("If this is not correct this WILL NOT work. Press enter to continue.")
    os.chdir("nodejs/backup-bot")
    if os.path.isdir('node_modules') == True:
        os.system('cmd /c RD /S /Q node_modules')
    os.system('cmd /c npm install')
    run()
elif Bot_Choice == "3":
    Repo_Folder = input("Enter the location of the cloned folder:")
    os.chdir(Repo_Folder)
    print(os.getcwd())
    input("If this is not correct this WILL NOT work. Press enter to continue.")
    os.chdir("nodejs")
    if os.path.isdir('node_modules') == True:
        os.system('cmd /c RD /S /Q node_modules')
    os.system('cmd /c npm install')
    os.chdir("backup-bot")
    if os.path.isdir('node_modules') == True:
        os.system('cmd /c RD /S /Q node_modules')
    os.system('cmd /c npm install')
    run()
else:
    input("Whoops! That wasn't supposed to happen Press enter to exit.")
    exit()