# Simple Earley Parser for CFG

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["boy"], ["girl"], ["ball"]],
    "V": [["eats"], ["kicks"]]
}


# Check whether a symbol is a non-terminal
def is_non_terminal(symbol):
    return symbol in grammar


# Add a state if it is not already present
def add_state(chart, position, state):
    if state not in chart[position]:
        chart[position].append(state)


# Earley Parser
def earley_parser(words):

    n = len(words)

    # Create chart
    chart = [[] for _ in range(n + 1)]

    # State format:
    # (left side, right side, dot position, start position)

    add_state(chart, 0, ("S'", ("S",), 0, 0))

    # Process every chart position
    for i in range(n + 1):

        index = 0

        while index < len(chart[i]):

            state = chart[i][index]

            left, right, dot, start = state

            # COMPLETED STATE
            if dot == len(right):

                for old_state in chart[start]:

                    old_left, old_right, old_dot, old_start = old_state

                    if old_dot < len(old_right):

                        next_symbol = old_right[old_dot]

                        if next_symbol == left:

                            new_state = (
                                old_left,
                                old_right,
                                old_dot + 1,
                                old_start
                            )

                            add_state(chart, i, new_state)

            # NEXT SYMBOL EXISTS
            else:

                next_symbol = right[dot]

                # PREDICT
                if is_non_terminal(next_symbol):

                    for rule in grammar[next_symbol]:

                        new_state = (
                            next_symbol,
                            tuple(rule),
                            0,
                            i
                        )

                        add_state(chart, i, new_state)

                # SCAN
                else:

                    if i < n and next_symbol == words[i]:

                        new_state = (
                            left,
                            right,
                            dot + 1,
                            start
                        )

                        add_state(chart, i + 1, new_state)

            index += 1

    # Final state
    final_state = ("S'", ("S",), 1, 0)

    return final_state in chart[n], chart


# Main program
sentence = input("Enter sentence: ").lower().split()

accepted, chart = earley_parser(sentence)

if accepted:
    print("Sentence is accepted by the grammar.")
else:
    print("Sentence is rejected by the grammar.")