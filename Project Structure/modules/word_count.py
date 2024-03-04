from typing import TypedDict

from modules.metadata import metadata
from modules.tokenizer import tokenizer


# Define the input and output types for the tokenizer function
class Input(TypedDict):
    metadata: dict[str, str]
    tokens: list[str]


class Output(TypedDict):
    metadata: dict[str, str]
    tokens: list[str]
    word_counts: dict[str, int]


def word_count(input: Input) -> Output:
    """
    Counts the frequency of each word in the tokenized list

    Args:
        tokens (list[str]): The list of tokens

    Returns:
        dict: A dictionary of words and their counts.
    """
    word_counts = {}
    for token in input["tokens"]:
        if token in word_counts:
            word_counts[token] += 1
        else:
            word_counts[token] = 1
    return {
        "metadata": input["metadata"],
        "tokens": input["tokens"],
        "word_counts": word_counts,
    }


if __name__ == "__main__":
    print(word_count(tokenizer(metadata({"doc": "file.docx"}))))
