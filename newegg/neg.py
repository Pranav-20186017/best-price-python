from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
f = open('ne.txt','r')
data = f.readlines()
index = dict()
data = [x.strip("\n") for x in data]
xpath = open('xpath.txt','r')
xp = xpath.readlines()
xp = [x.strip("\n") for x in xp]
options = Options()
options.add_argument("user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36")
options.headless = True
driver = webdriver.Chrome()
xc = 0
for _ in data:
	driver.get(_)
	product = driver.find_element_by_id(xp[xc]).text
	price = driver.find_element_by_xpath('//*[@id="landingpage-price"]/div/div/div[2]/div[2]').text
	price = price[2:]
	price = price.replace(",","")
	price = float(price)
	index[product] = price
	print(product +"\t\t" + str(price))
	xc += 1
driver.quit()
print(sum(index.values()))

