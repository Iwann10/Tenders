
###############
import unittest
from modules.metadata import metadata
from modules.Readability import readability

class TestReadability(unittest.TestCase):
    def test_readability(self):
        # Test case 1
        input_data = metadata({"text": "This is a simple text for testing readability."})
        result = readability(input_data)
        expected_result = {
            "metadata": {"text": "This is a simple text for testing readability."},
            "smog_index": 2.418
        }
        self.assertAlmostEqual(result["smog_index"], expected_result["smog_index"], places=3)

    def test_readability_null_input(self):
        # Test case for null input
        input_data = metadata({"text": None})
        result = readability(input_data)
        expected_result = {"metadata": {"text": None}, "smog_index": 0.0}
        self.assertEqual(result, expected_result)

    def test_readability_empty_text(self):
        # Test case for empty text
        input_data = metadata({"text": ""})
        result = readability(input_data)
        expected_result = {"metadata": {"text": ""}, "smog_index": 0.0}
        self.assertEqual(result, expected_result)

    def test_readability_complex_text(self):
        # Test case for a complex text
        input_data = metadata({"text": "This is a sophisticated document with numerous polysyllabic words to challenge readability calculations."})
        result = readability(input_data)
        expected_result = {
            "metadata": {"text": "This is a sophisticated document with numerous polysyllabic words to challenge readability calculations."},
            "smog_index": 8.062
        }
        self.assertAlmostEqual(result["smog_index"], expected_result["smog_index"], places=3)

    def test_readability_multiple_sentences(self):
        # Test case for multiple sentences
        input_data = metadata({"text": "This is sentence one. This is sentence two. This is sentence three."})
        result = readability(input_data)
        expected_result = {
            "metadata": {"text": "This is sentence one. This is sentence two. This is sentence three."},
            "smog_index": 3.162
        }
        self.assertAlmostEqual(result["smog_index"], expected_result["smog_index"], places=3)

    def test_readability_single_syllable_words(self):
        # Test case for single syllable words
        input_data = metadata({"text": "Simple words for testing."})
        result = readability(input_data)
        expected_result = {
            "metadata": {"text": "Simple words for testing."},
            "smog_index": 1.0
        }
        self.assertAlmostEqual(result["smog_index"], expected_result["smog_index"], places=3)

    def test_readability_complex_words(self):
        # Test case for complex words
        input_data = metadata({"text": "This document contains numerous complex and polysyllabic words."})
        result = readability(input_data)
        expected_result = {
            "metadata": {"text": "This document contains numerous complex and polysyllabic words."},
            "smog_index": 5.477
        }
        self.assertAlmostEqual(result["smog_index"], expected_result["smog_index"], places=3)

if __name__ == "__main__":
    unittest.main()