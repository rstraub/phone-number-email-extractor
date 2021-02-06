import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area Code
    (\s|-|\.)?          # Separator
    (\d{3})             # First three digits
    (\s|-|\.)?          # Separator
    (\d{4})             # Last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

# TODO: Create email regex

# TODO: Create email regex

# TODO: Find matches on clipboard

# TODO: Copy matches to clipboard
