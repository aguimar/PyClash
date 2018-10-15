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
senha = 'mat9807632'

my_ip = requests.get('https://ipapi.co/ip').text

MAX_WAIT = 10

print(my_ip)

browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')

browser.get(url_clash_api)


browser.find_element_by_id('email').send_keys(login)
browser.find_element_by_id('password').send_keys(senha)
browser.find_element_by_id('password').send_keys(Keys.ENTER)




