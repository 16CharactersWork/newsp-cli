from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import re

def urlify(s):

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with +
    s = re.sub(r"\s+", '+', s)

    return s

def urlifyundo(p):

    #Returns spaces
    p = re.sub(r"[+]", ' ', p)
    
    return p


options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())

url = "https://mgreader.com/?cat=231&s="
#newspsearch = urlify(input("What newspaper are you looking for: "))
newspsearch = urlify("Financial Times") 

#Pulls website from the users input
driver.get(url + newspsearch)

#Waits webpage to load
driver.implicitly_wait(2)

#Prints recent avalable selections
newspsearch = urlifyundo(newspsearch)
fillerprint = driver.find_elements(By.CSS_SELECTOR, 'h2.entry-title')
print(fillerprint.title)

#Ask user for webpage
#dateselected =  urlify(input("Which selection would you like to make?: "))

#printnewspsearch = driver.get
driver.quit()
