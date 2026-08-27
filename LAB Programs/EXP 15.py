# Probabilistic CFG Parser

grammar = {
    "S": [
        (["NP", "VP"], 1.0)
    ],

    "NP": [
        (["Det", "N"], 0.6),
        (["Name"], 0.4)
    ],

    "VP": [
        (["V", "NP"], 0.7),
        (["V"], 0.3)
    ],

    "Det": [
        (["the"], 0.5),
        (["a"], 0.5)
    ],

    "N": [
        (["boy"], 0.5),
        (["ball"], 0.5)
    ],

    "V": [
        (["eats"], 0.6),
        (["kicks"], 0.4)
    ],

    "Name": [
        (["john"], 1.0)
    ]
}


# Check whether a symbol is a non-terminal
def is_non_terminal(symbol):
    return symbol in grammar


# Parse a symbol
def parse(symbol, words, position):

    # Terminal
    if not is_non_terminal(symbol):

        if position < len(words) and symbol == words[position]:
            return [(symbol, position + 1, 1.0)]

        return []

    results = []

    # Try every grammar rule
    for rule, rule_probability in grammar[symbol]:

        current = [(symbol, position, rule_probability)]

        children = []
        current_position = position
        success = True

        for item in rule:

            parsed = parse(item, words, current_position)

            if not parsed:
                success = False
                break

            best = max(parsed, key=lambda x: x[2])

            children.append(best[0])
            current_position = best[1]
            rule_probability *= best[2]

        if success:
            tree = (symbol, children)

            results.append(
                (tree, current_position, rule_probability)
            )

    return results


# Print parse tree
def print_tree(tree, level=0):

    symbol, children = tree

    print("  " * level + symbol)

    for child in children:

        if isinstance(child, tuple):
            print_tree(child, level + 1)

        else:
            print("  " * (level + 1) + child)


# Main program
sentence = input("Enter sentence: ").lower().split()

results = parse("S", sentence, 0)

valid_results = []

for tree, position, probability in results:

    if position == len(sentence):
        valid_results.append((tree, probability))


if valid_results:

    best_tree, best_probability = max(
        valid_results,
        key=lambda x: x[1]
    )

    print("\nMost Probable Parse:")
    print_tree(best_tree)

    print("\nProbability:", best_probability)

else:

    print("\nNo valid parse found.")