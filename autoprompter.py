from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import pyperclip
import platform


def start_auto_prompter(category_and_prompts, result):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.debugger_address = "127.0.0.1:9222"

    service = Service(executable_path="./chromedriver")

    driver = webdriver.Chrome(service=service, options=chrome_options)

    time.sleep(5)

    answerCount = 0;
    answerDivs = []

    paste_key = Keys.COMMAND if platform.system() == "Darwin" else Keys.CONTROL

    for category, prompts in category_and_prompts:
        result[category] = []
        for question in prompts:
            textarea = driver.find_element(By.TAG_NAME, "textarea")  # Locate input field
            pyperclip.copy(question)
            textarea.click()
            ActionChains(driver).key_down(paste_key).send_keys("v").key_up(paste_key).perform()
            textarea.send_keys(Keys.RETURN)
            answerDivs = driver.find_elements("css selector", "div.ds-markdown.ds-markdown--block")
            while (answerCount == len(answerDivs)):
                time.sleep(5)
                answerDivs = driver.find_elements("css selector", "div.ds-markdown.ds-markdown--block")
            answerCount += 1            
            while (driver.execute_script( "return arguments[0].parentNode.children.length;", answerDivs[-1]) != 3):
                time.sleep(5)
            json_text = answerDivs[-1].find_element(By.TAG_NAME, "pre").text
            converted_text = json.loads(json_text)
            result[category].append(converted_text)