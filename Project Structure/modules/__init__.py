# You can add initialization code here if needed
# This file is required to treat the directory as a Python package
# It can be left empty if no initialization is needed

# Example: Importing modules from the package
# from .modules import module1, module2
# from .tests import test_module1, test_module2......

from .NGramAnalysis import ngram_analysis
from .PolySyllabic_Words import polysyllabic_words
from .Readability import readability
from .Sentiment_Analysis import sentiment_analysis

from modules import ngram_analysis, polysyllabic_words, readability, sentiment_analysis
