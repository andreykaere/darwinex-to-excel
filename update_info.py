#!/usr/bin/python3.5


from bs4 import BeautifulSoup as bs

import datetime
from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()


INFO = dict()

def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)

set_viewport_size(driver, 800, 600)


url = 'https://www.darwinex.com/login'
driver.get(url)


USERNAME = ""
PASSWORD = ""

username = driver.find_element_by_name('username')
username.send_keys(f"{USERNAME}")

password = driver.find_element_by_name('password')
password.send_keys(f"{PASSWORD}")

log_in_button = driver.find_element_by_id('submit-btn')
log_in_button.click()

# Wait for starting page to load
sleep(15)


def get_d_score(soup):
    return float(soup.select(".strategy-info-module.user-score > .score")[0].text)

def get_divergencia(soup):
    try:
        return float(soup.select(".strategy-info-module.user-data .font-size-xl > span")[-1].text.replace(' ', '').replace('%', ''))
    except:
        return 0

def get_ex(soup):
    return float(soup.select(".dropdown-menu.dropdown-menu-right progress")[0]['value'])

def get_la(soup):
    return float(soup.select(".dropdown-menu.dropdown-menu-right progress")[9]['value'])

def get_anos(soup):
    return datetime.datetime.now().year - int(soup.select(".table.table-return .text-right .text-left")[0].text) + 1

def get_equity(soup):
    return float(soup.select(".strategy-info-module.user-data .amount .font-size-xl > span > span")[0].text.replace(' ', '').replace('$', '').replace(',', '').replace('€', '').replace('£', ''))


def get_rentabilidad(soup):
    return float(soup.select(".text-sm-right .text-success.font-weight-bold")[0].text.replace(' ', '').replace('%', ''))


def get_data(name):
    url ='https://www.darwinex.com/darwin/' + name 
    driver.get(url)
    sleep(10) #5
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")


    soup = bs(html, 'html5lib')

    INFO[name] = {
        'd_score': get_d_score(soup),
        'divergencia': get_divergencia(soup),
        'ex': get_ex(soup),
        'la': get_la(soup),
        'anos': get_anos(soup),
        'equity': get_equity(soup),
        'rentabilidad': get_rentabilidad(soup),
    }

