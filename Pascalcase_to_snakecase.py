"""
Write a function that takes a string in PascalCase and returns a string in snake_case
"""


def pascalcase_to_snakecase(text: str) -> str:
    words = [[], ]
    n = 0
    i = 0

    assert isinstance(text, str), "Unsupported type of input"
    assert not text[0].isalpha() or text[0].isupper(), "Provided string wasn't in PascalCase"

    while i < len(text):
        if (not text[i].isalpha()) or text[i].isupper():
            words[n].append(text[i].lower())
            i += 1
            while i < len(text) and not text[i].isupper():
                words[n].append(text[i])
                i += 1
            n += 1
            words.append([])
        else:
            i += 1
            assert False, "Something went wrong"

    for i in range(len(words)):
        words[i] = "".join(words[i])
    return "_".join(words)[:-1]


if __name__ == "__main__":
    print(pascalcase_to_snakecase("TestController"))
    print(pascalcase_to_snakecase("MoviesAndBooks"))
    print(pascalcase_to_snakecase("App7Test"))
