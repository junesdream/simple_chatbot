import re
import random

# Predefined responses for specific keywords or phrases
faq_responses = {
    "hello|hi|hey": ["Hello!", "Hi there!", "Greetings!", "Hi!"],
    "how are you?|you good?": ["I'm good, thank you!", "I'm just a chatbot, but I'm doing great!"],
    "who are you|what is your name?": ["I am a simple chatbot.", "I am your virtual assistant."],
    "bye|ciao": ["Goodbye!", "See you later!", "Have a nice day!"],
    "help|support me": ["How can I assist you?", "I'm here to help!"],
    "weather|how is today?": ["Sorry, I don't have access to weather data.",
                              "The weather is always an interesting topic!"],
    "thank you|thanks": ["You're welcome!", "No problem!", "Happy to help!"]
}


# Function to find an answer based on keywords

def generate_faq_response(user_input):
    response = "I don't understand that. Can you put it another way?"

    # Durchsuche das Wörterbuch nach einem passenden Schlüsselwort
    for keyword, responses in faq_responses.items():
        # Entferne die Wortgrenzen und überprüfe nur, ob das Schlüsselwort im Text enthalten ist
        if re.search(keyword, user_input, re.IGNORECASE):
            response = random.choice(responses)
            break

    return response


# Main function of the chatbot
def chatbot():
    print("Welcome to the FAQ bot! Tap 'exit' to end the conversation.")

    while True:
        user_input = input("Du: ").lower()

        if user_input == 'exit':
            print("Bot: Bye bye! Glad you could make it.")
            break

        # Generate an answer based on FAQ keywords
        faq_response = generate_faq_response(user_input)
        print(f"Bot: {faq_response}")


# Start the chatbot
if __name__ == "__main__":
    chatbot()
