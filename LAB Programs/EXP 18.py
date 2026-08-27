import re


# Function to check a predicate
def is_predicate(expression):

    pattern = r"^[A-Za-z]+\([a-z]\)$"

    return re.match(pattern, expression) is not None


# Function to parse FOPC expression
def parse_expression(expression):

    expression = expression.strip()

    # Check for NOT
    if expression.startswith("NOT "):
        return parse_expression(expression[4:])

    # Check for AND
    if " AND " in expression:

        parts = expression.split(" AND ", 1)

        return (
            parse_expression(parts[0])
            and parse_expression(parts[1])
        )

    # Check for OR
    if " OR " in expression:

        parts = expression.split(" OR ", 1)

        return (
            parse_expression(parts[0])
            and parse_expression(parts[1])
        )

    # Check for predicate
    return is_predicate(expression)


# Main program
expression = input("Enter FOPC expression: ")

if parse_expression(expression):
    print("Valid FOPC expression")
else:
    print("Invalid FOPC expression")