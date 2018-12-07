import requests

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

def wait(fn):
        def modified_fn(*args, **kwargs):
            start_time = time.time()
            while True:
                try:
                    return fn(*args, **kwargs)
                except (AssertionError, WebDriverException) as e:
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.5)
        return modified_fn

@wait
def wait_for(fn):
        return fn()

url_clash_api_login = 'https://developer.clashroyale.com/#/login'
url_clash_api_new_key = 'https://developer.clashroyale.com/#/new-key' 

login = 'aguimar@gmail.com'
senha = 'mat9807632' # tirar isso daqui

my_ip = requests.get('https://ipapi.co/ip').text

MAX_WAIT = 10

print(my_ip)

browser = webdriver.Chrome(executable_path = './assets/chromedriver')

browser.get(url_clash_api_new_key)
browser.find_element_by_id('email').send_keys(login)
browser.find_element_by_id('password').send_keys(senha)

browser.find_element_by_id('password').send_keys(Keys.ENTER)

time.sleep(15)

print('Current URL -->' + browser.current_url)
# TODO https://developer.clashroyale.com/#/account
# Contar quantas chaves existem 

#browser.get(url_clash_api_new_key)
browser.get('http://developer.clashroyale.com/#/new-key')

#time.sleep(60)
time.sleep(15)
print('Current URL -->' + browser.current_url)

#browser.find_element_by_class_name('btn.btn-default.dropdown-toggle').submit()
#browser.find_element_by_css_selector('button.btn btn-default dropdown-toggle').submit()
browser.find_element_by_id('name').send_keys(my_ip)
browser.find_element_by_id('description').send_keys(my_ip)
browser.find_element_by_id('range-0').send_keys(my_ip)
browser.find_element_by_id('range-0').send_keys(Keys.ENTER)

time.sleep(15)
browser.get('https://developer.clashroyale.com/#/account')
content = browser.find_elements_by_class_name('api-key')
content = browser.find_elements_by_css_selector('li.api-key')
link = browser.find_elements_by_xpath('//a[contains(@href, "key")]')
# Abrir a nova chave e copiar o

key = content[-1]
key.click()

hash = browser.find_element_by_xpath('//samp')

print(hash.text)




