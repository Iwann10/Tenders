import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

from typing import TypedDict

from modules.metadata import metadata

class Input(TypedDict):
    metadata: dict[str, str]


class Output(TypedDict):
    metadata: dict[str, str]
    sentiment_scores: dict[str, float]

def sentiment_analysis(input: Input) -> Output:
    """
    Perform sentiment analysis on the given text and return sentiment scores.

    Positivity Score: Represents the extent of positive sentiment expressed in the text.
    Negativity Score: Represents the extent of negative sentiment expressed in the text.
    Neutral Score: Represents the extent of neutral sentiment expressed in the text.

    Args:
        metadata (dict): Metadata containing the text for sentiment analysis

    Returns:
        dict: Sentiment analysis scores of the document
    """
    # Ensure the document is a valid string
    text = input["metadata"]["text"]
    if not isinstance(text, str):
        raise ValueError(f"Expected a string document, but got: {type(text)}")

    # Perform sentiment analysis using NLTK
    sia = SentimentIntensityAnalyzer()

    try:
        sentiment_scores = sia.polarity_scores(text)
    except Exception as e:
        raise ValueError(f"Error during sentiment analysis: {e}")

    return {"metadata": input["metadata"], "sentiment_scores": sentiment_scores}

if __name__ == "__main__":
    # Example usage
    sample_metadata = metadata({"doc": "file.docx"})
    sample_input = {"metadata": sample_metadata}
    result = readability(sample_input)
    print(result)
