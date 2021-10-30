import re


UPPER_RE = re.compile(r"[A-Z]")
LOWER_RE = re.compile(r"[a-z]")
ALPHABET = re.compile(r"[a-z]", flags=re.IGNORECASE)
COMMA_SPACE_WORD = re.compile(r", [a-z]", flags=re.IGNORECASE)


PERIOD = "."
COMMA = ","
SPACE = " "


def is_grammar_good(text: str) -> bool:
    if not UPPER_RE.fullmatch(text[0]):  # doesn't start with uppercase
        return False
    if text[-1] != PERIOD:
        return False  # doesn't end with a period
    n = len(text)
    for i, char in enumerate(text):
        if char == PERIOD and i != n - 1:
            return False  # found an early period
        if char == COMMA:
            if i == 0 or not ALPHABET.fullmatch(text[i - 1]):
                return False  # not preceded by a word
            if not COMMA_SPACE_WORD.fullmatch(text[i:(i + 3)]):
                return False  # not followed by a space and a word
        if char == SPACE:
            if i > 0 and text[i - 1] == SPACE:
                return False  # this space was preceded by a space; two in a row
    # no problems
    return True


if __name__ == "__main__":
    bad_lines = list()
    try:
        line_number = 1
        while True:
            line = input()
            if not is_grammar_good(line):
                bad_lines.append(str(line_number))
            line_number += 1
    except EOFError:
        pass
    if len(bad_lines) == 0:
        print("No Problems")
    else:
        print(" ".join(bad_lines))
