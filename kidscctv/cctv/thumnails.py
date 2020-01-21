from selenium import webdriver
import urllib.request
import time
import os
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

driver = webdriver.Chrome("C:\\Users\\admin\\Desktop\\kidscctv\\kidscctv\\cctv\\chromedriver.exe", chrome_options=options)
driver.get('http://www.newsis.com')

driver.find_element_by_xpath('//*[@id="search_form"]/fieldset/input[1]').send_keys('어린이보호구역')
driver.find_element_by_xpath('//*[@id="search_form"]/fieldset/input[1]').send_keys(Keys.ENTER)
# driver.find_element_by_xpath('//*[@id="search_form"]/fieldset/input[2]').click()
time.sleep(2)
tmp = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[3]/ul')
tmp2 = tmp.find_elements_by_class_name('bundle')
print(tmp2)

link = []  
for i in tmp2:
    tmp3 = i.find_element_by_tag_name('a').get_attribute("href")
    link.append(tmp3)
    
print(link)

for i in range(1, 5, 1): 
    time.sleep(1)
    try:
        img = driver.find_element_by_xpath('//*[@id="imgartitable_['+ str(i) + ']/tbody/tr[1]/td/img') 
    except Exception as e:
        print(e)
        img = driver.find_element_by_xpath('//*[@id="imgartitable_['+ str(i) + ']/tbody/tr[1]/td/img')         
    link.append(img.get_attribute("src"))

for idx, tmp in enumerate(link):
    urllib.request.urlretrieve(tmp,os.path.join('C:\\Users\\admin\\Desktop\\kidscctv\\kidscctv\\cctv\\article_thumnails', "n"+ str(idx)+".jpg"))

    #img = dimg = driver.find_element_by_class_name('img') 
        # get(img)












