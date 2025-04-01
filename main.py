from chrome_runner import run_chrome
from autoprompter import start_auto_prompter
import json

def add_questions_to_context_prompt(questions):
    enumerated_questions = ""
    for i, question in enumerate(questions, start=1):
        enumerated_questions += f"Question {i}: {question}\n"

    context_prompt = f"""You are a text processor for discrete math questions. You are doing preprocessing to homogenize the questions enough so that the mathematical parts of the question don't interfere with clustering, as they can be represented in multiple ways even if they are the same thing. Respond in json

Use WRAPPING_STEP as a key here and as a value contains an array of objects containing original_question and wrapped_question as keys with their appropriate values. Given a discrete math question, identify all mathematical equations, expressions, operations, assignments, etc., and wrap them around square brackets like [SubsetOf = {{(X, Y) : X, Y ⊆ U and X ⊆ Y}}] or [¬p ∧ (¬q ∨ r)]. Do not modify the question other than the wrapping of square brackets, and do not replace the operation/equation/expression inside. Also, do not replace or modify the variables in the question, as well as the enumerations. Write down the question.

If you have any notes or explanations regarding your steps add it under the key WRAPPING_NOTES as an object in an array with notes as key. 

Put this under the key PREPROCESSED_TEXT as an object in an array with processed as key. Take all that you have wrapped in square brackets and replace the content inside with a descriptive natural language label that describes the mathematical operation, equation, expression, or assignment inside based on the context of the question. Keep the square brackets. Also, consider variables and labels mentioned in the modified question that are not surrounded with square brackets, for example, things like set A, relation R, proposition p, set 1, etc. You are to remove the letter or number. Also, when the question just mentions the variable without the preceding data type, replace that with just the datatype. Also, you may replace any indication of enumeration of sub-questions with (enumeration).

If you have any notes or explanations regarding your steps add it under the key PROCESSING_NOTES as an object in an array with notes as key.

Here's the question/s (each question is denoted as Question: question number. DO NOT split enumerated subquestions within a question):
{enumerated_questions}
"""
    return context_prompt

if __name__ == "__main__":
    
    with open("questions_partial.json", "r") as file:
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

        category_and_prompts = {}

        for category in data.keys():
            data_slice = data[category]
            prompts = []
            for i in range(0, len(data_slice), 2):
                pair = data_slice[i:i+2]  # Get up to 2 items
                prompts.append(add_questions_to_context_prompt(pair))
            category_and_prompts[category] = prompts


        category_and_answers = start_auto_prompter(category_and_prompts=category_and_prompts.items())

        with open("raw_partial.json", "w") as file:
            json.dump(category_and_answers, file, indent=4)

        print("Finished. pls append the results in raw_partial.json to raw.json then run finalizer.py to see the final output in processed.json")
        
    except Exception as e:
        with open("raw_partial.json", "w") as file:
            json.dump(category_and_answers, file, indent=4)
        print(f"Error: {e}")
        print("dumped incomplete results into raw_partial.json pls transfer these manually into raw.json then remove the questions in questions_partial.json that have already been answered prior to the error interrupt before rerunning the program again.")