# Parse Tree Generation using CFG

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the", "a"]],
    "N": [["boy", "girl", "ball"]],
    "V": [["eats", "kicks"]]
}


# Check whether symbol is a non-terminal
def is_non_terminal(symbol):
    return symbol in grammar


# Generate parse tree
def parse(symbol, words, position):

    # Terminal symbol
    if not is_non_terminal(symbol):

        if position < len(words) and symbol == words[position]:
            return (symbol, position + 1)

        return None

    # Try each rule
    for rule in grammar[symbol]:

        children = []
        current_position = position
        success = True

        for item in rule:

            result = parse(item, words, current_position)

            if result is None:
                success = False
                break

            tree, current_position = result
            children.append(tree)

        if success:
            return ((symbol, children), current_position)

    return None


# Print parse tree
def print_tree(tree, level=0):

    if isinstance(tree, str):
        print("  " * level + tree)
    else:
        symbol, children = tree
        print("  " * level + symbol)

        for child in children:
            print_tree(child, level + 1)


# Main program
sentence = input("Enter sentence: ").lower().split()

result = parse("S", sentence, 0)

if result is not None and result[1] == len(sentence):

    print("\nParse Tree:")
    print_tree(result[0])

else:
    print("\nNo parse tree found.")