######################################
import unittest
from modules.ngram_analysis import ngram_analysis
from modules.tokenizer import tokenizer
from modules.metadata import metadata

class TestNGramAnalysis(unittest.TestCase):
    def test_ngram_analysis(self):
        #test 1
        #testing the alice_smith_cat_story
        input_data = tokenizer(metadata({"doc": "tests/Alice_Smith_Cat_Story.docx"}))
        result = ngram_analysis(input_data)
        expected_result = {'metadata': {'author': 'Alice Smith', 'category': 'Story', 'comments': 'This is a story about a curious cat named Mittens.', 'content_status': 'Draft', 'created': '2013-12-23T23:15:00', 'identifier': '12345678-1234-1234-1234-123456789012', 'keywords': 'cat, story, adventure', 'language': 'en-US', 'last_modified_by': 'Alice Smith', 'last_printed': None, 'modified': '2013-12-23T23:15:00', 'revision': 1, 'subject': "A Cat's Adventure", 'title': 'fluttering butterfly outside the window.', 'version': '1.0', 'name': 'tests/Alice_Smith_Cat_Story.docx', 'paragraphs': ["Alice Smith's Cat", 'In a cozy little house nestled amidst the bustling city, lived a ginger cat named Mittens, the beloved companion of Alice Smith. She was known for her playful antics and insatiable curiosity. One sunny afternoon, while basking in a patch of warm sunlight, Mittens spotted a fluttering butterfly outside the window. She leaped off the window sill, tail swishing excitedly, and darted towards the fluttering wings. Mittens pounced and batted at the butterfly with her paws, but the nimble creature fluttered away, leaving her wanting more. Undeterred, Mittens continued to explore the house, searching for new adventures.'], 'text': "Alice Smith's Cat In a cozy little house nestled amidst the bustling city, lived a ginger cat named Mittens, the beloved companion of Alice Smith. She was known for her playful antics and insatiable curiosity. One sunny afternoon, while basking in a patch of warm sunlight, Mittens spotted a fluttering butterfly outside the window. She leaped off the window sill, tail swishing excitedly, and darted towards the fluttering wings. Mittens pounced and batted at the butterfly with her paws, but the nimble creature fluttered away, leaving her wanting more. Undeterred, Mittens continued to explore the house, searching for new adventures."}, 'tokens': ['alice', 'smiths', 'cat', 'in', 'a', 'cozy', 'little', 'house', 'nestled', 'amidst', 'the', 'bustling', 'city', 'lived', 'a', 'ginger', 'cat', 'named', 'mittens', 'the', 'beloved', 'companion', 'of', 'alice', 'smith', 'she', 'was', 'known', 'for', 'her', 'playful', 'antics', 'and', 'insatiable', 'curiosity', 'one', 'sunny', 'afternoon', 'while', 'basking', 'in', 'a', 'patch', 'of', 'warm', 'sunlight', 'mittens', 'spotted', 'a', 'fluttering', 'butterfly', 'outside', 'the', 'window', 'she', 'leaped', 'off', 'the', 'window', 'sill', 'tail', 'swishing', 'excitedly', 'and', 'darted', 'towards', 'the', 'fluttering', 'wings', 'mittens', 'pounced', 'and', 'batted', 'at', 'the', 'butterfly', 'with', 'her', 'paws', 'but', 'the', 'nimble', 'creature', 'fluttered', 'away', 'leaving', 'her', 'wanting', 'more', 'undeterred', 'mittens', 'continued', 'to', 'explore', 'the', 'house', 'searching', 'for', 'new', 'adventures'], 'top_ngrams': [(('alice', 'smiths'), 1), (('smiths', 'cat'), 1), (('cat', 'cozy'), 1), (('cozy', 'little'), 1), (('little', 'house'), 1), (('house', 'nestled'), 1), (('nestled', 'amidst'), 1), (('amidst', 'bustling'), 1), (('bustling', 'city'), 1), (('city', 'lived'), 1), (('lived', 'ginger'), 1), (('ginger', 'cat'), 1), (('cat', 'named'), 1), (('named', 'mittens'), 1), (('mittens', 'beloved'), 1), (('beloved', 'companion'), 1), (('companion', 'alice'), 1), (('alice', 'smith'), 1), (('smith', 'known'), 1), (('known', 'playful'), 1), (('playful', 'antics'), 1), (('antics', 'insatiable'), 1), (('insatiable', 'curiosity'), 1), (('curiosity', 'one'), 1), (('one', 'sunny'), 1), (('sunny', 'afternoon'), 1), (('afternoon', 'basking'), 1), (('basking', 'patch'), 1), (('patch', 'warm'), 1), (('warm', 'sunlight'), 1), (('sunlight', 'mittens'), 1), (('mittens', 'spotted'), 1), (('spotted', 'fluttering'), 1), (('fluttering', 'butterfly'), 1), (('butterfly', 'outside'), 1), (('outside', 'window'), 1), (('window', 'leaped'), 1), (('leaped', 'window'), 1), (('window', 'sill'), 1), (('sill', 'tail'), 1), (('tail', 'swishing'), 1), (('swishing', 'excitedly'), 1), (('excitedly', 'darted'), 1), (('darted', 'towards'), 1), (('towards', 'fluttering'), 1), (('fluttering', 'wings'), 1), (('wings', 'mittens'), 1), (('mittens', 'pounced'), 1), (('pounced', 'batted'), 1), (('batted', 'butterfly'), 1)]}
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