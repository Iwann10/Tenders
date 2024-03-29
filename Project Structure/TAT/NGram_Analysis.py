"""
    An n-gram is a contiguous sequence of n items, where an item can be a word, character, or even a sequence of words.
"""
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import nltk
nltk.download('omw-1.4')

class ngram_analysis: 
    
    def perform_ngram_analysis(self,smart_doc, n=2):

        """
        Search for N-grams in the text.

    If n=2, then all the sets of two words that co-occur together will be displayed (bi-grams).  If n=3, all the sets of
    three words that co-occur together will be displayed (tri-grams) etc.
    """
    

        # Ensure the document is a valid string
        document = smart_doc.get_text()
        if not isinstance(document, str):
            raise ValueError(f"Expected a string document, but got: {type(document)}")

        # Tokenize words and remove punctuation
        try:
            words = word_tokenize(document)
        except Exception as e:
            raise ValueError(f"Error during tokenization: {e}")
        
        words = [word.lower() for word in words if word.isalpha()]

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word not in stop_words]

        # Generate n-grams
        try:
            n_grams = list(ngrams(words, n))
        except Exception as e:
            raise ValueError(f"Error during n-gram generation: {e}")

        # Count the occurrences of each n-gram
        ngram_counts = Counter(n_grams)

        # Get the top 50 n-grams in descending order
        top_ngrams = ngram_counts.most_common(50)

        return top_ngrams