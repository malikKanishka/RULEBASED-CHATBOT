import pyttsx3
import random
from selenium import webdriver
import string

# Function to remove punctuation from the user input
def remove_punctuation(user_input):
    translator = str.maketrans('', '', string.punctuation)
    return user_input.translate(translator)

# Function to perform a Google search using Selenium
def Google_Search_Automation(user_input):
    keyword = user_input
    browser = webdriver.Chrome()
    browser.get('https://google.co.in/search?q=' + keyword)
    input("Press Enter to close the browser...")  # This will keep the browser open until the user presses Enter
    browser.quit()

# Function to select a random greeting response
def greetings_response():
    g_response = ["Hello!", "Hi there!", "Hey!", "Greetings!", "Salutations!", "Howdy!", "Hola!", "Bonjour!", "Ciao!", "Aloha!"]
    return random.choice(g_response)

# Function to select a random goodbye response
def goodbye_response():
    g_response = ["Goodbye!", "Bye!", "Farewell!", "Adieu!", "See you!", "Later!", "Ciao!", "Adios!", "Au revoir!", "Take care!"]
    return random.choice(g_response)

# Function to select a negative response (default for certain inputs)
def negative_response():
    g_response = ["Sorry, I'm a BOT!"]
    return random.choice(g_response)

# Function to use text-to-speech to speak the response
def speak(response_text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)  # Adjust the speed of speech
    engine.setProperty('volume', 1)  # Adjust the volume level
    engine.say(response_text)
    engine.runAndWait()

# Function to detect if the input matches a greeting pattern
def greetings_pattern(temp):
    list_greetings = ["hello", "hi", "hey", "greetings", "salutations", "howdy", "hola", "bonjour", "ciao", "aloha"]
    return sum(1 for word in temp if word in list_greetings)

# Function to detect if the input matches a goodbye pattern
def goodbye_pattern(temp):
    list_goodbye = ["goodbye", "bye", "farewell", "adieu", "seeya", "later", "ciao", "adios", "au revoir", "take care"]
    return sum(1 for word in temp if word in list_goodbye)

# Function to detect if the input matches a negative pattern
def negative_pattern(temp):
    list_negative = ["i", "love", "age", "you", "your", "name", "gender", "height", "weight", "hate", "kiss", "hug", "slap"]
    return sum(1 for word in temp if word in list_negative)

# Function to detect if the input matches a search pattern
def search_pattern(temp):
    list_question = [
        "search", "find", "look", "explore", "browse", "seek", "investigate", "query", "research", "discover", "lookup",
        "scan", "examine", "track", "identify", "uncover", "check", "survey", "probe", "assess", "what"
    ]
    return sum(1 for word in temp if word in list_question)

# Function to select the appropriate response based on the input pattern
def response_selection(temp):
    count_greetings = greetings_pattern(temp)
    count_goodbye = goodbye_pattern(temp)
    count_negative = negative_pattern(temp)
    count_search = search_pattern(temp)

    max_count = max(count_goodbye, count_greetings, count_negative, count_search)
    
    if max_count >= 1:
        if count_greetings == max_count:
            temp_ = greetings_response()
            speak(temp_)
            print("BOT: " + temp_)
        
        elif count_goodbye == max_count:
            temp_ = goodbye_response()
            speak(temp_)
            print("BOT: " + temp_)
        
        elif count_negative == max_count and count_greetings == 1:
            temp_ = negative_response()
            speak("Hi but " + temp_)
            print("BOT: HI! but " + temp_)

        elif count_negative == max_count and count_goodbye == 1:
            temp_ = negative_response()
            speak("Bye, " + temp_)
            print("BOT: Bye, " + temp_)

        elif count_negative == max_count:
            temp_ = negative_response()
            speak(temp_)
            print("BOT: " + temp_)
        
        elif count_search == max_count:
            speak("Opening your Chrome Browser!")
            Google_Search_Automation(user_input)
            print("BOT: Performed a search for '" + user_input + "'")

    else:
        speak("I don't understand!")
        print("BOT: I don't understand!")

# Function to split the user input into a list of words
def spliter(user_input):
    return user_input.lower().split()

# Main loop to continuously accept user input and generate a response
while True:
    user_input = input("YOU: ")
    if user_input == '_EXIT_':
        speak("VISIT AGAIN!")
        print("BOT: VISIT AGAIN!")
        break
    
    cleaned_text = remove_punctuation(user_input)
    temp = spliter(cleaned_text)
    response_selection(temp)
