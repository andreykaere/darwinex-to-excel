#!/usr/bin/python3.5


from bs4 import BeautifulSoup as bs

import datetime
#import requests

#url = 'https://www.darwinex.com/login'

# Fill in your details here to be posted to the login form.
#login_data = {
#    'username': 'sil28',
#    'password': 'Silvia123',
#    'captchaResponse': "03AGdBq26TS_fLfjBuf-BZSTrgvjfNqeOrmq28hmrZk_Xkvuupp0t95ddB-QICfTkMebZkHdDXMTkooPPi62Y99HW6EV1GrPme3iBxLE5hAJ5oWyPqqEFMLO8iYuiIg-vIlRqdvrOu7nyxvpv5gsQWHOmzDEywH98YKezFYH6h7Bv5R_L7YIs9lf3jpkZQ7deEkfqmzYoMWzZlFrqdz4oVjAUVTBP92ZOVQQjZ867BYCifSS28w2m09x1eu4IXeEiZTyVWnN4wP5pMiFiLTd1CP-R-wMNoURLuSEfdplgLdyavsLnFvO3akI22wbbsGRQHT3ZIjU6TAVFlz8v0cy6En5Ers_gZiTfFj6K345sAe3n4icBthqylfXz9j4LMI_sSEF7qwyMtTwfUviuk9D4WL3JCZa98ZV0xtDPzJObTf431bWA-GbcvcXdklfIhIfneIjvKEAdE2Yr1"
#}


#p = requests.post(url, data=payload, verify=False)

#print(p.content)
#print(p.text)

# Use 'with' to ensure the session context is closed after use.
#with requests.Session() as s:
#    r = s.get(url)
#    soup = bs(r.content, 'html5lib')
#    login_data['_csrf'] = soup.find('input', attrs={'name': '_csrf'})['value']
#
#    print(login_data)
#    
    #login_data['captchaResponse'] = s.cookies['captchaResponse']


#    p = s.post(url, data=login_data, headers={'Referer':'https://www.darwinex.com/login'})
    #p = s.post(, data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    #print(p.text)

    # An authorised request.
#    r = s.get('https://www.darwinex.com/darwin/JHU')
#    print(r.text)
        # etc...



#soup = bs(r.text, 'html.parser')

#divs = soup.div

#mydivs = soup.find_all("div", class_="strategy-info-module")

#print(mydivs)

from time import sleep
from selenium import webdriver

#driver = webdriver.Chrome('/usr/bin/google-chrome')
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


# locate email form by_name
username = driver.find_element_by_name('username')

username.send_keys("sil28")

# locate password form by_name
password = driver.find_element_by_name('password')

#locate password form id
#password = driver.find_element_by_id("password")

#locate password form by_xpath


# send_keys() to simulate key strokes
password.send_keys("Silvia123")


log_in_button = driver.find_element_by_id('submit-btn')

# locate submit button by_xpath
#log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
log_in_button.click()

sleep(15)

#url ='https://www.darwinex.com/darwin/' + 'JHU'
#driver.get(url)
#sleep(5)
#html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")


#soup = bs(html, 'html5lib')


def get_d_score(soup):
    return float(soup.select(".strategy-info-module.user-score > .score")[0].text)
        #print(i.select('.amount'))

def get_divergencia(soup):
    try:
        return float(soup.select(".strategy-info-module.user-data .font-size-xl > span")[-1].text.replace(' ', '').replace('%', ''))
    except:
        return 0

#
#def get_divergencia(soup):
#    s = '.strategy-info-module.user-data'

#    for j in soup.select(s + ' > span'):
#        title = j.text
#        #print(title)
#        
#        if title.find("Monthly divergence & Latency") != -1:
#            break
#
#   
#    return s

    #for i in s:
    #    if s['span'] =
    #[-1].text.replace(' ', '').replace('%', ''))


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

#print(soup.select(".dropdown-menu.dropdown-menu-right progress"))


#a = get_divergence()
#b = get_D_score()
#c = get_ex()
#d = get_la()
#
#print(a)
#print(b)
#print(c)
#print(d)

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



get_data('TDD')
#get_data('JHU')
#get_data('QJU')


print(INFO)
