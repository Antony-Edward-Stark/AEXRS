with open('/Users/Shared/userinfo.txt', 'r') as n:
    updated_info = n.read()
    info = updated_info.split(';')
    print(info[3])
