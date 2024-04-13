# Problem: https://www.codewars.com/kata/52f831fa9d332c6591000511/train/python

# Request1:
# help me please with this task in Python:
# For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object 

# Blackbox's answer:
def parse_molecule(formula):
    elements = {}
    i = 0
    while i < len(formula):
        if formula[i].islower():
            i += 1
            continue
        element = formula[i]
        count = 1
        i += 1
        while i < len(formula) and formula[i].isdigit():
            count = count * 10 + int(formula[i])
            i += 1
        elements[element] = elements.get(element, 0) + count
    return elements

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

# Blackbox's answer:
def parse_molecule(formula):
    elements = {}
    i = 0
    while i < len(formula):
        if formula[i] == '(':
            j = i + 1
            level = 1
            while level > 0:
                if formula[j] == '(':
                    level += 1
                elif formula[j] == ')':
                    level -= 1
                j += 1
            subformula = formula[i+1:j-1]
            index = 1
            if j < len(formula) and formula[j].isdigit():
                index = int(formula[j])
                j += 1
            subelements = parse_molecule(subformula)
            for element in subelements:
                elements[element] = elements.get(element, 0) + subelements[element] * index
            i = j
        elif formula[i].islower():
            i += 1
            continue
        else:
            element = formula[i]
            count = 1
            i += 1
            while i < len(formula) and formula[i].isdigit():
                count = count * 10 + int(formula[i])
                i += 1
            elements[element] = elements.get(element, 0) + count
    return elements

# Request3:
# It is great but you count H like 12 in ("H2O") example should equal {'H': 2, 'O': 1} because of index 2 near h and no index near o


# Blackbox's answer:
import re
from collections import Counter
def parse_molecule(formula):
    elements = Counter()
    i = 0
    while i < len(formula):
        if formula[i] == '(':
            j = i + 1
            level = 1
            while level > 0:
                if formula[j] == '(':
                    level += 1
                elif formula[j] == ')':
                    level -= 1
                j += 1
            subformula = formula[i+1:j-1]
            index = 1
            if j < len(formula) and formula[j].isdigit():
                index = int(re.search(r'\d+', formula[j:]).group())
                j += len(str(index))
            subelements = parse_molecule(subformula)
            for element, count in subelements.items():
                elements[element] += count * index
            i = j
        else:
            match = re.search(r'([A-Z][a-z]*)(\d*)', formula[i:])
            element, index = match.groups()
            if index:
                index = int(index)
            else:
                index = 1
            elements[element] += index
            i += match.end()
    return elements

# This code passed 2/3 tests but in 3 test error: AttributeError: 'NoneType' object has no attribute 'groups' occurred 
# and without a clear explanation of this error Blackbox could not deal with that, so after a long time of struggling 
# I made this request

# Request27:
# Your code worked great but had an error because of this line: element, index = match.groups() 
# maybe try branch: 
if match: 
  element, index = match.groups()

# Blackbox's answer:
import re
from collections import Counter
def parse_molecule(formula):
    elements = Counter()
    i = 0
    while i < len(formula):
        if formula[i] == '(':
            j = i + 1
            level = 1
            while level > 0:
                if formula[j] == '(':
                    level += 1
                elif formula[j] == ')':
                    level -= 1
                j += 1
            subformula = formula[i+1:j-1]
            index = 1
            if j < len(formula) and formula[j].isdigit():
                index = int(re.search(r'\d+', formula[j:]).group()
                j += len(str(index))
            subelements = parse_molecule(subformula)
            for element, count in subelements.items():
                elements[element] += count * index
            i = j
        else:
            match = re.search(r'([A-Z][a-z]*)(\d*)', formula[i:])
            if match:
                element, index = match.groups()
                if index:
                    index = int(index)
                else:
                    index = 1
                elements[element] += index
                i += match.end()
            else:
                element = formula[i]
                if element.isupper():
                    elements[element] += 1
                else:
                    index = int(element)
                    i += 1
                    while i < len(formula) and formula[i].isdigit():
                        index = index * 10 + int(formula[i])
                        i += 1
                    i -= 1
                    for element, count in elements.items():
                        elements[element] += count * index
                    i += 1
    return elements

# Request28:
# I guess you do not count these parents [], so now it occurs this error:
# ValueError: invalid literal for int() with base 10: ']'

# Blackbox's answer:
import re
from collections import Counter
def parse_molecule(formula):
    elements = Counter()
    i = 0
    while i < len(formula):
        if formula[i] == '(':
            j = i + 1
            level = 1
            while level > 0:
                if formula[j] == '(':
                    level += 1
                elif formula[j] == ')':
                    level -= 1
                j += 1
            subformula = formula[i+1:j-1]
            index = 1
            if j < len(formula) and formula[j].isdigit():
                index = int(re.search(r'\d+', formula[j:]).group())
                j += len(str(index))
            subelements = parse_molecule(subformula)
            for element, count in subelements.items():
                elements[element] += count * index
            i = j
        else:
            match = re.search(r'([A-Z][a-z]*)(\d*)?', formula[i:])
            if match:
                element, index = match.groups()
                if index:
                    index = int(index)
                else:
                    index = 1
                elements[element] += index
                i += match.end()
            else:
                element = formula[i]
                if element.isupper():
                    elements[element] += 1
                else:
                    index = int(element)
                    i += 1
                    while i < len(formula) and formula[i].isdigit():
                        index = index * 10 + int(formula[i])
                        i += 1
                    i -= 1
                    for element, count in elements.items():
                        elements[element] += count * index
                    i += 1
    return elements

# Request29:
# It seems like the code has a logic error when it encounters a closing square bracket ]. 
# Instead of handling it properly, the code attempts to convert it into an integer directly, which causes the ValueError.

# Blackbox's answer:
import re
from collections import Counter
def parse_molecule(formula):
    elements = Counter()
    i = 0
    while i < len(formula):
        if formula[i] == '(':
            j = i + 1
            level = 1
            while level > 0:
                if formula[j] == '(':
                    level += 1
                elif formula[j] == ')':
                    level -= 1
                j += 1
            subformula = formula[i+1:j-1]
            index = 1
            if j < len(formula) and formula[j].isdigit():
                index = int(re.search(r'\d+', formula[j:]).group())
                j += len(str(index))
            subelements = parse_molecule(subformula)
            for element, count in subelements.items():
                elements[element] += count * index
            i = j
        else:
            match = re.search(r'([A-Z][a-z]*)(\d*)?', formula[i:])
            if match:
                element, index = match.groups()
                if index:
                    index = int(index)
                else:
                    index = 1
                elements[element] += index
                i += match.end()
            else:
                element = formula[i]
                if element.isupper():
                    elements[element] += 1
                else:
                    index = 1
                    while i + 1 < len(formula) and formula[i+1].isdigit():
                        index = index * 10 + int(formula[i+1])
                        i += 1
                    elements[element] += index
                    i += 1
    return elements

# It fixed the ValueError but the code still gave this output: Counter({']': 12, 'O': 7, 'K': 4, 'S': 2, 'N': 1}) 
# instead of {'K': 4, 'O': 14, 'N': 2, 'S': 4} so I helped Blackbox with making code

# Request30:
# You do not get me we need an indented block for these patterns [] which will start like this:
elif formula[i] == '[':

# Blackbox's answer:
import re
from collections import Counter
def parse_molecule(formula):
    elements = Counter()
    i = 0
    while i < len(formula):
        if formula[i] == '(':
            j = i + 1
            level = 1
            while level > 0:
                if formula[j] == '(':
                    level += 1
                elif formula[j] == ')':
                    level -= 1
                j += 1
            subformula = formula[i+1:j-1]
            index = 1
            if j < len(formula) and formula[j].isdigit():
                index = int(re.search(r'\d+', formula[j:]).group())
                j += len(str(index))
            subelements = parse_molecule(subformula)
            for element, count in subelements.items():
                elements[element] += count * index
            i = j
        elif formula[i] == '[':
            j = i + 1
            level = 1
            while level > 0:
                if formula[j] == '[':
                    level += 1
                elif formula[j] == ']':
                    level -= 1
                j += 1
            subformula = formula[i+1:j-1]
            index = 1
            if j < len(formula) and formula[j].isdigit():
                index = int(re.search(r'\d+', formula[j:]).group())
                j += len(str(index))
            subelements = parse_molecule(subformula)
            for element, count in subelements.items():
                elements[element] += count * index
            i = j
        else:
            match = re.search(r'([A-Z][a-z]*)(\d*)?', formula[i:])
            if match:
                element, index = match.groups()
                if index:
                    index = int(index)
                else:
                    index = 1
                elements[element] += index
                i += match.end()
            else:
                element = formula[i]
                if element.isupper():
                    elements[element] += 1
                else:
                    index = 1
                    while i + 1 < len(formula) and formula[i+1].isdigit():
                        index = index * 10 + int(formula[i+1])
                        i += 1
                    elements[element] += index
                    i += 1
    return elements

# Request31:
# Good job and do it also for these parents {}

# Blackbox's answer:
import re
from collections import Counter
def parse_molecule(formula):
    elements = Counter()
    i = 0
    while i < len(formula):
        if formula[i] == '(':
            j = i + 1
            level = 1
            while level > 0:
                if formula[j] == '(':
                    level += 1
                elif formula[j] == ')':
                    level -= 1
                j += 1
            subformula = formula[i+1:j-1]
            index = 1
            if j < len(formula) and formula[j].isdigit():
                index = int(re.search(r'\d+', formula[j:]).group())
                j += len(str(index))
            subelements = parse_molecule(subformula)
            for element, count in subelements.items():
                elements[element] += count * index
            i = j
        elif formula[i] == '[':
            j = i + 1
            level = 1
            while level > 0:
                if formula[j] == '[':
                    level += 1
                elif formula[j] == ']':
                    level -= 1
                j += 1
            subformula = formula[i+1:j-1]
            index = 1
            if j < len(formula) and formula[j].isdigit():
                index = int(re.search(r'\d+', formula[j:]).group())
                j += len(str(index))
            subelements = parse_molecule(subformula)
            for element, count in subelements.items():
                elements[element] += count * index
            i = j
        elif formula[i] == '{':
            j = i + 1
            level = 1
            while level > 0:
                if formula[j] == '{':
                    level += 1
                elif formula[j] == '}':
                    level -= 1
                j += 1
            subformula = formula[i+1:j-1]
            index = 1
            if j < len(formula) and formula[j].isdigit():
                index = int(re.search(r'\d+', formula[j:]).group())
                j += len(str(index))
            subelements = parse_molecule(subformula)
            for element, count in subelements.items():
                elements[element] += count * index
            i = j
        else:
            match = re.search(r'([A-Z][a-z]*)(\d*)?', formula[i:])
            if match:
                element, index = match.groups()
                if index:
                    index = int(index)
                else:
                    index = 1
                elements[element] += index
                i += match.end()
            else:
                element = formula[i]
                if element.isupper():
                    elements[element] += 1
                else:
                    index = 1
                    while i + 1 < len(formula) and formula[i+1].isdigit():
                        index = index * 10 + int(formula[i+1])
                        i += 1
                    elements[element] += index
                    i += 1
    return elements

# This one is finally correct, BlackBox managed to count all types of parents after my help with its code,
# and managed to deal with all errors after my clear explanation of each of them 
# and finally made this problem resolved 
