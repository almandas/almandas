# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: C:\Users\FUJITSU\Documents\GitHub\ALMA_REPORTING\EmailClient.py
# Bytecode version: 3.8.0rc1+ (3413)
# Source timestamp: 2024-07-01 10:00:22 UTC (1719828022)

import socket
import os5
import random
from selenium import webdriver
import shutil
import zipfile
from menu import choice

def get_local_6ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        save_to_files('log.txt', e.args[0] + '\n')

def save_to_files(file_name, data, folder_name='result'):
    try:
        current_dir = os.getcwd()
        result_folder_path = os.path.join(current_dir, folder_name)
        if not os.path.exists(result_folder_path):
            os.makedirs(result_folder_path)
        file_path = os.path.join(result_folder_path, f'{file_name}.txt')
        with open(file_path, 'a') as file:
            file.write(data)
    except Exception as e:
        save_to_files('log', e.args[0] + '\n')

def get_config():
    try:
        config = 'config.json'
        folder = 'ressources'
        config_path = os.path.join(folder, config)
        with open(config_path, 'r') as file:
            lines = file.readline().strip()
            nbprocess, nbmsgs, nbLoops = lines.split(':')
            nbprocess = int(nbprocess)
            nbmsgs = int(nbmsgs)
            nbLoops = int(nbLoops)
        return (nbprocess, nbmsgs, nbLoops)
    except Exception as e:
        save_to_files('log.txt', e.args[0] + '\n')

def CreateDriver(IspUser, value=False):
    try:
        profile_folder_name = IspUser.email
        profiles_name = 'ChromesProfiles'
        default_user_path = os.path.expanduser('~')
        profiles_container_path = os.path.join(default_user_path, profiles_name)
        profile_folder_path = os.path.join(default_user_path, profiles_name, profile_folder_name)
        options = webdriver.ChromeOptions()
        if not os.path.exists(profiles_container_path):
            os.makedirs(profiles_container_path)
        if not os.path.exists(profile_folder_path):
            os.makedirs(profile_folder_path)
        options.add_argument(f'--user-data-dir={profile_folder_path}')
        options.add_argument('--disable-infobars')
        options.add_argument('--window-size=1200,900')
        options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--profile-directory=Default')
        options.add_argument('--no-sandbox')
        options.add_argument('--no-default-browser-check')
        options.add_argument('--no-first-run')
        options.add_argument('--lang=en-us')
        options.add_argument('--disable-web-security')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-plugins-discovery')
        if choice[0] == '25' or choice[0] == '26':
            try:
                options.add_extension('captcha_solver.crx')
            except:
                pass
    PROXY_HOST = IspUser.host
    PROXY_PORT = IspUser.port
    PROXY_USER = IspUser.proxyUser
    PROXY_PASS = IspUser.proxyPass
    if PROXY_USER and PROXY_PASS:
        manifest_json = '\n            {\n                \"manifest_version\": 2,\n                \"name\": \"Reporting Tools\",\n                \"description\": \"Reporting Tools\",\n                \"minimum_chrome_version\":\"124\",\n                \"version\": \"1.0.0\",\n                \"permissions\": [\n                    \"proxy\",\n                    \"tabs\",\n                    \"<all_urls>\",\n                    \"webRequest\",\n                    \"webRequestBlocking\",\n                    \"privacy\"\n                ],\t\t\t\t\t\t\n                \"background\": {\n                    \"scripts\": [\"background.js\"]\n                }\n                \n                \n            }\n            '
        background_js = '\n            var config = {\n                    mode: \"fixed_servers\",\n                    rules: {\n                    singleProxy: {\n                        scheme: \"http\",\n                        host: \"%s\",\n                        port: parseInt(%s)\n                    },\n                    bypassList: [\"localhost\"]\n                    }\n                };\n\n            chrome.proxy.settings.set({value: config, scope: \"regular\"}, function() {});\n\n            function callbackFn(details) {\n                return {\n                    authCredentials: {\n                        username: \"%s\",\n                        password: \"%s\"\n                    }\n                };\n            }\n\n            chrome.webRequest.onAuthRequired.addListener(\n                        callbackFn,\n                        {urls: [\"<all_urls>\"]},\n                        \n                        [\'blocking\']\n            );\n            ' % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)
        extension_directory = os.path.join(profile_folder_path, 'proxy')
        pluginfile = 'proxy_auth_plugin.zip'
        pluginpath = os.path.join(extension_directory, pluginfile)
        if not os.path.exists(extension_directory):
            os.makedirs(extension_directory)
        if not os.path.exists(pluginpath):
            with zipfile.ZipFile(pluginpath, 'w') as zp:
                zp.writestr('manifest.json', manifest_json)
                zp.writestr('background.js', background_js)
        options.add_extension(pluginpath)
    else:  # inserted
        if PROXY_HOST and PROXY_PORT:
            options.add_argument(f'--proxy-server={PROXY_HOST}:{PROXY_PORT}')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    if value:
        cookies = [{'domain': '.yahoo.com', 'expiry': 1740577603, 'httpOnly': True, 'name': 'T', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'af=JnRzPTE3MDkwNDE2MDImcHM9SEZGR3lxOEVIR1d3MXpOb0JpRzJjUS0t&d=bnMBeWFob28BZwFSSjRXUkhKN0lHVllZTTJOTFNOR1lVVDdJSQFhYwFBTXRtOTRoLgFhbAFhZGFtc19wYW03Mzg0AXNjAW1icl9sb2dpbgFmcwE3YjFVb0hObDNkVmUBenoBQ2ZlM2xCQTdFAWEBUUFFAWxhdAFDZmUzbEIBbnUBMA--&kt=EAAmbnRWTs9EVmOVGepEREPkw--~I&ku=FAAVV.VA24emwLild71Ctb6YvGihttbS4ffoTLK1iWxF6blujdrNH7lR5ghW9tUB9xHYCa_rF8mFTYSz_3avKQZT8xRPYmwrXKYCcKtqPjFExwyeO9FbNVk4dqipba58NBbfo5s8d3qBabN0Ii3bxOdA6F3ZGCEWDjDbL3sSk3YIiA-~E'}, {'domain': '.yahoo.com', 'expiry': 1740577603, 'httpOnly': True, 'name': 'OTH', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'v=2&s=2&d=eyJraWQiOiIwMTY0MGY5MDNhMjRlMWMxZjA5N2ViZGEyZDA5YjE5NmM5ZGUzZWQ5IiwiYWxnIjoiUlMyNTYifQ.eyJjdSI6eyJndWlkIjoiUko0V1JISjdJR1ZZWU0yTkxTTkdZVVQ3SUkiLCJwZXJzaXN0ZW50Ijp0cnVlLCJzaWQiOiI1eHhCcnZUUHNvRlcifX0.XS4jKRq5emvQToauk-z43F1nkhKGcpquxfj4GsvataOaLD3Nz6xi2pqUVI7FXN6cBX3szqggCP6NdmtNUVVCIdN6kX3-3TC4SseOVQd5yPB_6iLxofUeSxJr3wZMFrk9ELVgGRJ2cKFSt8zedM3G4rmiDjTh6DEYy-VmVL3rbBo'}, {'domain': '.yahoo.com', 'expiry': 1740603033, 'httpOnly': True, 'name': 'A1', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'd=AQABBBnk3GUCEDnv-GB_PDK5X494VeDMunYFEgAACAEx32UMZvCdb2UB9qMAAAcIGeTcZeDMunYID_Qtl43zgLTiBdBeER8nRQkBBwoBHQ&S=AQAAAjlKNHdZpiSSnwFOnLhZKek'}]
        browser.get('https://login.yahoo.com/?.src=ym&pspid=159600001&activity=mail-direct&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%2Ffolders%2F1')
        for cookie in cookies:
            browser.add_cookie(cookie)
    return browser
    except Exception as e:
        save_to_files('log.txt', e.args[0] + '\n')