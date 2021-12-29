import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
import time
import urllib.request as urllib2

# 1. Pegar conteudo HTML a partir da URL
url = "https://etherscan.io/token/0xab167E816E4d76089119900e941BEfdfA37d6b32"

option = Options()
option.headless = True

n = 1
while n > 0:
    driver = 0
    element = 0
    driver = webdriver.Firefox(options=option, executable_path=r'C:/geckodriver.exe')

    driver.get(url)
    time.sleep(3)

    driver.switch_to.frame(driver.find_element_by_xpath("//div[@id='transactions']//iframe"))

    results = []
    for i in range(3):
        element = driver.find_element_by_xpath(
            "//table")
        html_content = element.get_attribute('outerHTML')

        #2. Parsear o conteudo HTML - BeaultifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find(name='table')

        # # 3. Estruturar conteudo em um Data Frame - Pandas
        df_full = pd.read_html(str(table))[0]
        df = df_full[['Method', 'From', 'To', 'Quantity']]
        df.columns = ['method', 'from', 'to', 'quantity']

        result = {}
        result["page"] = i+1
        result["results"] = df.to_dict('records')

        results.append(result)

        time.sleep(1)
        driver.find_element_by_xpath(
            "//li[@data-original-title='Go to Next']//a").click()

    driver.quit()

    js = json.dumps(results)
    fp = open('result.json', 'w')
    fp.write(js)
    fp.close()