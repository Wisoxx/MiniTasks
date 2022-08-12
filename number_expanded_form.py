"""
You will be given a number, and you will need to return it as a string in expanded form.
Note: every number should be an integer more than 0
Example: expanded_form(12) -> "10 + 2"
"""


def expanded_form(number: int) -> str:
    number = str(number)
    result = ""
    length = len(number)
    i = 0
    for digit in number:
        if digit != "0":
            end = " + " if i < length - 1 else ""
            result += f"{int(digit) * 10**(length - 1 - i)}" + end
        i += 1
    return result


if __name__ == "__main__":
    print("12 =", expanded_form(12))
    print("42 =", expanded_form(42))
    print("70304 =", expanded_form(70304))
