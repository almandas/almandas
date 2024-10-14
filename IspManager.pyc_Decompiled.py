# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: C:\Users\FUJITSU\Documents\GitHub\ALMA_REPORTING\IspManager.py
# Bytecode version: 3.8.0rc1+ (3413)
# Source timestamp: 2024-07-01 21:19:59 UTC (1719868799)

from abc import ABC, abstractmethod
import IspAccount
import re
import os
from menu import GmailMenu, HotmailMenu, YahooMenu
from EmailClient import save_to_files

class ShowStringMixin:

    @abstractmethod
    def showString(self):
        string = f'{self.email};{self.password};{self.newPassword};{self.host};{self.port};{self.proxyUser};{self.proxyPass};{self.recovery};{self.newRecovery}\n'
        string = re.sub('None', '', string)
        string = re.sub(';+', ';', string)
        string = re.sub(';\\n', '\n', string)
        return string

class AbstractUserProfile(ABC, ShowStringMixin):

    def __init__(self, login):
        self.email = login['email']
        self.password = login['password']
        if ':::' in self.password:
            self.password, self.newPassword = self.password.split(':::')
        else:
            self.newPassword = None
        self.recovery = login['recovery']
        if self.recovery:
            if ':::' in self.recovery:
                self.recovery, self.newRecovery = self.recovery.split(':::')
            else:
                self.newRecovery = None
        else:
            self.recovery = None
            self.newRecovery = None
        self.host = login['host']
        self.port = login['port']
        self.proxyUser = login['proxyUser']
        self.proxyPass = login['proxyPwd']

    @classmethod
    def DetectIsp(cls, login, choice, i):
        try:
            folder = 'ressources'
            actsPath = os.path.join(folder, 'isp.txt')
            with open(actsPath, 'r') as file:
                isp = file.read().splitlines()[0]
        except:
            isp = ''
        email_domain = cls.split_email(login['email'])
        email_domain = email_domain.split('.')[0]
        HotmailList = ['hotmail', 'outlook', 'live', 'msn']
        if email_domain == email_domain:
            if i == 0:
                GmailMenu()
            IspUser = ISPUser(login)
            IspAccount.GmailChoices(IspUser, choice)
        else:
            raise ValueError(f'ISP unauthorized: {email_domain}')

    @staticmethod
    def split_email(email):
        try:
            if '@' in email:
                username, domain = email.split('@', 1)
                return domain
            raise ValueError("Invalid email format: no '@' symbol")
        except Exception as e:
            save_to_files('log', e)

class ISPUser(AbstractUserProfile):

    def __init__(self, login, is_active=True):
        super().__init__(login)
        self.is_active = is_active