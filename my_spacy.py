import spacy
import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer

nlp = spacy.load('en_core_web_sm')
stemmer = PorterStemmer()

example_string = """
I am Prashant Aher (PRN: UIT22M1002) is pursuing B.Tech in Information Technology  at Sanjivani College of Engineering.
I am passionate about Cyber Security.
I have have hands on experience on various tools and technologies like Kali Linux, Metasploit, Nmap, Nessus.
I enjoys working on Vulneribility Assessment and Penetration Testing.
In my free time I like to solve rooms on try hack me and also in VDP i do VAPT."""

doc = nlp(example_string)

sentences = [sent.text for sent in doc.sents]
print(sentences)

words = [token.text for token in doc if not token.is_punct]
print(words)

filtered_words = [token.text for token in doc if not token.is_punct and not token.is_stop]
print(filtered_words)

lemmatized_words = [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]
print(lemmatized_words)

stemmed_words = [stemmer.stem(token.text) for token in doc if not token.is_punct and not token.is_stop]
print(stemmed_words)