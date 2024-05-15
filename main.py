from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
from selenium.webdriver.common.keys import Keys
import openpyxl


my_dict = {'url': [], 'name': [], 'image_url': [], 'base_url': [], 'top_or_platinum': []}

url_list = ['https://www.hotsale.com.ar/electrodomesticos',
            'https://www.hotsale.com.ar/viajes',
            'https://www.hotsale.com.ar/muebles',
            'https://www.hotsale.com.ar/ropa',
            'https://www.hotsale.com.ar/deportes',
            'https://www.hotsale.com.ar/alimentos-y-bebidas',
            'https://www.hotsale.com.ar/maquillaje',
            'https://www.hotsale.com.ar/ninos',
            'https://www.hotsale.com.ar/autos'
]

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

for website_url in url_list:
    driver.get(website_url)

    sleep(4)

    driver.execute_script('document.body.style.zoom = 0.25;')
    driver.execute_script("window.scrollTo(0, (document.body.scrollHeight));")

    sleep(4)

    top_list = driver.find_element(By.CLASS_NAME, 'brand_list_wrapper')
    top_list_items = top_list.find_elements(By.CLASS_NAME, 'brand_item')
    for item in top_list_items:
        url = item.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        my_dict['url'].append(url)
        name = item.find_element(By.CSS_SELECTOR, 'a').get_attribute('data-name')
        my_dict['name'].append(name)
        image_url = item.find_element(By.CSS_SELECTOR, 'source').get_attribute('srcset')
        my_dict['image_url'].append(image_url)
        base_url = website_url
        my_dict['base_url'].append(base_url)
        top_or_platinum = 'top'
        my_dict['top_or_platinum'].append(top_or_platinum)

    platinum_list = driver.find_element(By.CLASS_NAME, 'platinum')
    platinum_list_items = platinum_list.find_elements(By.CLASS_NAME, 'brand_item')
    for item in platinum_list_items:
        url = item.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        my_dict['url'].append(url)
        name = item.find_element(By.CSS_SELECTOR, 'a').get_attribute('data-name')
        my_dict['name'].append(name)
        image_url = item.find_element(By.CSS_SELECTOR, 'source').get_attribute('srcset')
        my_dict['image_url'].append(image_url)
        base_url = website_url
        my_dict['base_url'].append(base_url)
        top_or_platinum = 'platinum'
        my_dict['top_or_platinum'].append(top_or_platinum)


df = pd.DataFrame(my_dict)
df.to_excel('results_final.xlsx')
df.to_csv('results_final.csv')






