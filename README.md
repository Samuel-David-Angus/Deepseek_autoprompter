# Project Setup Guide

This guide will walk you through the steps to set up and run the project on your local machine.

---

## Prerequisites

Before you begin, ensure you have the following installed:
- **Google Chrome**: The project requires Google Chrome to run.
- **Python**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

---

## Setup Instructions

### 1. Download ChromeDriver
If you don’t already have ChromeDriver installed, follow these steps:
1. **Download ChromeDriver**:
   - Visit the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/) and download the version that matches your installed version of Google Chrome.
2. **Place ChromeDriver in the Project Root**:
   - After downloading, place the `chromedriver` executable file in the **root folder** of this project.

---

### (Optional) Create a venv

Before running the project, create a virtual environment to manage dependencies.

### **Step 1: Navigate to the Project Directory**
Open a terminal and move into the project folder:

```sh
cd /path/to/your/project
```

### **Step 2: Create the Virtual Environment**
Run the following command based on your OS:

- **Windows (Command Prompt or PowerShell):**
  ```sh
  python -m venv venv
  ```
- **macOS/Linux:**
  ```sh
  python3 -m venv venv
  ```

This creates a `venv` folder in the project directory.

### **Step 3: Activate the Virtual Environment**
Activate the virtual environment using the appropriate command:

- **Windows (Command Prompt or PowerShell):**
  ```sh
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```sh
  source venv/bin/activate
  ```

Once activated, you should see `(venv)` in your terminal prompt.
When you're done, deactivate the virtual environment with:

```sh
deactivate
```
### 2. Install Python Dependencies
1. Navigate to the project root folder in your terminal.
2. Install the required Python packages using `pip`:
   ```bash
   pip install -r requirements.txt

### 3. Minor setup
There is a JSON file called questions_partial.json. Add all the questions there as it will be the one the program reads. You will need to modify this file between stops caused by human intervention or errors by manually removing the questions that have already been answered when continuing the prompting process.

### 4. Run the project
1. Type python main.py in the terminal or python3 main.py in mac and linux. If all goes well this will open a new browser window. DO NOT open your own browser window.
2. After a new browser window opens, you will see a message to navigate to deepseek and manually log in and start a blank new chat. Do that and type in "y" in the terminal after you have done so to initiate the auto prompting.
3. Wait for the program to end
4. Run finalizer.py to get the final result in processed.json

### In case the prgram cannot find the browser
If the program cannot find the path to the browser executable it won't be able to run. If this happens, you can manually add the path into the chrome_path variable in chrome_runner.py

### In case program cannot finish all the prompts in the JSON
If the program cannot finidh all the questions either due to chat limit exceeded or some error on deepseek's side then run extractor.py on the interrupted chat. This will dump all the answers inside the raw_partial.json file. Copy the values in the raw_partial and append to the raw.json then remove the questions that have already been answered in question_partial.json before restarting main.py