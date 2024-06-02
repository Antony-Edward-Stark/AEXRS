# import os
# def app_opener(app_name):
#     app_white_list = {'gimp':'GIMP.app',
#                     'vs code':"Visual\ Studio\ Code.app",
#                     'code':"Visual\ Studio\ Code.app",
#                     }
#     app_name_mod = app_name+'.app'
#     app_name_mod = app_name_mod.capitalize()
#     os.chdir("/Applications")
#     if app_name in app_white_list:
#         os.chdir("/Applications")
#         print("present in the list")
#         os.system("open "+app_white_list[app_name])
#     else:
#         if  app_name_mod in os.listdir(os.getcwd()):
#             print('App present in directory')
#             os.system("open "+app_name_mod)
#         elif app_name_mod not in os.listdir(os.getcwd()):
#             print("app not present")
# os.system("clear")
# x = input("Enter application name : ")
# app_opener(x)
# import datetime
# with open("info.txt", "r") as setup_info:
#     w = setup_info.read().split(';')
# # n = {"app_name": 'lol', "location": 'op'}
# with open('info.txt') as info:
#     app_lists = info.readlines()
# print(app_lists[0])
# print(app_lists)
# print(app_lists[1:])
# print(app_lists[1].split(';')[1:])
# subprocess.call('D:\Program Files\Telegram Desktop\Telegram.exe')
# current = datetime.datetime.now()
# print(current)
# import subprocess
# subprocess.Popen(r'explorer /select,"D:\Downloads\Setups"')

