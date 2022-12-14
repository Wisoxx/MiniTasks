"""
Given a chemical formula represented by a string, count the number of atoms of each element contained in the molecule
and return an object (dict dictionary).
Note: Braces can be represented as (), [], {} and be inside of each other
"""


def parse_molecule(formula: str, multiplier=1) -> dict:
    table = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K',
             'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb',
             'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs',
             'Ba', 'La', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr',
             'Ra', 'Ac', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og', 'Ce',
             'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Th', 'Pa', 'U', 'Np', 'Pu',
             'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']

    def check_and_add(atom, value=1):
        nonlocal result, multiplier
        if atom in result:
            result[atom] += value * multiplier
        else:
            result.setdefault(atom, value * multiplier)

    def parse_number(return_=False):
        nonlocal i, next

        number = next
        i += 1

        # finding the whole number
        for digit in formula[i + 2:]:
            if digit.isalpha():
                break
            number += digit
            i += 1

        if not return_:
            # adding the value to the dict
            check_and_add(symbol, int(number))
        else:
            return int(number)

    def parse_bracket(bracket):
        nonlocal i, next
        pairs = {"(": ")", "[": "]", "{": "}"}

        # finding text inside of brackets
        new_formula = ""
        for character in formula[i + 1:]:
            if character == pairs[bracket]:
                if i < len(formula) - 2:
                    next = formula[i + 2]
                    new_multiplier = parse_number(return_=True)
                    i += 1
                break
            new_formula += character
            i += 1

        # making recursion and adding coefficients to the main result
        for atom, coefficient in parse_molecule(new_formula, new_multiplier).items():
            check_and_add(atom, coefficient)

    result = {}

    i = 0

    while i < len(formula):
        symbol = formula[i]

        if symbol in "([{":
            parse_bracket(symbol)

        elif symbol.isalpha():
            # if i isn't the last
            if i < len(formula) - 1:
                next = formula[i + 1]

                if next.isalpha():
                    if next.isupper():
                        check_and_add(symbol)
                    elif next.islower():
                        symbol += next
                        i += 1
                        assert symbol in table, "Bad symbol!"
                        if i < len(formula) - 2:
                            next = formula[i + 1]
                            if next.isnumeric():
                                parse_number()
                            elif next.isalpha() or next in "([{":
                                check_and_add(symbol)
                        else:  # the last number
                            check_and_add(symbol)

                elif next.isnumeric():
                    parse_number()
                elif next in "([{":
                    check_and_add(symbol)
                    i += 1
                    parse_bracket(next)
            # the last symbol
            else:
                check_and_add(symbol)
                break
        i += 1

    return result


if __name__ == "__main__":
    print("K4[ON(SO3)2N5(OH)3]2", parse_molecule("K4[ON(SO3)2N5(OH)3]2"))
    print("Mg(OH)2:", parse_molecule("Mg(OH)2"))
    print("K4[ON(SO3)2]2: ", parse_molecule("K4[ON(SO3)2]2"))
    print("Ca2[SO4]2Mg3(HO)2: ", parse_molecule("Ca2[SO4]2Mg3(HO)2"))
