from chrome_runner import run_chrome
from autoprompter import start_auto_prompter
import json

def add_questions_to_context_prompt(questions):
    enumerated_questions = ""
    for i, question in enumerate(questions, start=1):
        enumerated_questions += f"Question {i}: {question}\n"

    context_prompt = f"""
    Your goal is to author the learning outcomes or knowledge components on discrete math questions that is needed to answer them.
A well-constructed learning objective/outcome contains three parts:
1. BEHAVIOR
The behavior is the real work to be accomplished by the student specified by an
action verb that connotes observable and measurable behaviors.
2. CONDITIONS
This is a statement that describes the exact conditions under which the defined
behavior is to be performed.
3. DEGREE
This is a statement that specifies how well the student must perform the behavior.

Here is the discrete math question/s (each question is denoted as Question: question number. DO NOT split enumerated subquestions within a question):

{enumerated_questions}

If the question/s was presented in a textbook for a discrete mathematics course, what domain-specific low-level detailed topics would the page cover? Note that the question is for a college audience with existing prior knowledge in discrete mathematics.
Based on these topics, reword them to begin with action words from Bloom’s Revised Taxonomy, while keeping them domain-specific, low-level, and detailed as well as containing the 3 parts explained above. Make sure the learning outcome contains only natural language and no math symbols, expressions, equations etc.
Take the initial learning outcomes and check if it can be generalized to other contexts outside of this question. If it can be generalized then do so. If it is already generalized then leave it alone and just copy as is.
Answer in json where the question number itself is the key and as a value, an object with the topics as key containing a string array of the textbook topics the question will be associated with and another key called initialLO for the initial learning outcomes and finalLO which contains the generalized question, all of these are string arrays. Don't put any explanation afterwards.
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

        category_and_answers = {}
        start_auto_prompter(category_and_prompts=category_and_prompts.items(), result=category_and_answers)

        print("Finished. pls append the results in raw_partial.json to raw.json then run finalizer.py to see the final output in processed.json")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("\nAborting")
        with open("raw_partial.json", "w") as file:
            json.dump(category_and_answers, file, indent=4)
        print("partial results dumped in raw_partial. pls review and append to raw.json and remove the answered questions in questions_partial.json before rerunning the program to continue.")