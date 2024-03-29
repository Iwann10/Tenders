import nltk
import pyphen
from typing import TypedDict

nltk.download('punkt')

from modules.metadata import metadata
from modules.tokenizer import tokenizer

# Define the input and output types for the tokenizer function
class Input(TypedDict):
    metadata: dict[str, str]
    tokens: list[str]
    numsyllables: int  # Number of syllables to filter polysyllabic words


class Output(TypedDict):
    metadata: dict[str, str]
    tokens: list[str]
    polysyllabic_list: dict[str, str]

def polysyllabic_words(input: Input) -> Output:
    """
    Extract polysyllabic words from the text based on the given number of syllables.

    Args:
        metadata (dict): Metadata containing the text to analyze
        tokens (list[str]): List of tokens
        numsyllables (int): Number of syllables to filter polysyllabic words

    Returns:
        dict: Polysyllabic words with their syllable count
    """

    # Check if numsyllables is provided and is an integer, otherwise use default value
    #defaults poly sylable words to 2
    numsyllables = input.get("numsyllables", 2)
    if not isinstance(numsyllables, int):
        raise ValueError("numsyllables must be an integer.")

    # Ensure the document is a valid string
    document = input["metadata"]["text"]
    if not isinstance(document, str):
        raise ValueError(f"Expected a string document, but got: {type(document)}")

    dic = pyphen.Pyphen(lang='en_US')

    words = input["tokens"]

    # Extract polysyllabic words with syllable count
    polysyllabic_list = []
    seen_words = set()

    for word in words:
        lowercase_word = word.lower()
        syllable_count = len(dic.inserted(lowercase_word).split('-'))
        if lowercase_word not in seen_words and syllable_count >= numsyllables:
            polysyllabic_list.append((word, syllable_count))
            seen_words.add(lowercase_word)

    # Sort the list in descending order based on the number of syllables
    polysyllabic_list.sort(key=lambda x: x[1], reverse=True)



    #################################################################################################
                                                # OPTIONAL OUTPUT
        #################################################################################################

        # Display polysyllabic words and their syllable count
        # for word, syllables_count in polysyllabic_words:
        #     print(f'{word}: {syllables_count}')

    return {"metadata": input["metadata"], "tokens": input["tokens"], "polysyllabic_list": polysyllabic_list}


if __name__ == "__main__":
    sample_input = tokenizer(metadata({"doc": "file.docx"}))
    sample_input["numsyllables"] = 2  # Set the value of 'n' for testing
    print(polysyllabic_words(sample_input))
