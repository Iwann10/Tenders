from nltk.util import ngrams
from nltk.corpus import stopwords
from collections import Counter
import nltk
nltk.download('omw-1.4')


import re
from typing import TypedDict

from modules.metadata import metadata
from modules.tokenizer import tokenizer

class Input(TypedDict):
    metadata: dict[str, str]
    tokens: list[str]


class Output(TypedDict):
    metadata: dict[str, str]
    tokens: list[str]
    top_ngrams: list[str]


#An n-gram is a contiguous sequence of n items, where an item can be a word, character, or even a sequence of words.
def ngram_analysis(input: Input) -> Output: #(self,smart_doc, n=2):

    """
    Search for N-grams in the text.

    If n=2, then all the sets of two words that co-occur together will be displayed (bi-grams).  If n=3, all the sets of
    three words that co-occur together will be displayed (tri-grams) etc.

    Args:
        tokens (list[str]): The list of tokens

    Returns:
        dict: sets of words in n=__ co-occurences
    """


    # Ensure the document is a valid string
    #document = smart_doc.get_text()
    #if not isinstance(document, str):
     #    raise ValueError(f"Expected a string document, but got: {type(document)}")

    # Tokenize words and remove punctuation
    #try:
    #    words = word_tokenize(document)
    #except Exception as e:
     #    raise ValueError(f"Error during tokenization: {e}")
    
    words = input["tokens"]
    
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

    return {
        "metadata": input["metadata"],
        "tokens": input["tokens"],
        "top_ngrams": top_ngrams,
    }



###work on here
    if __name__ == "__main__":
        print(ngram_analysis(tokenizer(metadata({"doc": "file.docx"}))))