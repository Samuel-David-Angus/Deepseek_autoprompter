from chrome_runner import run_chrome
from autoprompter import start_auto_prompter

if __name__ == "__main__":

    prompts = ["list 5 fruits that end in um", " in less than 10 words describe a cocunut", "list 3 fruits rich in vitamin c"]

    run_chrome()
    print("Please navigate to deepseek and login manually and open a blank new chat in the browser window that was just opened. Do NOT open your own browser window or this wont work.")
    
    response = ""
    while (response != "y"):
        print("Finished with logging in to deepseek and opening a blank new chat? (y/n)")
        response = input().lower()

    print("Starting auto prompting")
    question_and_answers = start_auto_prompter(prompts=prompts)
    print("Finished")