import unittest
from unittest.mock import patch
from io import StringIO
import sys
from main import chatbot


class TestChatbot(unittest.TestCase):

    @patch('builtins.input', side_effect=['hello', 'how are you', 'exit'])
    def test_chatbot(self, mock_input):
        # Intercept the output of print()
        captured_output = StringIO()
        original_stdout = sys.stdout  # Save original stdout
        sys.stdout = captured_output  # Redirect sys.stdout to StringIO

        # Run the chatbot
        chatbot()

        # Reset sys.stdout
        sys.stdout = original_stdout

        # Check the output
        output = captured_output.getvalue()

        # Check whether the expected expenses are included
        self.assertIn("Welcome to the FAQ bot!", output)
        self.assertIn("Bot:", output)  # Check if the bot responds
        self.assertIn("Bot: Bye bye! Glad you could make it.", output)

    @patch('builtins.input', side_effect=['random input', 'exit'])
    def test_chatbot_unknown_input(self, mock_input):
        # Intercept the output of print()
        captured_output = StringIO()
        original_stdout = sys.stdout  # Save original stdout
        sys.stdout = captured_output  # Redirect sys.stdout to StringIO

        # Run the chatbot
        chatbot()

        # Reset sys.stdout
        sys.stdout = original_stdout

        # Check the output
        output = captured_output.getvalue()

        # Check whether the expected expenses are included
        self.assertIn("Welcome to the FAQ bot!", output)
        self.assertIn("Bot: I don't understand that. Can you put it another way?", output)
        self.assertIn("Bot: Bye bye! Glad you could make it.", output)


if __name__ == '__main__':
    unittest.main()
