import re

# --------------------------------------------------
# Strong Password Validation using Lookahead Assertions
# --------------------------------------------------

def validate_password(password):
    pattern = r"""
        ^
        (?=.*[A-Z])        # At least one uppercase letter
        (?=.*[a-z])        # At least one lowercase letter
        (?=.*\d)           # At least one digit
        (?=.*[@$!%*?&])    # At least one special character
        .{8,}              # Minimum 8 characters
        $
    """

    if re.match(pattern, password, re.VERBOSE):
        print("Strong Password")
    else:
        print("Weak Password")


# --------------------------------------------------
# Demonstration of Regex Modifiers
# --------------------------------------------------

def regex_modifiers_demo():

    # re.IGNORECASE
    text1 = "Hello World"
    pattern1 = "hello"
    print("\nIGNORECASE:")
    print(re.search(pattern1, text1))
    print(re.search(pattern1, text1, re.IGNORECASE))

    # re.MULTILINE
    text2 = """Python is fun
Regex is powerful
Python is awesome"""
    pattern2 = r"^Python"
    print("\nMULTILINE:")
    print(re.findall(pattern2, text2))
    print(re.findall(pattern2, text2, re.MULTILINE))

    # re.DOTALL
    text3 = "Hello\nWorld"
    pattern3 = r"Hello.*World"
    print("\nDOTALL:")
    print(re.search(pattern3, text3))
    print(re.search(pattern3, text3, re.DOTALL))


# --------------------------------------------------
# Main Program
# --------------------------------------------------

password = input("Enter password: ")
validate_password(password)
regex_modifiers_demo()
