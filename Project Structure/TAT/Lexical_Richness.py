"""
    Lexical richness refers to the diversity and variety of vocabulary used in a piece of writing or speech.
    It measures the extent to which an individual or text employs a wide range of words and expressions.

    The TTR, Hapax legomena and MTLD scores was used to quantify lexical richness.  The average of the TTR and hapax
    scores are also calculated and presented as a metric on its own.

"""
import nltk
nltk.download('omw-1.4')


nltk.download('wordnet')
from nltk.tokenize import TreebankWordTokenizer, sent_tokenize
from collections import Counter
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from math import sqrt
from colorama import Fore, Style
import re


# Load document of text from file

class lexical_richness :
    def ttr(self,smart_doc):
        print("hello")
        """
        Calculate Type-Token Ratio (TTR) of given text and provide user with interpretation and context.
        The TTR score is calculated as the ratio of the number of unique words in a document to the total number of words in
        the document.
        NOTE: unique words don't refer to words that only occur once, rather the distinct or different words present in the
        document. (e.g. The word "apple" will count as unique word even if it occurs multiple time in the document).

        In the field of linguistics and language analysis, there is ongoing research and discussion regarding the
        interpretation of TTR scores and what can be considered a "good" score. However, it is important to note that there
        is no universally agreed-upon threshold or definitive range that applies to all types of texts or languages.

        From the writing assignments I analysed, it seemed that the most realistic ranges are 0-0.49 for bad, 0.5-0.69 for
        mediocre and 0.7-1 for good.
        """

        # Ensure the document is a valid string
        document = smart_doc.get_text()
        if not isinstance(document, str):
            raise ValueError(f"Expected a string document, but got: {type(document)}")

        # Tokenize words and sentences
        tokenizer = TreebankWordTokenizer()
        try:
            words = tokenizer.tokenize(document)
            sentences = sent_tokenize(document)
        except Exception as e:
            raise ValueError(f"Error during tokenization: {e}")
        
        # Remove stop words and lemmatize words
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        filtered_words = [lemmatizer.lemmatize(word.lower()) for word in words if
                        word.lower() not in stop_words and word.isalpha()]

        # Count occurrences of each word
        word_freq = Counter(filtered_words)

        # Count total number of words
        total_words = sum(word_freq.values())
         # Ensure the denominator is not zero before calculating TTR
        if total_words == 0:
            raise ValueError("Total number of words is zero. Cannot compute TTR.")


        

        # Calculate TTR
        ttr = len(word_freq) / total_words

        
        #################################################################################################
                                            # OPTIONAL OUTPUT
        #################################################################################################

        # Get unique words in text
        # unique_words = list(word_freq.keys())

        # Provide context and interpretation
        # print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "\nLexical Richness: Type-Token Ratio" + Style.RESET_ALL)
        # print("    Type-Token Ratio (TTR) measures the ratio of unique words to the total number of words in the text.\n")
        # print("    \033[1m\033[96mYour TTR score is {:.2f}.\033[0m".format(ttr))
        #
        # if ttr < 0.3:
        #     print(
        #         "    \033[1m\033[96mThis is a low value, which may be due to the text being too short or the vocabulary used being too limited.\033[0m".format(
        #             ttr))
        #     print(
        #         "    \033[1m\033[96mFor example, a children's storybook or a text written for English language learners may have a low TTR.\n\033[0m".format(
        #             ttr))
        # elif ttr < 0.6:
        #     print(
        #         "    \033[1m\033[96mThis is a moderate value, which indicates that the text has a reasonable degree of lexical diversity.\033[0m".format(
        #             ttr))
        #     print(
        #         "    \033[1m\033[96mFor example, a news article or a popular novel may have a moderate TTR.\n\033[0m".format(
        #             ttr))
        # else:
        #     print(
        #         "    \033[1m\033[96mThis is a high value, which indicates that the text has a good degree of lexical diversity.\033[0m".format(
        #             ttr))
        #     print(
        #         "    \033[1m\033[96mFor example, a scientific paper or a literary work may have a high TTR.\n\033[0m".format(
        #             ttr))
        #
        # print(f"    Unique words in the text: {unique_words}\n")
        #
        # # Provide recommended range
        # print(
        #     "    A common recommendation is that a TTR score of 0.4-0.6 indicates a good balance between lexical diversity and comprehensibility.")

        return ttr


    def hapax_legomena(self , smart_doc):
        """
        Calculate the hapax legomena ratio of given text and provide user with interpretation and context.

        Hapax Legomena refer to words that only occur once in the document (now the difference between unique and words
        that only occur once should become apparent).

        The hapax legomena score is calculated as the ratio of the number of words that occur only once in the document
        to the total number of UNIQUE words.


        The interpretation of a "good" hapax legomena ratio can depend on various factors such as the specific language,
        genre,and context of the text being analyzed. Hapax legomena ratios can vary widely depending on the nature of the
        text and its vocabulary richness.

        In general, a higher hapax legomena ratio indicates greater lexical diversity and a larger proportion of rare or
        unique words in the text. This can be an indicator of more varied vocabulary usage or a reflection of specialized or
        technical language in certain domains.

        I once again decided on the same ranges as that of the TTR, however, testing will need to be done on as many student
        writing assignments as possible to determine whether these ranges are sufficient.
        """

        document = smart_doc.get_text()
        if not isinstance(document, str):
            raise ValueError(f"Expected a string document, but got: {type(document)}")
        
        # Tokenize words
        tokenizer = TreebankWordTokenizer()
        try:
            words = tokenizer.tokenize(document)
        except Exception as e:
            raise ValueError(f"Error during tokenization: {e}")

        # Remove stopwords and punctuation
        stop_words = set(stopwords.words('english'))
        words = [word.lower() for word in words if word.lower() not in stop_words and word.isalpha()]

                # Calculate hapax legomena ratio
        word_freq = Counter(words)
        unique_words_count = len(word_freq)

        # Ensure the denominator is not zero before calculating hapax legomena ratio
        if unique_words_count == 0:
            raise ValueError("Number of unique words is zero. Cannot compute hapax legomena ratio.")
        
        # Calculate hapax legomena ratio
        word_freq = Counter(words)
        hapax_legomena_ratio = len([word for word, freq in word_freq.items() if freq == 1]) / unique_words_count

        #################################################################################################
                                                # OPTIONAL OUTPUT
        #################################################################################################

        # Provide context and interpretation
        # print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "\nLexical Richness: Hapax Legomena Ratio" + Style.RESET_ALL)
        # print("    The hapax legomena ratio measures the proportion of words that appear only once in a text.\n")
        # hapax_legomena = sum(1 for word in word_freq.values() if word == 1)
        # print(
        #     f"    \033[1m\033[96mThere are {hapax_legomena} hapax legomena, which are words that appear only once in the text.  There are {len(word_freq)} unique words in the text\033[0m")
        # print("    \033[1m\033[96mYour hapax legomena ratio is {:.2f}.\033[0m".format(hapax_legomena_ratio))
        #
        # if hapax_legomena_ratio < 0.05:
        #     print(
        #         "    \033[1m\033[96mThis is a low value, which indicates that the text has a high level of lexical diversity.\033[0m")
        #     print(
        #         "    \033[1m\033[96mFor example, a scientific paper or a literary work may have a low hapax legomena ratio.\n\033[0m")
        # elif hapax_legomena_ratio < 0.2:
        #     print(
        #         "    \033[1m\033[96mThis is a moderate value, which indicates that the text has a reasonable degree of lexical diversity.\033[0m")
        #     print(
        #         "    \033[1m\033[96mFor example, a news article or a popular novel may have a moderate hapax legomena ratio.\n\033[0m")
        # else:
        #     print(
        #         "    \033[1m\033[96mThis is a high value, which indicates that the text has a low level of lexical diversity.\033[0m")
        #     print(
        #         "    \033[1m\033[96mFor example, a children's storybook or a text written for English language learners may have a high hapax legomena ratio.\n\033[0m")
        #
        # # Get list of hapax legomena words
        # hapax_legomena_words = [word for word in word_freq if word_freq[word] == 1]
        #
        # print(f"    Hapax legomena words in the text: {hapax_legomena_words}\n")

        return hapax_legomena_ratio


    def mtld(self, smart_doc , threshold=42):
        """
        Calculate Measure of Textual Lexical Diversity (MTLD) of given text and provide user with interpretation and context.

        MTLD calculates lexical diversity by measuring the number of words within a text while considering the rate of new
        words introduced. The metric determines how many unique words are needed to achieve a certain level of lexical
        diversity within the text.

        The score is calculated as follows:
        1.	Determine a threshold value. This value represents the maximum number of continuous, readable words allowed
        before considering the text segment as a potential endpoint. The common threshold value is set to 42, but it can be
        adjusted based on the context and goals of the analysis.
        2.	Begin with an initial segment consisting of the first word of the text.
        3.	Expand the segment by adding words one by one until the length of the segment reaches the threshold value.
        4.	Calculate the lexical diversity within the segment using the TTR.
        5.	Repeat steps 3 and 4, creating subsequent segments, until the end of the text is reached.
        6.	Calculate the average TTR across all segments.
        7.	Reverse the process, starting from the last word of the text, to calculate the average TTR for backward segments.
        8.	Calculate the harmonic mean of the forward and backward average TTRs to obtain the MTLD score.

        """

        document = smart_doc.get_text()
        if not isinstance(document, str):
            raise ValueError(f"Expected a string document, but got: {type(document)}")
        
        # Tokenize words and remove non-alphabetic tokens
        tokenizer = RegexpTokenizer(r'\b[a-zA-Z]+\b')
        words = tokenizer.tokenize(smart_doc.get_text())
        words = [word.lower() for word in words]

        # Remove stop words and lemmatize words
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        filtered_words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]

        # Calculate the Type-Token Ratio
        if len(filtered_words) == 0:
            raise ValueError("Filtered words list is empty. Cannot compute TTR.")
        ttr = len(set(filtered_words)) / len(filtered_words)

         # Calculate the segments
        segments = [filtered_words[i:i+threshold] for i in range(0, len(filtered_words), threshold)]

        # Calculate the TTR for each segment
        segment_ttrs = [len(set(seg)) / len(seg) for seg in segments if len(seg) != 0]


        # Calculate the MTLD score
        if len(segment_ttrs) == 0:
            raise ValueError("No segments found. Cannot compute MTLD.")
        mtld_score = 1 / (sum([1 / ttr for ttr in segment_ttrs]) / len(segment_ttrs))

        return mtld_score



    def weighted_score(self, smart_doc):

        """
        This score is just the average of the TTR score and the Hapax Legomena score.  It was an attempt to quantify the
        Lexical diversity of the document with a single value.
        """
        result = smart_doc 
        hapax_score = self.hapax_legomena(result)
        ttr_score = self.ttr(result)
        score = (ttr_score + hapax_score) / 2

        return score
    
    
    # ttr(file_path)
    # hapax_legomena(file_path)
    # mtld(file_path)
    # weighted_score(file_path)

