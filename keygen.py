import requests

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
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

url_clash_api = 'https://developer.clashroyale.com/#/login'

login = 'aguimar@gmail.com'
senha = 'mat9807632' # tirar isso daqui

my_ip = requests.get('https://ipapi.co/ip').text

MAX_WAIT = 10

print(my_ip)

browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')

browser.get(url_clash_api)


browser.find_element_by_id('email').send_keys(login)
browser.find_element_by_id('password').send_keys(senha)

browser.find_element_by_id('password').send_keys(Keys.ENTER)
browser.switch_to.active_element

# TODO https://developer.clashroyale.com/#/account
# Contar quantas chaves existem 

browser.get('https://developer.clashroyale.com/#/new-key')
#browser.find_element_by_class_name('btn.btn-default.dropdown-toggle').submit()
#browser.find_element_by_css_selector('button.btn btn-default dropdown-toggle').submit()
browser.find_element_by_id('name').send_keys(my_ip)
browser.find_element_by_id('description').send_keys(my_ip)
browser.find_element_by_id('range-0').send_keys(my_ip)
browser.find_element_by_id('range-0').send_keys(Keys.ENTER)

browser.get('https://developer.clashroyale.com/#/account')
content = browser.find_elements_by_class_name('api-key')
content = browser.find_elements_by_css_selector('li.api-key')
link = browser.find_elements_by_tag_name('a')
# Abrir a nova chave e copiar o

key = content[-1]
browser.get('https://developer.clashroyale.com/#/key/' + key)

temp = browser.find_element_by_link_text('Aguimar Neto').click()
temp = browser.find_element_by_link_text('My Account')
temp.send_keys(Keys.ENTER)
browser.find_element_by_link_text('Create New Key').click()





