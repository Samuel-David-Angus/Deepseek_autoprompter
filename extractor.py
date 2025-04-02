from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

def extract_chat():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.debugger_address = "127.0.0.1:9222"

    service = Service(executable_path="./chromedriver")

    driver = webdriver.Chrome(service=service, options=chrome_options)

    pre_tags = driver.find_elements(By.TAG_NAME, "pre")

    extracted = {"results": []}

    for pre_tag in pre_tags:
        extracted["results"].append(json.loads(pre_tag.text))

    with open("raw_partial.json", "w") as file:
            json.dump(extracted, file, indent=4)

if __name__ == "__main__":
     extract_chat()
     print("finished extracting into raw_partial.json pls copy paste accordingly into raw.json")