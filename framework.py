import os

def error(x, y):
    if y == 0:
        print('The Program had a error on line',str(x)+'.')
    elif y!= 0:
        print('The Program may have had a error on line',str(x),'to line',str(y)+'.')
    input('Press enter to exit.')
    exit() 
def run_both_bat():
    os.system('cmd /k start node_normal_bot.bat')
    os.system('cmd /k start node_backup_bot.bat')
def stop_both_bat():
    os.system('cmd /c powershell taskkill /f /im node.exe')
def run_both_pm2():
    os.system('cmd /c start pm2_normal_bot.bat && start pm2_backup_bot.bat')
def stop_both_pm2():
    os.system('cmd /c pm2 delete among-us-bot && pm2 delete backup-among-us-bot')
def complete():
    input("Press enter when you are done using the bot(s).")