"""Tjaart van der Walt, 28846486"""

import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tokenize import TreebankWordTokenizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import normalize


"""
    Quantifying text coherence is an intricate process and cannot easily be quantified by using one specific method.
    This became apparent when I started testing different algorithms to try and quantify text coherence.
    All the methods I tested yielded very weak results.  I ended up only using the Jaccard similarity index even though
    it is not designed specifically for the purpose of quantifying coherence.
    
    Latent Semantic Analysis (LSA) is a recommended approach for coherence analysis, however, the results I obtained with
    LSA did not make sense.  I have included the LSA function code down below if a future team decides to try and
    investigate it further.
"""

class text_coherence:
    def jaccard_similarity_score(self, smart_doc):

        """
        1.  The text is tokenized into sentences using nltk.sent_tokenize(), which splits the text into individual sentences.
        2.  Stop words, commonly used words that do not carry significant meaning, are removed from each sentence.
            The code utilizes the NLTK library's stopwords module to obtain a set of stop words for the English language.
            Each sentence is then processed by tokenizing it into words using nltk.word_tokenize(), converting the words to
            lowercase, and filtering out any stop words.
        3.  A similarity matrix is computed to represent the similarity between sentences. The code uses the CountVectorizer
            class from the sklearn.feature_extraction.text module to transform the preprocessed sentences into binary vectors.
            The fit_transform() method converts the processed sentences into a matrix representation, where each row
            corresponds to a sentence, and each column indicates the presence or absence of a particular word.
            The dot product of the matrix with its transpose (vectorizer.dot(vectorizer.T)) computes the similarity scores
            between each pair of sentences. The result is converted to a 2D array using toarray().
        4.  The code calculates the average similarity score for each sentence. It iterates over each row of the similarity
            matrix and computes the sum of similarity values for that row (excluding the value corresponding to the
            sentence itself). The sum is divided by the number of sentences minus one to calculate the average similarity
            score for that sentence. The scores are stored in the similarity_scores list.
        5.  Finally, the code calculates the average similarity score across all sentences by summing up all the similarity
            scores and dividing it by the total number of similarity scores.
        """

            # Ensure the document is a valid string
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



    # cosine similarity function
    # Load document of text from file
    # file_path = "C:/Users/admin/Akademie 2023/BWIB 822/Assignment1.docx"   # replace with your file path


    # def cosine_similarity_score(file_path):
    #     if file_path.endswith('.docx'):
    #         doc = Document(file_path)
    #         full_text = []
    #         for para in doc.paragraphs:
    #             full_text.append(para.text)
    #         document = '\n'.join(full_text)
    #     else:
    #         with open(file_path, 'r', encoding='utf-8') as file:
    #             document = file.read()
    #
    #     # Tokenize words and sentences
    #     tokenizer = TreebankWordTokenizer()
    #     words = tokenizer.tokenize(document)
    #     sentences = sent_tokenize(document)
    #
    #     # Preprocess text
    #     stop_words = set(stopwords.words('english'))
    #     processed_sentences = [[word.lower() for word in nltk.word_tokenize(sentence) if word.lower() not in stop_words]
    #                            for sentence in sentences]
    #
    #     # Compute similarity matrix
    #     vectorizer = CountVectorizer().fit_transform([' '.join(sentence) for sentence in processed_sentences])
    #     similarity_matrix = cosine_similarity(vectorizer)
    #
    #     # Compute similarity scores
    #     similarity_scores = []
    #     for i in range(len(sentences)):
    #         similarity_scores.append(similarity_matrix[i])
    #
    #     # Visualize similarity matrix
    #     # sns.set()
    #     # plt.figure(figsize=(10, 8))
    #     # sns.heatmap(similarity_matrix, cmap='coolwarm', annot=True, fmt='.2f')
    #     # plt.title('Cosine Similarity Matrix')
    #     # plt.xlabel('Sentences')
    #     # plt.ylabel('Sentences')
    #     # plt.show()
    #
    #     # Output message
    #     avg_similarity = np.mean(similarity_scores)
    #     print(f"Average cosine similarity score is {avg_similarity:.2f}.")
    #     # for i in range(len(sentences)):
    #     #     if i == 0:
    #     #         continue
    #     #     similarity_to_prev = similarity_matrix[i][i-1]
    #     #     if similarity_to_prev < 0.2:
    #     #         print(f"Sentence {i} is not coherent with the previous sentence.")
    #     #     elif similarity_to_prev < 0.4:
    #     #         print(f"Sentence {i} is moderately coherent with the previous sentence.")
    #     #     else:
    #     #         print(f"Sentence {i} is highly coherent with the previous sentence.")
    #



    #LSA score
    # def lsa_score(file_path):
    #     # Read file
    #     if file_path.endswith('.docx'):
    #         doc = Document(file_path)
    #         full_text = []
    #         for para in doc.paragraphs:
    #             full_text.append(para.text)
    #         document = '\n'.join(full_text)
    #     else:
    #         with open(file_path, 'r', encoding='utf-8') as file:
    #             document = file.read()
    #
    #     # Tokenize and preprocess text
    #     sentences = nltk.sent_tokenize(document)
    #     stop_words = set(stopwords.words('english'))
    #     processed_sentences = [[word.lower() for word in nltk.word_tokenize(sentence) if word.lower() not in stop_words]
    #                            for sentence in sentences]
    #
    #     # Create document-term matrix
    #     vectorizer = CountVectorizer().fit_transform([' '.join(sentence) for sentence in processed_sentences])
    #
    #     # Apply LSA
    #     svd = TruncatedSVD(n_components=100, algorithm='randomized', n_iter=10, random_state=42)
    #     svd_matrix = svd.fit_transform(vectorizer)
    #     lsa = normalize(svd_matrix, norm='l2')
    #
    #     # Compute similarity matrix
    #     similarity_matrix = np.matmul(lsa, lsa.T)
    #
    #     # Compute average similarity score
    #     similarity_scores = []
    #     for i in range(len(sentences)):
    #         similarity_scores.append(sum(similarity_matrix[i]) / (len(sentences) - 1))
    #
    #     # Output message
    #     avg_similarity = sum(similarity_scores) / len(similarity_scores)
    #     if avg_similarity < 0.2:
    #         print(f"LSA similarity score is {avg_similarity:.2f}, which indicates low coherence.")
    #     elif avg_similarity < 0.4:
    #         print(f"LSA similarity score is {avg_similarity:.2f}, which indicates moderate coherence.")
    #     else:
    #         print(f"LSA similarity score is {avg_similarity:.2f}, which indicates high coherence.")
    #
    #     return avg_similarity

    #
    # cosine_similarity_score(file_path)
    # lsa_score(file_path)
