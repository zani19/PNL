""" PP.1.2. Exemplifique a stemização e a lematização de um texto, em língua
portuguesa. Ilustre um caso onde textos diferentes conduzem a uma mesma saída
através do stemming ou lemmatization. Considere como saída um vetor ordenado
contendo lemas e stems.

Stematização: processo de reduzir palavras flexionadas (ou às vezes derivadas) ao seu radical ou raiz.
Exemplo: correr -> corr

Lematização: processo de agrupar as formas flexionadas de uma palavra para que possam ser analisadas como um único item, identificado pelo lema da palavra.
Exemplo: correndo -> correr


"""

import spacy
from nltk.stem import RSLPStemmer
import string 

# Carregando o modelo de português do spaCy
nlp = spacy.load("pt_core_news_sm")

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Função para demonstrar stemming
def stemming_example(texts):
    stemmer = RSLPStemmer()
    return sorted(set(stemmer.stem(word.lower()) for text in texts for word in remove_punctuation(text).split()))

# Função para demonstrar lematização com spaCy
def lemmatization_example(texts):
    lemas = []
    for text in texts:
        doc = nlp(remove_punctuation(text))
        lemas.extend([token.lemma_ for token in doc])
    return sorted(set(lemas))

texts = [
    "No princípio, criou Deus os céus e a terra",
    "E disse Deus: Haja luz; e houve luz",
    "O Senhor é meu pastor, nada me faltará"
]

texts_same_output = [
    "Os meninos correram rapidamente",
    "O menino está correndo muito rápido"
]

# Aplicando stemming e lematização
print("Stems (textos bíblicos):", stemming_example(texts))
print()
print("Lemas (textos bíblicos):", lemmatization_example(texts))
print()

# Demonstrando textos diferentes com mesma saída
print("Stems (mesma saída):", stemming_example(texts_same_output))
print() 
print("Lemas (mesma saída):", lemmatization_example(texts_same_output))
