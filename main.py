from chrome_runner import run_chrome
from autoprompter import start_auto_prompter
import json
import re


if __name__ == "__main__":
    
    with open("questions.json", "r") as file:
        data = json.load(file)

    results = {}
    
    try:
        run_chrome()
        print("Please navigate to deepseek and login manually and open a blank new chat in the browser window that was just opened. Do NOT open your own browser window or this wont work.")
        
        response = ""
        while (response != "y"):
            print("Finished with logging in to deepseek and opening a blank new chat? (y/n)")
            response = input().lower()

        print("Starting auto prompting")

        for category in data.keys():
            prompts = [add_question_to_context_prompt(q) for q in list(data[category][:3])]

            prompt_and_answers = start_auto_prompter(prompts=prompts)

            results[category] = [extract_processed_text(t) for t in prompt_and_answers.values()]

        with open("processed.json", "w") as file:
            json.dump(results, file, indent=4)

        print("Finished")
        
    except Exception as e:
        print(f"Error: {e}")


def add_question_to_context_prompt(question):
    context_prompt = f"""You are a text processor for discrete math questions. You are doing preprocessing to homogenize the questions enough so that the mathematical parts of the question don't interfere with clustering, as they can be represented in multiple ways even if they are the same thing.

Label this part WRAPPING_STEP. Given a discrete math question, identify all mathematical equations, expressions, operations, assignments, etc., and wrap them around square brackets like [SubsetOf = {{(X, Y) : X, Y ⊆ U and X ⊆ Y}}] or [¬p ∧ (¬q ∨ r)]. Do not modify the question other than the wrapping of square brackets, and do not replace the operation/equation/expression inside. Also, do not replace or modify the variables in the question, as well as the enumerations. Write down the question.

Label this part PREPROCESSED_TEXT. Take all that you have wrapped in square brackets and replace the content inside with a descriptive natural language label that describes the mathematical operation, equation, expression, or assignment inside based on the context of the question. Keep the square brackets. Also, consider variables and labels mentioned in the modified question that are not surrounded with square brackets, for example, things like set A, relation R, proposition p, set 1, etc. You are to remove the letter or number. Also, when the question just mentions the variable without the preceding data type, replace that with just the datatype. Also, you may replace any indication of enumeration of sub-questions with (enumeration).

Here's the question/s:
{question}
"""
    return context_prompt

def extract_processed_text(text):
    match = re.search(r'(?<=PREPROCESSED_TEXT:\n)[\s\S]*', text)
    return match.group().strip()
