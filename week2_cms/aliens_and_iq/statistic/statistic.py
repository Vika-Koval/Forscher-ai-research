# My code:
import time
from memory_profiler import memory_usage
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

start = time.time()
rescue_people(read_file('smart_people.txt'),5)
end = time.time()
print((end - start)*(1000000))   
def rescue_people_with_memory_usage():
    return rescue_people(read_file('smart_people.txt'), 5)
mem_usage = memory_usage(rescue_people_with_memory_usage)
print("Maximum memory usage (in MiB):", max(mem_usage))   
# Time returned: 558.6147308349609
# Memory_profiler returned: Maximum memory usage (in MiB): 42.58984375

# Chat QPT's code:
import time
from memory_profiler import memory_usage
'''The module'''
def read_file(file_path):
    '''
    str->dict
    The function takes the path to the corresponding file 
    and returns a dictionary.
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        return {line.split(',')[0]: int(line.split(',')[1].strip()) for line in file if len(line.split(',')) == 2}

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

start = time.time()
rescue_people(read_file('smart_people.txt'),5)
end = time.time()
print((end - start)*(1000000)) 
def rescue_people_with_memory_usage():
    return rescue_people(read_file('smart_people.txt'), 5)
mem_usage = memory_usage(rescue_people_with_memory_usage)
print("Maximum memory usage (in MiB):", max(mem_usage))   
# Time returned: 52.45208740234375
# Memory_profiler returned: Maximum memory usage (in MiB): 43.31640625

# Blackbox's code:
'''The module'''
import time
from collections import OrderedDict
from memory_profiler import memory_usage
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

start = time.time()
rescue_people(read_file('smart_people.txt'),5)
end = time.time()
print((end - start)*(1000000))    
def rescue_people_with_memory_usage():
    return rescue_people(read_file('smart_people.txt'), 5)
mem_usage = memory_usage(rescue_people_with_memory_usage)
print("Maximum memory usage (in MiB):", max(mem_usage))   
# Time returned: 100.13580322265625
# Memory_profiler returned: Maximum memory usage (in MiB): 42.83984375
