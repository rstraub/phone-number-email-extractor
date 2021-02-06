import re

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

# TODO: Find matches on clipboard

# TODO: Copy matches to clipboard
