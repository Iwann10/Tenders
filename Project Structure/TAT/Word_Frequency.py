"""
    The word frequencies are self-explanatory.
"""


import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class word_frequency:

    def calculate_word_frequencies(self, smart_doc):
        """
        Calculate word frequencies for the provided document.
        """

        # Ensure the document is a valid string
        document = smart_doc.get_text()
        if not isinstance(document, str):
            raise ValueError(f"Expected a string document, but got: {type(document)}")

        # Remove typographical symbols and punctuation marks using regular expressions
        cleaned_document = re.sub(r'[^\w\s]', '', document)

        # Extract words using NLTK's word_tokenize
        try:
            words = word_tokenize(cleaned_document)
        except Exception as e:
            raise ValueError(f"Error during word tokenization: {e}")

        # Filter out numbers and convert words to lowercase
        words = [word.lower() for word in words if not word.isdigit()]

        # Get the English stop words from NLTK
        stop_words = set(stopwords.words('english'))

        # Count word frequencies while excluding stop words
        word_freq = Counter(word for word in words if word not in stop_words)

        # Sort words based on frequency in descending order
        sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

        return sorted_word_freq
    