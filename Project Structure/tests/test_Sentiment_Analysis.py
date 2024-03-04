########################################################
import unittest
from modules.sentiment_analysis import sentiment_analysis
from modules.metadata import metadata

class TestSentimentAnalysis(unittest.TestCase):
    def test_sentiment_analysis_positive(self):
        input_data = metadata({"text": "This is a positive document. It contains some happy content."})
        result = sentiment_analysis(input_data)
        expected_result = {
            "metadata": {"text": "This is a positive document. It contains some happy content."},
            "sentiment_scores": {"neg": 0.0, "neu": 0.352, "pos": 0.648, "compound": 0.7964}  # Example expected result
        }
        self.assertEqual(result, expected_result)

    def test_sentiment_analysis_negative(self):
        input_data = metadata({"text": "This is a negative document. It contains some sad content."})
        result = sentiment_analysis(input_data)
        expected_result = {
            "metadata": {"text": "This is a negative document. It contains some sad content."},
            "sentiment_scores": {"neg": 0.572, "neu": 0.428, "pos": 0.0, "compound": -0.6249}  # Example expected result
        }
        self.assertEqual(result, expected_result)

    def test_sentiment_analysis_neutral(self):
        input_data = metadata({"text": "This is a neutral document. It contains factual information."})
        result = sentiment_analysis(input_data)
        expected_result = {
            "metadata": {"text": "This is a neutral document. It contains factual information."},
            "sentiment_scores": {"neg": 0.0, "neu": 1.0, "pos": 0.0, "compound": 0.0}  # Example expected result
        }
        self.assertEqual(result, expected_result)

    def test_sentiment_analysis_null_text(self):
        input_data = metadata({"text": None})
        with self.assertRaises(ValueError):
            sentiment_analysis(input_data)

    def test_sentiment_analysis_empty_text(self):
        input_data = metadata({"text": ""})
        result = sentiment_analysis(input_data)
        expected_result = {
            "metadata": {"text": ""},
            "sentiment_scores": {"neg": 0.0, "neu": 1.0, "pos": 0.0, "compound": 0.0}  # Example expected result for empty text
        }
        self.assertEqual(result, expected_result)

    def test_sentiment_analysis_invalid_input(self):
        input_data = {"invalid_key": "This is an invalid input."}
        with self.assertRaises(ValueError):
            sentiment_analysis(input_data)

if __name__ == "__main__":
    unittest.main()