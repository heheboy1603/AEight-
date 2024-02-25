import datetime
import webbrowser as wb
import os

while True:
    user_name = input("Hi, what's your name? \n")
    user_query = input(f"Hi {user_name}, what can I help you? \n")

    if user_name in locals():
    	continue

    def get_time():
    """
     Gets the time.
 
     :returns:   The time.
     :rtype:     { return_type_description }
     """ #Time reply function
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return f"The current time is {current_time}."

    if "time" in user_query.lower():
        print(get_time())

    elif "search" in user_query.lower():
        search_query = input("What do you want to search for? ")
        wb.open(f"https://www.google.com/search?q={search_query}")

    elif "open app" in user_query.lower():
        app_name = input("Which app do you want to open? ")
        try:
            os.startfile(app_name)
        except FileNotFoundError:
            print(f"App '{app_name}' not found.")

    else:
        print("I'm not sure what you mean. Can you please repeat your request?")
