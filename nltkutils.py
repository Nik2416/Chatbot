<<<<<<< HEAD
import nltk
import numpy as np
nltk.download('punkt')
nltk.download('punkt_tab')

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return nltk.stem.porter.PorterStemmer().stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    bag = np.zeros(len(words),dtype=np.float32)
    tokenized_sentence=[stem(word) for word in tokenized_sentence]
    for id,word in enumerate(words):
        if word in tokenized_sentence:
            bag[id] = 1.0
    return bag




=======
import nltk
import numpy as np
nltk.download('punkt')
nltk.download('punkt_tab')

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return nltk.stem.porter.PorterStemmer().stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    bag = np.zeros(len(words),dtype=np.float32)
    tokenized_sentence=[stem(word) for word in tokenized_sentence]
    for id,word in enumerate(words):
        if word in tokenized_sentence:
            bag[id] = 1.0
    return bag




>>>>>>> origin/main
