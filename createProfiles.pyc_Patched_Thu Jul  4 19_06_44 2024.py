# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: C:\Users\FUJITSU\Documents\GitHub\ALMA_REPORTING\createProfiles.py
# Bytecode version: 3.8.0rc1+ (3413)
# Source timestamp: 2024-07-01 21:16:35 UTC (1719868595)

import random
import time
from EmailClient import save_to_files, CreateDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from twocaptcha import TwoCaptcha
import requests
import os

def save_data_to_list(login_data):
    try:
        data = ''
        if login_data['newpassword']!= None and login_data['newrecovery']!= None:
            data = f"{login_data['email']};{login_data['password']}###{login_data['newpassword']};{login_data['ip']};{login_data['port']};{login_data['recovery']}###{login_data['newrecovery']}\n"
            return data
    except:
        pass
    try:
        if login_data['newpassword']!= None:
            data = f"{login_data['email']};{login_data['password']}###{login_data['newpassword']};{login_data['ip']};{login_data['port']};{login_data['recovery']}\n"
            return data
    except:
        pass
    try:
        if login_data['newrecovery']!= None:
            data = f"{login_data['email']};{login_data['password']};{login_data['ip']};{login_data['port']};{login_data['recovery']}###{login_data['newrecovery']}\n"
            return data
    except:
        pass
    try:
        data = f"{login_data['email']};{login_data['password']};{login_data['ip']};{login_data['port']};{login_data['recovery']}\n"
        return data
    except:
        pass

def solve_captcha(driver, url, isp='', IspUser=''):
    try:
        api_key = ''
        if url == 'check':
            solver = TwoCaptcha(api_key)
            i = 0
            while i < 3:
                try:
                    img = driver.find_element(By.CSS_SELECTOR, 'img[src*=\"Captcha\"]')
                    img_src = img.get_attribute('src')
                    result = solver.normal(img_src)
                    code = result['code']
                    driver.find_element(By.CSS_SELECTOR, 'input[type=\"text\"]').send_keys(code)
                    time.sleep(1)
                    driver.find_element(By.CSS_SELECTOR, 'button[class*=\'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ \']').click()
                    time.sleep(3)
                    check_url = driver.current_url
                    check_url = check_url.split('?')[0]
                    if check_url == 'https://accounts.google.com/v3/signin/challenge/pwd' or check_url == 'https://accounts.google.com/signin/v2/challenge/pwd':
                        break
                except:
                    pass
        while True:  # inserted
            try:
                pwd = driver.find_element('xpath', '//input[@type=\"password\" and @name=\"password\"]')
                break
            except:
                try:
                    pwd = driver.find_element('xpath', '//input[@type=\"password\" and @name=\"Passwd\"]')
                    break
                except:
                    pass
        auth = False
        try:
            driver.find_element(By.CSS_SELECTOR, 'div[class=\'captcha-solver captcha-solver_inner\']')
            auth = True
        except:
            pass
        if auth or len(driver.window_handles) > 1:
            try:
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(1)
                input = driver.find_element(By.CSS_SELECTOR, 'input[type=\"text\"]')
                input.clear()
                input.send_keys(api_key)
                driver.find_element(By.CSS_SELECTOR, 'button[id=\"connect\"]').click()
                try:
                    driver.close()
                except:
                    driver.close()
            except:
                pass
        else:  # inserted
            try:
                driver.execute_script('window.open(\'\');')
                driver.switch_to.window(driver.window_handles[1])
                driver.get('chrome-extension://ifibfemgeogfhoebkmokieepdoobkbpo/options/options.html')
                time.sleep(1)
                input = driver.find_element(By.CSS_SELECTOR, 'input[type=\"text\"]')
                input.clear()
                input.send_keys(api_key)
                driver.find_element(By.CSS_SELECTOR, 'button[id=\"connect\"]').click()
                try:
                    driver.close()
                except:
                    driver.close()
            except:
                pass
            driver.switch_to.window(driver.window_handles[0])
            driver.refresh()
            time.sleep(3)
        solving = True
        try:
            driver.find_element(By.CSS_SELECTOR, 'div[class=\'captcha-solver captcha-solver_inner\']').click()
        except:
            solving = False
        while solving:
            try:
                driver.find_element(By.CSS_SELECTOR, 'div[data-state=\'solved\']')
                break
            except:
                pass
        time.sleep(1)
        try:
            submit_btn = driver.find_elements(By.CSS_SELECTOR, 'button[type=\"submit\"],button[type=\"button\"]')[0]
            submit_btn.click()
        except:
            pass
        time.sleep(2)
        if isp == 'gmail':
            try:
                pwd = driver.find_element('xpath', '//input[@type=\"password\" and @name=\"password\"]')
            else:  # inserted
                try:
                    pwd = driver.find_element('xpath', '//input[@type=\"password\" and @name=\"Passwd\"]')
                except:
                    pass
            try:
                if pwd:
                    @pwd.send_keys
                    IspUser.password)
                    time.sleep(1)

                    @driver.find_element
                    By.CSS_SELECTOR('button[class*=\'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ\']').click()
                pass
            except:
                pass
            try:
                time.sleep(3)

                @driver.find_elements
                send_keys = By.CSS_SELECTOR('input[type=\"password\"]')[0].send_keys
                IspUser.password('1')
                time.sleep(1)

                @driver.find_elements
                send_keys = By.CSS_SELECTOR('input[type=\"password\"]')[1].send_keys
                IspUser.password('1')
                time.sleep(1)
                By.CSS_SELECTOR('input[type=\'submit\'],button[type=\'button\']').click()

                @save_to_files('forced_tochangePwd')
                IspUser.showString()
            except:
                pass  # postinserted
            try:
                pwd_wrong = By.CSS_SELECTOR('div[jsname=\'B34EJ\'] span[jsslot=\'\']') if pwd_wrong else 'div[jsname=\'B34EJ\'] span[jsslot=\'\']'
                save_to_files('wrong_password', IspUser.showString())(driver.quit())
                pass
            except:
                pass
            try:
                @driver.find_elements
                recov = By.CSS_SELECTOR('div[role=\'link\'][data-accountrecovery=\'false\']')
                recov[2].click()
            else:  # inserted
                recov[1].click()

                @driver.find_element
                recoveryInput = By.CSS_SELECTOR('input[type=\'email\']')
                IspUser.recovery)
                time.sleep(1)
                nextBtn = By.CSS_SELECTOR('button[class*=\'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ\']')
                nextBtn.click()
                try:
                    try:
                        recov_wrong = By.CSS_SELECTOR('div.o6cuMc.Jj6Lae')
                    except:
                        try:
                            recov_wrong = By.CSS_SELECTOR('div[jsname=\'TMYUoe\']')
                        except:
                            pass  # postinserted
                    pass
                    if recov_wrong:
                        save_to_files('wrong_recovery', IspUser.showString())(driver.quit())
                    pass
                except:
                    pass  # postinserted
            pass
            except:
                pass
            try:
                @driver.find_element
                By.CSS_SELECTOR('div[class=\'captcha-solver captcha-solver_inner\']').click()
            else:  # inserted
                solving = False
            time.sleep(10)
        pass
    else:  # inserted
        pass  # postinserted
    pass
    except Exception as e:
        try:
            pass  # postinserted
        e = None
    else:  # inserted
        pass
    return None

def sms_recieve(driver):
    SELECTORS = {'next': ['//button[@class=\'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b\']', '//input[@type=\'submit\']', '//button[@class=\'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b\']', '//button[contains(text(),\'Next\')]'], 'code': ['idvAnyPhonePin', 'smsUserPin']}
    WAIT = 4
    AUTO_GENERATE_NUMBER = 10
    API_KEY = ''
    COUNTRY_CODE = '6'
    REQUEST_MAX_TRY = 5
    sms_activate_url = 'https://sms-activate.org/stubs/handler_api.php'
    phone_request_params = {'api_key': API_KEY, 'action': 'getNumber', 'country': COUNTRY_CODE, 'service': 'go'}
    status_param = {'api_key': API_KEY, 'action': 'getStatus'}
    try:
        phone_number_input = driver.find_element(By.XPATH, '//*[@type=\'tel\']')
        if phone_number_input:
            while True:  # inserted
                count = 0
                while count < REQUEST_MAX_TRY:
                    res = requests.get(url=sms_activate_url, params=phone_request_params)
                    data = res.text
                    if 'ACCESS_NUMBER' in data:
                        activationId = data.split(':')[1]
                        number = data.split(':')[2]
                        number = '+' + number
                    else:  # inserted
                        if 'NO_BALANCE' in data:
                            exit()
                        count = count + 1
                        time.sleep(WAIT)
                if number == '':
                    break
                phone_number_input.clear()
                phone_number_input.send_keys(number)
                for selector in SELECTORS['next']:
                    try:
                        driver.find_element(By.XPATH, selector).click()
                        break
                    except:
                        pass
                try:
                    time.sleep(3)
                    for selector in SELECTORS['code']:
                        try:
                            inputcode = driver.find_element(By.ID, selector)
                            break
                        except:
                            pass
                    try:
                        if inputcode:
                            break
                    except:
                        pass
                    else:  # inserted
                        try:
                            driver.find_element(By.CSS_SELECTOR, 'button[name=\'action\']').click()
                        except:
                            pass
                except:
                    pass
                time.sleep(2)
            time.sleep(WAIT)
            count_status = 0
            code = ''
            while count_status < REQUEST_MAX_TRY:
                status_param['id'] = activationId
                res_code = requests.get(url=sms_activate_url, params=status_param)
                data_code = res_code.text
                if 'STATUS_OK' in data_code:
                    code = data_code.split(':')[1]
                    break
                count_status = count_status + 1
                time.sleep(WAIT * 5)
            if code == '':
                driver.get('https://accounts.google.com/v3/signin/challenge/pwd?')
                break
            for selector in SELECTORS['code']:
                try:
                    driver.find_element(By.ID, selector).send_keys(code)
                    break
                except:
                    pass
            for selector in SELECTORS['next']:
                try:
                    driver.find_element(By.XPATH, selector).click()
                    break
                except:
                    pass
    except:
        pass

def support_verfication(IspUser, driver, isp, manual):
    url = driver.current_url
    try:
        if driver.find_element(By.XPATH, './/iframe[@title=\'reCAPTCHA\']'):
            solve_captcha(driver, url, isp, IspUser)
    except:
        pass
    if not manual:
        try:
            try:
                driver.find_element(By.CSS_SELECTOR, 'input[aria-label=\'Enter code\']')
            except:
                if driver.find_element(By.XPATH, '//*[@type=\'tel\']'):
                    sms_recieve(driver)
        except:
            pass
        try:
            driver.find_elements(By.CSS_SELECTOR, 'input[type=\"password\"]')[0].send_keys(IspUser.password + '1')
            time.sleep(1)
            driver.find_elements(By.XPATH, 'input[id=\"Password\"]')[1].send_keys(IspUser.password + '1')
            time.sleep(1)
            driver.find_element(By.XPATH, 'input[type=\'submit\']').click()
            save_to_files('forced_tochangePwd', IspUser.showString())
        except:
            pass
    else:  # inserted
        while True:  # inserted
            try:
                driver.current_url
            except:
                break
            else:  # inserted
                exit()

def generate_message(file='request_msgs.txt'):
    path = os.path.join('ressources', file)
    with open(path, 'r') as file:
        lines = file.readlines()
    extracted_messages = []
    current_message = ''
    for line in lines:
        if line.strip():
            current_message += line.strip() + '\n'
        else:  # inserted
            if current_message:
                extracted_messages.append(current_message.strip())
                current_message = ''
    if current_message:
        extracted_messages.append(current_message.strip())
    message = random.choice(extracted_messages)
    return message

def generate_email(file='request_emails.txt'):
    path = os.path.join('ressources', file)
    with open(path, 'r') as file:
        lines = file.readlines()
    message = random.choice(lines)
    return message

def support_disabled(IspUser, driver, manual):
    try:
        if not manual:
            url = driver.current_url
            url = url.split('?')[0]
            if url == 'https://accounts.google.com/signin/v2/disabled/appeal/received':
                save_to_files('already_requested', IspUser.showString())
                driver.quit()
                return True
            driver.find_element(By.CSS_SELECTOR, 'button[class*=\'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ').click()
            url = driver.current_url
            url = url.split('?')[0]
            if url == 'https://accounts.google.com/signin/v2/disabled/appeal/received':
                save_to_files('already_requested', IspUser.showString())
                driver.quit()
                return True
            time.sleep(3)
            driver.find_element(By.CSS_SELECTOR, 'button[class*=\'VfPpkd\']').click()
            msg = generate_message()
            time.sleep(1)
            input = driver.find_elements(By.CSS_SELECTOR, 'textarea[class=\'KHxj8b tL9Q4c\']')[0]
            time.sleep(1)
            input.send_keys(msg)
            time.sleep(3)
            inpt = driver.find_element(By.CSS_SELECTOR, 'input[type=\'email\']')
            time.sleep(1)
            file_path = os.path.join('ressources', 'request_emails.txt')
            email = generate_email()
            inpt.send_keys(email)
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, 'button[class*=\'VfPpkd\']').click()
            time.sleep(3)
            save_to_files('requested', IspUser.showString())
            driver.quit()
            return True
        while True:  # inserted
            try:
                driver.current_url
            except:
                break
            else:  # inserted
                exit()
    except:
        driver.quit()
        return True

def support_restracted(IspUser, driver, manual):
    driver.get('https://myaccount.google.com/restrictions/54')
    try:
        driver.find_element(By.CSS_SELECTOR, 'div[class=\'wLFk5\']')
        save_to_files('already_requested', IspUser.showString())
    except:
        try:
            driver.find_element(By.CSS_SELECTOR, 'div[class=\'VfPpkd-ksKsZd-XxIAqe i3FRte\']').click()
            if not manual:
                msg = generate_message()
                input = driver.find_elements(By.CSS_SELECTOR, 'textarea[class*=\'VfPpkd\']')[0]
                input.send_keys(msg)
                driver.find_element(By.CSS_SELECTOR, 'button[class*=\'UywwFc-LgbsSe\']').click()
                save_to_files('requested', IspUser.showString())
            else:  # inserted
                while True:  # inserted
                    try:
                        driver.current_url
                    except:
                        break
        except:
            save_to_files('restricted_2step', IspUser.showString())

def result_check_gmail(IspUser, driver, close, support, manual):
    try:
        MainUrl = 'https://mail.google.com/mail/u/0/'
        RestrictedUrl = 'https://accounts.google.com/v3/signin/productaccess/landing'
        RestrictedUrl2 = 'https://support.google.com/accounts/answer/40039'
        RestrictedUrl3 = 'https://myaccount.google.com/restrictions/54'
        disable = 'https://accounts.google.com/signin/v2/deniedsigninrejected'
        disable2 = 'https://accounts.google.com/v3/signin/rejected'
        disable3 = 'https://accounts.google.com/signin/v2/disabled/explanation'
        captchaV2 = 'https://accounts.google.com/signin/v2/challenge/recaptcha'
        captchaV3 = 'https://accounts.google.com/v3/signin/challenge/recaptcha'
        insecure = 'https://accounts.google.com/v3/signin/confirmidentifier'
        easy_captcha = 'https://accounts.google.com/speedbump/captchareenable'
        undertandsuit = 'https://accounts.google.com/speedbump/gaplustos'
        not_now = 'https://gds.google.com/web/chip'
        phonenumber = 'https://accounts.google.com/v3/signin/challenge/iap'
        verification = 'https://accounts.google.com/speedbump/idvreenable'
        verification2 = 'https://accounts.google.com/speedbump/idvreenable/sendidv'
        twostep = ['https://accounts.google.com/v3/signin/challenge/ipp/collect', 'https://accounts.google.com/v3/signin/challenge/bc', 'https://accounts.google.com/v3/signin/challenge/wa', 'https://accounts.google.com/v3/signin/challenge/ootp', 'https://accounts.google.com/v3/signin/challenge/sq', 'https://accounts.google.com/v3/signin/challenge/ipe/verify', 'https://accounts.google.com/v3/signin/challenge/dp', 'https://accounts.google.com/v3/signin/challenge/ipp/consent', 'https://accounts.google.com/signin/v2/challenge/bc']
        time.sleep(2)
        current_url = driver.current_url
        current_url = current_url.split('?', 1)[0]
        if current_url == RestrictedUrl or current_url == RestrictedUrl2 or current_url == RestrictedUrl3:
            if close and support == False:
                save_to_files('Restricted', IspUser.showString())
                driver.quit()
                return True
            if support:
                support_restracted(IspUser, driver, manual)
                driver.quit()
                return True
            while True:  # inserted
                try:
                    driver.current_url
                except:
                    break
        else:  # inserted
            if current_url == disable or current_url == disable2 or current_url == disable3:
                if close:
                    element = driver.find_element(By.CSS_SELECTOR, 'span.VfPpkd-vQzf8d')
                    text = element.text
                    if text == 'Continue' or text == 'Continuer':
                        save_to_files('VerifyItsYou', IspUser.showString())
                        driver.quit()
                        return True
                    if disable3 and support:
                        result = support_disabled(IspUser, driver, manual)
                        if result:
                            return True
                    else:  # inserted
                        save_to_files('disabled', IspUser.showString())
                        driver.quit()
                        return True
                else:  # inserted
                    while True:  # inserted
                        try:
                            driver.current_url
                        except:
                            break
            else:  # inserted
                if current_url == captchaV2:
                    if close and support == False:
                        save_to_files('recaptchaV2', IspUser.showString())
                        driver.quit()
                        return True
                    if support:
                        url = driver.current_url
                        solve_captcha(driver, url, 'gmail', IspUser)
                        result = result_check_gmail(IspUser, driver, close, support, manual)
                        if result:
                            driver.quit()
                            return True
                    else:  # inserted
                        while True:  # inserted
                            try:
                                driver.current_url
                            except:
                                break
                else:  # inserted
                    if current_url == captchaV3:
                        if close and support == False:
                            save_to_files('recaptchaV3', IspUser.showString())
                            driver.quit()
                            return True
                        if support:
                            url = driver.current_url
                            solve_captcha(driver, url, 'gmail', IspUser)
                            result = result_check_gmail(IspUser, driver, close, support, manual)
                            if result:
                                driver.quit()
                                return True
                        else:  # inserted
                            while True:  # inserted
                                try:
                                    driver.current_url
                                except:
                                    break
                    else:  # inserted
                        if current_url == phonenumber or current_url == verification:
                            if close:
                                if support == False:
                                    save_to_files('phonenumber', IspUser.showString())
                                    driver.quit()
                                    return True
                            if support:
                                result = support_verfication(IspUser, driver, 'gmail', manual)
                                if result:
                                    return True
                            else:  # inserted
                                while True:  # inserted
                                    try:
                                        driver.current_url
                                    except:
                                        break
                        else:  # inserted
                            if not current_url == verification:
                                if current_url == verification2:
                                    pass  # postinserted
                            if close and support == False:
                                save_to_files('verification', IspUser.showString())(driver.quit())
                            if support:
                                result = support_verfication(IspUser, driver, 'gmail', manual) if result else True
                            else:  # inserted
                                while True:  # inserted
                                    try:
                                        pass  # postinserted
                                    else:  # inserted
                                        break
                                        else:  # inserted
                                            continue
                            pass
                                else:  # inserted
                                    if not current_url == insecure or close:
                                        save_to_files('confirmidentifier', IspUser.showString())(driver.quit())
                                    while True:  # inserted
                                        try:
                                            pass  # postinserted
                                        else:  # inserted
                                            break
                                            else:  # inserted
                                                continue
                                    if not (current_url in twostep and (not close)):
                                        save_to_files('2tep_vrf', IspUser.showString())(driver.quit())
                                    while True:  # inserted
                                        try:
                                            pass  # postinserted
                                        else:  # inserted
                                            break
                                            else:  # inserted
                                                continue
                                    if not current_url == easy_captcha or close:
                                        save_to_files('easy_captcha', IspUser.showString())(driver.quit())
                                    while True:  # inserted
                                        try:
                                            pass  # postinserted
                                        else:  # inserted
                                            break
                                            else:  # inserted
                                                continue
                                    if current_url == undertandsuit:
                                        driver.find_element(By.CSS_SELECTOR, 'input[class=\'MK9CEd MVpUfe\']').click()
                                    except:
                                        time.sleep(2)
                                        driver.find_element(By.CSS_SELECTOR, 'div[class=\'T-P-aut-UR T-P-aut\']').click()
                                    except:
                                        pass
                                    else:  # inserted
                                        if current_url == not_now and driver.get(MainUrl):
                                            save_to_files('ok', IspUser.showString())(driver.quit())
        pass
    else:  # inserted
        pass  # postinserted
    pass
    except Exception as e:
        try:
            pass  # postinserted
        e = None
    else:  # inserted
        pass
    return None

def login_to_gmail(IspUser, driver, close, support, manual):
    while True:  # inserted
        try:
            LoginUrl = 'https://accounts.google.com/signin/v2/identifier?hl=en&continue=https%3A%2F%2Fmail.google.com%2Fmail&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession'
            MainUrl = 'https://mail.google.com/mail/u/0/'
            AccountUrl = 'https://myaccount.google.com/'
            pliUrl = 'https://myaccount.google.com/?pli=1'
            pliUrlMail = 'https://mail.google.com/mail/u/0/?pli=1'
            SpamUrl = 'https://mail.google.com/mail/u/0/#spam'
            okurl = 'https://mail.google.com/mail/u/0/#inbox'
            url_list = [LoginUrl, MainUrl, AccountUrl, pliUrl, pliUrlMail, SpamUrl, okurl]
            driver.get(LoginUrl)
            try:
                email = driver.find_element(By.CSS_SELECTOR, 'input[name*=\'identifier\']')
                email.send_keys(IspUser.email)
                driver.find_element(By.CSS_SELECTOR, 'button[class*=\'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 \']').click()
            except:
                pass
            try:
                disabled = driver.find_element(By.CSS_SELECTOR, 'a[class=\'WpHeLc VfPpkd-mRLv6 VfPpkd-RLmnJb\']')
                if disabled:
                    driver.quit()
                    save_to_files('disabled', IspUser.showString())
                    driver.quit()
                    break
            except:
                pass
            try:
                driver.find_element('id', 'identifierNext').click()
                keywrds_captcha = driver.find_element(By.CSS_SELECTOR, 'input[type=\"text\"].whsOnd.zHQkBf')
                keywrds_captcha.send_keys()
                if keywrds_captcha and (not support):
                    save_to_files('captcha', IspUser.showString())
                    driver.quit()
                    break
                url = driver.current_url
                solve_captcha(driver, 'check', 'gmail', IspUser)
            except:
                pass
            result = result_check_gmail(IspUser, driver, close, support, manual)
            if result:
                break
            try:
                pwd = driver.find_element('xpath', '//input[@type=\"password\" and @name=\"password\"]')
            except:
                try:
                    pwd = driver.find_element('xpath', '//input[@type=\"password\" and @name=\"Passwd\"]')
                except:
                    pass
            try:
                if pwd:
                    pwd.send_keys(IspUser.password)
                    time.sleep(1)
                    driver.find_element(By.CSS_SELECTOR, 'button[class*=\'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ\']').click()
            except:
                pass
            try:
                pwd_wrong = driver.find_element(By.CSS_SELECTOR, 'div[jsname=\'B34EJ\'] span[jsslot=\'\']')
                if pwd_wrong:
                    save_to_files('wrong_password', IspUser.showString())
                    driver.quit()
                    break
            except:
                pass
            try:
                try:
                    driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\']').click()
                except:
                    pass
                driver.find_element(By.CSS_SELECTOR, 'input[name=\'ConfirmPassword\']')
            except:
                pass
            try:
                recov = driver.find_elements(By.CSS_SELECTOR, 'div[role=\'link\'][data-accountrecovery=\'false\']')
                recov[2].click()
                recoveryInput = driver.find_element(By.CSS_SELECTOR, 'input[type=\'email\']')
                recoveryInput.send_keys(IspUser.recovery)
                time.sleep(1)
                nextBtn = driver.find_element(By.CSS_SELECTOR, 'button[class*=\'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ\']')
                nextBtn.click()
                try:
                    recov_wrong = driver.find_element(By.CSS_SELECTOR, 'div[class=\'Ekjuhf Jj6Lae\']')
                except:
                    try:
                        recov_wrong = driver.find_element(By.CSS_SELECTOR, 'div[jsname=\'TMYUoe\']')
                    except:
                        pass
                    if recov_wrong:
                        save_to_files('wrong_recovery', IspUser.showString())
                        driver.quit()
                        break
                except:
                    pass
            except:
                pass
            try:
                current_url = driver.current_url
                if current_url in url_list:
                    driver.get(MainUrl)
                    time.sleep(5)
                    try:
                        driver.find_element(By.CSS_SELECTOR, 'div[class=\'T-P-aut-UR T-P-aut\']').click()
                    except:
                        pass
                    save_to_files('ok', IspUser.showString())
            except:
                save_to_files('failed', IspUser.showString())(driver.quit())
                break
            else:  # inserted
                driver.implicitly_wait(2)
                result_check_gmail(IspUser, driver, close, support)
                result = manual() if result else manual(manual)
            else:  # inserted
                try:
                    email_value = IspUser.email
                    mail = By.CSS_SELECTOR('div[data-identifier=\'', f'{email_value}\']')
                except:
                    pass
                try:
                    confirm = By.XPATH('//img[@src=\'//www.gstatic.com/identity/boq/accounthealthinterstitialsui/images/dont_get_locked_out.png\']')(confirm, driver.get(MainUrl) if confirm else MainUrl)
                    save_to_files('ok', IspUser.showString())
                else:  # inserted
                    pass
                except:
                    pass
                try:
                    date = By.CSS_SELECTOR('.VfPpkd-fmcmS-wGMbrd')(date, driver.get(MainUrl) if date else MainUrl)
                    save_to_files('ok', IspUser.showString())
                else:  # inserted
                    pass
                except:
                    pass
                try:
                    pass  # postinserted
                except:
                    save_to_files('failed', IspUser.showString())(driver.quit())
                    break
                else:  # inserted
                    for separator in ['#inbox', '#spam'] + separators:
                        current_url = current_url.split(separator, 1)[0]
                    except:
                        continue
                if current_url in url_list and driver.get(MainUrl):
                    time.sleep(5)
                    save_to_files('ok', IspUser.showString())
                else:  # inserted
                    driver.refresh()
                    pass
                except:
                    pass
                continue
    else:  # inserted
        pass
        except Exception as e:
            try:
                save_to_files('log', e.args[0] + '\n')(driver.quit())
                break
            e = None
        else:  # inserted
            pass
    return None

def mainlnesia(driver, mailPart, value=False):
    driver.execute_script('window.open(\'\', \'_blank\');')
    driver.switch_to.window(driver.window_handles[1])
    for i in range(3):
        try:
            driver.get(f'https://mailnesia.com/mailbox/{mailPart}')
            time.sleep(1)
            if value:
                driver.find_element(By.CSS_SELECTOR, 'a[href*=\'mail/\']').click()
            else:  # inserted
                driver.find_element(By.XPATH, '//a[contains(text(), \'Microsoft account security code\')]').click()
            data = driver.find_elements(By.CSS_SELECTOR, '[style*=\'Segoe UI Bold\']')[1]
            data = data.text
            if data:
                break
        except:
            driver.refresh()
    try:
        driver.find_element(By.CSS_SELECTOR, 'img[alt=\'Delete all mail\']').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'input[type=\'button\']').click()
        time.sleep(1)
    except:
        pass
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    try:
        if data:
            tel = driver.find_element(By.CSS_SELECTOR, 'input[type=\'tel\']')
            tel.clear()
            tel.send_keys(data)
            driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\']').click()
            return True
        return False
    except:
        return False

def mailforspam(driver, mailPart, value=False):
    time.sleep(8)
    driver.execute_script('window.open(\'\', \'_blank\');')
    driver.switch_to.window(driver.window_handles[1])
    for i in range(3):
        try:
            driver.get(f'https://www.mailforspam.com/mail/{mailPart}')
            time.sleep(1)
            if value:
                try:
                    driver.find_element(By.CSS_SELECTOR, 'a[href*=\'mail/\']').click()
                except:
                    pass
            else:  # inserted
                try:
                    driver.find_element(By.XPATH, '//a[contains(text(), \'Microsoft account security code\')]').click()
                except:
                    driver.find_element(By.XPATH, '//a[contains(text(), \'Code de sécurité du compte Microsoft\')]').click()
            time.sleep(1)
            body_element = driver.find_element(By.ID, 'messagebody')
            lines = body_element.text.split('\n')
            if value:
                for line in lines:
                    patterns = ['Your single-use code is: ', 'Your single-use code is : ', 'Votre code à usage unique est: ', 'Votre code à usage unique est : ']
                    data = next((line.split(pattern)[1] for pattern in patterns if pattern in line), None)
                    if data:
                        break
            else:  # inserted
                for line in lines:
                    patterns = ['Code de sécurité : ', 'Code de sécurité: ', 'Security code : ', 'Security code: ']
                    data = next((line.split(pattern)[1] for pattern in patterns if pattern in line), None)
                    if data:
                        break
            if data:
                break
        except:
            driver.refresh()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    try:
        if data:
            tel = driver.find_element(By.CSS_SELECTOR, 'input[type=\'tel\']')
            tel.clear()
            tel.send_keys(data)
            driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\']').click()
            return True
        return False
    except:
        return False

def getFirstPart(email, secend=False):
    try:
        if '@' in email:
            username, domain = email.split('@', 1)
            if secend:
                return domain
            return username
    except:
        pass

def login_to_hotmail(IspUser, driver, close=False, wait=False):
    try:
        LoginUrl = 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=21&ct=1708442704&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26nlp%3d1%26deeplink%3dowa%252f%26RpsCsrfState%3d65d04c9c-21c5-309e-2c28-5482fe0bc4f6&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c'
        MainUrl = 'https://outlook.live.com/mail/0/'
        SpamUrl = 'https://outlook.live.com/mail/0/junkemail'
        ContactUrl = 'https://outlook.live.com/people/0/'
        ArchiveUrl = 'https://outlook.live.com/mail/0/archive'
        url_list = [MainUrl, ContactUrl, SpamUrl, ArchiveUrl]
        driver.get(LoginUrl)
        driver.implicitly_wait(5)
        while True:  # inserted
            try:
                time.sleep(1)
                email = driver.find_element(By.CSS_SELECTOR, 'input[type=\"email\"][name=\"loginfmt\"]')
                email.send_keys(Keys.CONTROL + 'a')
                email.send_keys(Keys.DELETE)
                email.send_keys(IspUser.email)
                time.sleep(1)
                nextBtn = driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\'],button[type=\'submit\']')
                nextBtn.click()
                time.sleep(random.randint(1, 2))
            except:
                pass
        try:
            pwd = driver.find_element('xpath', '//input[@type=\"password\" and @name=\"passwd\"]')
            pwd.send_keys(Keys.CONTROL + 'a')
            pwd.send_keys(Keys.DELETE)
            pwd.send_keys(IspUser.password)
            time.sleep(1)
            nextBtn = driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\'],button[type=\'submit\']')
            nextBtn.click()
        except:
            pass
        try:
            driver.find_element(By.CSS_SELECTOR, 'input[id=\'iLooksGood\']').click()
        except:
            pass
        try:
            driver.find_element(By.ID, 'acceptButton').click()
        except:
            pass
        try:
            current_url = driver.current_url
            try:
                current_url = current_url.split('?')[0]
            except:
                pass
            if current_url in url_list:
                driver.get(MainUrl)
                save_to_files('ok', IspUser.showString())
                if close:
                    driver.quit()
                break
        except:
            break
        else:  # inserted
            try:
                secendpart = getFirstPart(IspUser.recovery, True)
                mailPart = getFirstPart(IspUser.recovery)
                recovery = driver.find_element(By.CSS_SELECTOR, 'input[type=\'email\'][aria-label=\'Alternate email address\']')
                recovery.clear()
                if secendpart == 'mailforspam.com':
                    recovery.send_keys(f'{mailPart}@{secendpart}')
                    driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\']').click()
                    check = mailforspam(driver, mailPart)
                else:  # inserted
                    if secendpart == 'mainlnesia.com':
                        recovery.send_keys(f'{mailPart}@{secendpart}')
                        driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\']').click()
                        check = mainlnesia(driver, mailPart)
                if not check and (not wait):
                    save_to_files('failed_add_recovery', IspUser.showString())
                    driver.quit()
                    break
                if wait:
                    while True:  # inserted
                        try:
                            currentUrl = driver.current_url
                        except:
                            driver.close()
                            break
            except:
                pass
            try:
                driver.find_elements(By.CSS_SELECTOR, 'input[type=\'radio\']')[0].click()
                driver.find_element(By.CSS_SELECTOR, 'input[id=\'iProofEmail\']').send_keys(mailPart)
                driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\']').click()
                if secendpart == 'mailforspam.com':
                    fact = mailforspam(driver, mailPart)
                else:  # inserted
                    if secendpart == 'mainlnesia.com':
                        fact = mainlnesia(driver, mailPart)
                if not fact and (not wait):
                    save_to_files('recovery_wrong', IspUser.showString())
                    driver.quit()
                    break
                try:
                            currentUrl = driver.current_url
                        except:
                            driver.close()
                            break
                        else:  # inserted
                            pass
            except:
                pass
            try:
                @mailforspam
                fact = driver(mailPart, True)
            else:  # inserted
                if secendpart == 'mainlnesia.com':
                    fact = mainlnesia(driver, mailPart, True)
                if not fact and (not wait):
                    save_to_files('recovery_wrong', IspUser.showString())
                    driver.quit()
                else:  # inserted
                    pass
            except:
                pass  # postinserted
            try:
                @driver.find_element
                By.ID('acceptButton').click()
            except:
                pass  # postinserted
            try:
                @driver.find_element
                By.CSS_SELECTOR('a[id=\"iCancel\"]').click()
            except:
                pass  # postinserted
            try:
                try:
                    element = By.ID('iVerifyCodeError')
                except:
                    try:
                        element = By.ID('iVerificationErr')
                    except:
                        pass  # postinserted
                pass
                if element and driver.get(LoginUrl):
                    pass  # postinserted
                pass
            except:
                pass  # postinserted
            try:
                @driver.find_element
                pwd_wrong = By.ID('i0118Error') if pwd_wrong else 'i0118Error'
                save_to_files('wrong_password', IspUser.showString())(driver.quit())
            else:  # inserted
                pass
            except:
                pass  # postinserted
            try:
                By.CSS_SELECTOR('a[data-bi-cn=\'SignIn\']')(driver.get(LoginUrl))
            except:
                pass  # postinserted
            try:
                vrf = By.CSS_SELECTOR('input[id=\'StartAction\' i]') if vrf else 'input[id=\'StartAction\' i]'

                @save_to_files('verification')
                IspUser.showString())(driver.quit())
            else:  # inserted
                pass
            except:
                pass  # postinserted
            driver.refresh()
            time.sleep(1)
            driver.current_url = driver.current_url * (current_url.split('?')[0] + (driver.get(MainUrl) if current_url in url_list else MainUrl))
                save_to_files('ok', IspUser.showString()) if close:
                    driver.quit()
                break
            else:  # inserted
                continue
        else:  # inserted
            break
    pass
    else:  # inserted
        pass  # postinserted
    pass
    except Exception as e:
        try:
            save_to_files('log', e.args[0] + '\n')
        e = None
    else:  # inserted
        pass
    return None

def login_to_yahoo(IspUser, driver, close=False):
    try:
        MainUrl = 'https://mail.yahoo.com/'
        url_list = [MainUrl]
        while True:  # inserted
            driver.implicitly_wait(5)
            try:
                driver.find_element(By.CSS_SELECTOR, 'a[name=\'username\']').click()
            except:
                pass
        try:
            email = driver.find_element(By.CSS_SELECTOR, 'input[name=\"username\"]')
            email.clear()
            email.send_keys(IspUser.email)
            time.sleep(2)
            nextBtn = driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\']')
            nextBtn.click()
            time.sleep(random.randint(3, 5))
        except:
            pass
        try:
            driver.find_element(By.CSS_SELECTOR, 'p[id=\'wait-desc\'][class=\'challenge-desc\']')
            save_to_files('blocked_for_now', IspUser.showString())
            break
        except:
            pass
        url = 'https://login.yahoo.net/account/challenge/recaptcha/recaptcha-script?display=login&.lang=en-US&src=homepage&activity=ybar-signin&pspid=2023538075&add=1&done=https%3A%2F%2Fwww.yahoo.com%2F&prefill=0&prompt=login&chllngnm=fail&sessionIndex=QQ--&acrumb=lKC0qfal&authMechanism=primary&lang=en-US&siteKey=6LcbmroaAAAAANQ34XOxul9o_UgaJ6dkdq62Xey6&recaptchaLang=en&recaptchaDomain=www.google.com'
        solve_captcha(driver, url)
        try:
            pwd = driver.find_element(By.CSS_SELECTOR, 'input[type=\"password\"]')
            pwd.send_keys(Keys.CONTROL + 'a')
            pwd.send_keys(Keys.DELETE)
            pwd.send_keys(IspUser.password)
            time.sleep(2)
            nextBtn = driver.find_element(By.CSS_SELECTOR, 'button[type=\'submit\']')
            nextBtn.click()
            driver.find_element(By.CSS_SELECTOR, 'p[class=\'error-msg\']')
            save_to_files('wrong_password', IspUser.showString())
            break
        except:
            pass
        try:
            driver.find_element(By.CSS_SELECTOR, 'button[class*=\'validate-btn\']')
            save_to_files('2step_vrf', IspUser.showString())
            break
        except:
            pass
        try:
            driver.find_element(By.ID, 'scroll-down-btn').click()
            driver.find_element(By.CSS_SELECTOR, 'button[class=\'btn secondary accept-all \']').click()
        except:
            pass
        try:
            driver.find_element(By.CSS_SELECTOR, 'button[type=\'button\'][id*=\'decline\']').click()
        except:
            pass
        try:
            driver.find_element(By.CSS_SELECTOR, 'button[type=\'submit\']').click()
        except:
            pass
        try:
            driver.find_element(By.CSS_SELECTOR, 'button[class*=\'P_1Eu6qC\']').click()
        except:
            pass
        try:
            driver.find_element(By.CSS_SELECTOR, 'button[class*=\'P_0 C_Z29WjXl\']').click()
        except:
            pass
        time.sleep(1)
        try:
            current_url = driver.current_url
            separators = ['d/folders']
            for separator in separators:
                try:
                    current_url = current_url.split(separator, 1)[0]
                except:
                    pass
            if current_url in url_list:
                driver.get(MainUrl)
                time.sleep(5)
                save_to_files('ok', IspUser.showString())
                if close:
                    driver.quit()
                break
        except:
            break
    except Exception as e:
        save_to_files('log', e.args[0] + '\n')