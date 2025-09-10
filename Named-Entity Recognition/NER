import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976 in California. Today, Apple’s headquarters is located in Cupertino, and the company is valued at over 2 trillion dollars. In 2021, Tim Cook announced new products at the Worldwide Developers Conference (WWDC).")
for ent in doc.ents:
      print(f"{ent.text:<25} {ent.start_char:<5} {ent.end_char:<5} {ent.label_}")

displacy.serve(doc, style="ent")
