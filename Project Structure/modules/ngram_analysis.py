from nltk.util import ngrams
from nltk.corpus import stopwords
from collections import Counter
import nltk
nltk.download('omw-1.4')

from modules.metadata import metadata
from modules.tokenizer import tokenizer

from typing import TypedDict

class Input(TypedDict):
    metadata: dict[str, str]
    tokens: list[str]
    #gets value for n the ngram analysis
    #must set the value for n when wanting to use the module
    n: int

class Output(TypedDict):
    metadata: dict[str, str]
    tokens: list[str]
    top_ngrams: list[str]


def ngram_analysis(input: Input) -> Output:
    """
    Search for N-grams in the text.

    If n=2, then all the sets of two words that co-occur together will be displayed (bi-grams).  If n=3, all the sets of
    three words that co-occur together will be displayed (tri-grams) etc.

    Args:
        tokens (list[str]): The list of tokens
        n (int): The size of the n-grams to generate

    Returns:
        Sets of words in n=__ co-occurrences
    """

    n = input.get("numsyllables", 2)
    #error handeling if not null
    if not isinstance(n, int):
        raise ValueError("n must be an integer.")

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

# Testing the function
if __name__ == "__main__":
    sample_input = tokenizer(metadata({"doc": "file.docx"}))
    sample_input["n"] = 2  # Set the value of 'n' for testing
    print(ngram_analysis(sample_input))
