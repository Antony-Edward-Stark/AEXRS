import os
app_name = 'ls'
if app_name  == 'ls':
        print('User applications')
        for app in os.listdir('/Applications'): print('\t',app)
        print('System applications')
        for app in os.listdir('/system/Applications'): print('\t',app)