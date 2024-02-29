import unittest
from modules.sentiment_analysis import SentimentAnalysis, Input

class TestSentimentAnalysis(unittest.TestCase):
    def setUp(self):
        self.sentiment_analysis = SentimentAnalysis()

    def test_valid_input(self):
        input_data = {"text": "This is a sample text for testing sentiment analysis."}
        result = self.sentiment_analysis.perform_sentiment_analysis(input_data)
        self.assertTrue(isinstance(result['result'], float))

    def test_null_input(self):
        with self.assertRaises(ValueError):
            self.sentiment_analysis.perform_sentiment_analysis(None)

    def test_empty_input(self):
        input_data = {"text": ""}
        result = self.sentiment_analysis.perform_sentiment_analysis(input_data)
        self.assertTrue(isinstance(result['result'], float))

    def test_invalid_input_type(self):
        input_data = {"text": 123}
        with self.assertRaises(ValueError):
            self.sentiment_analysis.perform_sentiment_analysis(input_data)

    def test_missing_text_key(self):
        input_data = {"content": "This is a sample text for testing sentiment analysis."}
        with self.assertRaises(KeyError):
            self.sentiment_analysis.perform_sentiment_analysis(input_data)

    def test_single_word_input(self):
        input_data = {"text": "Test"}
        result = self.sentiment_analysis.perform_sentiment_analysis(input_data)
        self.assertTrue(isinstance(result['result'], float))

if __name__ == "__main__":
    unittest.main()
