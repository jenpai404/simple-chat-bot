import random
import requests

# basic communication function
def basic_coms(input_coms,username):
    print(f"\nj-bot: Hello there {username}. Are you feeling good today?? (yes/no)")
    feelingInput=input("You: ")
    if feelingInput.lower()=="yes":
        print("\nj-bot: Glad to hear that. Spread the positive vibes 😉")
    elif feelingInput.lower()=="no" or feelingInput.lower()=="no how bout you":
        print("\nj-bot:  I'm so sorry to hear that. I hope you feel better soon 😇")
        quoteInput=input("\nj-bot:  Would you like quote to cheer you up?? (yes/no)\nYou:  ")
        if quoteInput.lower()=="yes" or quoteInput.lower()=="sure why not":
            print(getQuote(username))
        else:
            exit
    else:
        print("\nj-bot:  Sorry my model is not trained enough to operate on that input 😞")

# function to get weather report
def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"\nj-bot:  The weather in {city} is {weather} with a temperature of {temp}°C. 🧐"
    else:
        return f"\nj-bot:  Error: {data.get('message', 'Unable to fetch weather data')}"
    
# function to call and print weather report
def weatherReport():
    api_key = "f0469ee4bd54a230c8f73674898de16e"  # Replace this with your real API key
    city = input("\nj-bot:  Your city is?? 🤔\nYou:  ").strip()
    if city.lower() == "exit":
        print("\nj-bot:  Goodbye! Stay warm (or cool 😎)")
    else:
        print(get_weather(city, api_key))

# function to get quote
def getQuote(username):
    return f"\nj-bot:  Dear {username}, life is hard but you can be harder 😏"


username=input("\n\nPlease enter your name: ")
print(f"\nHello {username}. This is a chat-bot made using Python.\nType exit to stop the j-bot")
input_coms=input("\nPlease say hello.\nYou:  ")    
if input_coms.lower()=="exit":
    print("\nj-bot:  Thank you for using j-bot. I hope we meet again 😊")
elif input_coms.lower()=="hello":
    basic_coms(input_coms,username)
    input_coms=input("\nj-bot:  Would you like to know about the weather today?? 😁 (yes/no)\nYou:  ")
    if input_coms.lower()=="yes":
        weatherReport()
    elif input_coms.lower()=="no":
        print(f"\nj-bot:  Okhay {username}. The weather will be a mystery i guess 😏")
    else:
        print("\nj-bot:  Sorry my model is not trained enough to operate on that input 😞")


