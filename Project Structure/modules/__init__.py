# You can add initialization code here if needed
# This file is required to treat the directory as a Python package
# It can be left empty if no initialization is needed

# Example: Importing modules from the package
# from .modules import module1, module2
# from .tests import test_module1, test_module2......

from .ngram_analysis import ngram_analysis
from .polysyllabic_words import polysyllabic_words
from .readability import readability
from .sentiment_analysis import sentiment_analysis
from .tokenizer import tokenizer
from .metadata import metadata

from modules import ngram_analysis, polysyllabic_words, readability, sentiment_analysis, tokenizer, metadata

