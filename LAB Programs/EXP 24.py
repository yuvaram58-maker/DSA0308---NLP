import nltk
import re

nltk.download("punkt", quiet=True)

def recognize_dialog_act(sentence):
    sentence_lower = sentence.lower().strip()

    # Greeting
    if re.search(r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b",
                 sentence_lower):
        return "Greeting"

    # Goodbye
    elif re.search(r"\b(bye|goodbye|see you|see ya|take care)\b",
                   sentence_lower):
        return "Goodbye"

    # Thanks
    elif re.search(r"\b(thank you|thanks|thank you very much)\b",
                   sentence_lower):
        return "Thanking"

    # Question
    elif sentence_lower.endswith("?"):
        return "Question"

    # Request
    elif re.search(r"\b(please|could you|would you|can you|would you please)\b",
                   sentence_lower):
        return "Request"

    # Agreement
    elif re.search(r"\b(yes|yeah|sure|okay|ok|exactly|correct|agree)\b",
                   sentence_lower):
        return "Agreement"

    # Disagreement
    elif re.search(r"\b(no|not really|disagree|wrong|don't agree)\b",
                   sentence_lower):
        return "Disagreement"

    # Apology
    elif re.search(r"\b(sorry|apologize|apologies)\b",
                   sentence_lower):
        return "Apology"

    # Statement
    else:
        return "Statement"


def recognize_dialog(text):
    sentences = nltk.sent_tokenize(text)

    print("DIALOG ACT RECOGNITION")
    print("=" * 60)

    for i, sentence in enumerate(sentences, start=1):
        dialog_act = recognize_dialog_act(sentence)

        print(f"\nUtterance {i}: {sentence}")
        print(f"Dialog Act: {dialog_act}")


# Given conversation
dialog = """
Hello, how are you?
I am fine, thank you.
Could you help me with my assignment?
Sure, I can help you.
What topic is your assignment about?
It is about Natural Language Processing.
Sorry, I don't understand the question.
Please explain it again.
Yes, that is correct.
Thank you for your help.
Goodbye, see you later.
"""

recognize_dialog(dialog)