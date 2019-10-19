import webbrowser, sys, requests, time
from urllib.parse import urlparse
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
#options = webdriver.ChromeOptions()
#chrome_driver_path = r"D:\Users\Ryan\Documents\MADHACKS\chromedriver.exe"
#"C:\Users\Ryan\AppData\Local\Google\Chrome SxS\Application\79.0.3944.0\chrome.exe.sig"
#"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
browser = webdriver.Chrome("D:\\Users\\Ryan\\Documents\\MADHACKS\\chromedriver.exe") #chrome_driver_path, chrome_options=options)
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
#results = browser.find_elements_by_css_selector('div.g')
#link = results[0].find_element_by_tag_name("a")
time.sleep(5)
browser.quit()
print(results)
#print(urlparse.parse_qs(urlparse.urlparse(href).query)["q"])
#browser.find_element_by_link_text(<input class="gLFyf gsfi" maxlength="2048" name="q" type="text" jsaction="paste:puy29d" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" role="combobox" spellcheck="false" title="Search" value="" aria-label="Search" data-ved="0ahUKEwjL1cyMn6nlAhWUjp4KHf74Bn0Q39UDCAY">)
