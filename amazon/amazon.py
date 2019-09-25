from selenium import webdriver
from selenium.webdriver.chrome.options import Options
f = open('links.txt','r')
data = f.readlines()
index = dict()
data = [x.strip("\n") for x in data]
options = Options()
options.headless = True
driver = webdriver.Chrome(options = options)
for _ in data:
	driver.get(_)
	product = driver.find_element_by_xpath('//*[@id="title"]').text
	price = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[5]/div[3]/div[10]/div/div/table/tbody/tr[2]/td[2]/span[1]').text
	price = price[2:]
	price = price.replace(",","")
	price = float(price)
	index[product] = price
	print(product +"\t\t" + str(price))
driver.quit()
print(sum(index.values()))
#8686677000