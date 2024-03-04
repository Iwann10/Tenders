import re
import math
from typing import TypedDict

from modules.metadata import metadata

class Input(TypedDict):
    metadata: dict[str, str]

class Output(TypedDict):
    metadata: dict[str, str]
    smog_index: float

def readability(input: Input) -> Output:
    """
    Calculate the SMOG index for readability of a given text.
    
    Args:
        input (dict): The input dictionary containing metadata with the text to analyze.
        
    Returns:
        The calculated SMOG index along with the original metadata.
    """

    # Extract text from metadata
    document = input["metadata"]["text"]

    # Split the document into sentences
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', document)
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

    # Return the result
    return {"metadata": input["metadata"], "smog_index": smog_index}

if __name__ == "__main__":
    # Example usage
    sample_metadata = metadata({"doc": "file.docx"})
    sample_input = {"metadata": sample_metadata}
    result = readability(sample_input)
    print(result)
