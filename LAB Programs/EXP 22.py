import nltk
import re

# Download required NLTK resources
nltk.download("punkt", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)

def reference_resolution(text):
    # Split text into sentences
    sentences = nltk.sent_tokenize(text)

    # Store previously mentioned nouns
    noun_references = []

    print("REFERENCE RESOLUTION")
    print("=" * 60)

    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)

        resolved_sentence = sentence

        # Identify nouns and proper nouns
        for word, tag in tagged_words:
            if tag.startswith("NN"):
                noun_references.append(word)

        # Pronouns to be resolved
        pronouns = ["he", "she", "it", "they", "him", "her", "them"]

        for word in words:
            if word.lower() in pronouns and noun_references:
                # Use the most recently mentioned noun
                reference = noun_references[-1]

                # Replace pronoun with its possible reference
                pattern = r"\b" + re.escape(word) + r"\b"
                resolved_sentence = re.sub(
                    pattern,
                    f"{word} ({reference})",
                    resolved_sentence,
                    count=1,
                    flags=re.IGNORECASE
                )

        print("\nOriginal Sentence:")
        print(sentence)

        print("Resolved Sentence:")
        print(resolved_sentence)


# Input text
text = """
John went to the library. He borrowed a book.
The book was interesting. It contained many useful examples.
Mary met John there. She discussed the book with him.
"""

reference_resolution(text)