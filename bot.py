def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today."
    elif "what is your name" in user_input:
        return "I'm a simple chatbot created by you."
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm doing great! How about you?"
    elif "im fine" in user_input:
        return "I'm glad to hear that..."
    elif "can you help me" in user_input:
        return "Sure, I'm here to help. What do you need assistance with?"
    elif "maybe later" in user_input:
        return "Okay Thank You!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Test the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)



