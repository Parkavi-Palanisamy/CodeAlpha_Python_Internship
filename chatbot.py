def get_response(user_input):
    message = user_input.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"

    elif message in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How are you?"

    elif message in ["good", "fine", "great"]:
        return "That's nice to hear!"

    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand. Can you try another message?"


print("===== Simple Chatbot =====")
print("Type 'bye' to end the conversation.")

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Bot:", response)

    if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
        break