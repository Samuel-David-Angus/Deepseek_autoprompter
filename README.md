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

### 2. Find the Path to the Chrome Executable
The project requires the path to your Chrome browser executable. The chrome_runner.py script has a variable at the top of the file named chrome_path and automatically tried to find the path but it is still best to try knowing the path yourself in case the script cannot find it. Here’s how to find it:
- **On macOS**:
  - The default path is usually:
    ```
    /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
    ```
- **On Windows**:
  - The default path is usually:
    ```
    C:\Program Files\Google\Chrome\Application\chrome.exe
    ```
- **On Linux**:
  - The default path is usually:
    ```
    /usr/bin/google-chrome
    ```

If Chrome is installed in a custom location, locate the `chrome` or `chrome.exe` file and note its full path.
If the program fails to run since it cannot find the chrome path then you can input the path manually in chrome_runner.py in the chrome_path at the top of the file.

### 3. Install Python Dependencies
1. Navigate to the project root folder in your terminal.
2. Install the required Python packages using `pip`:
   ```bash
   pip install -r requirements.txt