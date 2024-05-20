# import functions as f 
# f.maintainance_tasks()
import os
os.system('clear')
print(os.getcwd())
username = list(os.path.expanduser('~').split("/"))[2]
os.chdir('/Users/'+username+'/Library/Caches')
for file in os.listdir(os.getcwd()):
    path =  os.path.join('/Users/'+username+'/Library/Caches',file)
    os.system()