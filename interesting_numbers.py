"""
Prologue
Let's make sure that Bob never misses a single interesting number. We hacked into his car's computer, and we have a box
that reads mileage. The box is glued to his dashboard, which lights up yellow or green depending on whether it gets
a 1 or 2 (respectively).

Description
Write a function that parses the number of miles entered and returns 2 if the number is "interesting" (see below),
1 if the number is interesting within the next two miles, or 0 if the number is not interesting.

"Interesting" numbers
Interesting numbers are numbers with 3 or more digits that meet one or more of the following criteria:
• Any digit followed by all zeros: 100, 90000
• Each digit is the same number: 1111.
• Numbers consecutive, spliced: 1234
• Numbers are sequential, descending: 4321
• The numbers are a palindrome: 1221 or 73837.
• The numbers correspond to one of the values in the awesome_phrases array.
• For ascending sequences, 0 must come after 9, not before 1 as in 7890.
• For descending sequences, 0 must come after 1, not before 9 as in 3210.
"""


def is_interesting(mile, awesome_phrases):
    def all_zeros(num: int):
        num = str(num)
        return True if len(num) > 1 and num[0] != 0 and len(set(num)) == 2 and "0" in set(num) else False

    def repeating_nums(num):
        return set(str(num)) == 1

    def is_palindrome(num):
        num = str(num)
        left = num[:(len(num) // 2) + 1 if int(num) % 2 != 0 else 0]
        right = num[len(num) // 2:]
        return left == right[::-1]

    score = 2
    for i in range(3):
        if len(str(mile)) >= 3 and any((mile in awesome_phrases,
                                        repeating_nums(mile),
                                        all_zeros(mile),
                                        str(mile) in "1234567890",
                                        str(mile) in "9876543210",
                                        is_palindrome(mile))):
            return score
        if i == 0:
            score -= 1
        mile += 1
    return 0


# "boring numbers"
print("is_interesting(3, [1337, 256]), 0, ", is_interesting(3, [1337, 256]))  # 0
print("is_interesting(3236, [1337, 256]), 0,", is_interesting(3236, [1337, 256]))  # 0

# approaching to an "interesting" number
print("is_interesting(11207, []), 0,", is_interesting(11207, []))  # 0
print("is_interesting(11208, []), 0,", is_interesting(11208, []))  # 0
print("is_interesting(11209, []), 1,", is_interesting(11209, []))  # 1
print("is_interesting(11210, []), 1,", is_interesting(11210, []))  # 1
print("is_interesting(11211, []), 2,", is_interesting(11211, []))  # 2

# approaching to awesome_phrases
print("is_interesting(1335, [1337, 256]), 1", is_interesting(1335, [1337, 256]))  # 1
print("is_interesting(1336, [1337, 256]), 1", is_interesting(1336, [1337, 256]))  # 1
print("is_interesting(1337, [1337, 256]), 2", is_interesting(1337, [1337, 256]))  # 2
