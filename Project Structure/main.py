# an example for how the registerMethod function could be modified is:
# The output of the previous function does not have to match the input of the next function exactly. Instead, it should just have, at least, the properties required by the input of the next function.

# This means that the output of the previous function can have many additional properties that are not necessary for the next function but must have the properties required by the input of the next function.


# example:


# previous function output:
# {
# "doc": input.doc,
# "tokens": tokens,
# "word_counts": word_counts
# }

# next function input:
# {
# "doc": input.doc,
# "tokens": tokens
# }

# this should be compatible because the next function only requires the "doc" and "tokens" properties, which are present in the output of the previous function.


# In that way, the output of the previous function can be a superset of the input of the next function. This allows for more flexibility in the order of the functions and the data they operate on.

from typing import get_type_hints


def registerMethod(methods):
    """
    Register a sequence of methods and create a new function that applies them in order.

    Args:
        methods (list): A list of methods to be registered.

    Returns:
        function: A new function that applies the registered methods in order to the input document.

    """

    def retFunc(doc):
        output = doc
        for method in methods:
            output = method(output)
        return output

    return retFunc


# ------------------------------------------------------------------------------------------------------------------------------------

#stuff given to us
from modules.metadata import metadata
from modules.tokenizer import tokenizer
from modules.word_count import word_count


#testing new methods imports
from modules.ngram_analysis import ngram_analysis
from modules.polysyllabic_words import polysyllabic_words
from modules.readability import readability
from modules.sentiment_analysis import sentiment_analysis

doc = {"doc": "tests/Alice_Smith_Cat_Story.docx"}

# Use the registerMethod function to create a chain of methods
methods = {
    "word count": registerMethod([metadata, tokenizer, word_count]),
    # other methods...

    #methods we testing in the main
    "ngram analysis": registerMethod([metadata, tokenizer, ngram_analysis]),

    "polysyllabic words": registerMethod([metadata, tokenizer, polysyllabic_words]),

    "readability": registerMethod([metadata, readability]),

    "sentiment analysis" :registerMethod([metadata, sentiment_analysis])
}

result = methods["word count"](doc)
result2 = methods["ngram analysis"](doc)
result3 = methods["polysyllabic words"](doc)
result4 = methods["readability"](doc)
result5 = methods["sentiment analysis"](doc)

print("word count\n", result , "\n\n\n\n\n\n" )
print("ngram analysis\n", result2 , "\n\n\n\n\n\n" )
print("poly words\n", result3 , "\n\n\n\n\n\n" )
print("readability\n", result4 , "\n\n\n\n\n\n" )
print("sentiment\n", result5 , "\n\n\n\n\n\n" )