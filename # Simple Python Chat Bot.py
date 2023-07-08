# Simple Python Chat Bot

def get_bot_response(user_input):
    # Define bot responses based on user input
    if user_input.lower() == "hello":
        return "Hi there!"
    elif user_input.lower() == "how are you?":
        return "I'm good, thank you!"
    elif user_input.lower() == "what's your name?":
        return "I'm a chat bot. You can call me ChatBot."
    elif user_input.lower() == "exit":
        return "Goodbye!"
    else:
        return "I'm sorry, I didn't understand that."

# Main program loop
while True:
    # Get user input
    user_input = input("User: ")

    # Check for exit command
    if user_input.lower() == "exit":
        print("ChatBot: Goodbye!")
        break

    # Get bot response and display it
    bot_response = get_bot_response(user_input)
    print("ChatBot:", bot_response)