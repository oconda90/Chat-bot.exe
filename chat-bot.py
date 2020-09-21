#we will now make a function called get_bot_response
#with this bot we'll talk about gaming mouse prefrence 
from random import choice

def get_bot_response(user_response):

    bot_response_logitech = ["They surely do make amazing mice!", "My All time favortie was the G pro wireless", "Nice! have you looked into their lightspeed tech?"]
    bot_response_razer = ["Their Viper ultimte is top of the line! highly recommended", "The Sure do have amazing peripherals", "The Optical switches are real game changers"]

    if user_response == "logitech":
        return choice(bot_response_logitech)
    elif user_response == "razer":
        return choice(bot_response_razer)
    else:
        return "certainly! That's it's a good peripheral company"


print("Hello there user, today we'll chat about gaming peripheral companies")
print("What company's product do you use the most while gaming? ")

user_response =""
while True:
    user_response = input("what company's mouse do you use? ")

    if user_response == 'done':
        break
    bot_response = get_bot_response(user_response)
    print(bot_response)