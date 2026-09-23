"""
validation.py
Input validation functions implemented strictly WITHOUT try/except or exception handling.

Course topics demonstrated:
- Input/output, strings, conditionals, while loops, comparison operators,
  logical operators, membership operators, and type conversion.
"""


def is_valid_integer(text):
    """
    Checks if a string represents a valid non-negative integer using only
    string methods and basic conditionals (no try/except).
    """
    cleaned = text.strip()
    if len(cleaned) == 0:
        return False
    # Check if all characters are numerical digits
    return cleaned.isdigit()


def is_valid_float(text):
    """
    Checks if a string represents a valid non-negative float using only
    character inspections, string methods, and conditionals (no try/except).
    """
    cleaned = text.strip()
    if len(cleaned) == 0:
        return False

    # A valid decimal number has at most one dot
    if cleaned.count(".") > 1:
        return False

    # Remove one decimal point and verify the remainder consists entirely of digits
    without_dot = cleaned.replace(".", "", 1)
    if len(without_dot) == 0:
        return False

    return without_dot.isdigit()


def get_valid_integer(prompt, min_val=0, max_val=100000):
    """
    Prompts the user repeatedly until a valid integer within [min_val, max_val] is entered.
    """
    while True:
        raw_val = input(prompt)
        if not is_valid_integer(raw_val):
            print("Invalid input! Please enter whole numerical digits only.")
            continue

        # Type conversion from str to int
        val = int(raw_val)

        # Comparison operators to check bounds
        if val < min_val or val > max_val:
            print(f"Value out of bounds! Must be between {min_val} and {max_val}.")
            continue

        return val


def get_valid_float(prompt, min_val=0.0, max_val=100.0):
    """
    Prompts the user repeatedly until a valid floating-point number within [min_val, max_val] is entered.
    """
    while True:
        raw_val = input(prompt)
        if not is_valid_float(raw_val):
            print("Invalid input! Please enter a valid numerical number.")
            continue

        # Type conversion from str to float
        val = float(raw_val)

        # Relational and logical comparison
        if val < min_val or val > max_val:
            print(f"Value out of bounds! Must be between {min_val} and {max_val}.")
            continue

        return val


def get_non_empty_string(prompt):
    """
    Prompts the user repeatedly until a non-empty string is provided.
    """
    while True:
        text = input(prompt).strip()
        if len(text) == 0:
            print("Input cannot be empty. Please enter valid text.")
            continue
        return text


def get_menu_choice(prompt, valid_choices):
    """
    Validates user menu selection against a collection of valid choice strings.
    Demonstrates membership operator ('in').
    """
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice! Please select an option from the menu list.")
