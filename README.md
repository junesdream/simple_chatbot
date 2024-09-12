# 🤖 Simple FAQ Chatbot

## Description
Welcome to **FAQ Chatbot**! This project implements a simple FAQ chatbot in Python. The chatbot can respond to specific keywords and phrases, providing predefined answers to frequently asked questions (FAQs).

## Features
- Responds to basic greetings and farewells 🖐
- Offers responses to common questions such as "How are you?" or "Who are you?" 🤔
- Keyword matching powered by **regular expressions (regex)** 📜
- Random response selection to keep things lively 🎲
- Simple and easy to extend!

## Requirements
- Python 3.x

## Installation
1. Make sure you have Python installed (version 3.6+).
2. Clone this repository
3. Navigate to the project folder:
    ```bash
    cd simple_chatbot
    ```
4. Run the chatbot:
    ```bash
    python main.py
    ```

## Usage
Once you run the script, the bot will start listening for user inputs. You can type phrases like:

- "hi", "hey", "hallo" 🖐 
- "how are you?", "you good?" 😄
- "who are you?", "what is your name?" 🧐
- "bye", "ciao" 👋
- "help", "support me" 🆘
- "weather", "how is today?" 🌤️
- "thank you", "thanks" 🙏

The bot will search for a keyword match and respond accordingly. For example:
```bash
Du: hi
Bot: Hello!
 ```
Type exit at any time to end the conversation.

🧠 How it Works

    The bot uses a dictionary of predefined keywords mapped to a list of possible responses.
    When the user inputs text, the bot scans for any keyword matches using regular expressions.
    Upon finding a match, the bot chooses a random response from the corresponding list to simulate a conversational reply.

## Example of the faq_responses dictionary:
```bash
faq_responses = {
    "hallo|hi|hey": ["Hello!", "Hi there!", "Greetings!", "Hi!"],
    "how are you?|you good?": ["I'm good, thank you!", "I'm just a chatbot, but I'm doing great!"],
    "who are you|what is your name?": ["I am a simple chatbot.", "I am your virtual assistant."],
    "bye|ciao": ["Goodbye!", "See you later!", "Have a nice day!"],
    "help|support me": ["How can I assist you?", "I'm here to help!"],
    "weather|how is today?": ["Sorry, I don't have access to weather data.", "The weather is always an interesting topic!"],
    "thank you|thanks": ["You're welcome!", "No problem!", "Happy to help!"]
}
```

YesChatREADME Generator

Here’s your README in Markdown format:

markdown

# 🤖 FAQ Chatbot

Welcome to **FAQ Chatbot**! This project is a simple Python-based chatbot that responds to predefined user inputs using regular expressions. It provides basic conversational capabilities for frequently asked questions. The bot recognizes specific keywords and phrases, and replies with random predefined responses to simulate a basic conversation. 

## 🚀 Features

- Responds to basic greetings and farewells 🖐
- Offers responses to common questions such as "How are you?" or "Who are you?" 🤔
- Keyword matching powered by **regular expressions (regex)** 📜
- Random response selection to keep things lively 🎲
- Simple and easy to extend!

## 🛠️ Installation

1. Make sure you have Python installed (version 3.6+).
2. Clone this repository:
    ```bash
    git clone https://github.com/your-username/faq-chatbot.git
    ```
3. Navigate to the project folder:
    ```bash
    cd faq-chatbot
    ```
4. Run the chatbot:
    ```bash
    python chatbot.py
    ```

## 💡 Usage

Once you run the script, the bot will start listening for user inputs. You can type phrases like:

- "hi", "hey", "hallo" 🖐 
- "how are you?", "you good?" 😄
- "who are you?", "what is your name?" 🧐
- "bye", "ciao" 👋
- "help", "support me" 🆘
- "weather", "how is today?" 🌤️
- "thank you", "thanks" 🙏

The bot will search for a keyword match and respond accordingly. For example:

```bash
Du: hi
Bot: Hello!
```
Type exit at any time to end the conversation.
🧠 How it Works

    The bot uses a dictionary of predefined keywords mapped to a list of possible responses.
    When the user inputs text, the bot scans for any keyword matches using regular expressions.
    Upon finding a match, the bot chooses a random response from the corresponding list to simulate a conversational reply.

Example of the faq_responses dictionary:
```bash
faq_responses = {
    "hallo|hi|hey": ["Hello!", "Hi there!", "Greetings!", "Hi!"],
    "how are you?|you good?": ["I'm good, thank you!", "I'm just a chatbot, but I'm doing great!"],
    "who are you|what is your name?": ["I am a simple chatbot.", "I am your virtual assistant."],
    "bye|ciao": ["Goodbye!", "See you later!", "Have a nice day!"],
    "help|support me": ["How can I assist you?", "I'm here to help!"],
    "weather|how is today?": ["Sorry, I don't have access to weather data.", "The weather is always an interesting topic!"],
    "thank you|thanks": ["You're welcome!", "No problem!", "Happy to help!"]
}
```

🔧 Customization

Want to add more questions or customize responses? You can easily modify the faq_responses dictionary in the script.

    Add new keywords or phrases as the dictionary keys.
    Provide a list of potential responses for each keyword.
    Make sure the keys are regular expression patterns for flexible matching.

Example of adding a new response:
```bash
faq_responses["good morning|morning"] = ["Good morning!", "Hope you have a great day ahead!"]
```
📋 To-Do

    Add more responses to increase variety.
    Allow for multi-turn conversations (e.g., follow-up questions).
    Integrate external APIs for more dynamic responses (e.g., weather API).

🤝 Contributing

Feel free to fork the project, submit pull requests, or open issues if you have any ideas or improvements. Contributions are always welcome! 🙌
