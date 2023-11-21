from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv 

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options=chrome_options)
driver.get("https://shopping.naver.com/home")
driver.find_element(By.CSS_SELECTOR,'span._combineHeader_expansion_search_inner_1VxB3').click()
query = driver.find_element(By.CSS_SELECTOR, 'input._ac_input')

query.send_keys("아이폰")
query.send_keys(Keys.RETURN)

befor_h = driver.execute_script("return window.scrollY")

while True:

    driver.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)

    after_h = driver.execute_script("return window.scrollY")

    if befor_h == after_h:
        break
    befor_h = after_h

f = open(r"C:\Users\user\Desktop\scrapper\data.csv",'w',encoding = 'CP949', newline = '')
csvWriter = csv.writer(f)

items = driver.find_elements(By.CSS_SELECTOR,"div.product_txt_area__muU07")


for item in items:
    name = item.find_element(By.CSS_SELECTOR,"span.product_info_tit__c5_pb").text
    price = item.find_element(By.CSS_SELECTOR,"div.product_price__fi5oo").text
    print(name, price)
    csvWriter.writerow([name, price])
   
f.close