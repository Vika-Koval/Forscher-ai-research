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

# Blackbox's answer:
'''The module'''
def read_file(file_path):
    '''
    str->dict
    The function takes the path to the corresponding file 
    and returns a dictionary.
    '''
    with open(file_path,'r',encoding='utf-8') as en:
        smarties = {line.strip().split(',')[0]: int(line.strip().split(',')[1]) for line in en if len(line.strip().split(',')) == 2}
    return smarties

def rescue_people(smarties, limit_iq):
    '''
    (dict,int)->tuple
    The function returns a tuple of the number of required trips and a list of lists,
    where each inner list represents a trip and contains the names of the people 
    transported on that trip in the order in which they were chosen by the aliens.
    >>> rescue_people({"Albert Einstein": 160, "Sir Isaac Newton": 195, "Nikola Tesla": 189},500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein']])
    '''
    if not smarties:
        return 0, []
    for name, iq in list(smarties.items()):
        if iq < 130:
            del smarties[name]
    smarties = dict(sorted(smarties.items(), key=lambda x: x[1], reverse=True))
    trips = []
    while smarties:
        people_on_trip = []
        current_iq = 0
        for name, iq in smarties.items():
            if current_iq + iq <= limit_iq:
                people_on_trip.append(name)
                current_iq += iq
                del smarties[name]
                if not smarties:
                    break
        trips.append(people_on_trip)
    return len(trips), trips
# This version was very bad, it passed just 3 tests and returned a RuntimeError,
# after Blackbox managed to fix it, KeyError occurred, so I decided to split the code into parts,
# starting with rescue_people function, because read_file was already optimized 

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

# Blackbox's answer:
limit_iq1 = limit_iq
lst1 = []
lst2 = []
smarties = {k: v for k, v in smarties.items() if v >= 130}
smarties = dict(sorted(smarties.items(), key=lambda x: x[1], reverse=True))
aaa1 = max(smarties.values())
if limit_iq < aaa1:
    return 0, []
# This version still was very bad, so I decided to split this part of code also

# Request5:
# Okay, let's try this way, optimize this part of the code  
if len(smarties)==0:
    return 0,[]
for key, value in list(smarties.items()):
    if value<130:
        del smarties[key]

# Blackbox's answer:
smarties = {k: v for k, v in smarties.items() if v >= 130}
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

# Blackbox's answer:
smarties = dict(sorted(smarties.items(), key=lambda x: x[1], reverse=True))
aaa1 = smarties.get(list(smarties.keys())[0])
if limit_iq < aaa1:
    return 0, []
# This version still does not work for sorting by alphabet

# Request7:
# But this way you do not sort through the alphabet,
# for this example rescue_people({'pb':160,'pa':160},500) I need to have this (1, [['pa', 'pb']]), not this (1, [['pb', 'pa']])

# Blackbox's answer:
smarties = dict(sorted(smarties.items(), key=lambda x: (x[1], x[0])))
smarties = dict(sorted(smarties.items(), key=lambda x: x[1], reverse=True))
aaa1 = smarties.get(list(smarties.keys())[0])
if limit_iq < aaa1:
    return 0, []
# This one worked well, but optimized nothing, so after a lot of requests 
# Blackbox started to return me something like this:
# 000248654577665700000000000000000000000000000000000...0
# So I started a new chat and after some attempts 
# I managed to get something like this

# Request28:
#Works great but can you make the code smaller and more optimized

# Blackbox's answer:
from collections import OrderedDict
smarties = OrderedDict(sorted(smarties.items(), key=lambda x: (-x[1], x[0])))
aaa1 = max(smarties.values())
if limit_iq < aaa1:
    return 0, []

# Request29:
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

# Blackbox's answer:
lst2 = []
while smarties:
    lst1 = []
    for key, value in list(smarties.items()):
        if value <= limit_iq:
            lst1.append(key)
            limit_iq -= value
            smarties.pop(key)
            break
    else:
        break
    lst2.append(lst1)
return len(lst2), lst2

# This code returned (2, [['Sir Isaac Newton'], ['Nikola Tesla']]) for this input rescue_people({"Albert Einstein": 160, "Sir Isaac Newton": 195, "Nikola Tesla": 189},500),
# but it needed to be (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein']]).
# It took me a lot of requests to fix it 

# Request57:
# The issue you're encountering arises because you are modifying limit_iq within the loop,
# but not resetting it correctly back to its original value before the next trip.

# Blackbox's answer:
limit_iq1 = limit_iq
lst2 = []
while smarties:
    lst1 = []
    remaining_iq = limit_iq1  
    for key, value in list(smarties.items()):
        if value <= remaining_iq:
            lst1.append(key)
            remaining_iq -= value
            smarties.pop(key)
    if not lst1: 
        break
    lst2.append(lst1)
return len(lst2), lst2
# This optimization was good

#Finally, the whole optimized code, which passes all tests:
'''The module'''
from collections import OrderedDict
def read_file(file_path):
    '''
    str->dict
    The function takes the path to the corresponding file 
    and returns a dictionary.
    '''
    with open(file_path,'r',encoding='utf-8') as en:
        smarties = {line.strip().split(',')[0]: int(line.strip().split(',')[1]) for line in en if len(line.strip().split(',')) == 2}
    return smarties
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
    smarties = {k: v for k, v in smarties.items() if v >= 130}
    if not smarties:
        return 0, []
    smarties = OrderedDict(sorted(smarties.items(), key=lambda x: (-x[1], x[0])))
    aaa1 = max(smarties.values())
    if limit_iq < aaa1:
        return 0, []
    while smarties:
        lst1 = []
        remaining_iq = limit_iq1  
        for key, value in list(smarties.items()):
            if value <= remaining_iq:
                lst1.append(key)
                remaining_iq -= value
                smarties.pop(key)
        if not lst1: 
            break
        lst2.append(lst1)
    return len(lst2), lst2



