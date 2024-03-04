########################################################
import unittest
from modules.metadata import metadata
from modules.sentiment_analysis import sentiment_analysis

class TestSentimentAnalysis(unittest.TestCase):
    def test_sentiment_analysis(self):
        #test 1
        #testing the alice_smith_cat_story.docx
        input_data = metadata({"doc": "tests/Alice_Smith_Cat_Story.docx"})
        result = sentiment_analysis(input_data)
        expected_result = {'metadata': {'author': 'Alice Smith', 'category': 'Story', 'comments': 'This is a story about a curious cat named Mittens.', 'content_status': 'Draft', 'created': '2013-12-23T23:15:00', 'identifier': '12345678-1234-1234-1234-123456789012', 'keywords': 'cat, story, adventure', 'language': 'en-US', 'last_modified_by': 'Alice Smith', 'last_printed': None, 'modified': '2013-12-23T23:15:00', 'revision': 1, 'subject': "A Cat's Adventure", 'title': 'fluttering butterfly outside the window.', 'version': '1.0', 'name': 'tests/Alice_Smith_Cat_Story.docx', 'paragraphs': ["Alice Smith's Cat", 'In a cozy little house nestled amidst the bustling city, lived a ginger cat named Mittens, the beloved companion of Alice Smith. She was known for her playful antics and insatiable curiosity. One sunny afternoon, while basking in a patch of warm sunlight, Mittens spotted a fluttering butterfly outside the window. She leaped off the window sill, tail swishing excitedly, and darted towards the fluttering wings. Mittens pounced and batted at the butterfly with her paws, but the nimble creature fluttered away, leaving her wanting more. Undeterred, Mittens continued to explore the house, searching for new adventures.'], 'text': "Alice Smith's Cat In a cozy little house nestled amidst the bustling city, lived a ginger cat named Mittens, the beloved companion of Alice Smith. She was known for her playful antics and insatiable curiosity. One sunny afternoon, while basking in a patch of warm sunlight, Mittens spotted a fluttering butterfly outside the window. She leaped off the window sill, tail swishing excitedly, and darted towards the fluttering wings. Mittens pounced and batted at the butterfly with her paws, but the nimble creature fluttered away, leaving her wanting more. Undeterred, Mittens continued to explore the house, searching for new adventures."}, 'sentiment_scores': {'neg': 0.0, 'neu': 0.876, 'pos': 0.124, 'compound': 0.8658}}
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