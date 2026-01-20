import re

print("----- 1. Strong Password Validation using Lookahead Assertions -----")

password = "Strong@123"

password_pattern = r"""
^
(?=.*[A-Z])        # At least one uppercase letter
(?=.*[a-z])        # At least one lowercase letter
(?=.*\d)           # At least one digit
(?=.*[@$!%*?&])    # At least one special character
.{8,}              # Minimum 8 characters
$
"""

if re.match(password_pattern, password, re.VERBOSE):
    print("Password is STRONG")
else:
    print("Password is WEAK")


print("\n----- 2. Lookahead Assertion Explanation -----")
print("Lookahead (?=) checks conditions without consuming characters")


print("\n----- 3. Regex Modifiers Demonstration -----")

# IGNORECASE
print("\n• re.IGNORECASE")
text1 = "Python is Powerful"
match1 = re.search("python", text1, re.IGNORECASE)
print("Match found:", match1.group())


# MULTILINE
print("\n• re.MULTILINE")
text2 = """Hello World
Python Programming
Java"""

match2 = re.search("^Python", text2, re.MULTILINE)
print("Match found:", match2.group())


# DOTALL
print("\n• re.DOTALL")
text3 = "Start\nEnd"

match3 = re.search("Start.*End", text3, re.DOTALL)
print("Match found:", match3.group())


print("\n----- 4. Effect of Modifiers -----")
print("IGNORECASE  → Case insensitive matching")
print("MULTILINE   → ^ and $ work for each line")
print("DOTALL      → . matches newline characters")
