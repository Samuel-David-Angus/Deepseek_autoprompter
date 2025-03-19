import os
import platform
import subprocess
import shutil

chrome_path = None

def find_chrome():
    """Finds the path of Chrome executable based on the OS."""
    system = platform.system()

    if system == "Windows":
        paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        ]
        for path in paths:
            if os.path.exists(path):
                return path
    elif system == "Darwin":  # macOS
        return "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    elif system == "Linux":
        return shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("google-chrome-stable")

    return None

def get_user_data_dir():
    """Gets the appropriate user data directory based on OS."""
    system = platform.system()

    if system == "Windows":
        return "C:\\chrome-profile"
    elif system == "Darwin":  # macOS
        return os.path.expanduser("~/Library/Application Support/Google/Chrome/Profile")
    elif system == "Linux":
        return os.path.expanduser("~/.config/google-chrome-profile")

    return None

def run_chrome():
    """If no chrome path provided then try to find it"""
    if not chrome_path:
        chrome_path = find_chrome()
    if not chrome_path:
        print("Chrome not found!")
        return

    user_data_dir = get_user_data_dir()
    if not user_data_dir:
        print("Cannot find user data")
        return

    command = [chrome_path, "--remote-debugging-port=9222", f"--user-data-dir={user_data_dir}"]
    subprocess.run(command)

