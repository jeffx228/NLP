# Import the English language class
from spacy.lang.en import English
import spacy
from spacy.matcher import Matcher

# Create the nlp object
nlp = English()

doc = nlp("Hello world!")


for token in doc:
    print(token.text)

token = doc[0]

print(token.text)

span = doc[1:3]

print(span.text)

newdoc = nlp("It costs $5. ")

print("Index: ", [token.i for token in newdoc])
print("Text: ", [token.text for token in newdoc])

print("is_alpha:", [token.is_alpha for token in newdoc])
print("is_punct:", [token.is_punct for token in newdoc])
print("like_num:", [token.like_num for token in newdoc])


nlp = spacy.load("en_core_web_sm")

doc = nlp("She ate the pizza")

for token in doc:
    # pos = part-of-speech tag
    print(token.text, token.pos_, token.dep_, token.head.text)



doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for ent in doc.ents:
    print(ent.text, ent.label_)

print(spacy.explain("GPE"))

matcher = Matcher(nlp.vocab)

# Add the pattern to the matcher

pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", None, pattern)

# Process some text
doc = nlp("Upcoming iPhone X release date leaked")

# Call the matcher on the doc

matches = matcher(doc)

for match_id, start, end in matches:
    #Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)



pattern = [
    {"IS_DIGIT": True}, 
    {"LOWER": "fifa"}, 
    {"LOWER": "world"}, 
    {"LOWER": "cup"},
    {"IS_PUNCT": True}
    ]

matcher.add("FIFA_PATTERN", None, pattern)

doc = nlp("2018 FIFA World Cup: France won!")

matches = matcher(doc)

for match_id, start, end in matches:
    #Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)




pattern = [
    {"LEMMA": "love", "POS": "VERB"}, 
    {"POS": "NOUN"}, 
    ]

matcher.add("PETS_PATTERN", None, pattern)

doc = nlp("I loved dogs but now I love cats more, but then, I loved humans even more.")

matches = matcher(doc)

for match_id, start, end in matches:
    #Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)


pattern = [
    {"LEMMA": "buy"}, 
    {"POS": "DET", "OP": "?"}, 
    {"POS": "NOUN"}, 
    ]

matcher.add("OPTIONAL_PATTERN", None, pattern)

doc = nlp("I bought a smartphone. I bought the watch. Now I'm buying apps.")

matches = matcher(doc)

for match_id, start, end in matches:
    #Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)

