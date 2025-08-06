import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

example_string = """
I am Prashant Aher (PRN: UIT22M1002) is pursuing B.Tech in Information Technology  at Sanjivani College of Engineering.
I am passionate about Cyber Security.
I have have hands on experience on various tools and technologies like Kali Linux, Metasploit, Nmap, Nessus.
I enjoys working on Vulneribility Assessment and Penetration Testing.
In my free time I like to solve rooms on try hack me and also in VDP i do VAPT.
"""

sentences = sent_tokenize(example_string)
print(sentences)

words = word_tokenize(example_string)

words = [word for word in words if word.isalnum()]

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

print(filtered_words)
print(stemmed_words)
print(lemmatized_words)