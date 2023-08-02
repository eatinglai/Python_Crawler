from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import schedule

login_url = 'https://store.sony.com.tw/member/login'
product_url = 'https://store.sony.com.tw/product/show/ff8080816cd70b2d016cff6726d9581b'
cart_url = 'https://store.sony.com.tw/shopping/showCart'
username = 'abc'
password = 'abc'
owner = '君の名は'
Path = '/Library/Developer/CommandLineTools/usr/bin/chromedriver'
browser = webdriver.Chrome(Path)


#登入
def login():
    browser.get(login_url)
    #into & type ID
    try:
        login = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'account')) 
        )
        login.click()
        login.send_keys(username)
    except:
        print("cant into ID")
        browser.quit()
    #into PASS
    try:
        passwd = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'password')) 
        )
        passwd.click()
        passwd.send_keys(password)
    except:
        print("cant into pass")
        browser.quit()

#購買結帳
def purchase():
    #addcart
    for x in range(1,50):
        browser.get(product_url)
        try:
            addcart = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[5]/main/section[1]/div/div/form/div[2]/nav/button')) 
            )
            addcart.click()
        except:
            continue
        else:
            print('addcart try %s' %(x) )
            break

    #confirm1
    for x in range(1,50):
        browser.get(cart_url)
        try:
            confirm1 = WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="cart-aside"]/div/div[3]/button')) 
            )
            confirm1.click()
        except:
            print("confirm1")
            continue
        else:
            print('confirm1 try %s' %(x) )
            break
    

    try:
        confirm2 = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, 'pdAlertDeferSubmit2')) 
        )
        confirm2.click()
    except:
        print("confirm2")

    browser.execute_script("window.scrollBy(0, 500);")
    time.sleep(1)
    try:
        credit = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/main/section/div/form/section/div[2]/div[2]/ul/li[3]/label')))
        credit.click()                                                                                                                                
    except:
        print("credit")
    try:
        once = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/main/section/div/form/section/div[2]/div[2]/ul/li[3]/div/div[1]/label')))
        once.click()
    except:
        print("once")
    #銀行
    try:
        bank = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/main/section/div/form/section/div[2]/div[2]/ul/li[3]/div/div[1]/label')))
        bank.click()
    except:
        print("bank")
    try:
        bank2 = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="CreditCardBank_cc_online"]/option[10]')))
        bank2.click()
    except:
        print("bank2")
    #持卡人
    try:
        man = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'CreditCardOwner')))
        man.send_keys(owner)
    except:
        print("man")
    try:
        same = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/main/section/div/form/section/div[2]/div[2]/ul/li[3]/div/div[1]/div/div[3]/div[1]/div/label')))
        same.click()
    except:
        print("same")
    browser.execute_script("window.scrollBy(0, 500);")
    time.sleep(1)
    try:
        envoice = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/main/section/div/form/section/div[3]/div[2]/ul/li[1]/label')))
        envoice.click()
    except:
        print("envoice")
    browser.execute_script("window.scrollBy(0, 500);")
    time.sleep(1)
    try:
        delivery = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/main/section/div/form/section/div[4]/div[2]/ul/li[1]/label')))
        delivery.click()
    except:
        print("delivery")
    try:
        delivery2 = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="normalAddressID"]')))
        delivery2.click()
    except:
        print("delivery2")
    try:
        delivery3 = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="normalAddressID"]/option[2]')))
        delivery3.click()
    except:
        print("delivery2")
    try:
        done = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cart-aside"]/div/div[2]/button')))
        done.click()
    except:
        print("done")
    browser.execute_script("window.scrollBy(0, 2000);")
    time.sleep(1)
    try:
        accept = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="accept"]')))
        accept.click()
    except:
        print("accept")

def checklogin():
    try:
        checklogin = WebDriverWait(browser, 18).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/main/section/div/p[1]/strong'))         )
    except:
        print("checklogin erro")
        browser.quit()


#main
login()
checklogin()
purchase()
'''
schedule.every().day.at("11:00").do(purchase)

while 1:
    schedule.run_pending()
    time.sleep(1)
'''

#//*[@id="cart-aside"]/div/div[2]/button
#/html/body/div[1]/div[6]/main/section/div/form/section/div[4]/div[2]/ul/li[1]/div/div[1]/label
#/html/body/div[1]/div[6]/main/section/div/form/section/div[4]/div[2]/ul/li[1]/label
#/html/body/div[1]/div[6]/main/section/div/form/section/div[3]/div[2]/ul/li[1]/label
#/html/body/div[1]/div[6]/main/section/div/form/section/div[2]/div[2]/ul/li[3]/div/div[1]/div/div[3]/div[1]/div/label
#https://store.sony.com.tw/shopping/choosePaymentmethod
#/html/body/div[1]/div[5]/main/section[1]/div/div/form/div[2]/nav/button
#ps5_link#https://store.sony.com.tw/product/show/ff8080817e29d7dd017e2ea5452702a9
#//*[@id="CreditCardBank_cc_online"]/option[10]