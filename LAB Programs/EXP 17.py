import nltk
from nltk.corpus import wordnet

# Download WordNet data
nltk.download("wordnet")
nltk.download("omw-1.4")

# Get word from user
word = input("Enter a word: ").lower()

# Retrieve synsets
synsets = wordnet.synsets(word)

if synsets:
    print("\nWord:", word)
    print("Number of Synsets:", len(synsets))
    print("\nMeanings:")
    print("----------------------------")

    for synset in synsets:
        print("Synset:", synset.name())
        print("Definition:", synset.definition())

        examples = synset.examples()

        if examples:
            print("Example:", examples[0])
        else:
            print("Example: No example available")

        print()
else:
    print("No synsets found for the given word.")