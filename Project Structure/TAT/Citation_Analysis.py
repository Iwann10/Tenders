from docx import Document
import re
import nltk
nltk.download('omw-1.4')


class Citations:
    def get_unique_citations(self, smart_doc):
        """
        Extract the in-text citations that the writer used.
        """
        document = smart_doc.get_text()

        # Check if document is a valid string
        if not isinstance(document, str):
            raise ValueError(
                "Expected a string document, but got: {}".format(type(document)))

        # Find all citations in the text. The code looks for all text of the form ( , )
        citations = []
        start_index = 0
        while True:
            start_index = document.find('(', start_index)
            if start_index == -1:
                break
            end_index = document.find(')', start_index)
            if end_index == -1:
                break
            citation = document[start_index:end_index + 1]
            # More flexible condition
            if ',' in citation or re.search(r'\w+ \d{4}', citation):
                citations.append(citation)
            start_index = end_index + 1

        # Extract unique citations
        unique_citations = list(set(citations))

        # Return the list of unique citations
        return unique_citations
