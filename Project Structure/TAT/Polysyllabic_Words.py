import nltk
from nltk.tokenize import word_tokenize
import pyphen

nltk.download('punkt')

class polysyllabic_words:
    def extract_polysyllabic_words(self,smart_doc, numsyllables=2):

        """
        Polysyllabic words are simply words with multiple syllables.  Words with a higher number of syllables can contribute
        to the syntactic complexity as well as the lexical richness of the text.

        To filter the words on the number of syllables they contain, simply change the numsyllables parameter
        e.g. numsyllables=4.
        """
  # Ensure the document is a valid string
        document = smart_doc.get_text()
        if not isinstance(document, str):
            raise ValueError(f"Expected a string document, but got: {type(document)}")

        dic = pyphen.Pyphen(lang='en_US')

        # Tokenize the document into words
        try:
            words = word_tokenize(document)
        except Exception as e:
            raise ValueError(f"Error during tokenization: {e}")

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

        return polysyllabic_list

  

