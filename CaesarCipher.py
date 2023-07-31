"""
Write a class that takes a string and returns a string in uppercase in which every letter is shifted on N positions
"""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

NUM_LET = {number: letter for (number, letter) in zip(range(len(ALPHABET)), ALPHABET)}
LET_NUM = {letter: number for (number, letter) in zip(range(len(ALPHABET)), ALPHABET)}


class CaesarCipher:
    def __init__(self, N: int):
        if N < 1:
            N = 1
        elif N > len(ALPHABET):
            N = len(ALPHABET)
        self.N = N

    def encode(self, text: str) -> str:
        result = ""
        for i in text.upper():
            if i not in ALPHABET:
                return ""
            n = LET_NUM[i] + self.N
            n = n - len(ALPHABET) if n > len(ALPHABET) else n
            result += NUM_LET[n]
        return result

    def decode(self, text: str) -> str:
        result = ""
        for i in text.upper():
            if i not in ALPHABET:
                return ""
            n = LET_NUM[i] - self.N
            n = n + len(ALPHABET) if n < 0 else n
            result += NUM_LET[n]
        return result


if __name__ == "__main__":
    c = CaesarCipher(5)
    print(c.encode('Codewars'))  # 'HTIJBFWX'
    print(c.decode('BFKKQJX'))   # 'WAFFLES'
