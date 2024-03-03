"""
    Readability of text refers to how easy or difficult it is for readers to understand and comprehend text.
    
    The SMOG index was used to quantify the readability of the text.  It represents the grade level at which the reader
    must be to understand the text.  A SMOG score of 12 would indicate that the reader requires a grade 12 education to
    understand the text and a score higher than that indicates a more complex read and further education neccessary
    to understand the text.
    
    The score ranges from 3 to 20. (higher = better)
"""
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

import re
from typing import TypedDict

from modules.metadata import metadata

class Input(TypedDict):
    metadata: dict[str, str]


class Output(TypedDict):
    metadata: dict[str, str]
    tokens: list[str]
# import necessary modules



def calculate_smog_index(input: Input) -> Output: #(self, smart_doc):

    """
    The SMOG index, also known as Simple Measure of Gobbledygook, is a readability formula that estimates the reading
    level required to understand a piece of written text. It provides a measure of the document's comprehension
    difficulty based on the number of polysyllabic words it contains.

        Args:
        doc (doc.Doc): The document to test for readability

    Returns:
        dict: The readibility score needed to understand the documnet
    """


    # split the document into sentences
    document = input["metadata"]["text"]
    if not isinstance(document, str):
        raise ValueError(f"Expected a string document, but got: {type(document)}")

    # Split the document into sentences
    try:
        sentences = re.split(r' *[\.\?!][\'"\)\]]* *', document)
    except Exception as e:
        raise ValueError(f"Error during sentence splitting: {e}")
    num_sentences = len(sentences)

    # Count the number of polysyllabic words
    num_complex_words = 0
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            num_syllables = sum(word.count(vowel) for vowel in ['a', 'e', 'i', 'o', 'u', 'y'])
            if word.endswith(('es', 'ed')) or (len(word) > 1 and word[-2] in ['a', 'e', 'i', 'o', 'u'] and word[-1] == 'e'):
                num_syllables -= 1
            if num_syllables >= 3:
                num_complex_words += 1 

    # Calculate the SMOG index
    if num_sentences == 0:
        raise ValueError("No sentences found. Cannot compute SMOG index.")
    smog_index = 1.043 * math.sqrt(num_complex_words * (30 / num_sentences)) + 3.1291

    return {"metadata": input["metadata"], "smog_index": smog_index}

    if __name__ == "__main__":
        print(calculate_smog_index(metadata({"doc": "file.docx"})))
