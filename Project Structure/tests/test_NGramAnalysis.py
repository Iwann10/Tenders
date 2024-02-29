import unittest
from modules.ngram_analysis import NgramAnalysis, Input

class TestNgramAnalysis(unittest.TestCase):
    def setUp(self):
        self.ngram_analysis = NgramAnalysis()

    def test_valid_input(self):
        input_data = {"text": "This is a sample text for testing n-gram analysis."}
        result = self.ngram_analysis.perform_ngram_analysis(input_data)
        self.assertTrue(isinstance(result['result'], list))

    def test_null_input(self):
        with self.assertRaises(ValueError):
            self.ngram_analysis.perform_ngram_analysis(None)

    def test_empty_input(self):
        input_data = {"text": ""}
        result = self.ngram_analysis.perform_ngram_analysis(input_data)
        self.assertEqual(result['result'], [])

    def test_invalid_input_type(self):
        input_data = {"text": 123}
        with self.assertRaises(ValueError):
            self.ngram_analysis.perform_ngram_analysis(input_data)

    def test_missing_text_key(self):
        input_data = {"content": "This is a sample text for testing n-gram analysis."}
        with self.assertRaises(KeyError):
            self.ngram_analysis.perform_ngram_analysis(input_data)

    def test_single_word_input(self):
        input_data = {"text": "Test"}
        result = self.ngram_analysis.perform_ngram_analysis(input_data)
        self.assertEqual(result['result'], [])

if __name__ == "__main__":
    unittest.main()
