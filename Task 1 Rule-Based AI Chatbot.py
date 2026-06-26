import datetime

def enhanced_chatbot():
    print("Chatbot: Hello! I am an enhanced rule-based bot. (Type 'bye' or 'exit' to quit)")

    # Run in a continuous loop
    while True:
        user_input = input("You: ").strip().lower()

        # Handle exit commands
        if user_input in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Flexible Greeting Match: Checks if ANY greeting word is in the input
        elif any(greeting in user_input for greeting in ['hello', 'hi', 'hey']):
            print("Chatbot: Hello there! What's on your mind?")

        # Dynamic Response: Time
        elif 'time' in user_input:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Chatbot: The current time is {current_time}.")

        # Dynamic Response: Date
        elif 'date' in user_input:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            print(f"Chatbot: Today is {current_date}.")

        # State/Mood Check
        elif 'how are you' in user_input or 'how do you do' in user_input:
            print("Chatbot: I'm operating flawlessly! Thanks for asking.")

        # Capability Rule
        elif 'weather' in user_input:
            print("Chatbot: I don't have internet access to check the weather, but I hope it's clear skies!")

        # Identity Rule
        elif 'who are you' in user_input or 'name' in user_input:
            print("Chatbot: I am RuleBot 2.0, a simple Python assistant.")

        # Fallback for unknown inputs
        else:
            print("Chatbot: I don't quite understand that. Try asking me for the time, the date, or saying hi!")

if __name__ == "__main__":
    enhanced_chatbot()