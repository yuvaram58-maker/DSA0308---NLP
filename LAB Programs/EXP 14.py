grammar = {
    "S": ["NP VP"],
    "NP": ["Det N"],
    "VP": ["V"],
    "Det": ["the"],

    "N_singular": ["boy", "girl", "student"],
    "N_plural": ["boys", "girls", "students"],

    "V_singular": ["runs", "plays", "eats"],
    "V_plural": ["run", "play", "eat"]
}


# Function to check agreement
def check_agreement(subject, verb):

    if (subject in grammar["N_singular"] and
            verb in grammar["V_singular"]):
        return "Correct Agreement"

    elif (subject in grammar["N_plural"] and
          verb in grammar["V_plural"]):
        return "Correct Agreement"

    else:
        return "Incorrect Agreement"


# Main program
subject = input("Enter subject: ").lower()
verb = input("Enter verb: ").lower()

result = check_agreement(subject, verb)

print("Subject:", subject)
print("Verb:", verb)
print("Result:", result)