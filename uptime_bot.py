# building an Uptime bot.
# uptime_bot.py
# Checks website periodically and sends notifications and alerts if website is down.
import time
import urllib.request

# Three tasks that I want the bot to accomplish:
# Have a loop that queries a URL

# Catch an Exception
# Have a loop that queries a URL
# know if there is an exception and catch it using a Try:Except block.
def uptime_bot(url, retries = 3): # function
    fails = 0
    while fails < retries: # while loop will execute until your code runs into three exceptions 
        try:
            urllib.request.urlopen(url)
        except Exception as e: 
            fails += 1 # increment fails inside except block. Makes sure the code checks it only a couple of times.
            # If it is not fine, this prints out error.
            print(f"{e}: for {url}")
        else:
            print(f"{url } is up")
        time.sleep(3) # Sleep in between calls
        
        # Send an email notification. Add benefits to it.
        
if __name__ == "__main__":
    # variable url defined here
    url = "https://docs.python.org/3/" # url that you want to query.
    # run uptime bot with url
    uptime_bot(url)