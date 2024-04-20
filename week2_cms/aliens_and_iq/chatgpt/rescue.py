# Problem:https://cms.ucu.edu.ua/mod/vpl/forms/submissionview.php?id=306723&userid=9849
# My version of the code
'''The module'''
def read_file(file_path):
    '''
    str->dict
    The function takes the path to the corresponding file 
    and returns a dictionary.
    '''
    with open(file_path,'r',encoding='utf-8') as en:
        a=[]
        c=[]
        d={}
        for line in en:
            a.append(line)
        for item in a:
            b=item.split(',')
            if len(b)==2:
                b[1]=b[1].replace('\n', '')
                b[1]=int(b[1])
                c.append(b)
        for i in c:
            x={i[0]:i[1]}
            d.update(x)
    return d

def rescue_people(smarties, limit_iq):
    '''
    (dict,int)->tuple
    The function returns a tuple of the number of required trips and a list of lists,
    where each inner list represents a trip and contains the names of the people 
    transported on that trip in the order in which they were chosen by the aliens.
    >>> rescue_people({"Albert Einstein": 160, "Sir Isaac Newton": 195, "Nikola Tesla": 189},500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein']])
    '''
    limit_iq1=limit_iq
    lst1=[]
    lst2=[]
    if len(smarties)==0:
        return 0,[]
    for key, value in list(smarties.items()):
        if value<130:
            del smarties[key]
    smarties=dict(sorted(smarties.items()))
    smarties=dict(sorted(smarties.items(), key=lambda x: x[1], reverse=True))
    aaa1=max(smarties.values())
    if limit_iq<aaa1:
        return 0,[]
    while True:
        lst1=[]
        for key, value in list(smarties.items()):
            if value<=limit_iq:
                lst1.append(key)
                limit_iq=limit_iq-value
                del smarties[key]
        limit_iq=limit_iq1
        lst2.append(lst1)
        if len(smarties)==0:
            break
    count=len(lst2)
    return count,lst2
  
# Request1:
# Hello, I need to optimize this code but don't change its functionality

# GPT's answer:
def read_file(file_path):
    '''
    str -> dict
    Read the file at file_path and return a dictionary.
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        return {line.split(',')[0]: int(line.split(',')[1].strip()) for line in file if len(line.split(',')) == 2}
def rescue_people(smarties, limit_iq):
    '''
    (dict, int) -> tuple
    Returns the number of required trips and a list of lists representing each trip.
    '''
    trips = []
    remaining_iq = limit_iq
    if not smarties:
        return 0, trips
    smarties = {name: iq for name, iq in smarties.items() if iq >= 130}
    if not smarties:
        return 0, trips
    sorted_smarties = sorted(smarties.items(), key=lambda x: x[1], reverse=True)
    while sorted_smarties:
        trip = []
        for name, iq in sorted_smarties[:]:
            if iq <= remaining_iq:
                trip.append(name)
                remaining_iq -= iq
                sorted_smarties.remove((name, iq))
        trips.append(trip)
        remaining_iq = limit_iq
    return len(trips), trips
# This version was very good, but the last 5 tests were failing because chat GPT did not sort the dictionary by alphabet

# Request2:
# Please, change this version of the code so that sorted smarties will be also sorted by alphabet

# GPT's answer:
def read_file(file_path):
    '''
    str -> dict
    Read the file at file_path and return a dictionary.
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        return {line.split(',')[0]: int(line.split(',')[1].strip()) for line in file if len(line.split(',')) == 2}

def rescue_people(smarties, limit_iq):
    '''
    (dict, int) -> tuple
    Returns the number of required trips and a list of lists representing each trip.
    '''
    trips = []
    remaining_iq = limit_iq
    if not smarties:
        return 0, trips
    smarties = {name: iq for name, iq in smarties.items() if iq >= 130}
    if not smarties:
        return 0, trips
    sorted_smarties = sorted(smarties.items(), key=lambda x: (x[1], x[0]), reverse=True)
    while sorted_smarties:
        trip = []
        for name, iq in sorted_smarties[:]:
            if iq <= remaining_iq:
                trip.append(name)
                remaining_iq -= iq
                sorted_smarties.remove((name, iq))
        trips.append(trip)
        remaining_iq = limit_iq
    return len(trips), trips
# This version was completely broken and passed none of the tests, so I decided to split the code into parts,
# starting with rescue_people function, because read_file was already optimized 

# Request3:
# Now optimize just rescue_people function without changing the main concept

# GPT's answer:
def rescue_people(smarties, limit_iq):
    '''
    (dict, int) -> tuple
    Returns the number of required trips and a list of lists representing each trip.
    '''
    limit_iq1 = limit_iq
    trips = []
    smarties = {name: iq for name, iq in smarties.items() if iq >= 130}
    sorted_smarties = sorted(smarties.items(), key=lambda x: x[1], reverse=True)
    if not sorted_smarties:
        return 0, trips
    max_iq = max(smarties.values())
    if limit_iq < max_iq:
        return 0, trips
    while sorted_smarties:
        trip = []
        for name, iq in sorted_smarties[:]:
            if iq <= limit_iq:
                trip.append(name)
                limit_iq -= iq
                sorted_smarties.remove((name, iq))
        trips.append(trip)
        limit_iq = limit_iq1
    return len(trips), trips
# The code was changed but it still did not pass the last 5 tests, so I decided to split the function into parts

# Request4:
# Okay, then optimize just this part
  limit_iq1=limit_iq
  lst1=[]
  lst2=[]
  if len(smarties)==0:
      return 0,[]
  for key, value in list(smarties.items()):
      if value<130:
          del smarties[key]
  smarties=dict(sorted(smarties.items()))
  smarties=dict(sorted(smarties.items(), key=lambda x: x[1], reverse=True))
  aaa1=max(smarties.values())

# GPT's answer:
limit_iq1 = limit_iq
lst1 = []
lst2 = []
if not smarties or max(smarties.values()) > limit_iq:
    return 0, []
smarties = {name: iq for name, iq in smarties.items() if iq >= 130}
sorted_smarties = sorted(smarties.items(), key=lambda x: x[1], reverse=True)
# This version was completely broken and passed none of the tests, so I decided to split the code even more

# Request5:
# Okay, let's try this way, optimize this part of the code  
if len(smarties)==0:
    return 0,[]
for key, value in list(smarties.items()):
    if value<130:
        del smarties[key]

# GPT's answer:
smarties = {name: iq for name, iq in smarties.items() if iq >= 130}
if not smarties:
    return 0, []
# This optimization was good

# Request6:
# Now optimize this part:
smarties=dict(sorted(smarties.items()))
smarties=dict(sorted(smarties.items(), key=lambda x: x[1], reverse=True))
aaa1=max(smarties.values())
if limit_iq<aaa1:
    return 0,[]

# GPT's answer:
sorted_smarties = sorted(smarties.items(), key=lambda x: x[1], reverse=True)
if sorted_smarties and sorted_smarties[0][1] > limit_iq:
    return 0, []
# GPT decided to change the dictionary with a list

# Request7:
# But smarties need to still be a dictionary

# GPT's answer:
sorted_smarties = dict(sorted(smarties.items(), key=lambda x: x[1], reverse=True))
if sorted_smarties and next(iter(sorted_smarties.values())) > limit_iq:
    return 0, []
# This version still does not work for sorting by alphabet

# Request8:
# But this way you do not sort through the alphabet,
# for this example rescue_people({'pb':160,'pa':160},500) I need to have this (1, [['pa', 'pb']]), not this (1, [['pb', 'pa']])

# GPT's answer:
sorted_smarties = dict(sorted(smarties.items(), key=lambda x: (-x[1], x[0])))
if sorted_smarties and next(iter(sorted_smarties.values())) > limit_iq:
    return 0, []
# This optimization was good

# Request9:
# And now optimize this one:
while True:
    lst1=[]
    for key, value in list(smarties.items()):
        if value<=limit_iq:
            lst1.append(key)
            limit_iq=limit_iq-value
            del smarties[key]
    limit_iq=limit_iq1
    lst2.append(lst1)
    if len(smarties)==0:
        break
count=len(lst2)
return count,lst2

# GPT's answer:
lst2 = []
while smarties:
    lst1 = [key for key, value in smarties.items() if value <= limit_iq]
    lst2.append(lst1)
    smarties = {key: value for key, value in smarties.items() if value > limit_iq}
count = len(lst2)
return count, lst2

# Request10:
#But now it appends to lst2 elements just one time, 
#but we need to append a list of passengers every time it becomes to be full,
#for example, rescue_people({"Albert Einstein": 160, "Sir Isaac Newton": 195, "Nikola Tesla": 189},500),
#this example should return this (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein']]),
#not this (1, [['Sir Isaac Newton', 'Nikola Tesla', 'Albert Einstein']])

# GPT's answer:
lst2 = []
while smarties:
    lst1 = []
    remaining_iq = limit_iq
    for key, value in smarties.items():
        if value <= remaining_iq:
            lst1.append(key)
            remaining_iq -= value
    lst2.append(lst1)
    smarties = {key: value for key, value in smarties.items() if key not in lst1}
count = len(lst2)
return count, lst2
# This optimization was good

#Finally, the whole optimized code, which passes all tests:
'''The module'''
def read_file(file_path):
    '''
    str->dict
    The function takes the path to the corresponding file 
    and returns a dictionary.
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        return {line.split(',')[0]: int(line.split(',')[1].\
strip()) for line in file if len(line.split(',')) == 2}
def rescue_people(smarties, limit_iq):
    '''
    (dict,int)->tuple
    The function returns a tuple of the number of required trips and a list of lists,
    where each inner list represents a trip and contains the names of the people 
    transported on that trip in the order in which they were chosen by the aliens.
    >>> rescue_people({"Albert Einstein": 160, "Sir Isaac Newton": 195, "Nikola Tesla": 189},500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein']])
    '''
    smarties = {name: iq for name, iq in smarties.items() if iq >= 130}
    if not smarties:
        return 0, []
    smarties = dict(sorted(smarties.items(), key=lambda x: (-x[1], x[0])))
    if smarties and next(iter(smarties.values())) > limit_iq:
        return 0, []
    lst2 = []
    while smarties:
        lst1 = []
        remaining_iq = limit_iq
        for key, value in smarties.items():
            if value <= remaining_iq:
                lst1.append(key)
                remaining_iq -= value
        lst2.append(lst1)
        smarties = {key: value for key, value in smarties.items() if key not in lst1}
    count = len(lst2)
    return count, lst2











