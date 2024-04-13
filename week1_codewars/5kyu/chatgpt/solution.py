# Problem: https://www.codewars.com/kata/52f831fa9d332c6591000511/train/python

# Request1:
# help me please with this task in Python:
# For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object 

# GPT's answer:
import re
def parse_molecule (formula):
    def parse_formula(formula):
        pattern = r'([A-Z][a-z]*)(\d*)'
        atoms = {}
        for element, count in re.findall(pattern, formula):
            count = int(count) if count else 1
            atoms[element] = atoms.get(element, 0) + count
        return atoms
    atoms_count = parse_formula(formula)
    return atoms_count

# Request2:
# Here are some examples for a better understanding:
# water = 'H2O'
# parse_molecule(water)                 # return {H: 2, O: 1}

# magnesium_hydroxide = 'Mg(OH)2'
# parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

# var fremy_salt = 'K4[ON(SO3)2]2'
# parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}
# As you can see, some formulas have brackets in them. 
# The index outside the brackets tells you that you have to multiply count of each atom inside the bracket on this index. 
# For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms and six oxygen atoms.

# GPT's answer:
import re
def parse_molecule (formula):
    def parse_formula(formula, multiplier=1):
        pattern = r'([A-Z][a-z]*)(\d*)|(\[.*?\])(\d*)'
        atoms = {}
        for element, count, group, group_count in re.findall(pattern, formula):
            if element:
                count = int(count) if count else 1
                atoms[element] = atoms.get(element, 0) + count * multiplier
            elif group:
                group_atoms = parse_formula(group[1:-1], multiplier=int(group_count) if group_count else 1)
                for atom, count in group_atoms.items():
                    atoms[atom] = atoms.get(atom, 0) + count
        return atoms  
    atoms_count = parse_formula(formula)
    return atoms_count


# Request3:
# It is great but you do not count index before parents for example there  Mg(OH)2: 
# should equal {'Mg': 1, 'O': 2, 'H': 2}  O and H need to be 2 because of their index before parents

# GPT's answer:
import re
def parse_molecule (formula):
    def parse_formula(formula, multiplier=1):
        pattern = r'([A-Z][a-z]*)(\d*)|(\(.*?\))(\d*)'
        atoms = {}
        for element, count, group, group_count in re.findall(pattern, formula):
            if element:
                count = int(count) if count else 1
                atoms[element] = atoms.get(element, 0) + count * multiplier
            elif group:
                group_atoms = parse_formula(group[1:-1], multiplier=int(group_count) if group_count else 1)
                for atom, count in group_atoms.items():
                    atoms[atom] = atoms.get(atom, 0) + count * multiplier
        return atoms
    atoms_count = parse_formula(formula)
    return atoms_count

# Request4:
# Great but we also need to count the index before this kind of parents [] 
# so in this example K4[ON(SO3)2]2 should equal {'K': 4, 'O': 14, 'N': 2, 'S': 4}
# o is 14 because we multiply 3 by 2 after that append one o which is near on it begins to be 7 
# and after that we multiply it by 2 because of the index near [] this parents

# GPT's answer:
import re
def count_atoms(formula):
    def parse_formula(formula, multiplier=1):
        pattern = r'([A-Z][a-z]*)(\d*)|(\(.*?\))(\d*)|\[(.*?)\](\d*)'
        atoms = {}
        for element, count, group, group_count, square_group, square_count in re.findall(pattern, formula):
            if element:
                count = int(count) if count else 1
                atoms[element] = atoms.get(element, 0) + count * multiplier
            elif group:
                group_atoms = parse_formula(group[1:-1], multiplier=int(group_count) if group_count else 1)
                for atom, count in group_atoms.items():
                    atoms[atom] = atoms.get(atom, 0) + count * multiplier
            elif square_group:
                square_atoms = parse_formula(square_group, multiplier=int(square_count) if square_count else 1)
                for atom, count in square_atoms.items():
                    atoms[atom] = atoms.get(atom, 0) + count * multiplier
        return atoms
    atoms_count = parse_formula(formula)
    return atoms_count

# Request5:
# And also you need to count these parents {} 
# Should parse really weird molecule: As2{Be4C5[BCo3(CO2)3]2}4Cu5:
# you have this {'As': 2, 'Be': 4, 'C': 11, 'B': 2, 'Co': 6, 'O': 12, 'Cu': 5} 
# but should equal {'As': 2, 'Be': 16, 'C': 44, 'B': 8, 'Co': 24, 'O': 48, 'Cu': 5}

# GPT's answer:
import re
def count_atoms(formula):
    def parse_formula(formula, multiplier=1):
        pattern = r'([A-Z][a-z]*)(\d*)|(\(.*?\))(\d*)|\[(.*?)\](\d*)|\{(.*?)\}(\d*)'
        atoms = {}
        for element, count, group, group_count, square_group, square_count, curly_group, curly_count in re.findall(pattern, formula):
            if element:
                count = int(count) if count else 1
                atoms[element] = atoms.get(element, 0) + count * multiplier
            elif group:
                group_atoms = parse_formula(group[1:-1], multiplier=int(group_count) if group_count else 1)
                for atom, count in group_atoms.items():
                    atoms[atom] = atoms.get(atom, 0) + count * multiplier
            elif square_group:
                square_atoms = parse_formula(square_group, multiplier=int(square_count) if square_count else 1)
                for atom, count in square_atoms.items():
                    atoms[atom] = atoms.get(atom, 0) + count * multiplier
            elif curly_group:
                curly_atoms = parse_formula(curly_group, multiplier=int(curly_count) if curly_count else 1)
                for atom, count in curly_atoms.items():
                    atoms[atom] = atoms.get(atom, 0) + count * multiplier
        return atoms   
    atoms_count = parse_formula(formula)
    return atoms_count
  
  # This one is finally correct, GPT already managed to count all types of parents and made this problem resolved 
