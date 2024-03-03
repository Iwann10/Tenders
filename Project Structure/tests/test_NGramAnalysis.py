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

######################################
import unittest
from modules.NGramAnalysis import ngram_analysis
from modules.metadata import metadata

class TestNGramAnalysis(unittest.TestCase):
    def test_ngram_analysis(self):
        # Test case 1
        input_data = {
            "metadata": {"text": "This is a sample document."},
            "tokens": ["this", "is", "a", "sample", "document"]
        }
        result = ngram_analysis(input_data)
        expected_result = {
            "metadata": {"text": "This is a sample document."},
            "tokens": ["this", "is", "a", "sample", "document"],
            "top_ngrams": [(("this", "is"), 1), (("is", "a"), 1), (("a", "sample"), 1), (("sample", "document"), 1)]  # Example expected result
        }
        self.assertEqual(result, expected_result)

    def test_ngram_analysis_null_input(self):
        # Test case for null input
        input_data = {"metadata": {"text": "This is a sample document."}, "tokens": None}
        result = ngram_analysis(input_data)
        expected_result = {"metadata": {"text": "This is a sample document."}, "tokens": None, "top_ngrams": []}
        self.assertEqual(result, expected_result)

    def test_ngram_analysis_empty_tokens(self):
        # Test case for empty tokens
        input_data = {"metadata": {"text": "This is a sample document."}, "tokens": []}
        result = ngram_analysis(input_data)
        expected_result = {"metadata": {"text": "This is a sample document."}, "tokens": [], "top_ngrams": []}
        self.assertEqual(result, expected_result)

    def test_ngram_analysis_multiple_occurrences(self):
        # Test case for multiple occurrences of n-grams
        input_data = {
            "metadata": {"text": "This is a sample document with a sample content. This is a duplicate sample."},
            "tokens": ["this", "is", "a", "sample", "document", "with", "a", "sample", "content", "this", "is", "a", "duplicate", "sample"]
        }
        result = ngram_analysis(input_data)
        expected_result = {
            "metadata": {"text": "This is a sample document with a sample content. This is a duplicate sample."},
            "tokens": ["this", "is", "a", "sample", "document", "with", "a", "sample", "content", "this", "is", "a", "duplicate", "sample"],
            "top_ngrams": [(("this", "is"), 2), (("is", "a"), 2), (("a", "sample"), 2), (("sample", "document"), 1), (("document", "with"), 1)]
        }
        self.assertEqual(result, expected_result)

    def test_ngram_analysis_long_text(self):
        # Test case for long text with various n-grams
        input_data = {
            "metadata": {"text": "This is a long document with various n-grams and repeated words. This document will have a mix of unique and repeated n-grams."},
            "tokens": ["this", "is", "a", "long", "document", "with", "various", "n-grams", "and", "repeated", "words", "this", "document", "will", "have", "a", "mix", "of", "unique", "and", "repeated", "n-grams"]
        }
        result = ngram_analysis(input_data)
        # Example expected result for one of the n-grams
        expected_result = {
            "metadata": {"text": "This is a long document with various n-grams and repeated words. This document will have a mix of unique and repeated n-grams."},
            "tokens": ["this", "is", "a", "long", "document", "with", "various", "n-grams", "and", "repeated", "words", "this", "document", "will", "have", "a", "mix", "of", "unique", "and", "repeated", "n-grams"],
            "top_ngrams": [(("this", "is"), 2), (("is", "a"), 2), (("a", "long"), 1), (("long", "document"), 1), (("document", "with"), 1)]
        }
        self.assertEqual(result, expected_result)

    def test_ngram_analysis_large_n(self):
        # Test case for a large value of n
        input_data = {
            "metadata": {"text": "This is a document with a large value of n for n-gram analysis."},
            "tokens": ["this", "is", "a", "document", "with", "a", "large", "value", "of", "n", "for", "n-gram", "analysis"]
        }
        result = ngram_analysis(input_data)
        expected_result = {
            "metadata": {"text": "This is a document with a large value of n for n-gram analysis."},
            "tokens": ["this", "is", "a", "document", "with", "a", "large", "value", "of", "n", "for", "n-gram", "analysis"],
            "top_ngrams": [(("this", "is", "a"), 1), (("is", "a", "document"), 1), (("a", "document", "with"), 1), (("document", "with", "a"), 1), (("with", "a", "large"), 1)]
        }
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()