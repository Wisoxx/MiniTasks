"""
Write a function to transform a string to an integer in range from zero to a million
Note: "and" should be skipped: "one hundred and four" = 104
All numbers are real, no need to check
"""


def word_to_number(text: str) -> int:
    text = text.lower().replace(" and ", " ").split()
    words = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
             "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
             "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40,
             "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
             "hundred": 100, "hundreds": 100, "thousand": 1e3, "thousands": 1e3, "million": 1e6, "millions": 1e6}
    millions, thousands, hundreds, tens = 0, 0, 0, 0
    for word in text:
        x = words.get(word)
        if x == 1e6:
            millions, tens = tens, millions
        elif x == 1e3:
            tens += hundreds * 100
            hundreds = 0
            thousands, tens = tens, thousands
        elif x == 100:
            hundreds, tens = tens, hundreds
        else:
            tens += x

    return int(1e6 * millions + 1e3 * thousands + 100 * hundreds + tens)


print("one", word_to_number("one"))
print("twelve", word_to_number("twelve"))
print("two hundred forty six", word_to_number("two hundred forty six"))
print("seven hundred eighty three thousand nine hundred twelve", word_to_number("seven hundred eighty three thousand nine hundred twelve"))
print("five hundreds fifty three thousands nineteen", word_to_number("five hundreds fifty three thousands nineteen"))
