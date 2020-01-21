from selenium import webdriver
import urllib. request
import time
import cx_Oracle as oci

options = webdriver.ChromeOptions()

options.add_argument('headless')
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

driver = webdriver.Chrome("C:\\Users\\admin\\Desktop\\kidscctv\\kidscctv\\cctv\\chromedriver.exe", chrome_options=options)

url  = "http://www.newsis.com/search/schlist/?val=%25EC%2596%25B4%25EB%25A6%25B0%25EC%259D%25B4%25EB%25B3%25B4%25ED%2598%25B8%25EA%25B5%25AC%25EC%2597%25AD&sort=acc&jo=sub&bun=all_bun&sdate=&term=allday&edate=&s_yn=Y&catg=1&t=1&page=1&"
driver.get(url)

# print("start")

# title       = list()
# link        = list()
# thumbnail   = list()
# report      = list()
# content     = list()
# pub_date    = list()

# articles = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[3]')
# article = articles.find_elements_by_class_name('bundle')

# for tmp in article:
#     title.append(tmp.find_element_by_class_name('title').text)
#     link.append(tmp.find_element_by_tag_name("a").get_attribute("href"))
#     # thumbnail.append(tmp.find_element_by_class_name('img'))

#     reporter_date = tmp.find_element_by_class_name('date').text
#     report.append(tmp.reporter_date.split("|")[0])
#     pub_date.append(tmp.reporter_date.split("|")[1].strip())
    
#     content.append(tmp.find_elements_by_tag_name("a")[1].text[:100] +"...")

    # title.append(tmp.find_element_by_tag_name("a").get_attribute("href").text)
    # thumbnail.append(tmp.find_element_by_class_name('img')
    # report.append(tmp.find_element_by_class_name('date').text)
    # content.append( tmp.find_element_by_tag_name("a").get_attribute("href").text[:100] )
    # print(tmp.find_elements_by_tag_name("a")[1].text[:100] +"..."   )
    # pub_date.append(tmp.find_element_by_class_name('date').text)