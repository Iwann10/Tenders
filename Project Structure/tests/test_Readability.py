import unittest
from modules.readability import Readability, Input

class TestReadability(unittest.TestCase):
    def setUp(self):
        self.readability = Readability()

    def test_valid_input(self):
        input_data = {"text": "This is a sample text for testing readability."}
        result = self.readability.calculate_smog_index(input_data)
        self.assertTrue(isinstance(result['result'], float))

    def test_null_input(self):
        with self.assertRaises(ValueError):
            self.readability.calculate_smog_index(None)

    def test_empty_input(self):
        input_data = {"text": ""}
        result = self.readability.calculate_smog_index(input_data)
        self.assertTrue(isinstance(result['result'], float))

    def test_invalid_input_type(self):
        input_data = {"text": 123}
        with self.assertRaises(ValueError):
            self.readability.calculate_smog_index(input_data)

    def test_missing_text_key(self):
        input_data = {"content": "This is a sample text for testing readability."}
        with self.assertRaises(KeyError):
            self.readability.calculate_smog_index(input_data)

    def test_single_word_input(self):
        input_data = {"text": "Test"}
        result = self.readability.calculate_smog_index(input_data)
        self.assertTrue(isinstance(result['result'], float))

if __name__ == "__main__":
    unittest.main()