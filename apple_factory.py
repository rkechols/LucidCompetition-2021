REQUIRED = {
    "a": 1,
    "p": 2,
    "l": 1,
    "e": 1
}


if __name__ == "__main__":
    text = input()
    counts = {letter: 0 for letter in REQUIRED.keys()}
    for char in text:
        try:
            counts[char] += 1
        except KeyError:
            pass  # we don't want to count other letters
    min_count = None
    for letter, count in counts.items():
        req_count = REQUIRED[letter]
        makeable = count // req_count
        if min_count is None or makeable < min_count:
            min_count = makeable
    print(min_count)
