"""
    Syntactic complexity of a text refers to the level of sophistication and intricacy in the structure and arrangement of
    sentences and phrases within that text. It measures the degree to which a piece of writing or speech exhibits a wide
    range of sentence structures, sentence types, and syntactic features.
"""

import nltk
nltk.download('large_grammars')



class syntactic_complexity: 
    def calculate_syntactic_complexity(self, smart_doc):

        """
        The syntactic complexity score is calculated as follows:
        1.  The code calculates the average number of words per sentence. It counts the total number of sentences and the
            total number of words in the text by tokenizing each sentence into words using nltk.tokenize.word_tokenize().
            The average number of words per sentence is obtained by dividing the total number of words by the total number
            of sentences.
        2.  Next, the code aims to calculate the average number of phrases per sentence. It uses a predefined
            grammar (atis.cfg) loaded from the nltk.data module. The EarleyChartParser from the nltk.parse module is used to
            parse each sentence and count the number of phrases. However, it is important to note that the code provided
            assumes the availability of the specific grammar file and may require modification or substitution with an
            appropriate grammar for the desired analysis.
        3.  The average number of phrases per sentence is calculated by dividing the total number of phrases by the total
            number of sentences.
        4.  Finally, the syntactic complexity score is obtained by summing the average number of words per sentence and
            the average number of phrases per sentence.
        """



        #   Ensure the document is a valid string
        document = smart_doc.get_text()
        if not isinstance(document, str):
            raise ValueError(f"Expected a string document, but got: {type(document)}")

        # Tokenize the document into sentences
        try:
            sent_tokenizer = nltk.tokenize.PunktSentenceTokenizer()
            sentences = sent_tokenizer.tokenize(document)
        except Exception as e:
            raise ValueError(f"Error during sentence tokenization: {e}")

        # Calculate the average number of words per sentence
        num_sentences = len(sentences)
        try:
            num_words = sum(len(nltk.tokenize.word_tokenize(sent)) for sent in sentences)
            avg_words_per_sent = num_words / num_sentences
        except ZeroDivisionError:
            avg_words_per_sent = 0

        # Calculate the average number of phrases per sentence
        try:
            grammar = nltk.data.load('grammars/large_grammars/atis.cfg')
            parser = nltk.parse.EarleyChartParser(grammar)
        except Exception as e:
            raise ValueError(f"Error loading the grammar or initializing the parser: {e}")

        num_phrases = 0
        for sent in sentences:
            try:
                num_phrases += len(list(parser.parse(nltk.tokenize.word_tokenize(sent))))
            except ValueError:
                pass

        try:
            avg_phrases_per_sent = num_phrases / num_sentences
        except ZeroDivisionError:
            avg_phrases_per_sent = 0

        # Calculate the syntactic complexity score
        score = avg_words_per_sent + avg_phrases_per_sent

        return score
