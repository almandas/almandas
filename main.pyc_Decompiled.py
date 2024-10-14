# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: main.py
# Bytecode version: 3.8.0rc1+ (3413)
# Source timestamp: 2024-10-04 16:40:07 UTC (1728060007)

from IspManager import AbstractUserProfile
from EmailClient import get_local_ip, save_to_files
from IspAccount import nbLoops
from menu import input_event, choice
import time
import concurrent.futures
import os

def read_logins():
    try:
        logins = []
        filename = 'seed.txt'
        folder = 'ressources'
        seed_path = os.path.join(folder, filename)
        with open(seed_path, 'r') as file:
            for line in file:
                login_info = line.strip().split(';')
                email = login_info[0]
                password = login_info[1]
                ip = login_info[2] if len(login_info) >= 4 else None
                port = login_info[3] if len(login_info) >= 4 else None
                proxy_user = login_info[4] if len(login_info) >= 6 else None
                proxy_pwd = login_info[5] if len(login_info) >= 6 else None
                recovery = login_info[-1] if proxy_pwd != login_info[-1] and len(login_info) >= 3 else None
                login_data = {'email': email.lower(), 'password': password, 'host': ip, 'port': port, 'recovery': recovery, 'proxyUser': proxy_user, 'proxyPwd': proxy_pwd}
                logins.append(login_data)
        checkData = len(logins)
        if checkData == 0:
            print('seed.txt is empty...')
            time.sleep(10)
        return logins
    except Exception as e:
        save_to_files('log', e.args[0] + '\n')

def main():
    try:
        local_ip_address = get_local_ip()
        othorised_ips = ['23.227.90.224']
        if local_ip_address == local_ip_address:
            print('Welcome, othorisation granted ... ')
            seed = read_logins()
            i = 0
            with concurrent.futures.ThreadPoolExecutor() as executor:
                for loop in range(nbLoops):
                    for login in seed:
                        executor.submit(AbstractUserProfile.DetectIsp, login, choice, i)
                        if i == 0:
                            input_event.wait()
                            input_event.clear()
                        time.sleep(2)
                        i += 1
        else:
            print('You are not authorised to use this script, please contact the IT')
    except Exception as e:
        save_to_files('log', e.args[0] + '\n')
if __name__ == '__main__':
    main()