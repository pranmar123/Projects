#Twitter Bot automation
#Credits to John G. Fisher for inspiring this project. 

from selenium import webdriver
from time import sleep
import os
import sys


#This snippet is needed so that when the executable is created,
#the exe can find the CHROMEDRIVER in its folders.
def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)


##ENTER YOUR USERNAME AND PASSWORD HERE
username = ''
password = ''

chromedriverpath = find_data_file("chromedriver.exe")


#url of the twitter
url = 'https://www.twitter.com/login/'

'''this is going to open up the web browser.
You can download the webdriver at:
https://chromedriver.storage.googleapis.com/index.html?path=2.38/'''

driver = webdriver.Chrome(chromedriverpath) #This should be the path of where your chromedriver exists



#tells our driver to get url and launch to the url
driver.get(url)

sleep(1) #we do this so we give the page time to load.

'''using inspect element you find the "Username" button and finding a unique id or class name
@class or @id depending on the unique name '''

#.send_keys will send text to the element that the driver finds. 
driver.find_element_by_class_name('js-username-field').send_keys(username)

sleep(1)

driver.find_element_by_class_name('js-password-field').send_keys(password)

sleep(1)

driver.find_element_by_xpath('//*[@class="submit EdgeButton EdgeButton--primary EdgeButtom--medium"]').click()

