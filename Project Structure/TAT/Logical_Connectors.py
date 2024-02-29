"""
    Logical connectors are linguistic devices used in writing to establish logical relationships between ideas,
    sentences, or paragraphs. They serve as bridges that guide readers through the text, making the connections between
    different parts of the content more coherent and organized.

    Proper use of logical connectors can contribute greatly to the readability and coherence of text.
"""

import re
from collections import Counter
import nltk
nltk.download('omw-1.4')

class logical_connnectors: 
    def extract_logical_connectors(self,smart_doc):
        """
    A list of typical logical connectors are specified and the code searches for occurrences of words in the text that
    are present in the list.
    """
        # Define a list of logical connectors.  More can be added if deemed necessary.
        logical_connectors = [
                "And",
                "Or",
                "Not",
                "If",
                "Only if",
                "Implies",
                "Equivalent to",
                "Moreover",
                "Furthermore",
                "Additionally",
                "In addition",
                "Similarly",
                "Likewise",
                "Conversely",
                "On the other hand",
                "However",
                "Nevertheless",
                "Nonetheless",
                "In contrast",
                "Whereas",
                "While",
                "Although",
                "Though",
                "Despite",
                "In spite of",
                "Regardless",
                "Notwithstanding",
                "Hence",
                "Therefore",
                "Thus",
                "Consequently",
                "As a result",
                "Accordingly",
                "In summary",
                "In conclusion",
                "In brief",
                "To summarize",
                "Ultimately",
                "In essence",
                "Overall",
                "For example",
                "For instance",
                "Namely",
                "That is",
                "In other words",
                "On the contrary",
                "In fact",
                "Indeed",
                "In particular",
                "Specifically",
                "As a matter of fact",
                "To be precise",
                "By all means",
                "In reality",
                "In truth",
                "In short",
                "To illustrate",
                "To clarify",
                "To demonstrate",
                "In any event",
                "In any case",
                "Under these circumstances",
                "In this case",
                "In such a scenario",
                "Given these points",
                "Considering this",
                "On this basis",
                "In light of this",
                "In the same way",
                "In a similar fashion",
                "Equally",
                "Likewise",
                "In a like manner",
                "Just like",
                "Compared to",
                "In comparison",
                "In a different manner",
                "On the flip side",
            # Add more logical connectors as needed
        ]

        # Ensure the document is a valid string
        document = smart_doc.get_text()
        if not isinstance(document, str):
            raise ValueError(f"Expected a string document, but got: {type(document)}")

        # Extract logical connectors using regular expressions
        pattern = r'\b(?:' + '|'.join(re.escape(connector) for connector in logical_connectors) + r')\b'
        try:
            extracted_connectors = re.findall(pattern, document, flags=re.IGNORECASE)
        except Exception as e:
            raise ValueError(f"Error during regex matching: {e}")
        
        # Count the frequency of logical connectors
        connector_frequency = Counter(extracted_connectors)

        # Sort logical connectors based on frequency in descending order
        sorted_connector_freq = sorted(connector_frequency.items(), key=lambda x: x[1], reverse=True)

        return sorted_connector_freq


# extract_logical_connectors(file_path)