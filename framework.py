import os

def error():
    input("Something went wrong! Press enter to exit")
    exit()
def cmd():
    cmd_choice = input("Enter the number on which cmd program you want to use.\n[1] Node\n[2] PM2\n")
def run_both_bat():
    os.system('cmd /k node_normal_bot.bat')
    os.system('cmd /k node_backup_bot.bat')
def run_both_pm2():
    os.system('cmd /c pm2_normal_bot.bat && pm2_backup_bot.bat')
def stop_both_pm2():
    os.system('cmd /c pm2 delete among-us-bot && pm2 delete backup-among-us-bot')
def complete():
    input("Press enter when you are done using the bot(s).")