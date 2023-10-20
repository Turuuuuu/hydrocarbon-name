import csv
import re
from molecule import Molecule

molecules: list[Molecule] = []
prefixes: dict[int, str] = {}

def load_prefixes_from_file(filename: str):
    prefixes: dict[int, str] = {}

    with open(filename, 'r') as f:
        csvfile = csv.reader(f)

        for line in csvfile:
            # we trust the user to input real int and not some bullshit
            # i put so much trust on you
            prefixes[int(line[1])] = line[0]

    return prefixes

def parse_formula(formula: str):
    parsed_formula = re.findall(r'([A-Z][a-z]*)(\d*)', formula)
    compound: list[Molecule] = []

    for symbol, count in parsed_formula:
        compound.append(Molecule(symbol, int(count if count != '' else '1')))

    return compound

# perfect function name
def name_the_hydrocarbon(mixture: list[Molecule]) -> str:
    # lets trust user input again
    name = prefixes[mixture[0].count]
    hcount = mixture[0].count * 2

    # plz fix
    # dangerous code, don't touch.
    # it barely works
    if hcount + 1 == mixture[1].count and mixture[2] == Molecule('O', 1) and mixture[3] == Molecule('H', 1):
        name += 'anol'
    
    elif hcount + 2 == mixture[1].count:
        name += 'ane'
    elif hcount == mixture[1].count:
        name += 'ene'
    elif hcount - 2 == mixture[1].count:
        name += 'yne'

    else:
        print('Invalid')
        return
    
    return name

def main():
    while True:
        formula = input('Input hydrocarbon compound: ')
        parsed = parse_formula(formula)

        name = name_the_hydrocarbon(parsed)
        print(name)
        print()

if __name__ == '__main__':
    prefixes = load_prefixes_from_file('prefixes.csv')

    main()
