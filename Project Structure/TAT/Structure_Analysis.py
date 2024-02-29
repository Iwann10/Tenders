import re
import statistics

class structure_analysis: 
    def structure_analysis(self,smart_doc):

        """
        We simply calculate some basic statistics such as average sentence length, standard deviation of sentence length,
        average word length.  There are many more statistics that can potentially be calculated here.
        """

# Ensure the document is a valid string
        document = smart_doc.get_text()
        if not isinstance(document, str):
            raise ValueError(f"Expected a string document, but got: {type(document)}")

        # Split the document into sentences
        try:
            sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', document)
        except Exception as e:
            raise ValueError(f"Error during sentence splitting: {e}")

        # Calculate basic statistics
        total_words = sum(len(sentence.split()) for sentence in sentences)
        total_sentences = len(sentences)
        sentence_lengths = [len(sentence.split()) for sentence in sentences]
        word_lengths = [len(word) for sentence in sentences for word in sentence.split()]

        # Average sentence length
        try:
            average_sentence_length = round(total_words / total_sentences)
        except ZeroDivisionError:
            average_sentence_length = 0

        # Average word length
        try:
            average_word_length = round(statistics.mean(word_lengths))
        except statistics.StatisticsError:
            average_word_length = 0

        # Standard deviation of sentence lengths
        try:
            sentence_deviation = round(statistics.stdev(sentence_lengths))
        except statistics.StatisticsError:
            sentence_deviation = 0

        return average_sentence_length, sentence_deviation, average_word_length
