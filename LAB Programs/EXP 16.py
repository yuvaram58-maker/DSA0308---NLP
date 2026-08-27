import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Barack Obama was born in Hawaii. He was the President of the United States."

# Process the text
doc = nlp(text)

# Display named entities
print("Named Entities")
print("----------------")

for entity in doc.ents:
    print(entity.text, "->", entity.label_)