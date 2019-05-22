from winreg import OpenKey,HKEY_CURRENT_USER,EnumKey,EnumValue

reg = r'Software\PremiumSoft\NavicatMSSQL\Servers'
key = OpenKey(HKEY_CURRENT_USER,reg)

# 连接名
conns = []
try:
    i = 0
    while 1:
        name = EnumKey(key,i)
        conns.append(name)
        i += 1
except:
    pass

# 主机名
hosts = []
# 用户名
usernames = []
# 密码
passwords = []
for i in conns:
    key = OpenKey(HKEY_CURRENT_USER,reg + '\\' + i)
    try:
        j = 0
        while 1:
            name, value, type = EnumValue(key, j)
            if name == 'Host':
                hosts.append(value)
            if name == 'UserName':
                usernames.append(value)
            if name == 'Pwd':
                passwords.append(value)
            j += 1
    except:
        pass

for i in range(len(hosts)):
    with open('result.txt', 'a+') as f:
        f.write(conns[i] + ' ' + hosts[i]  + ' ' + usernames[i] + ' ' + passwords[i] + '\n')
