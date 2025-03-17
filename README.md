# README - Exemplos de Stemming e Lematização em Português

Este projeto demonstra o uso de **Stemming** e **Lematização** em textos em língua portuguesa, utilizando as bibliotecas `nltk` e `spacy`. O código foi desenvolvido para ilustrar como essas técnicas funcionam e como podem ser aplicadas em diferentes textos.

## O que são Stemming e Lematização?

### Stemming
Stemming é o processo de reduzir palavras flexionadas ou derivadas ao seu radical ou raiz. É uma técnica mais simples e geralmente menos precisa, pois não considera o contexto da palavra.

**Exemplo:**
- Palavra: "correr"
- Radical (stem): "corr"

### Lematização
Lematização é o processo de agrupar as formas flexionadas de uma palavra para que possam ser analisadas como um único item, identificado pelo lema da palavra. É mais precisa que o stemming, pois considera o contexto gramatical.

**Exemplo:**
- Palavra: "correndo"
- Lema: "correr"

---

## Estrutura do Código

### Importações
O código utiliza as seguintes bibliotecas:
- `spacy`: Para realizar a lematização.
- `nltk.stem.RSLPStemmer`: Para realizar o stemming em português.
- `string`: Para manipulação de pontuações.

```python
import spacy
from nltk.stem import RSLPStemmer
import string
```

### Carregamento do Modelo de Lematização
O modelo de português do `spaCy` é carregado para realizar a lematização:
```python
nlp = spacy.load("pt_core_news_sm")
```

### Função para Remover Pontuações
Antes de aplicar o stemming ou a lematização, as pontuações são removidas dos textos:
```python
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))
```

### Função de Stemming
A função `stemming_example` aplica o stemming em uma lista de textos. Ela utiliza o `RSLPStemmer` da biblioteca `nltk`:
```python
def stemming_example(texts):
    stemmer = RSLPStemmer()
    return sorted(set(stemmer.stem(word.lower()) for text in texts for word in remove_punctuation(text).split()))
```

### Função de Lematização
A função `lemmatization_example` aplica a lematização em uma lista de textos, utilizando o modelo do `spaCy`:
```python
def lemmatization_example(texts):
    lemas = []
    for text in texts:
        doc = nlp(remove_punctuation(text))
        lemas.extend([token.lemma_ for token in doc])
    return sorted(set(lemas))
```

### Textos de Entrada
O código utiliza dois conjuntos de textos:
1. **Textos bíblicos**: Para demonstrar o funcionamento básico de stemming e lematização.
2. **Textos com mesma saída**: Para ilustrar como diferentes frases podem produzir o mesmo resultado.

```python
texts = [
    "No princípio, criou Deus os céus e a terra",
    "E disse Deus: Haja luz; e houve luz",
    "O Senhor é meu pastor, nada me faltará"
]

texts_same_output = [
    "Os meninos correram rapidamente",
    "O menino está correndo muito rápido"
]
```

### Execução do Código
O código aplica as funções de stemming e lematização nos dois conjuntos de textos e exibe os resultados no console:
```python
print("Stems (textos bíblicos):", stemming_example(texts))
print()
print("Lemas (textos bíblicos):", lemmatization_example(texts))
print()

print("Stems (mesma saída):", stemming_example(texts_same_output))
print()
print("Lemas (mesma saída):", lemmatization_example(texts_same_output))
```

---

## Resultados Esperados

### Textos Bíblicos
- **Stems**: Lista de radicais das palavras nos textos bíblicos.
- **Lemas**: Lista de lemas das palavras nos textos bíblicos.

### Textos com Mesma Saída
- **Stems**: Radicais semelhantes para palavras relacionadas (ex.: "correram" e "correndo").
- **Lemas**: Mesmo lema para palavras relacionadas (ex.: "correr").

---

## Requisitos para Execução

1. Instale as dependências:
   - `spacy`
   - `nltk`
2. Baixe o modelo de português do `spaCy`:
   ```bash
   python -m spacy download pt_core_news_sm
   ```
3. Execute o script `pp_1_2.py`:
   ```bash
   python pp_1_2.py
   ```

---

## Conclusão

Este projeto demonstra como o stemming e a lematização podem ser usados para processar textos em português. Ele também ilustra as diferenças entre essas técnicas e como elas podem produzir resultados semelhantes em alguns casos.

Sinta-se à vontade para modificar os textos de entrada e explorar os resultados!
