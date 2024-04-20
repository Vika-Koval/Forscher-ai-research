#My code:
"""
This module consists of functions for calculation.
"""
def find_max_1(f:callable, points:list)->float:
    """ 
    (function, list(number)) -> (number)
    
    Find and return maximal value of function f in points.
    
    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """
    return max((f(i) for i in points))

def find_max_2(f:callable, points:list)->list:
    """ 
    (function, list(number)) -> (number)
    
    Find and return list of points where function f has the maximal value.
    
    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    >>> find_max_2(lambda x: x ** 2 + x, [1, 6, 3, -1])
    [6]
    """
    return [i  for i in points if f(i) == max((f(i) for i in points))]

def compute_limit(seq:callable)->float:
    """
    (function) -> (number)
    
    Compute and return limit of a convergent sequence.
    
    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.0
    >>> compute_limit(lambda n: (2*n ** 2 + n) / (4*n**2))
    0.5
    """
    results = []
    i = 0
    while True:
        mmm = 10 ** i
        results.append(seq(mmm))
        if i != 0 and abs(results[i] - results[i - 1]) < 0.001:
            return float(round(results[i], 2))
        i += 1

def compute_derivative(f:callable, x_0:float)->float:
    """
    (function, number) -> (number)
    
    Compute and return derivative of function f in the point x_0.
    
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    """
    d_x = 1
    alf = lambda x0: (f(x0 + d_x) - f(x0))/d_x
    mmm= alf(x_0) + 100
    while True:
        if abs(alf(x_0) - mmm) <= 0.001:
            break
        mmm = alf(x_0)
        d_x *= 0.1
    return round(alf(x_0), 2)


def get_tangent(f:callable, x_0:float)->str:
    """
    (function, number) -> (str)
    
    Compute and return tangent line to function f in the point x_0.
    
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'
    """
    a, b = compute_derivative(f, x_0), compute_derivative(f, x_0)*-(x_0) + f(x_0)
    symb1, symb2 = '', '+'
    if str(a)[0] == '-':
        symb1, a = '- ', (str(a))[1:]
    if str(b)[0] == '-':
        symb2, b = '-', (str(b))[1:]
    return f'{symb1}{a} * x {symb2} {b}'

def get_root(f:callable, a:float, b:float)->float:
    """
    (function, number, number) -> (number)
    
    Compute and return root of the function f in the interval (a, b).
    
    >>> get_root(lambda x: x, -1, 1)
    0.0
    >>> get_root(lambda x: x-2, -4, 6)
    2.0
    """
    eps = 0.001
    res = 0
    while abs(a - b) > eps:
        res = (a + b)/2
        if res == 0:
            break
        kof1 = f(a)
        kof2 = f(res)
        if kof1*kof2 < 0:
            b = res
        else:
            a = res
    return float(round(res,2))



#Request1:
#imrove this code

#Answer:
import functools
import math
import statistics
from typing import Callable, List


def find_max_1(f: Callable[[float], float], points: List[float]) -> float:
    """
    Find and return maximal value of function f in points.
    """
    return max(f(i) for i in points)

@functools.lru_cache(maxsize=None)
def find_max_2(f: Callable[[float], float], points: List[float]) -> List[float]:
    """
    Find and return list of points where function f has the maximal value.
    """
    max_val = find_max_1(f, points)
    return [i for i in points if math.isclose(f(i), max_val)]

def compute_limit(seq: Callable[[int], float]) -> float:
    """
    Compute and return limit of a convergent sequence.
    """
    results = []
    for i in range(1000):
        mmm = 10 ** i
        results.append(seq(mmm))
        if i != 0 and math.isclose(results[i], results[i - 1], rel_tol=0.001):
            return round(results[i], 2)
    return None
#ERROR HERE
#@functools.lru_cache(maxsize=None)
#def compute_derivative(f: Callable[[float]], x_0: float) -> float:
#    """
#    Compute and return derivative of function f in the point x_0.
#    """
#    d_x = 1
#    alf = lambda x0: (f(x0 + d_x) - f(x0)) / d_x
#    mmm = alf(x_0) + 100
#    while abs(alf(x_0) - mmm) > 0.001:
#        mmm = alf(x_0)
#        d_x *= 0.1
#    return round(alf(x_0), 2)

#def get_tangent(f: Callable[[float]], x_0: float) -> str:
#    """
#    Compute and return tangent line to function f in the point x_0.
#    """
#    a, b = compute_derivative(f, x_0), compute_derivative(f, x_0) * (-x_0) + f(x_0)
#    symb1, symb2 = '', '+'
#    if str(a)[0] == '-':
#        symb1, a = '- ', str(a)[1:]
#    if str(b)[0] == '-':
#        symb2, b = '-', str(b)[1:]
#    return f'{symb1}{a} * x {symb2} {b}'

#def get_root(f: Callable[[float]], a: float, b: float) -> float:
#    """
#    Compute and return root of the function f in the interval (a, b).
#    """
#    eps = 0.001
#    res = 0
#    while abs(a - b) > eps:
#        res = (a + b) / 2
#        if res == 0:
#            break
#        if math.isclose(f(res), 0, rel_tol=0.001):
#            break
#        kof1 = f(a)
#        kof2 = f(res)
#        if kof1 * kof2 < 0:
#            b = res
#        else:
#            a = res
#    return round(res, 2)

## this code has an ERROR in typecinting, but after fixing it, the code is working, except of second function


#Request2:
#there is a problemfind max 2: in unhashable type: 'list'
def find_max_2(f, points: List[float]) -> List[float]:
    """
    Find and return list of points where function f has the maximal value.
    """
    max_val = find_max_1(f, points)
    max_points = {(f(p), p): p for p in points}
    return [point for val, point in max_points.items() if val == max_val]
#nothing changed


#Request3:
#Failed example: find_max_2(lambda x: x ** 2 + x, [1, 6, 3, -1]) Expected: [6] Got: []
def find_max_2(f, points: List[float]) -> List[float]:
    """
    Find and return list of points where function f has the maximal value.
    """
    max_val = find_max_1(f, points)
    max_points = [p for p in points if f(p) == max_val]
    return max_points
#The code is finally working, but we have to fix the pylint


#Request4:
#Fix pylint for this code

#FINAL CODE:
import functools
import math
from typing import Callable, List


def find_max_1(f: Callable[[float], float], points: List[float]) -> float:
    """
    Find and return maximal value of function f in points.
    """
    return max(f(point) for point in points)

def find_max_2(f: Callable[[float], float], points: List[float]) -> List[float]:
    """
    Find and return list of points where function f has the maximal value.
    """
    max_val = find_max_1(f, points)
    max_points = [point for point in points if f(point) == max_val]
    return max_points

def compute_limit(seq: Callable[[int], float]) -> float:
    """
    Compute and return limit of a convergent sequence.
    """
    results = []
    for i in range(1000):
        mmm = 10 ** i
        results.append(seq(mmm))
        if i != 0 and math.isclose(results[i], results[i - 1], rel_tol=0.001):
            return round(results[i], 2)
    return None

@functools.lru_cache(maxsize=None)
def compute_derivative(f: Callable[[float], float], x_0: float) -> float:
    """
    Compute and return derivative of function f in the point x_0.
    """
    d_x = 1
    alf = lambda x0: (f(x0 + d_x) - f(x0)) / d_x
    mmm = alf(x_0) + 100
    while abs(alf(x_0) - mmm) > 0.001:
        mmm = alf(x_0)
        d_x *= 0.1
    return round(alf(x_0), 2)

def get_tangent(f: Callable[[float], float], x_0: float) -> str:
    """
    Compute and return tangent line to function f in the point x_0.
    """
    a = compute_derivative(f, x_0)
    b = a * (-x_0) + f(x_0)
    symb1, symb2 = '', '+'
    if a < 0:
        symb1 = '-'
        a = -a
    return f'{symb1}{a} * x {symb2} {b}'

def get_root(f: Callable[[float], float], a: float, b: float) -> float:
    """
    Compute and return root of the function f in the interval (a, b).
    """
    eps = 0.001
    res = (a + b) / 2
    while abs(a - b) > eps:
        if res == 0:
            break
        if math.isclose(f(res), 0, rel_tol=0.001):
            break
        kof1 = f(a)
        kof2 = f(res)
        if kof1 * kof2 < 0:
            b = res
        else:
            a = res
        res = (a + b) / 2
    return round(res, 2)

#Blckbox managed to change the code with no problems, however it needed to use a lot of libraries\
# and there were some errors due to typehints, also the pylint was not fixed as expected.
