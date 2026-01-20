import re

print("----- 1. re.match(): Employee ID Validation -----")
emp_id = "EMP123"

match_emp = re.match(r"(EMP)(\d{3})", emp_id)

if match_emp:
    print("Valid Employee ID")
    print("Full Match :", match_emp.group())
    print("Group 1 (Prefix):", match_emp.group(1))
    print("Group 2 (Digits):", match_emp.group(2))
else:
    print("Invalid Employee ID")


print("\n----- 2. re.search(): Email Search -----")
text = "Please contact us at dbhargav098@gmail.com for help"

email_pattern = r"([\w\.]+)@([\w]+)\.(\w+)"
search_email = re.search(email_pattern, text)

if search_email:
    print("Email Found :", search_email.group())
    print("Username   :", search_email.group(1))
    print("Domain     :", search_email.group(2))
    print("Extension  :", search_email.group(3))
else:
    print("No Email Found")


print("\n----- 3. Meta-characters & Special Sequences Demo -----")

sample_text = "User_01 scored 95 marks"

patterns = {
    r"\d+": "Digits (\\d)",
    r"\w+": "Word characters (\\w)",
    r"\s": "Whitespace (\\s)",
    r"U.*1": "Dot and Star (.*)",
    r"User_+": "Plus (+)",
    r"marks?": "Question Mark (?)"
}

for pattern, description in patterns.items():
    result = re.search(pattern, sample_text)
    if result:
        print(f"{description}: {result.group()}")


print("\n----- 4. Capturing Parentheses (Matched Groups) -----")
date = "Date: 11-01-2026"

date_match = re.search(r"(\d{2})-(\d{2})-(\d{4})", date)

if date_match:
    print("Full Date :", date_match.group())
    print("Day       :", date_match.group(1))
    print("Month     :", date_match.group(2))
    print("Year      :", date_match.group(3))
