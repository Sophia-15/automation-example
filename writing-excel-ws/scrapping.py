from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep

prices = []
names = []

driver = webdriver.Chrome()
driver.get('https://www.coingecko.com/')
sleep(15)

raw_html = driver.page_source

parsed_html = bs(raw_html, "html.parser")

coins = parsed_html.find_all("tr", class_="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm")

for coin in coins[:10]:
  name = coin.find("div", class_="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5")
  price = coin.find("td", class_="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50")
  
  names.append(name.contents[0].strip())
  prices.append(price.span.text)

driver.quit()

