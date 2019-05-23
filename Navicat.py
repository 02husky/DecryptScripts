from winreg import OpenKey, HKEY_CURRENT_USER, EnumKey, EnumValue

regs = {'mssql': r'Software\PremiumSoft\NavicatMSSQL\Servers', 'mysql': r'Software\PremiumSoft\Navicat\Servers',
        'oracle': r'Software\PremiumSoft\NavicatOra\Servers', 'pgsql': r'Software\PremiumSoft\NavicatPG\Servers',
        'MariaDB': r'Software\PremiumSoft\NavicatMARIADB\Servers'}


def get_info(dbname,reg):
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
    with open('result.txt', 'a') as f:
        f.write('\n' + dbname + ' connections:' + '\n')
    for i in range(len(hosts)):
        with open('result.txt', 'a') as f:
            f.write(' conn_name:' + conns[i] + '      ' + 'host_name:'+ hosts[i] + '      '
                    + 'username:' + usernames[i] + '      ' + 'password:' + passwords[i] + '\n')


if __name__ == '__main__':
    for i, j in regs.items():
        try:
            get_info(i, j)
        except:
            continue
