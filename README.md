# Building an Uptime Bot

## Project Description
This project involves building an uptime bot, a script named `uptime_bot.py`, which periodically checks a website and sends notifications and alerts if the website is down. The bot continuously queries a specified URL and detects if there are any exceptions indicating that the website is not accessible. In such cases, it logs the error and retries a specified number of times before giving up. Additionally, the bot can be extended to send email notifications to notify relevant stakeholders about website downtime.

## Features
- **Periodic Website Checking**: The bot has a loop that queries a specified URL at regular intervals.
- **Exception Handling**: It catches exceptions that occur during the website query process using a `try-except` block.
- **Retries**: The bot retries querying the URL a specified number of times if it encounters exceptions.
- **Logging**: It logs errors when the website is down, providing information about the error and the URL.
- **Sleep Interval**: It waits for a specified time interval between consecutive queries to prevent overwhelming the server.

## Usage
To use the uptime bot, follow these steps:
1. Ensure you have Python installed on your system.
2. Clone or download the `uptime_bot.py` script.
3. Modify the script to specify the URL you want to monitor and adjust any other parameters as needed.
4. Run the script using the command `python uptime_bot.py`.

## Script Explanation
The `uptime_bot.py` script performs the following tasks:

1. **URL Query Loop**: It has a loop that continuously queries the specified URL.
2. **Exception Handling**: It catches exceptions that occur during the URL query process using a `try-except` block.
3. **Retry Mechanism**: If an exception occurs, the script retries querying the URL a specified number of times (default: 3 times).
4. **Error Logging**: It logs errors when the website is down, providing information about the error and the URL.
5. **Sleep Interval**: It waits for a specified time interval (default: 3 seconds) between consecutive queries to prevent overwhelming the server.
6. **Email Notification (Potential Extension)**: The script can be extended to include functionality for sending email notifications to notify relevant stakeholders about website downtime.

## Example
```python
if __name__ == "__main__":
    url = "https://example.com"  # Specify the URL to monitor
    uptime_bot(url)  # Run the uptime bot with the specified URL
