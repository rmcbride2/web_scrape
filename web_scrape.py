import webbrowser, sys, requests, time
from urllib.parse import urlparse
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

browser = webdriver.Chrome("D:\\Users\\Ryan\\Documents\\MADHACKS\\chromedriver.exe") 
browser.get('https://google.com')
search = browser.find_element_by_name('q')
search.send_keys("Jimmy John's news")
search.send_keys(Keys.RETURN)
results = browser.find_elements_by_xpath('//a')
url = []
for urls in results:
    print (urls.get_attribute("href"))
    if urls.get_attribute("href") != None:
        url.append(urls.get_attribute("href"))

for urls in url:
    if 'google' not in urls:
        print("opening " + urls)
        browser.get(urls)
        time.sleep(5)

time.sleep(5)
browser.quit()
print(results)
