from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
time.sleep(5)

#clicking laptop section
laptops_link = driver.find_element(By.LINK_TEXT, "Laptops")
laptops_link.click()
time.sleep(5)

laptops = driver.find_elements(By.CLASS_NAME, "card-block")
laptops_list = []
for laptop in laptops:
    name = laptop.find_element(By.CLASS_NAME, "card-title")
    price = laptop.find_element(By.XPATH, ".//h5")
    description = laptop.find_element(By.CLASS_NAME, "card-text")

    laptops_list.append({
        "name": name.text,
        "price": price.text,
        "description": description.text
    })


next_button = driver.find_element(By.ID, "next2")
next_button.click()
time.sleep(5)

more_laptops = driver.find_elements(By.CLASS_NAME,"card-block")
for laptop in more_laptops:
    name = laptop.find_element(By.CLASS_NAME, "card-title")
    price = laptop.find_element(By.XPATH, ".//h5")
    description = laptop.find_element(By.CLASS_NAME, "card-text")

    laptops_list.append({
        "name": name.text,
        "price": price.text,
        "description": description.text
    })

import json
with open("laptops.json", "w") as f:
    json.dump(laptops_list,f, indent = 2)

driver.quit()