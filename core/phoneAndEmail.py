#! python3
import re

import pyperclip

phoneRegex = re.compile(
    r"""(
    (\d{3}|\(\d{3}\))?  # Area Code
    (\s|-|\.)?          # Separator
    (\d{3})             # First three digits
    (\s|-|\.)?          # Separator
    (\d{4})             # Last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
)""",
    re.VERBOSE,
)

emailRegex = re.compile(
    r"""(
        [a-zA-Z0-9._%+-]+   # User name
        @
        [a-zA-Z0-9.-]+      # Domain name
        (\.[a-zA-Z]{2,4})   # Top-level domain
    )""",
    re.VERBOSE,
)

# Find matches on clipboard
text = str(pyperclip.paste())

matches = []
for phoneNumbers in phoneRegex.findall(text):
    phoneNum = "-".join([phoneNumbers[1], phoneNumbers[3], phoneNumbers[5]])
    if phoneNumbers[8] != "":
        phoneNum += " x" + phoneNumbers[8]
    matches.append(phoneNum)

for emailAddresses in emailRegex.findall(text):
    matches.append(emailAddresses[0])

# TODO: Copy matches to clipboard
