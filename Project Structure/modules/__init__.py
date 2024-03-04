# You can add initialization code here if needed
# This file is required to treat the directory as a Python package
# It can be left empty if no initialization is needed

# Example: Importing modules from the package
# from .modules import module1, module2
# from .tests import test_module1, test_module2....

from modules.NGramAnalysis import ngram_analysis
from modules.PolySyllabic_Words import polysyllabic_words
from modules.Readability import readability
from modules.Sentiment_Analysis import sentiment_analysis
from modules.metadata import metadata
from modules.tokenizer import tokenizer

from tests import test_NGramAnalysis, test_PolySyllabic_Words, test_Readability, test_Sentiment_Analysis
