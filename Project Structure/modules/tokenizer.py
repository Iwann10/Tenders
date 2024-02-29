import re
from typing import TypedDict

from modules.metadata import metadata


# Define the input and output types for the tokenizer function
class Input(TypedDict):
    metadata: dict[str, str]


class Output(TypedDict):
    metadata: dict[str, str]
    tokens: list[str]


# tokenizer takes an input with a doc attribute of type SmartDocument
# and returns an output with a doc attribute (the same doc as input) and an additional tokens attribute (a list of strings)
def tokenizer(input: Input) -> Output:
    """
    Tokenizes the document into a dictionary of words and their frequencies

    Args:
        doc (doc.Doc): The document to tokenize

    Returns:
        dict: A dictionary of words and their frequencies
    """
    # convert the document to a string
    text = input["metadata"]["text"]
    # remove all non-alphanumeric characters
    # convert the string to lowercase and split the string into a list of words
    tokens = re.sub(r"[^a-zA-Z0-9\s]", "", text).lower().split()
    return {"metadata": input["metadata"], "tokens": tokens}


if __name__ == "__main__":
    print(tokenizer(metadata({"doc": "file.docx"})))
