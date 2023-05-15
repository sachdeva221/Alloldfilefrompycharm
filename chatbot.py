import random

# define a list of possible bot responses
responses = ["I'm sorry, I don't understand.", "Could you please rephrase that?", "Interesting, tell me more."]

# define a function to generate a bot response based on user input
def generate_response(user_input):
    return random.choice(responses)

# greet the user
print("Hello! I'm ChatBot. How can I help you?")

# loop to keep the conversation going until the user types "exit"
while True:
    # get user input
    user_input = input("> ")

    # check if the user wants to exit
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # generate and display bot response
    bot_response = generate_response(user_input)
    print(bot_response)

