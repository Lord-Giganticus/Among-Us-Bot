import os
from framework import *

bot_choice = input("Enter the number on which bot you wish to run.\n[1] Normal Bot\n[2] Backup Bot\n[3] Both\n")
if bot_choice == "1":
    cmd_choice = input("Enter the number on which cmd program you want to use.\n[1] Node\n[2] PM2\n")
    if cmd_choice == "1":
        try:
            os.system('cmd /k start node_normal_bot.bat')
            complete()
            os.system('cmd /c powershell taskkill /f /im node.exe')
            exit()
        except:
            error(8, 12)
    elif cmd_choice == "2":
        try:
            os.system('cmd /c start pm2_normal_bot.bat')
            complete()
            os.system('cmd /c pm2 delete among-us-bot')
            exit()
        except:
            error(16, 20)
    else:
        error(6, 0)
elif bot_choice == "2":
    cmd_choice = input("Enter the number on which cmd program you want to use.\n[1] Node\n[2] PM2\n")
    if cmd_choice == "1":
        try:
            os.system('cmd /k start node_backup_bot.bat')
            complete()
            os.system('cmd /c powershell taskkill /f /im node.exe')
            exit()
        except:
            error(28, 32)
    elif cmd_choice == "2":
        try:
            os.system('cmd /c start pm2_backup_bot.bat')
            complete()
            os.system('cmd /c pm2 delete backup-among-us-bot')
            exit()
        except:
            error(36, 40)
    else:
        error(26, 0)
elif bot_choice == "3":
    cmd_choice = input("Enter the number on which cmd program you want to use.\n[1] Node\n[2] PM2\n")
    if cmd_choice == "1":
        try:
            run_both_bat()
            complete()
            stop_both_bat()
            exit()
        except:
            error(48, 52)
    elif cmd_choice == "2":
        try:
            run_both_pm2()
            complete()
            stop_both_pm2()
            exit()
        except:
            error(56, 60)
    else:
        error(46, 0)
else:
    error(4, 0)