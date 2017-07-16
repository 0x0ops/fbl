#
#	Create by Thync
#	Contact: thync@outlook.com
#
from selenium import webdriver

# call browser
browser = webdriver.Firefox(executable_path="D:\Thync Lib\geckodriver-v0.18.0-win64\geckodriver.exe")
browser.get(r'https://facebook.com/login/')

def login(username_fb, password_fb):
    #auto fill
    user = browser.find_element_by_id('email')
    user.send_keys(username_fb)
    pwd = browser.find_element_by_id('pass')
    pwd.send_keys(password_fb)
    # click login
    sign_in = browser.find_element_by_id('loginbutton')
    sign_in.click()

def scroll():
    last = browser.execute_script("return document.body.scrollHeight")
    while True :
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        new = browser.execute_script("return document.body.scrollHeight")

        if new == last:
            break
        else:
            last = new

def action(url):
    browser.get(url)
    while True:
        try:
            button = browser.find_element_by_xpath("//*[@data-testid='fb-ufi-likelink']")
            button.click()
            scroll()
        except:
            break

if __name__ == '__main__':
    username = 'Your Account'
    password = 'Your Password'
    url = r'https://www.facebook.com/groups/1527827824105880/'
    login(username, password)
    action(url)

