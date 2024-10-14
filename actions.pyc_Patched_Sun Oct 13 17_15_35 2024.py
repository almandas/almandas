# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: C:\Users\FUJITSU\Documents\GitHub\ALMA_REPORTING\actions.py
# Bytecode version: 3.8.0rc1+ (3413)
# Source timestamp: 2024-06-21 00:17:25 UTC (1718929045)

import time
import random
import os
import string
import secrets
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import createProfiles
from EmailClient import save_to_files
from createProfiles import mainlnesia, getFirstPart, mailforspam

def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join((secrets.choice(characters) for _ in range(length)))

class GmailActions:
    def urls():
        LoginUrl = 'https://accounts.google.com/signin/v2/identifier?hl=en&continue=https%3A%2F%2Fmail.google.com%2Fmail&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession'
        MainUrl = 'https://mail.google.com/mail/u/0/'
        AccountUrl = 'https://myaccount.google.com/'
        pliUrl = 'https://myaccount.google.com/?pli=1'
        pliUrlMail = 'https://mail.google.com/mail/u/0/?pli=1'
        SpamUrl = 'https://mail.google.com/mail/u/0/#spam'
        url_list = [LoginUrl, MainUrl, AccountUrl, pliUrl, pliUrlMail, SpamUrl]
        return url_list

    @classmethod
    def read_file(cls, filename):
        try:
            folder = 'ressources'
            actsPath = os.path.join(folder, filename)
            with open(actsPath, 'r') as file:
                data = file.read().splitlines()
                return data
        except:
            print(f'File {filename} not found.')
            return None

    @classmethod
    def close_secend_window(cls, driver):
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    def checkAccount(IspUser, driver, close=False, support=False, manual=False):
        print(IspUser.email + ' on process...')
        LoginUrl = 'https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AaSxoQzm968VljTGXXK-IuqveUXb4V0LSpMHkPLtHcJXBRD44RhmWlkyucT011lBGvtnJfthH0sF&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1090154760%3A1716904486100740&ddm=0'
        MainUrl = 'https://mail.google.com/mail/u/0/'
        try:
            time.sleep(1)
            driver.get(MainUrl)
        except:
            save_to_files('failed', IspUser.showString())
            driver.quit()
        time.sleep(1)
        currentUrl = driver.current_url
        separators = ['#inbox', '#spam']
        for separator in separators:
            try:
                currentUrl = currentUrl.split(separator, 1)[0]
            except:
                pass
        url_list = GmailActions.urls()
        try:
            driver.find_element(By.CSS_SELECTOR, 'strong[jscontent=\'failedUrl\'],a[id=\'error-information-button\']')
            save_to_files('proxy_failed', IspUser.showString())
            driver.quit()
        except:
            pass
        if currentUrl in url_list and close:
            try:
                driver.find_element(By.CSS_SELECTOR, 'div[class=\'T-P-aut-UR T-P-aut\']').click()
            except:
                pass
            save_to_files('ok', IspUser.showString())
            driver.quit()
        else:  # inserted
            if currentUrl!= MainUrl:
                createProfiles.login_to_gmail(IspUser, driver, close, support, manual)

    @classmethod
    def openMsg(cls, driver):
        try:
            driver.implicitly_wait(3)
            rows = driver.find_element(By.CSS_SELECTOR, 'tr[class=\"zA yO\"], tr[class=\"zA zE\"]')
            rows.click()
            time.sleep(random.randint(3, 6))
        except:
            pass
        driver.implicitly_wait(10)

    @classmethod
    def loginWait(cls, driver):
        while True:  # inserted
            try:
                currentUrl = driver.current_url
            except:
                driver.close()
                break

    @classmethod
    def ReporNotSpam(cls, driver):
        spamUrl = 'https://mail.google.com/mail/u/0/#spam'
        driver.get(spamUrl)
        driver.refresh()
        time.sleep(random.randint(2, 4))
        while True:  # inserted
            try:
                try:
                    parent = driver.find_element(By.CSS_SELECTOR, 'span[class=\"x2\"]')
                except:
                    break
                else:  # inserted
                    cls.openMsg(driver)
                    driver.find_element(By.CSS_SELECTOR, 'button[class=\'bzq bzr IdsTHf\']').click()
                    time.sleep(random.randint(3, 5))
            except:
                try:
                    refresh = driver.find_element(By.CSS_SELECTOR, 'div[class=\"T-I J-J5-Ji nu T-I-ax7 L3\"]')
                    refresh.click()
                except:
                    try:
                        driver.refresh()
                    except:
                        pass

    @classmethod
    def selectPage(cls, driver):
        selectall = driver.find_element(By.CSS_SELECTOR, 'span.T-Jo.J-J5-Ji')
        selectall.click()
        time.sleep(random.randint(3, 5))

    @classmethod
    def notSpam(cls, driver):
        driver.find_element(By.CSS_SELECTOR, 'div[class*=\'T-I J-J5-Ji aFk\']').click()
        time.sleep(random.randint(3, 6))

    @classmethod
    def selectPage_notSpam(cls, driver):
        spamUrl = 'https://mail.google.com/mail/u/0/#spam'
        driver.get(spamUrl)
        driver.refresh()
        time.sleep(random.randint(2, 4))
        while True:  # inserted
            try:
                try:
                    parent = driver.find_element(By.CSS_SELECTOR, 'span[class=\"x2\"]')
                except:
                    break
                else:  # inserted
                    cls.selectPage(driver)
                    cls.notSpam(driver)
            except:
                try:
                    refresh = driver.find_element(By.CSS_SELECTOR, 'div[class=\"T-I J-J5-Ji nu T-I-ax7 L3\"]')
                    refresh.click()
                except:
                    try:
                        driver.refresh()
                        time.sleep(random.randint(2, 4))
                    except:
                        pass

    @classmethod
    def nextMsg(cls, driver):
        try:
            nextBtn = driver.find_element(By.CSS_SELECTOR, '[jslog=\'168965; u014N:cOuCgd,Kr2w4b;\']')
            nextBtn.click()
            time.sleep(random.randint(3, 6))
        except:
            pass

    @classmethod
    def nextPage(cls, driver):
        nextPage = driver.find_elements(By.CSS_SELECTOR, 'div[class*=\'T-I J-J5-Ji amD T-I-awG T-I-ax7 T-I-Js-Gs L3\']')
        if len(nextPage) > 1:
            nextPage[1].click()
        else:  # inserted
            nextPage[0].click()

    @classmethod
    def click(cls, driver):
        try:
            image_elements = driver.find_elements(By.CSS_SELECTOR, 'img')
            largest_image = None
            largest_area = 0
            for img in image_elements:
                width = int(img.get_attribute('width') or 0)
                height = int(img.get_attribute('height') or 0)
                area = width * height
                if area > largest_area:
                    largest_area = area
                    largest_image = img
            largest_image.click()
            if len(driver.window_handles) > 1:
                time.sleep(random.randint(5, 8))
                cls.close_secend_window(driver)
                time.sleep(random.randint(1, 2))
            wrong_img = None
            wrong_img = driver.find_element(By.CSS_SELECTOR, '.aLF-aPX-aPU-JX')
            if wrong_img:
                time.sleep(random.randint(1, 2))
                back_btn = driver.find_element(By.CSS_SELECTOR, '.aLF-aPX-Jq-I.aLF-aPX-auO-I.J-J5-Ji.aLF-aPX-I')
                back_btn.click()
        except:
            pass

    @classmethod
    def inbox_openClick(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            cls.openMsg(driver)
            cls.click(driver)
            cls.nextMsg(driver)

    @classmethod
    def markAsImportant(cls, driver):
        try:
            hover_element = driver.find_element(By.CSS_SELECTOR, 'div[class=\'T-I J-J5-Ji nf T-I-ax7 L3\']')
            hover_element.click()
            time.sleep(random.randint(2, 4))
            important = driver.find_elements(By.CSS_SELECTOR, 'div.J-N[jslog=\'172448; u014N:cOuCgd,Kr2w4b;\']')
            important[0].click()
        except:
            try:
                hover_element.click()
                time.sleep(random.randint(2, 4))
            except:
                pass

    @classmethod
    def inbox_openClickImportant(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            cls.openMsg(driver)
            cls.click(driver)
            cls.markAsImportant(driver)
            cls.nextMsg(driver)

    @classmethod
    def addStar(cls, driver):
        try:
            star = driver.find_element(By.CSS_SELECTOR, '.zd.bi4')
            star.click()
            time.sleep(random.randint(2, 5))
        except:
            pass

    @classmethod
    def inbox_openClickStart(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            cls.openMsg(driver)
            cls.click(driver)
            cls.addStar(driver)
            cls.nextMsg(driver)

    @classmethod
    def inbox_openClickImportantStart(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            cls.openMsg(driver)
            cls.click(driver)
            cls.markAsImportant(driver)
            cls.addStar(driver)
            cls.nextMsg(driver)

    @classmethod
    def reply(cls, driver):
        try:
            replys = cls.read_file('replys.txt')
            if replys:
                replyMsg = random.choice(replys)
            else:  # inserted
                replyMsg = generate_random_string()
            replyBtn = driver.find_element(By.CSS_SELECTOR, '.T-I.J-J5-Ji.T-I-Js-IF.aaq.T-I-ax7.L3')
            replyBtn.click()
            time.sleep(random.randint(2, 5))
            replyInput = driver.find_element(By.CSS_SELECTOR, '.Am.aO9.Al.editable.LW-avf.tS-tW')
            replyInput.clear()
            replyInput.send_keys(replyMsg)
            time.sleep(random.randint(2, 5))
            sendReply = driver.find_element(By.CSS_SELECTOR, 'div[role=\'button\'].T-I.J-J5-Ji.aoO.v7.T-I-atl.L3')
            sendReply.click()
            time.sleep(random.randint(2, 5))
        except:
            pass

    @classmethod
    def inbox_openClickReply(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            cls.openMsg(driver)
            cls.click(driver)
            cls.reply(driver)
            cls.nextMsg(driver)

    @classmethod
    def archive(cls, driver):
        try:
            archive = driver.find_elements(By.CSS_SELECTOR, 'div.T-I.J-J5-Ji.lR.T-I-ax7.T-I-Js-Gs.T-I-Js-IF.mA')
            archive[1].click()
            time.sleep(random.randint(2, 5))
        except:
            pass

    @classmethod
    def inbox_openClickArchive(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            cls.openMsg(driver)
            cls.click(driver)
            cls.archive(driver)
            cls.nextMsg(driver)

    @classmethod
    def selectPage_notSpam_inbox_OpenClickImportantStar(cls, driver, nbMsgs):
        cls.selectPage_notSpam(driver)
        driver.get('https://mail.google.com/mail/u/0/')
        cls.inbox_openClickImportantStart(driver, nbMsgs)

    @classmethod
    def selectPage_notSpam_inbox_OpenClickReply(cls, driver, nbMsgs):
        cls.selectPage_notSpam(driver)
        driver.get('https://mail.google.com/mail/u/0/')
        cls.inbox_openClickReply(driver, nbMsgs)

    @classmethod
    def importContact(cls, IspUser, driver):
        try:
            current_project_path = os.getcwd()
            try:
                file_path = current_project_path + '\\ressources\\contacts.csv'
            except:
                pass
            while True:  # inserted
                try:
                    contact_url = 'https://contacts.google.com/'
                    driver.get(contact_url)
                except:
                    pass
            try:
                parent_a_element = driver.find_element(By.CSS_SELECTOR, '.d5NbRd-EScbFb-JIbuQc.dgqZp')
                parent_a_element.click()
            except:
                pass
            try:
                file_input = driver.find_element(By.XPATH, '//input[@type=\'file\']')
                file_input.send_keys(file_path)
                time.sleep(random.randint(3, 5))
            except:
                pass
            try:
                txt = ''
                span = driver.find_element(By.XPATH, '//span[@jsname=\'wRkGLe\']')
                txt = span.text
            except:
                pass
            if txt == 'contacts.csv':
                try:
                    imprt = driver.find_element(By.CSS_SELECTOR, 'button[jsaction*=\'click\'][data-mdc-dialog-action=\'ok\']')
                    imprt.click()
                    save_to_files('add_contact_done', IspUser.showString())
                    time.sleep(random.randint(8, 10))
                    break
                except:
                    pass
        except:
            save_to_files('add_contact_failed', IspUser.showString())

    @classmethod
    def changePassword(cls, IspUser, driver):
        try:
            cls.checkAccount(IspUser, driver)
            new_password = IspUser.newPassword
            if new_password == None:
                print('syntax incorrect: To change password pls follow this sayntax password:::newpassword')
            else:  # inserted
                driver.get('https://myaccount.google.com/signinoptions/rescuephone?continue=https://myaccount.google.com/security?authuser%3D0%26rapt%3DAEjHL4OkvE43ZrGYrwo1J506Ttc2chZshKiPB-5a0ZIcFvjWwOqZIBMsbzR-94GCy6oApbfrq575iqtkZ5ILT3C4JPgE9jlLfGe3BukhBgSRSedbI2e9J7A&pli=1&rapt=AEjHL4MnerH600fBIblVBWE4dfdd1msVZSEQnP-ypf3NXBmnyLrnVB475qZcUwkvUQ69925U2a7xra0pIS_A5E9K6Obh135JMZY21D3zvpV_iOG5QoxaRvY')
                try:
                    old_password = IspUser.password
                    time.sleep(random.randint(3, 5))
                    password_field = driver.find_element(By.XPATH, '//input[@type=\'password\' and @name=\'Passwd\']')
                    time.sleep(random.randint(3, 5))
                    password_field.send_keys(old_password)
                    time.sleep(random.randint(3, 5))
                    next = driver.find_element(By.CSS_SELECTOR, '.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ')
                    next.click()
                except:
                    pass
                time.sleep(random.randint(3, 5))
                url = driver.current_url
                new_url = url.replace('rescuephone', 'password')
                time.sleep(random.randint(3, 5))
                driver.get(new_url)
                time.sleep(random.randint(3, 5))
                while True:  # inserted
                    url = driver.current_url
                    if new_url == url:
                        break
                    driver.get(new_url)
                    time.sleep(random.randint(3, 5))
                newpwd_input = driver.find_elements(By.CSS_SELECTOR, '.VfPpkd-fmcmS-wGMbrd.uafD5')
                newpwd_input[0].send_keys(new_password)
                time.sleep(random.randint(3, 5))
                newpwd_input[1].send_keys(new_password)
                time.sleep(random.randint(3, 5))
                nextbtn = driver.find_element(By.XPATH, '//button[@type=\'submit\']')
                nextbtn.click()
                time.sleep(random.randint(8, 10))
                save_to_files('password_changed', IspUser.showString())
        except:
            save_to_files('password_NotChanged', IspUser.showString())

    @classmethod
    def changeRecovry(cls, IspUser, driver, bouth=False):
        try:
            new_recovery = IspUser.newRecovery
            if new_recovery == None:
                print('syntax incorrect: To change password pls follow this sayntax recovery:::newrecovery')
            else:  # inserted
                recovryLink = 'https://myaccount.google.com/signinoptions/rescuephone?continue=https://myaccount.google.com/security?authuser%3D0%26rapt%3DAEjHL4OkvE43ZrGYrwo1J506Ttc2chZshKiPB-5a0ZIcFvjWwOqZIBMsbzR-94GCy6oApbfrq575iqtkZ5ILT3C4JPgE9jlLfGe3BukhBgSRSedbI2e9J7A&pli=1&rapt=AEjHL4MnerH600fBIblVBWE4dfdd1msVZSEQnP-ypf3NXBmnyLrnVB475qZcUwkvUQ69925U2a7xra0pIS_A5E9K6Obh135JMZY21D3zvpV_iOG5QoxaRvY'
                if not bouth:
                    cls.checkAccount(IspUser, driver)
                    password = IspUser.password
                    driver.get(recovryLink)
                    password_field = driver.find_element(By.XPATH, '//input[@type=\'password\' and @name=\'Passwd\']')
                    time.sleep(random.randint(3, 5))
                    password_field.send_keys(password)
                    time.sleep(random.randint(3, 5))
                    next = driver.find_element(By.CSS_SELECTOR, '.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.qIypjc.TrZEUc.lw1w4b')
                    next.click()
                    time.sleep(random.randint(3, 5))
                else:  # inserted
                    driver.get(recovryLink)
                    time.sleep(random.randint(3, 5))
                urlrecov = driver.current_url
                new_urlrecov = urlrecov.replace('signinoptions/rescuephone', 'recovery/email')
                driver.get(new_urlrecov)
                time.sleep(random.randint(3, 5))
                newrecovery_input = driver.find_element(By.CSS_SELECTOR, 'input[type=\"email\"]')
                newrecovery_input.clear()
                time.sleep(random.randint(1, 2))
                newrecovery_input.send_keys(new_recovery)
                time.sleep(random.randint(3, 5))
                nextbtn = driver.find_element(By.CSS_SELECTOR, '.UywwFc-LgbsSe.UywwFc-LgbsSe-OWXEXe-dgl2Hf.wMI9H')
                nextbtn.click()
                time.sleep(random.randint(3, 5))
                save_to_files('recovery_changed', IspUser.showString())
                time.sleep(2)
        except:
            save_to_files('recovery_NotChanged', IspUser.showString())

    @classmethod
    def changePasswordRecovry(cls, IspUser, driver):
        cls.changePassword(IspUser, driver)
        cls.changeRecovry(IspUser, driver, True)

    @classmethod
    def cleanAll(cls, driver):
        driver.get('https://mail.google.com/mail/u/0/#all')
        i = 0
        driver.refresh()
        while True:  # inserted
            i += 1
            try:
                try:
                    parent = driver.find_element(By.CSS_SELECTOR, '.J-J5-Ji.amH.J-JN-I')
                except:
                    break
                else:  # inserted
                    all = driver.find_element(By.CSS_SELECTOR, 'span[class*=\'T-Jo J-J5-Ji\']')
                    all.click()
                    try:
                        full = driver.find_element(By.CSS_SELECTOR, 'div[class=\'T-I J-J5-Ji nX T-I-ax7 T-I-Js-Gs  mA\']')
                        full.click()
                        time.sleep(random.randint(1, 3))
                    except:
                        pass
                delete = driver.find_element(By.CSS_SELECTOR, 'div[data-tooltip=\'Delete\']')
                delete.click()
                time.sleep(random.randint(1, 3))
                driver.find_element(By.CSS_SELECTOR, '.J-at1-auR.J-at1-atl').click()
                time.sleep(10)
                if i == 5:
                    driver.refresh()
                    i = 0
            except:
                try:
                    driver.current_url
                except:
                    break

    @classmethod
    def markAsRead(cls, driver):
        try:
            driver.find_element(By.CSS_SELECTOR, 'div[class*=\'T-I J-J5-Ji m9 T-I-ax7\']').click()
        except:
            pass

    @classmethod
    def search(cls, driver):
        try:
            seachkey = cls.read_file('search.txt')
            try:
                search_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-owns=\'gs_sbt50\']')
                search_input.send_keys(seachkey)
                search_input.send_keys(Keys.RETURN)
                driver.refresh()
                time.sleep(random.randint(1, 4))
            except:
                pass
        except:
            print('search.txt not exist')

    @classmethod
    def allStar(cls, driver):
        try:
            hover_element = driver.find_element(By.CSS_SELECTOR, '.T-I.J-J5-Ji.nf.T-I-ax7.L3')
            hover_element.click()
            time.sleep(random.randint(2, 4))
            star = driver.find_element(By.CSS_SELECTOR, 'div.J-N[jslog=\'56746; u014N:cOuCgd,Kr2w4b;\']')
            star.click()
            time.sleep(random.randint(2, 4))
        except:
            try:
                hover_element.click()
            except:
                pass

    @classmethod
    def inbox_selectpageReadImportantStart_bySearch(cls, driver, nbMsgs):
        cls.search(driver)
        for i in range(nbMsgs):
            cls.selectPage(driver)
            cls.markAsRead(driver)
            cls.markAsImportant(driver)
            cls.allStar(driver)
            cls.nextPage(driver)

    @classmethod
    def actionByChoice(cls, IspUser, driver, nbMsgs):
        acts_filename = 'actions.txt'
        acts_list = cls.read_file(acts_filename)
        cat, acts_func = acts_list[0].split(':')
        acts_func = acts_func.split(';')
        if acts_func == 'changePassword':
            cls.changePassword(IspUser, driver)
        else:  # inserted
            if acts_func == 'changeRecovry':
                cls.changeRecovry(IspUser, driver)
            else:  # inserted
                if acts_func == 'changePasswordRecovry':
                    cls.changePasswordRecovry(IspUser, driver)
                else:  # inserted
                    if acts_func == 'importContact':
                        cls.importContact(IspUser, driver)
                    else:  # inserted
                        if acts_func == 'clean':
                            cls.cleanAll(IspUser, driver)
                        else:  # inserted
                            if acts_func == 'checkAccount' or acts_func == 'createProfiles':
                                cls.checkAccount(IspUser, driver)
                            else:  # inserted
                                if acts_func:
                                    instance = GmailActions()
                                    if cat == 'spam':
                                        driver.get('https://mail.google.com/mail/u/0/#spam')
                                        driver.refresh()
                                    for i in range(nbMsgs):
                                        for act in acts_func:
                                            method = getattr(GmailActions, act, None)
                                            if method and callable(method) and hasattr(method, '__self__') and (method.__self__ is GmailActions):
                                                method(driver)
                                            else:  # inserted
                                                save_to_files('log', f'Function \'{act}\' not found or not callable.')

    def selectPage_notSpam_inbox_selectpageReadImportantStartArchive(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            cls.selectPage_notSpam(driver)
            cls.selectPage(driver)
            cls.markAsRead(driver)
            cls.markAsImportant(driver)
            cls.allStar(driver)
            cls.archive(driver)

    @classmethod
    def inbox_openStartReply(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            cls.openMsg(driver)
            cls.addStar(driver)
            cls.reply(driver)
            cls.nextMsg(driver)

    @classmethod
    def notPromotions(cls, driver, nbMsgs):
        driver.get('https://mail.google.com/mail/u/0/#category/promotions')
        driver.refresh()
        time.sleep(random.randint(3, 5))
        for i in range(nbMsgs):
            try:
                All = driver.find_element(By.CSS_SELECTOR, 'span[class*=\'T-Jo J-J5-Ji\']')
                All.click()
                time.sleep(random.randint(3, 5))
                not_promo = driver.find_element(By.CSS_SELECTOR, 'div[class*=\'T-I J-J5-Ji T-I-ax7 L3\']')
                not_promo.click()
                time.sleep(random.randint(3, 5))
                try:
                    driver.find_element(By.CSS_SELECTOR, 'dic[class=\'J-J5-Ji amH J-JN-I\']')
                except:
                    break
            except:
                break

    @classmethod
    def randomActions(cls, driver, nbMsgs):
        function_data = [(cls.click, [driver]), (cls.markAsImportant, [driver]), (cls.addStar, [driver]), (cls.reply, [driver]), (cls.archive, [driver])]
        for _ in range(nbMsgs):
            cls.openMsg(driver)
            num_functions_to_select = random.randint(1, len(function_data))
            selected_functions = random.sample(function_data, k=num_functions_to_select)
            for selected_function, args in selected_functions:
                selected_function(*args)
            cls.nextMsg(driver)

    @classmethod
    def first_login_changePassword(cls, IspUser, driver):
        try:
            cls.checkAccount(IspUser, driver)
            new_password = IspUser.newPassword
            print(new_password)
            if new_password == None:
                print('syntax incorrect: To change password pls follow this sayntax password:::newpassword')
            else:  # inserted
                time.sleep(random.randint(3, 5))
                newpwd_input = driver.find_elements(By.CSS_SELECTOR, 'input[name=\'Password\']')
                newpwd_input[0].send_keys(new_password)
                time.sleep(random.randint(3, 5))
                newpwd_input = driver.find_elements(By.CSS_SELECTOR, 'input[name=\'ConfirmPassword\']')
                newpwd_input[0].send_keys(new_password)
                time.sleep(random.randint(3, 5))
                nextbtn = driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\']')
                nextbtn.click()
                time.sleep(random.randint(8, 10))
                save_to_files('password_changed', IspUser.showString())
        except:
            save_to_files('password_NotChanged', IspUser.showString())

class HotmailActions:
    def urls():
        LoginUrl = 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=21&ct=1707744265&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26nlp%3d1%26deeplink%3dowa%252f0%252f%253fstate%253d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC8%26RpsCsrfState%3d09d06961-57fc-31bf-932b-46cd145a6aa3&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c'
        MainUrl = 'https://outlook.live.com/mail/0/'
        SpamUrl = 'https://outlook.live.com/mail/0/junkemail'
        ContactUrl = 'https://outlook.live.com/people/0/'
        ArchiveUrl = 'https://outlook.live.com/mail/0/archive'
        urlPro = 'https://account.microsoft.com/'
        office = 'https://outlook.office365.com/mail/'
        url_list = [MainUrl, ContactUrl, SpamUrl, ArchiveUrl, urlPro, office]
        return url_list

    @classmethod
    def read_file(cls, filename):
        try:
            folder = 'ressources'
            actsPath = os.path.join(folder, filename)
            with open(actsPath, 'r') as file:
                data = file.read().splitlines()
                return data
        except:
            print(f'File {filename} not found.')
            return None

    @classmethod
    def close_secend_window(cls, driver):
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    def checkAccount(IspUser, driver, close=False):
        logUrl = 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=21&ct=1708442704&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26nlp%3d1%26deeplink%3dowa%252f%26RpsCsrfState%3d65d04c9c-21c5-309e-2c28-5482fe0bc4f6&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c'
        driver.get(logUrl)
        time.sleep(3)
        currentUrl = driver.current_url
        url_list = HotmailActions.urls()
        currentUrl = currentUrl.split('?')[0]
        if currentUrl in url_list:
            if close:
                save_to_files('ok', IspUser.showString())
                driver.quit()
            time.sleep(3)
            try:
                driver.find_elements(By.CSS_SELECTOR, 'button[class*=\'ms-Button ms-Button--primary E8L0k root\']')[1].click()
            except:
                pass
            try:
                driver.find_elements(By.CSS_SELECTOR, 'button[class*=\'ms-Button ms-Button--primary EpKAV root\']')[1].click()
            except:
                pass
        else:  # inserted
            createProfiles.login_to_hotmail(IspUser, driver, close)

    @classmethod
    def openMsg(cls, driver, i=0):
        try:
            driver.implicitly_wait(3)
            rows = driver.find_elements(By.CSS_SELECTOR, 'div[class=\"ESO13 gy2aJ Ejrkd\"],div[class*=\"IjzWp\"]')[i]
            rows.click()
            time.sleep(random.randint(3, 6))
            driver.implicitly_wait(10)
        except:
            pass

    @classmethod
    def loginWait(cls, IspUser, driver):
        cls.checkAccount(IspUser, driver, False)
        while True:  # inserted
            try:
                currentUrl = driver.current_url
            except:
                driver.close()
                break

    @classmethod
    def goToJunk(cls, driver):
        try:
            spamUrl = 'https://outlook.live.com/mail/0/junkemail'
            driver.get(spamUrl)
            driver.refresh()
            time.sleep(random.randint(5, 8))
        except:
            pass

    @classmethod
    def NotJunk(cls, driver):
        driver.find_elements(By.CSS_SELECTOR, 'button[class*=\'ms-Button splitMenuButton splitButtonMenuButton\']')[2].click()
        time.sleep(random.randint(3, 5))
        driver.find_element(By.CSS_SELECTOR, 'button[class*=\'root-\'][tabindex=\'-1\'][role=\'menuitem\']').click()
        time.sleep(random.randint(3, 5))
        driver.find_element(By.CSS_SELECTOR, 'button[class*=\'ms-Button ms-Button--primary jya0z root-\']').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    def moveToInbox(cls, driver):
        driver.find_element(By.CSS_SELECTOR, 'button[aria-label=\'Déplacer vers\'],button[aria-label=\'Move to\']').click()
        time.sleep(random.randint(3, 5))
        driver.find_element(By.CSS_SELECTOR, 'button[name=\'Inbox\']').click()
        time.sleep(random.randint(3, 5))
        driver.find_element(By.CSS_SELECTOR, 'button[class*=\'ms-Button ms-Button--primary jya0z root-\']').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    def reportNotJunk(cls, driver):
        cls.goToJunk(driver)
        cls.search(driver)
        while True:  # inserted
            try:
                cls.openMsg(driver)
                cls.NotJunk(driver)
            except:
                break

    @classmethod
    def reportToInbox(cls, driver):
        cls.goToJunk(driver)
        cls.search(driver)
        while True:  # inserted
            try:
                cls.openMsg(driver)
                cls.moveToInbox(driver)
            except:
                break

    @classmethod
    def selectPage(cls, driver):
        lastMsg = ''
        while True:  # inserted
            selectMsg = driver.find_elements(By.CSS_SELECTOR, 'div[role=\'checkbox\'][tabindex=\'-1\']')[(-1)]
            if lastMsg == selectMsg:
                break
            lastMsg = selectMsg
            selectMsg.location_once_scrolled_into_view
            time.sleep(1)
        lastMsg.click()
        time.sleep(random.randint(3, 5))
        selectAll = driver.find_element(By.CSS_SELECTOR, 'div[role=\'checkbox\'][tabindex=\'0\']')
        selectAll.click()
        time.sleep(random.randint(3, 5))

    @classmethod
    def selectPage_notJunk(cls, driver):
        cls.goToJunk(driver)
        cls.search(driver)
        while True:  # inserted
            try:
                cls.selectPage(driver)
                cls.NotJunk(driver)
            except:
                break

    @classmethod
    def nextMsg(cls, driver):
        try:
            nextBtn = driver.find_elements(By.CSS_SELECTOR, 'button[class*=\'ms-Button ms-Button--icon xoRaD\']')
            if len(nextBtn) > 1:
                nextBtn[1].click()
            else:  # inserted
                nextBtn[0].click()
            time.sleep(random.randint(3, 6))
        except:
            pass

    @classmethod
    def click(cls, driver):
        try:
            image_elements = driver.find_elements(By.CSS_SELECTOR, 'img')
            largest_image = None
            largest_area = 0
            for img in image_elements:
                width = int(img.get_attribute('width') or 0)
                height = int(img.get_attribute('height') or 0)
                area = width * height
                if area > largest_area:
                    largest_area = area
                    largest_image = img
            if largest_area!= 1024:
                largest_image.click()
            time.sleep(2)
            if len(driver.window_handles) > 1:
                time.sleep(random.randint(4, 6))
                cls.close_secend_window(driver)
                time.sleep(random.randint(1, 2))
            wrong_img = None
            wrong_img = driver.find_element(By.CSS_SELECTOR, '.aLF-aPX-aPU-JX')
            if wrong_img:
                time.sleep(random.randint(1, 2))
                back_btn = driver.find_element(By.CSS_SELECTOR, '.aLF-aPX-Jq-I.aLF-aPX-auO-I.J-J5-Ji.aLF-aPX-I')
                back_btn.click()
        except:
            pass

    @classmethod
    def archive(cls, driver):
        try:
            archiveBtn = driver.find_elements(By.CSS_SELECTOR, 'Button[class*=\'ms-Button root\']')[3]
            archiveBtn.click()
            time.sleep(random.randint(2, 5))
        except:
            pass

    @classmethod
    def removePin(cls, driver):
        while True:  # inserted
            try:
                pinBtn = driver.find_element(By.CSS_SELECTOR, 'i[data-icon-name=\'PinFilled\']')
                pinBtn.click()
                time.sleep(random.randint(1, 3))
            except:
                break

    @classmethod
    def Categorize(cls, driver):
        try:
            CategoriBtn = driver.find_element(By.CSS_SELECTOR, 'button[type=\'button\'][aria-label*=\'Cat\']')
            CategoriBtn.click()
            time.sleep(random.randint(2, 5))
            BlueBtn = driver.find_elements(By.CSS_SELECTOR, 'button[name*=\'Blue\'], button[name*=\'Bleu\']')
            GreenBtn = driver.find_elements(By.CSS_SELECTOR, 'button[name*=\'Green\'],button[name*=\'Vert\']')
            random_color = random.choice([BlueBtn, GreenBtn])
            random_color[0].click()
            time.sleep(random.randint(2, 5))
        except:
            pass

    @classmethod
    def flag(cls, driver):
        try:
            flagBtn = driver.find_element(By.CSS_SELECTOR, 'button[type=\'button\'][aria-label*=\'Flag\']')
            flagBtn.click()
            time.sleep(random.randint(2, 5))
        except:
            pass

    @classmethod
    def inbox_openClick(cls, driver, nbMsgs):
        cls.search(driver)
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.click(driver)
                cls.nextMsg(driver)
            except:
                break

    @classmethod
    def inbox_openCategorize(cls, driver, nbMsgs):
        cls.search(driver)
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.Categorize(driver)
                cls.nextMsg(driver)
            except:
                break

    @classmethod
    def inbox_openFlag(cls, driver, nbMsgs):
        cls.search(driver)
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.flag(driver)
                cls.nextMsg(driver)
            except:
                break

    @classmethod
    def inbox_openArchive(cls, driver, nbMsgs):
        cls.search(driver)
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver)
                cls.archive(driver)
            except:
                break

    @classmethod
    def inbox_openReply(cls, driver, nbMsgs):
        cls.search(driver)
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.reply(driver)
                cls.nextMsg(driver)
            except:
                break

    @classmethod
    def inbox_openClickCategorize(cls, driver, nbMsgs):
        cls.search(driver)
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.click(driver)
                cls.Categorize(driver)
                cls.nextMsg(driver)
            except:
                break

    @classmethod
    def inbox_openClickCategorizeFlag(cls, driver, nbMsgs):
        cls.search(driver)
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.click(driver)
                cls.Categorize(driver)
                cls.flag(driver)
                cls.nextMsg(driver)
            except:
                break

    @classmethod
    def inbox_openClickCategorizeArchive(cls, driver, nbMsgs):
        cls.search(driver)
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver)
                cls.click(driver)
                cls.Categorize(driver)
                cls.archive(driver)
            except:
                break

    @classmethod
    def reply(cls, driver):
        try:
            replys = cls.read_file('replys.txt')
            if replys:
                replyMsg = random.choice(replys)
            else:  # inserted
                replyMsg = generate_random_string()
            replyBtn = driver.find_elements(By.CSS_SELECTOR, 'button[aria-label=\'Répondre\'],button[aria-label=\'Reply\']')[0]
            replyBtn.click()
            time.sleep(random.randint(2, 5))
            reply_input = driver.find_element(By.CSS_SELECTOR, 'div[role=\'textbox\'][tabindex=\'0\']')
            reply_input.clear()
            reply_input.send_keys(replyMsg)
            time.sleep(random.randint(2, 5))
            send_reply = driver.find_element(By.CSS_SELECTOR, 'button[aria-label=\'Envoyer\'],button[aria-label=\'Send\']')
            send_reply.click()
            time.sleep(random.randint(2, 5))
        except:
            pass

    @classmethod
    def inbox_openClickCategorizeReply(cls, driver, nbMsgs):
        cls.search(driver)
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.click(driver)
                cls.Categorize(driver)
                cls.reply(driver)
                cls.nextMsg(driver)
            except:
                pass

    @classmethod
    def inbox_openClickReplyArchive(cls, driver, nbMsgs):
        cls.search(driver)
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver)
                cls.click(driver)
                cls.reply(driver)
                cls.archive(driver)
            except:
                pass

    @classmethod
    def inbox_openClickReplyFlag(cls, driver, nbMsgs):
        cls.search(driver)
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.click(driver)
                cls.reply(driver)
                cls.flag(driver)
                cls.nextMsg(driver)
            except:
                pass

    @classmethod
    def archive_openFlag(cls, driver, nbMsgs):
        archiveUrl = 'https://outlook.live.com/mail/0/archive'
        driver.get(archiveUrl)
        time.sleep(5)
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.flag(driver)
                cls.nextMsg(driver)
            except:
                pass

    @classmethod
    def importContact(cls, IspUser, driver):
        try:
            current_project_path = os.getcwd()
            try:
                file_path = current_project_path + '\\ressources\\contacts.csv'
            except:
                pass
            while True:  # inserted
                try:
                    contact_url = 'https://outlook.live.com/people/0/'
                    driver.get(contact_url)
                    time.sleep(3)
                except:
                    pass
            while True:  # inserted
                try:
                    manageBtn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label=\'Gérer les contacts\'],Button[aria-label=\'Manage contacts\']')
                    manageBtn.click()
                    time.sleep(1)
                    try:
                        importOpt = driver.find_element(By.CSS_SELECTOR, 'button[name*=\'Import\']')
                        importOpt.click()
                        time.sleep(random.randint(3, 5))
                        break
                    except:
                        pass
                except:
                    pass
        else:  # inserted
            pass  # postinserted
        try:
            file_input = driver.find_element(By.XPATH, '//input[@type=\'file\']')
            file_input.send_keys(file_path)
            time.sleep(random.randint(3, 5))
        except:
            pass
            try:
                span = driver.find_element(By.XPATH, '//span[contains(text(), \'contacts.csv\')]')
                if span:
                    parent = driver.find_element(By.CSS_SELECTOR, 'div[class=\'jtWOl\']')
                    importBtn = parent.find_element(By.CSS_SELECTOR, 'button[class*=\'ms-Button ms-Button--primary\']')
                    importBtn.click()
                    save_to_files('add_contact_done', IspUser.showString())
                    time.sleep(random.randint(3, 5))
                    break
            except:
                pass
        except:
            save_to_files('add_contact_failed', IspUser.showString())

    @classmethod
    def changePassword(cls, IspUser, driver):
        try:
            cls.checkAccount(IspUser, driver)
            new_password = IspUser.newPassword
            old_password = IspUser.password
            if new_password == None:
                print('syntax incorrect: To change password pls follow this sayntax password:::newpassword')
            else:  # inserted
                driver.get('https://account.live.com/password/Change?mkt=fr-FR&refd=account.microsoft.com&refp=profile')
                try:
                    time.sleep(random.randint(1, 3))
                    pwdInput = driver.find_element(By.CSS_SELECTOR, 'input[name=\'passwd\']')
                    pwdInput.send_keys(Keys.CONTROL + 'a')
                    pwdInput.send_keys(Keys.DELETE)
                    pwdInput.send_keys(old_password)
                    time.sleep(random.randint(1, 3))
                    nextBtn = driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\'],button[type=\'submit\']')
                    nextBtn.click()
                except:
                    pass
                try:
                    mailPart = getFirstPart(IspUser.email)
                    time.sleep(random.randint(1, 3))
                    EmailBtn = driver.find_element(By.CSS_SELECTOR, 'div[role=\'button\']')
                    time.sleep(1)
                    EmailBtn.click()
                    email = driver.find_element(By.CSS_SELECTOR, 'input[id*=\"idTxtBx\"]')
                    email.send_keys(Keys.CONTROL + 'a')
                    email.send_keys(Keys.DELETE)
                    secendpart = getFirstPart(IspUser.recovery, True)
                    email.send_keys(f'{mailPart}@{secendpart}')
                    time.sleep(random.randint(1, 3))
                    sendBtn = driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\'],button[type=\'submit\']')
                    sendBtn.click()
                    if secendpart == 'mailforspam.com':
                        fact = mailforspam(driver, mailPart)
                    else:  # inserted
                        fact = mainlnesia(driver, mailPart)
                    if not fact:
                        save_to_files('recovery-wrong', IspUser.showString())
                        driver.quit()
                    try:
                        continueBtn = driver.find_element(By.CSS_SELECTOR, 'button[type=\'button\']')
                        continueBtn.click()
                        time.sleep(random.randint(1, 3))
                    except:
                        pass
                try:
                    notNow = driver.find_element(By.CSS_SELECTOR, 'a[id=\'iCancel\']')
                    notNow.click()
                    time.sleep(random.randint(1, 3))
                except:
                    pass
                except:
                    pass
                time.sleep(random.randint(1, 3))
                password_fields = driver.find_elements(By.CSS_SELECTOR, 'input[type=\'password\']')
                time.sleep(random.randint(2, 3))
                password_fields[0].send_keys(old_password)
                time.sleep(random.randint(2, 3))
                password_fields[1].send_keys(new_password)
                time.sleep(random.randint(2, 3))
                password_fields[2].send_keys(new_password)
                time.sleep(random.randint(2, 3))
                submitBtn = driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\']')
                submitBtn.click()
                time.sleep(random.randint(3, 5))
                save_to_files('password_changed', IspUser.showString())
        except:
            save_to_files('password_NotChanged', IspUser.showString())

    @classmethod
    def createFilter(cls, driver):
        return

    @classmethod
    def cleanAll(cls, driver):
        while True:  # inserted
            try:
                cls.selectPage(driver)
                deletBtn = driver.find_elements(By.CSS_SELECTOR, 'button[class*=\'splitPrimaryButton root\']')[1]
                deletBtn.click()
                time.sleep(1)
                okBtn = driver.find_element(By.CSS_SELECTOR, 'button[class*=\'ms-Button ms-Button--primary jya0z root-\']')
                okBtn.click()
            except:
                break

    @classmethod
    def search(cls, driver):
        try:
            seachkey = cls.read_file('search.txt')
            if seachkey:
                try:
                    search_input = driver.find_element(By.CSS_SELECTOR, 'input[class*=\'uz227\']')
                    search_input.send_keys(seachkey)
                    search_input.send_keys(Keys.RETURN)
                    time.sleep(random.randint(1, 4))
                except:
                    pass
        except:
            print('search.txt not exist')

    @classmethod
    def actionByChoice(cls, IspUser, driver, nbMsgs):
        acts_filename = 'actions.txt'
        acts_list = cls.read_file(acts_filename)
        cat, acts_func = acts_list[0].split(':')
        acts_func = acts_func.split(';')
        if acts_func == 'changePassword':
            cls.changePassword(IspUser, driver)
        else:  # inserted
            if acts_func == 'importContact':
                cls.importContact(IspUser, driver)
            else:  # inserted
                if acts_func == 'clean':
                    cls.cleanAll(IspUser, driver)
                else:  # inserted
                    if acts_func == 'checkAccount' or acts_func == 'createProfiles':
                        cls.checkAccount(IspUser, driver)
                    else:  # inserted
                        if acts_func:
                            instance = HotmailActions()
                            if cat == 'spam':
                                cls.goToJunk(driver)
                                driver.refresh()
                            for i in range(nbMsgs):
                                for act in acts_func:
                                    method = getattr(HotmailActions, act, None)
                                    if method and callable(method) and hasattr(method, '__self__') and (method.__self__ is HotmailActions):
                                        method(driver)
                                    else:  # inserted
                                        save_to_files('log', f'Function \'{act}\' not found or not callable.')

    @classmethod
    def randomActions(cls, driver, nbMsgs):
        function_data = [(cls.click, [driver]), (cls.Categorize, [driver]), (cls.flag, [driver]), (cls.reply, [driver]), (cls.archive, [driver])]
        for _ in range(nbMsgs):
            cls.openMsg(driver)
            num_functions_to_select = random.randint(1, len(function_data))
            selected_functions = random.sample(function_data, k=num_functions_to_select)
            for selected_function, args in selected_functions:
                selected_function(*args)
            cls.nextMsg(driver)

class YahooActions:
    def urls():
        LoginUrl = 'https://login.yahoo.com/'
        MainUrl = 'https://mail.yahoo.com/'
        url_list = [MainUrl]
        return url_list

    @classmethod
    def read_file(cls, filename):
        try:
            folder = 'ressources'
            actsPath = os.path.join(folder, filename)
            with open(actsPath, 'r') as file:
                data = file.read().splitlines()
                return data
        except:
            print(f'File {filename} not found.')
            return None

    @classmethod
    def close_secend_window(cls, driver):
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    @classmethod
    def checkAccount(cls, IspUser, driver, close=False):
        MainUrl = 'https://mail.yahoo.com/'
        time.sleep(3)
        currentUrl = driver.current_url
        separators = ['d/folders']
        for separator in separators:
            try:
                currentUrl = currentUrl.split(separator, 1)[0]
            except:
                pass
        url_list = cls.urls()
        if not (currentUrl in url_list and (not close)):
            save_to_files('ok', IspUser.showString())
            driver.quit()
        else:  # inserted
            if currentUrl!= MainUrl:
                createProfiles.login_to_yahoo(IspUser, driver)

    @classmethod
    def openMsg(cls, driver, i=0):
        driver.implicitly_wait(3)
        rows = driver.find_elements(By.CSS_SELECTOR, 'div[class*=\"D_F r_P a\"]')[i]
        rows.click()
        time.sleep(random.randint(3, 6))
        driver.implicitly_wait(10)

    @classmethod
    def loginWait(cls, driver):
        while True:  # inserted
            try:
                currentUrl = driver.current_url
            except:
                driver.close()
                break

    @classmethod
    def goToSpam(cls, driver):
        spamUrl = 'https://mail.yahoo.com/d/folders/6'
        driver.get(spamUrl)
        driver.refresh()
        time.sleep(random.randint(2, 4))

    @classmethod
    def NotSpam(cls, driver):
        driver.find_element(By.CSS_SELECTOR, 'button[aria-label*=\'spam\'], button[aria-label*=\'légitime\']').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    def reportNotSpam(cls, driver):
        cls.goToSpam(driver)
        while True:  # inserted
            try:
                cls.openMsg(driver)
                cls.NotSpam(driver)
            except:
                break

    @classmethod
    def selectPage(cls, driver):
        driver.find_element(By.CSS_SELECTOR, 'button[tabindex=\'30\']').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    def selectPage_notSpam(cls, driver):
        cls.goToSpam(driver)
        while True:  # inserted
            try:
                cls.selectPage(driver)
                cls.NotSpam(driver)
            except:
                break

    @classmethod
    def click(cls, driver):
        try:
            image_elements = driver.find_elements(By.CSS_SELECTOR, 'img')
            largest_image = None
            largest_area = 0
            for img in image_elements:
                width = int(img.get_attribute('width') or 0)
                height = int(img.get_attribute('height') or 0)
                if width > 32:
                    area = width * height
                if area > largest_area:
                    largest_area = area
                    largest_image = img
            largest_image.click()
            if len(driver.window_handles) > 1:
                time.sleep(random.randint(5, 8))
                cls.close_secend_window(driver)
                time.sleep(random.randint(1, 2))
            wrong_img = None
            wrong_img = driver.find_element(By.CSS_SELECTOR, '.aLF-aPX-aPU-JX')
            if wrong_img:
                time.sleep(random.randint(1, 2))
                back_btn = driver.find_element(By.CSS_SELECTOR, '.aLF-aPX-Jq-I.aLF-aPX-auO-I.J-J5-Ji.aLF-aPX-I')
                back_btn.click()
        except:
            pass

    @classmethod
    def archive(cls, driver):
        try:
            archiveBtn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label*=\'Archiv\' i]').click()
            time.sleep(random.randint(2, 5))
        except:
            pass

    @classmethod
    def star(cls, driver):
        try:
            driver.find_element(By.CSS_SELECTOR, 'button[data-test-id*=\'star\'],button[data-test-id*=\'étoile\']').click()
            time.sleep(random.randint(2, 5))
        except:
            pass

    @classmethod
    def nextMsg(cls, driver):
        try:
            driver.find_element(By.CSS_SELECTOR, 'button[data-test-id*=\'next\'],button[data-test-id*=\'suivante\']').click()
            time.sleep(random.randint(2, 5))
        except:
            pass

    @classmethod
    def inbox_openClick(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver)
                cls.click(driver)
                cls.nextMsg(driver)
            except:
                break

    @classmethod
    def inbox_openClickStar(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver)
                cls.click(driver)
                cls.star(driver)
                cls.nextMsg(driver)
            except:
                break

    @classmethod
    def inbox_openClickArchive(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver)
                cls.click(driver)
                cls.archive(driver)
                cls.nextMsg(driver)
            except:
                break

    @classmethod
    def reply(cls, driver):
        try:
            replys = cls.read_file('replys.txt')
            if replys:
                replyMsg = random.choice(replys)
            else:  # inserted
                replyMsg = generate_random_string()
            replyBtn = driver.find_elements(By.CSS_SELECTOR, 'button[data-kind*=\'reply\']')[0]
            replyBtn.click()
            time.sleep(random.randint(2, 5))
            reply_input = driver.find_element(By.CSS_SELECTOR, 'div[role=\'textbox\']')
            reply_input.clear()
            reply_input.send_keys(replyMsg)
            time.sleep(random.randint(2, 5))
            send_reply = driver.find_element(By.CSS_SELECTOR, 'button[data-test-id=\'compose-send-button\']')
            send_reply.click()
            time.sleep(random.randint(2, 5))
        except:
            pass

    @classmethod
    def inbox_openReply(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.reply(driver)
                cls.nextMsg(driver)
            except:
                break

    @classmethod
    def inbox_openStar(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.star(driver)
                cls.nextMsg(driver)
            except:
                break

    @classmethod
    def inbox_openArchive(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.archive(driver)
                cls.nextMsg(driver)
            except:
                break

    @classmethod
    def inbox_openClickReply(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.click(driver)
                cls.reply(driver)
                cls.nextMsg(driver)
            except:
                break

    @classmethod
    def inbox_openClickReplyArchive(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver)
                cls.click(driver)
                cls.reply(driver)
                cls.archive(driver)
                cls.nextMsg(driver)
            except:
                break

    @classmethod
    def inbox_openClickStarReply(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.click(driver)
                cls.star(driver)
                cls.reply(driver)
                cls.nextMsg(driver)
            except:
                pass

    @classmethod
    def inbox_openClickStarArchive(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.click(driver)
                cls.star(driver)
                cls.archive(driver)
                cls.nextMsg(driver)
            except:
                pass

    @classmethod
    def inbox_openClickStarReplyArchive(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.click(driver)
                cls.star(driver)
                cls.reply(driver)
                cls.archive(driver)
                cls.nextMsg(driver)
            except:
                pass

    @classmethod
    def inbox_openStarReplyArchive(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.star(driver)
                cls.reply(driver)
                cls.archive(driver)
                cls.nextMsg(driver)
            except:
                pass

    @classmethod
    def inbox_openReplyArchive(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.reply(driver)
                cls.archive(driver)
                cls.nextMsg(driver)
            except:
                pass

    @classmethod
    def inbox_openStarArchive(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.star(driver)
                cls.archive(driver)
                cls.nextMsg(driver)
            except:
                pass

    @classmethod
    def inbox_allArchive(cls, driver, nbMsgs):
        for i in range(nbMsgs):
            try:
                cls.openMsg(driver, i)
                cls.selectPage(driver)
                cls.archive(driver)
            except:
                pass

    @classmethod
    def importContact(cls, IspUser, driver):
        try:
            current_project_path = os.getcwd()
            file_path = current_project_path + '\\ressources\\contacts.csv'
            try:
                time.sleep(3)
                ContatsBtn = driver.find_element(By.CSS_SELECTOR, 'button[title*=\'Contact\' i]')
                ContatsBtn.click()
                time.sleep(1)
                file_input = driver.find_element(By.XPATH, '//input[@type=\'file\']')
                file_input.send_keys(file_path)
                time.sleep(random.randint(5, 8))
                save_to_files('add_contact_done', IspUser.showString())
            except:
                pass
        except:
            save_to_files('add_contact_failed', IspUser.showString())

    @classmethod
    def changePassword(cls, IspUser, driver):
        try:
            cls.checkAccount(IspUser, driver)
            new_password = IspUser.newPassword
            old_password = IspUser.password
            if new_password == None:
                print('syntax incorrect: To change password pls follow this sayntax password:::newpassword')
            else:  # inserted
                driver.get('https://login.yahoo.com/account/security?.intl=us&.lang=en-US&.done=https%3A%2F%2Fwww.yahoo.com%2F')
                try:
                    time.sleep(random.randint(1, 3))
                    email = driver.find_element(By.CSS_SELECTOR, 'input[name=\"username\"]')
                    email.clear()
                    email.send_keys(IspUser.email)
                    time.sleep(2)
                    nextBtn = driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\'],button[type=\'submit\']')
                    nextBtn.click()
                    time.sleep(random.randint(3, 5))
                    pwd = driver.find_element(By.CSS_SELECTOR, 'input[class=\"password\"]')
                    pwd.send_keys(Keys.CONTROL + 'a')
                    pwd.send_keys(Keys.DELETE)
                    pwd.send_keys(old_password)
                    time.sleep(2)
                    time.sleep(random.randint(1, 3))
                    nextBtn = driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\'],button[type=\'submit\']')
                    nextBtn.click()
                except:
                    pass
                time.sleep(random.randint(1, 3))
                driver.find_elements(By.CSS_SELECTOR, 'a[class=\'idc-action\']')[0].click()
                pwdInput = driver.find_element(By.CSS_SELECTOR, 'input[id=\'createNPwdTxtField\']')
                pwdInput.send_keys(Keys.CONTROL + 'a')
                pwdInput.send_keys(Keys.DELETE)
                pwdInput.send_keys(new_password)
                time.sleep(random.randint(1, 3))
                nextBtn = driver.find_element(By.CSS_SELECTOR, 'button[class*=\'btn btn-primary\']')
                nextBtn.click()
                save_to_files('password_changed', IspUser.showString())
        except:
            save_to_files('password_NotChanged', IspUser.showString())

    @classmethod
    def cleanAll(cls, driver):
        while True:  # inserted
            try:
                cls.selectPage(driver)
                deletBtn = driver.find_element(By.CSS_SELECTOR, 'button[data-test-id=\'toolbar-delete\']')
                deletBtn.click()
                time.sleep(5)
            except:
                break

    @classmethod
    def actionByChoice(cls, IspUser, driver, nbMsgs):
        acts_filename = 'actions.txt'
        acts_list = cls.read_file(acts_filename)
        cat, acts_func = acts_list[0].split(':')
        acts_func = acts_func.split(';')
        if acts_func == 'changePassword':
            cls.changePassword(IspUser, driver)
        else:  # inserted
            if acts_func == 'changeRecovry':
                cls.changeRecovery(IspUser, driver)
            else:  # inserted
                if acts_func == 'changePasswordRecovry':
                    cls.changePasswordRecovery(IspUser, driver)
                else:  # inserted
                    if acts_func == 'importContact':
                        cls.importContact(IspUser, driver)
                    else:  # inserted
                        if acts_func == 'clean':
                            cls.cleanAll(IspUser, driver)
                        else:  # inserted
                            if acts_func == 'checkAccount' or acts_func == 'createProfiles':
                                cls.checkAccount(IspUser, driver)
                            else:  # inserted
                                if acts_func:
                                    instance = YahooActions()
                                    if cat == 'spam':
                                        cls.goToSpam(driver)
                                    for i in range(nbMsgs):
                                        for act in acts_func:
                                            method = getattr(YahooActions, act, None)
                                            if method and callable(method) and hasattr(method, '__self__') and (method.__self__ is YahooActions):
                                                method(driver)
                                            else:  # inserted
                                                save_to_files('log', f'Function \'{act}\' not found or not callable.')

    @classmethod
    def randomActions(cls, driver, nbMsgs):
        function_data = [(cls.click, [driver]), (cls.star, [driver]), (cls.reply, [driver]), (cls.archive, [driver])]
        for _ in range(nbMsgs):
            cls.openMsg(driver)
            num_functions_to_select = random.randint(1, len(function_data))
            selected_functions = random.sample(function_data, k=num_functions_to_select)
            for selected_function, args in selected_functions:
                selected_function(*args)
            cls.nextMsg(driver)