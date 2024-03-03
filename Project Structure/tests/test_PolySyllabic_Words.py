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


###################################
import unittest
from modules.PolySyllabic import polysyllabic_words
from modules.metadata import metadata

class TestPolySyllabic(unittest.TestCase):
    def test_polysyllabic_words(self):
        input_data = {
            "metadata": {"text": "This is a test document."},
            "tokens": ["this", "is", "a", "test", "document"],
            "numsyllables": 2
        }
        result = polysyllabic_words(input_data)
        expected_result = {
            "metadata": {"text": "This is a test document."},
            "tokens": ["this", "is", "a", "test", "document"],
            "polysyllabic_list": [("document", 3), ("test", 1)]
        }
        self.assertEqual(result, expected_result)

    def test_polysyllabic_words_null_input(self):
        input_data = {
            "metadata": {"text": None},
            "tokens": None,
            "numsyllables": 2
        }
        result = polysyllabic_words(input_data)
        expected_result = {"metadata": {"text": None}, "tokens": None, "polysyllabic_list": []}
        self.assertEqual(result, expected_result)

    def test_polysyllabic_words_empty_tokens(self):
        input_data = {
            "metadata": {"text": "This is a test document."},
            "tokens": [],
            "numsyllables": 2
        }
        result = polysyllabic_words(input_data)
        expected_result = {"metadata": {"text": "This is a test document."}, "tokens": [], "polysyllabic_list": []}
        self.assertEqual(result, expected_result)

    def test_polysyllabic_words_complex_text(self):
        input_data = {
            "metadata": {"text": "This is a more complex document with polysyllabic words."},
            "tokens": ["this", "is", "a", "more", "complex", "document", "with", "polysyllabic", "words"],
            "numsyllables": 2
        }
        result = polysyllabic_words(input_data)
        expected_result = {
            "metadata": {"text": "This is a more complex document with polysyllabic words."},
            "tokens": ["this", "is", "a", "more", "complex", "document", "with", "polysyllabic", "words"],
            "polysyllabic_list": [("document", 3), ("polysyllabic", 5), ("complex", 2), ("more", 1)]
        }
        self.assertEqual(result, expected_result)

    def test_polysyllabic_words_high_num_syllables(self):
        input_data = {
            "metadata": {"text": "This is a test document."},
            "tokens": ["this", "is", "a", "test", "document"],
            "numsyllables": 5
        }
        result = polysyllabic_words(input_data)
        expected_result = {
            "metadata": {"text": "This is a test document."},
            "tokens": ["this", "is", "a", "test", "document"],
            "polysyllabic_list": []
        }
        self.assertEqual(result, expected_result)

    def test_polysyllabic_words_with_duplicates(self):
        input_data = {
            "metadata": {"text": "This is a test document. Document test."},
            "tokens": ["this", "is", "a", "test", "document", "document", "test"],
            "numsyllables": 2
        }
        result = polysyllabic_words(input_data)
        expected_result = {
            "metadata": {"text": "This is a test document. Document test."},
            "tokens": ["this", "is", "a", "test", "document", "document", "test"],
            "polysyllabic_list": [("document", 3), ("test", 1)]
        }
        self.assertEqual(result, expected_result)

    def test_polysyllabic_words_negative_num_syllables(self):
        input_data = {
            "metadata": {"text": "This is a test document."},
            "tokens": ["this", "is", "a", "test", "document"],
            "numsyllables": -2
        }
        with self.assertRaises(ValueError):
            polysyllabic_words(input_data)

if __name__ == "__main__":
    unittest.main()
