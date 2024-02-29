import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')



class sentiment_analysis: 
    def perform_sentiment_analysis(self, smart_doc):

        """
        Positivity Score: The positivity score represents the extent to which the text or document expresses positive
        sentiment. It indicates the presence and intensity of positive emotions, attitudes, or opinions conveyed in the
        text. A higher positivity score suggests a more positive sentiment associated with the text.

        Negativity Score: The negativity score indicates the degree of negative sentiment expressed in the text.
        It represents the presence and intensity of negative emotions, attitudes, or opinions conveyed in the text.
        A higher negativity score suggests a more negative sentiment associated with the text.

        Neutral Score: The neutral score represents the extent to which the text or document lacks any strong positive or
        negative sentiment. It indicates the presence of statements or content that are considered neutral, factual, or
        lacking emotional connotations. A higher neutral score suggests a more neutral or objective tone in the text.
        """
        # Ensure the document is a valid string
        document = smart_doc.get_text()
        if not isinstance(document, str):
            raise ValueError(f"Expected a string document, but got: {type(document)}")

        # Perform sentiment analysis using NLTK
        sia = SentimentIntensityAnalyzer()
        try:
            sentiment_scores = sia.polarity_scores(document)
        except Exception as e:
            raise ValueError(f"Error during sentiment analysis: {e}")

        return sentiment_scores

  