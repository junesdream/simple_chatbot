import unittest
from main import generate_faq_response


class TestChatbot(unittest.TestCase):

    def test_hello_response(self):
        # Tests whether “hello” returns one of the greeting responses
        response = generate_faq_response("hello")
        self.assertIn(response, ["Hello!", "Hi there!", "Greetings!", "Hi!"])

    def test_bye_response(self):
        # Tests whether “bye” returns one of the farewell responses
        response = generate_faq_response("bye")
        self.assertIn(response, ["Goodbye!", "See you later!", "Have a nice day!"])

    def test_unknown_response(self):
        # Tests whether an unknown input returns an appropriate response
        response = generate_faq_response("unknown")
        self.assertEqual(response, "I don't understand that. Can you put it another way?")

    def test_weather_response(self):
        # Tests whether an unknown input returns an appropriate response
        response = generate_faq_response("weather")
        self.assertIn(response,
                      ["Sorry, I don't have access to weather data.", "The weather is always an interesting topic!"])


if __name__ == '__main__':
    unittest.main()
