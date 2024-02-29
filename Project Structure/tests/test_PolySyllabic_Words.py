import unittest
from modules.polysyllabic_words import PolysyllabicWords, Input

class TestPolysyllabicWords(unittest.TestCase):
    def setUp(self):
        self.polysyllabic_words = PolysyllabicWords()

    def test_valid_input(self):
        input_data = {"text": "This is a sample text for testing polysyllabic words analysis."}
        result = self.polysyllabic_words.extract_polysyllabic_words(input_data)
        self.assertTrue(isinstance(result['result'], list))

    def test_null_input(self):
        with self.assertRaises(ValueError):
            self.polysyllabic_words.extract_polysyllabic_words(None)

    def test_empty_input(self):
        input_data = {"text": ""}
        result = self.polysyllabic_words.extract_polysyllabic_words(input_data)
        self.assertEqual(result['result'], [])

    def test_invalid_input_type(self):
        input_data = {"text": 123}
        with self.assertRaises(ValueError):
            self.polysyllabic_words.extract_polysyllabic_words(input_data)

    def test_missing_text_key(self):
        input_data = {"content": "This is a sample text for testing polysyllabic words analysis."}
        with self.assertRaises(KeyError):
            self.polysyllabic_words.extract_polysyllabic_words(input_data)

    def test_no_polysyllabic_words(self):
        input_data = {"text": "This is a simple test sentence."}
        result = self.polysyllabic_words.extract_polysyllabic_words(input_data)
        self.assertEqual(result['result'], [])

if __name__ == "__main__":
    unittest.main()
