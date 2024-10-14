# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: C:\Users\FUJITSU\Documents\GitHub\ALMA_REPORTING\IspAccount.py
# Bytecode version: 3.8.0rc1+ (3413)
# Source timestamp: 2024-06-20 23:35:03 UTC (1718926503)

from EmailClient import CreateDriver, get_config
from actions import GmailActions, HotmailActions, YahooActions
from threading import Semaphore
nbProcess, nbMsgs, nbLoops = get_config()
semaphore = Semaphore(nbProcess)

def GmailChoices(IspUser, choice):
    try:
        semaphore.acquire()
        while True:  # inserted
            dontCheck = ['1', '2', '15', '16', '17', '25', '26', 0]
            if choice[0]!= 0:
                driver = CreateDriver(IspUser)
            if choice[0] not in dontCheck:
                GmailActions.checkAccount(IspUser, driver)
            if choice[0] == '1':
                GmailActions.checkAccount(IspUser, driver, True)
                break
            if choice[0] == '2':
                GmailActions.checkAccount(IspUser, driver, True)
                break
            if choice[0] == '3':
                GmailActions.loginWait(driver)
                break
            if choice[0] == '4':
                GmailActions.ReporNotSpam(driver)
                break
            if choice[0] == '5':
                GmailActions.selectPage_notSpam(driver)
                break
            if choice[0] == '6':
                GmailActions.inbox_openClick(driver, nbMsgs)
                break
            if choice[0] == '7':
                GmailActions.inbox_openClickImportant(driver, nbMsgs)
                break
            if choice[0] == '8':
                GmailActions.inbox_openClickStart(driver, nbMsgs)
                break
            if choice[0] == '9':
                GmailActions.inbox_openClickImportantStart(driver, nbMsgs)
                break
            if choice[0] == '10':
                GmailActions.inbox_openClickReply(driver, nbMsgs)
                break
            if choice[0] == '11':
                GmailActions.inbox_openClickArchive(driver, nbMsgs)
                break
            if choice[0] == '12':
                GmailActions.selectPage_notSpam_inbox_OpenClickImportantStar(driver, nbMsgs)
                break
            if choice[0] == '13':
                GmailActions.selectPage_notSpam_inbox_OpenClickReply(driver, nbMsgs)
                break
            if choice[0] == '14':
                GmailActions.importContact(IspUser, driver)
                break
            if choice[0] == '15':
                GmailActions.changePassword(IspUser, driver)
                break
            if choice[0] == '16':
                GmailActions.changeRecovry(IspUser, driver)
                break
            if choice[0] == '17':
                GmailActions.changePasswordRecovry(IspUser, driver)
                break
            if choice[0] == '18':
                GmailActions.cleanAll(driver)
                break
            if choice[0] == '19':
                GmailActions.inbox_selectpageReadImportantStart_bySearch(driver, nbMsgs)
                break
            if choice[0] == '20':
                GmailActions.actionByChoice(IspUser, driver, nbMsgs)
            else:  # inserted
                if choice[0] == '21':
                    GmailActions.selectPage_notSpam_inbox_selectpageReadImportantStartArchive(driver, nbMsgs)
                    break
                if choice[0] == '22':
                    GmailActions.inbox_openStartReply(driver, nbMsgs)
                    break
                if choice[0] == '23':
                    GmailActions.notPromotions(driver, nbMsgs)
                    break
                if choice[0] == '24':
                    GmailActions.randomActions(driver, nbMsgs)
                    break
            if choice[0] == '25':
                GmailActions.checkAccount(IspUser, driver, True, True)
                break
            if choice[0] == '26':
                GmailActions.checkAccount(IspUser, driver, True, True, True)
                break
            if choice[0] == '0':
                break
        pass
    except:
        semaphore.release()
    finally:  # inserted
        try:
            driver.quit()

def HotmailChoices(IspUser, choice):
    try:
        semaphore.acquire()
        while True:  # inserted
            dontCheck = ['1', '2', '3', '16', 0]
            if choice[0]!= 0:
                driver = CreateDriver(IspUser)
            if choice[0] not in dontCheck:
                HotmailActions.checkAccount(IspUser, driver)
            if choice[0] == '1':
                HotmailActions.checkAccount(IspUser, driver, True)
                break
            if choice[0] == '2':
                HotmailActions.checkAccount(IspUser, driver, True)
                break
            if choice[0] == '3':
                HotmailActions.loginWait(IspUser, driver)
                break
            if choice[0] == '4':
                HotmailActions.reportNotJunk(driver)
                break
            if choice[0] == '5':
                HotmailActions.reportToInbox(driver)
                break
            if choice[0] == '6':
                HotmailActions.selectPage_notJunk(driver)
                break
            if choice[0] == '7':
                HotmailActions.inbox_openClick(driver, nbMsgs)
                break
            if choice[0] == '8':
                HotmailActions.inbox_openCategorize(driver, nbMsgs)
                break
            if choice[0] == '9':
                HotmailActions.inbox_openFlag(driver, nbMsgs)
                break
            if choice[0] == '10':
                HotmailActions.inbox_openArchive(driver, nbMsgs)
                break
            if choice[0] == '11':
                HotmailActions.inbox_openReply(driver, nbMsgs)
                break
            if choice[0] == '12':
                HotmailActions.inbox_openClickCategorize(driver, nbMsgs)
                break
            if choice[0] == '13':
                HotmailActions.inbox_openClickCategorizeFlag(driver, nbMsgs)
                break
            if choice[0] == '14':
                HotmailActions.inbox_openClickCategorizeArchive(driver, nbMsgs)
                break
            if choice[0] == '15':
                HotmailActions.inbox_openClickCategorizeReply(driver, nbMsgs)
                break
            if choice[0] == '16':
                HotmailActions.inbox_openClickReplyArchive(driver, nbMsgs)
                break
            if choice[0] == '17':
                HotmailActions.inbox_openClickReplyFlag(driver, nbMsgs)
                break
            if choice[0] == '18':
                HotmailActions.archive_openFlag(driver, nbMsgs)
                break
            if choice[0] == '19':
                HotmailActions.importContact(IspUser, driver)
                break
            if choice[0] == '20':
                HotmailActions.changePassword(IspUser, driver)
                break
            if choice[0] == '21':
                HotmailActions.cleanAll(driver)
                break
            if choice[0] == '22':
                HotmailActions.actionByChoice(IspUser, driver, nbMsgs)
                break
            if choice[0] == '23':
                HotmailActions.randomActions(driver, nbMsgs)
                break
            if choice[0] == '24':
                HotmailActions.removePin(driver)
                break
            if choice[0] == '0':
                break
    except:
        pass
    finally:  # inserted
        semaphore.release()
        driver.quit()

def YahooChoices(IspUser, choice):
    try:
        semaphore.acquire()
        while True:  # inserted
            dontCheck = ['1', '2', '22', 0]
            if choice[0]!= 0:
                driver = CreateDriver(IspUser, True)
            if choice[0] not in dontCheck:
                YahooActions.checkAccount(IspUser, driver)
            if choice[0] == '1':
                YahooActions.checkAccount(IspUser, driver, True)
                break
            if choice[0] == '2':
                YahooActions.checkAccount(IspUser, driver, True)
                break
            if choice[0] == '3':
                YahooActions.loginWait(driver)
                break
            if choice[0] == '4':
                YahooActions.selectPage_notSpam(driver)
                break
            if choice[0] == '5':
                YahooActions.reportNotSpam(driver)
                break
            if choice[0] == '6':
                YahooActions.inbox_openClick(driver)
                break
            if choice[0] == '7':
                YahooActions.inbox_openReply(driver, nbMsgs)
                break
            if choice[0] == '8':
                YahooActions.inbox_openStar(driver, nbMsgs)
                break
            if choice[0] == '9':
                YahooActions.inbox_openArchive(driver, nbMsgs)
                break
            if choice[0] == '10':
                YahooActions.inbox_openClickStar(driver, nbMsgs)
                break
            if choice[0] == '11':
                YahooActions.inbox_openClickReply(driver, nbMsgs)
                break
            if choice[0] == '12':
                YahooActions.inbox_openClickArchive(driver, nbMsgs)
                break
            if choice[0] == '13':
                YahooActions.inbox_openClickReplyArchive(driver, nbMsgs)
                break
            if choice[0] == '14':
                YahooActions.inbox_openClickStarReply(driver, nbMsgs)
                break
            if choice[0] == '15':
                YahooActions.inbox_openClickStarArchive(driver, nbMsgs)
                break
            if choice[0] == '16':
                YahooActions.inbox_openClickStarReplyArchive(driver, nbMsgs)
                break
            if choice[0] == '17':
                YahooActions.inbox_openStarReplyArchive(driver, nbMsgs)
                break
            if choice[0] == '18':
                YahooActions.inbox_openReplyArchive(driver, nbMsgs)
                break
            if choice[0] == '19':
                YahooActions.inbox_openStarArchive(driver, nbMsgs)
                break
            if choice[0] == '20':
                YahooActions.inbox_allArchive(driver, nbMsgs)
                break
            if choice[0] == '21':
                YahooActions.importContact(IspUser, driver)
                break
            if choice[0] == '22':
                YahooActions.changePassword(IspUser, driver)
                break
            if choice[0] == '23':
                YahooActions.cleanAll(driver)
                break
            if choice[0] == '24':
                YahooActions.actionByChoice(IspUser, driver, nbMsgs)
                break
            if choice[0] == '25':
                YahooActions.randomActions(driver, nbMsgs)
                break
            if choice[0] == '0':
                break
    except:
        pass
    finally:  # inserted
        semaphore.release()
        driver.quit()