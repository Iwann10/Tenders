"""
    Cohesion markers are linguistic elements used in writing to create cohesion and coherence within a text.
    They connect different parts of the writing together, ensuring that ideas flow smoothly and are logically linked.
"""

import re
from collections import Counter
import nltk
nltk.download('omw-1.4')

class extract_cohesion_markers:
    def extract_cohesion_markers(self,smart_doc):
        """A list of typical cohesion markers are specified and the code searches for occurrences of words in the text that are present in the list.""" 
        
        # Define a list of cohesion markers.  More can be added if deemed necessary.
        cohesion_markers = [
            "First",
            "Second",
            "Third",
            "Lastly",
            "Finally",
            "In conclusion",
            "To sum up",
            "On the one hand",
            "On the other hand",
            "Moreover",
            "Furthermore",
            "Additionally",
            "In addition",
            "Similarly",
            "Likewise",
            "In the same way",
            "In the same vein",
            "Contrarily",
            "Conversely",
            "On the contrary",
            "In contrast",
            "However",
            "Nevertheless",
            "Nonetheless",
            "Despite",
            "In spite of",
            "Regardless",
            "Notwithstanding",
            "Yet",
            "Although",
            "Though",
            "While",
            "Even though",
            "In a similar manner",
            "In a different manner",
            "By comparison",
            "In comparison",
            "Compared to",
            "In a like manner",
            "Accordingly",
            "Therefore",
            "Thus",
            "Consequently",
            "Hence",
            "As a result",
            "For this reason",
            "Because",
            "Since",
            "As",
            "Due to",
            "Owing to",
            "Based on",
            "In the case of",
            "Regarding",
            "With respect to",
            "In terms of",
            "As for",
            "Concerning",
            "Regarding",
            "As regards",
            "In this regard",
            "In relation to",
            "In connection with",
            "With regard to",
            # Add more cohesion markers as needed
        ]

        # Ensure the document is a valid string
        document = smart_doc.get_text()
        if not isinstance(document, str):
            raise ValueError(f"Expected a string document, but got: {type(document)}")

        # Extract cohesion markers using regular expressions
        pattern = r'\b(?:' + '|'.join(re.escape(marker) for marker in cohesion_markers) + r')\b'
        extracted_markers = re.findall(pattern, document, flags=re.IGNORECASE)

        # Count the frequency of cohesion markers
        marker_frequency = Counter(extracted_markers)

        # Sort cohesion markers based on frequency in descending order
        sorted_marker_freq = sorted(marker_frequency.items(), key=lambda x: x[1], reverse=True)

        return sorted_marker_freq