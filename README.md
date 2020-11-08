# CCI508 Language Technology
Exercises/Assignments for the CCI 508 Language Technology Course

In addition to the dependencies in `requirements.txt`, you will have to install some `nltk` packages:

```python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('stopwords')
```

After installing the dependencies and nltk packages, execute `main.py`. It should present you with a menu item with 5 options:

- Data cleaning
- POS tagging
- Named Entity Recognition
- Parsing
- Quit

**Data Cleaning** option removes stopwords, non-ascii charactersm, html and punctuations

**POS tagging** tags the different parts of speech

**Named Entity Recognition** identifies and categorises various named entities

**Parsing** uses the [Stanford NLP parser](http://nlp.stanford.edu:8080/parser/) to generate a parse tree 

**Quit** exits the program