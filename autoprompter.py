from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

prompts = ["what is a circle", "what is a square", "what is a rectangle"]

def start_auto_prompter():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.debugger_address = "127.0.0.1:9222"

    service = Service(executable_path="./chromedriver")

    driver = webdriver.Chrome(service=service, options=chrome_options)

    time.sleep(5)

    try:
        answerCount = 0;
        answerDivs = []
        qna = {}
        for index, question in enumerate(prompts, start = 1):
            textarea = driver.find_element(By.TAG_NAME, "textarea")  # Locate input field
            textarea.send_keys(question)
            textarea.send_keys(Keys.RETURN)
            answerDivs = driver.find_elements("css selector", "div.ds-markdown.ds-markdown--block")
            while (answerCount == len(answerDivs)):
                time.sleep(5)
                answerDivs = driver.find_elements("css selector", "div.ds-markdown.ds-markdown--block")
            answerCount += 1            
            while (driver.execute_script( "return arguments[0].parentNode.children.length;", answerDivs[-1]) != 3):
                time.sleep(5)
                
        for index, answer in enumerate(answerDivs, start = 0):
            qna[prompts[index]] = answer.text

        return qna


    except Exception as e:
        print("Error:", e)