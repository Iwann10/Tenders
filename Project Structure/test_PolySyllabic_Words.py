###################################
import unittest
from modules.polysyllabic_words import polysyllabic_words
from modules.tokenizer import tokenizer
from modules.metadata import metadata

class TestPolySyllabic(unittest.TestCase):
    def test_polysyllabic_words(self):
        #test 1
        #testing the alice_smith_cat_story
        input_data = tokenizer(metadata({"doc": "tests/Alice_Smith_Cat_Story.docx"}))
        result = polysyllabic_words(input_data)
        expected_result = {'metadata': {'author': 'Alice Smith', 'category': 'Story', 'comments': 'This is a story about a curious cat named Mittens.', 'content_status': 'Draft', 'created': '2013-12-23T23:15:00', 'identifier': '12345678-1234-1234-1234-123456789012', 'keywords': 'cat, story, adventure', 'language': 'en-US', 'last_modified_by': 'Alice Smith', 'last_printed': None, 'modified': '2013-12-23T23:15:00', 'revision': 1, 'subject': "A Cat's Adventure", 'title': 'fluttering butterfly outside the window.', 'version': '1.0', 'name': 'tests/Alice_Smith_Cat_Story.docx', 'paragraphs': ["Alice Smith's Cat", 'In a cozy little house nestled amidst the bustling city, lived a ginger cat named Mittens, the beloved companion of Alice Smith. She was known for her playful antics and insatiable curiosity. One sunny afternoon, while basking in a patch of warm sunlight, Mittens spotted a fluttering butterfly outside the window. She leaped off the window sill, tail swishing excitedly, and darted towards the fluttering wings. Mittens pounced and batted at the butterfly with her paws, but the nimble creature fluttered away, leaving her wanting more. Undeterred, Mittens continued to explore the house, searching for new adventures.'], 'text': "Alice Smith's Cat In a cozy little house nestled amidst the bustling city, lived a ginger cat named Mittens, the beloved companion of Alice Smith. She was known for her playful antics and insatiable curiosity. One sunny afternoon, while basking in a patch of warm sunlight, Mittens spotted a fluttering butterfly outside the window. She leaped off the window sill, tail swishing excitedly, and darted towards the fluttering wings. Mittens pounced and batted at the butterfly with her paws, but the nimble creature fluttered away, leaving her wanting more. Undeterred, Mittens continued to explore the house, searching for new adventures."}, 'tokens': ['alice', 'smiths', 'cat', 'in', 'a', 'cozy', 'little', 'house', 'nestled', 'amidst', 'the', 'bustling', 'city', 'lived', 'a', 'ginger', 'cat', 'named', 'mittens', 'the', 'beloved', 'companion', 'of', 'alice', 'smith', 'she', 'was', 'known', 'for', 'her', 'playful', 'antics', 'and', 'insatiable', 'curiosity', 'one', 'sunny', 'afternoon', 'while', 'basking', 'in', 'a', 'patch', 'of', 'warm', 'sunlight', 'mittens', 'spotted', 'a', 'fluttering', 'butterfly', 'outside', 'the', 'window', 'she', 'leaped', 'off', 'the', 'window', 'sill', 'tail', 'swishing', 'excitedly', 'and', 'darted', 'towards', 'the', 'fluttering', 'wings', 'mittens', 'pounced', 'and', 'batted', 'at', 'the', 'butterfly', 'with', 'her', 'paws', 'but', 'the', 'nimble', 'creature', 'fluttered', 'away', 'leaving', 'her', 'wanting', 'more', 'undeterred', 'mittens', 'continued', 'to', 'explore', 'the', 'house', 'searching', 'for', 'new', 'adventures'], 'polysyllabic_list': [('curiosity', 4), ('excitedly', 4), ('companion', 3), ('insatiable', 3), ('afternoon', 3), ('fluttering', 3), ('butterfly', 3), ('undeterred', 3), ('continued', 3), ('adventures', 3), ('alice', 2), ('little', 2), ('nestled', 2), ('ginger', 2), ('mittens', 2), ('playful', 2), ('antics', 2), ('sunny', 2), ('basking', 2), ('sunlight', 2), ('spotted', 2), ('outside', 2), ('window', 2), ('swishing', 2), ('darted', 2), ('towards', 2), ('batted', 2), ('nimble', 2), ('creature', 2), ('fluttered', 2), ('leaving', 2), ('wanting', 2), ('explore', 2), ('searching', 2)]}
        self.assertEqual(result, expected_result)

        #test 2
        #testing the Bob_Johnson_Kitten_Story.docx
        

        #test 3
        #testing the Charlie_Brown_Cat.docx

        #test 4
        #testing the Jane_Doe_Cat_Story.docx

        #test 5
        #testing the test_document5.docx  (an empty document)
        
        #test 6
        #testing null


if __name__ == "__main__":
    unittest.main()
