"""
    Cohesion in a written text refers to the logical and meaningful connections between different parts of the text.
    It is the quality that allows a piece of writing to flow smoothly and coherently, enabling readers to understand the
    intended message or information effectively.
    
    A custom function was used to quantify cohesion based on lexical repition.
"""
import math
import statistics
import string
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize



# Load document of text from file

class text_cohesion:
    def calculate_cohesion_score(self, smart_doc):
        """
        The given code calculates the cohesion score of a document based on lexical repetition.  By quantifying cohesion
        based on lexical repetition, the code aims to provide a measure of how closely related the words in the document
        are to each other.

        Lexical repetition refers to the repeated use of the same or similar words or lexical items within a given text or
        discourse. It involves the recurrence of specific words, phrases, or vocabulary throughout the writing.
        """

        # Ensure the document is a valid string
        document = smart_doc.get_text()
        if not isinstance(document, str):
            raise ValueError(f"Expected a string document, but got: {type(document)}")

        # Tokenize the document into words
        try:
            words = word_tokenize(document.lower())
        except Exception as e:
            raise ValueError(f"Error during word tokenization: {e}")

        # Ensure we have a non-empty list of words
        if not words:
            raise ValueError("The document contains no valid words.")

        # Calculate word frequencies
        word_freqs = Counter(words)

        # Calculate cohesion score based on lexical repetition
        try:
            cohesion_score = sum(count - 1 for count in word_freqs.values()) / len(words)
        except ZeroDivisionError:
            cohesion_score = 0

        return cohesion_score

    """Alternative algorithm"""

    #
    # def calculate_cohesion_score(file_path):
    #     # Load document of text from file
    #     if file_path.endswith('.docx'):
    #         doc = Document(file_path)
    #         full_text = []
    #         for para in doc.paragraphs:
    #             full_text.append(para.text)
    #         document = '\n'.join(full_text)
    #     else:
    #         with open(file_path, 'r', encoding='utf-8') as file:
    #             document = file.read()
    #
    #     # Tokenize the document into sentences and words
    #     sentences = sent_tokenize(document)
    #     words = word_tokenize(document.lower())
    #
    #     # Remove stop words and punctuation from words
    #     stop_words = set(stopwords.words('english'))
    #     words = [word for word in words if word not in stop_words and word not in string.punctuation]
    #
    #     # Calculate the word frequency distribution
    #     freq_dist = nltk.FreqDist(words)
    #
    #     # Calculate the total number of words and unique words
    #     total_words = len(words)
    #     unique_words = len(set(words))
    #
    #     # Calculate the average frequency of each word
    #     avg_word_freq = statistics.mean(freq_dist.values())
    #
    #     # Calculate the cohesion score
    #     cohesion_score = 1 - (math.log(unique_words) / math.log(total_words)) * (1 - (1 / avg_word_freq))
    #
    #     return cohesion_score