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
from typing import Callable, List

def find_max_1(f: Callable, points: List[float]) -> float:
    """Find and return the maximal value of function f in points."""
    return max(f(point) for point in points)

def find_max_2(f: Callable, points: List[float]) -> List[float]:
    """Find and return a list of points where function f has the maximal value."""
    max_value = max(f(point) for point in points)
    return [point for point in points if f(point) == max_value]

def compute_limit(seq: Callable) -> float:
    """Compute and return the limit of a convergent sequence."""
    results = []
    i = 0
    while True:
        mmm = 10 ** i
        results.append(seq(mmm))
        if i != 0 and abs(results[i] - results[i - 1]) < 0.001:
            return round(results[i], 2)
        i += 1

def compute_derivative(f: Callable, x_0: float) -> float:
    """Compute and return the derivative of function f at point x_0."""
    dx = 1
    alpha = lambda x0: (f(x0 + dx) - f(x0)) / dx
    prev_alpha = alpha(x_0) + 100
    while True:
        if abs(alpha(x_0) - prev_alpha) <= 0.001:
            break
        prev_alpha = alpha(x_0)
        dx *= 0.1
    return round(alpha(x_0), 2)

def get_tangent(f: Callable, x_0: float) -> str:
    """Compute and return the tangent line to function f at point x_0."""
    a, b = compute_derivative(f, x_0), compute_derivative(f, x_0) * -x_0 + f(x_0)
    symb1, symb2 = ('', '+') if a >= 0 else ('- ', '-')
    return f'{symb1}{abs(a)} * x {symb2} {abs(b)}'

def get_root(f: Callable, a: float, b: float) -> float:
    """Compute and return the root of the function f in the interval (a, b)."""
    eps = 0.001
    res = 0
    while abs(a - b) > eps:
        res = (a + b) / 2
        if res == 0:
            break
        kof1 = f(a)
        kof2 = f(res)
        if kof1 * kof2 < 0:
            b = res
        else:
            a = res
    return round(res, 2)
#all of this code works, except for get_tangent

#Request2:
# get_tangent stopped working after your improvements
def get_tangent(f: Callable, x_0: float) -> str:
    """Compute and return the tangent line to function f at point x_0."""
    derivative_at_x0 = compute_derivative(f, x_0)
    constant_term = compute_derivative(f, x_0) * -x_0 + f(x_0)
    
    if derivative_at_x0 == 0:
        return str(f(x_0))
    
    # Construct the string representation of the tangent line equation
    slope_sign = '+' if derivative_at_x0 >= 0 else '-'
    derivative_abs = abs(derivative_at_x0)
    constant_abs = abs(constant_term)
    
    return f"{slope_sign} {derivative_abs} * x {slope_sign} {constant_abs}"
#still the same




#Request3:
#  get_tangent(lambda x: - x ** 2 + x, 2)
#Expected:
#    '- 3.0 * x + 4.0'
#Got:
#    '-3.0 * x 4.0'
def get_tangent(f: callable, x_0: float) -> str:
    """
    Compute and return the tangent line to function f at point x_0.
    """
    # Calculate the derivative and the value of the function at x_0
    derivative_at_x0 = compute_derivative(f, x_0)
    y_0 = f(x_0)
    
    # Calculate the slope and y-intercept of the tangent line
    slope = round(derivative_at_x0, 2)
    y_intercept = round(y_0 - derivative_at_x0 * x_0, 2)
    
    # Construct the string representation of the tangent line equation
    if slope == 0:
        return str(y_intercept)
    elif slope == 1:
        slope_str = ""
    else:
        slope_str = str(slope)
    y_intercept_str = f" {y_intercept}" if y_intercept >= 0 else f" - {abs(y_intercept)}"
    
    return f"{slope_str} * x{y_intercept_str}"
#chat gpt realied the problem is extra space in string, but the fixing did not help




#Request4:
#expected:
#    '5.0 * x - 4.0'
#Got:
#    '5.0 * x  - 4.0'
#Answer:
def get_tangent(f: callable, x_0: float) -> str:
    """
    Compute and return the tangent line to function f at point x_0.
    """
    # Calculate the derivative and the value of the function at x_0
    derivative_at_x0 = compute_derivative(f, x_0)
    y_0 = f(x_0)
    
    # Calculate the slope and y-intercept of the tangent line
    slope = round(derivative_at_x0, 2)
    y_intercept = round(y_0 - derivative_at_x0 * x_0, 2)
    
    # Construct the string representation of the tangent line equation
    if slope == 0:
        return str(y_intercept)
    elif slope == 1:
        slope_str = ""
    else:
        slope_str = str(slope)
        
    # Handle negative slope and y-intercept properly
    if slope_str.startswith("-"):
        slope_str = "- " + slope_str[1:]
    if y_intercept < 0:
        y_intercept_str = f" - {abs(y_intercept)}"
    else:
        y_intercept_str = f" + {y_intercept}"
    
    return f"{slope_str} * x {y_intercept_str}"
# The code is finally working, however there are some problems with pylint


#Request5:
# fix pylint and style



#FINAL CODE:

"""
This module consists of functions for calculus operations.
"""

from typing import Callable, List


def find_max_1(f: Callable, points: List[float]) -> float:
    """Find and return the maximal value of function f in points."""
    return max(f(point) for point in points)


def find_max_2(f: Callable, points: List[float]) -> List[float]:
    """Find and return a list of points where function f has the maximal value."""
    max_value = max(f(point) for point in points)
    return [point for point in points if f(point) == max_value]


def compute_limit(seq: Callable) -> float:
    """Compute and return the limit of a convergent sequence."""
    results = []
    i = 0
    while True:
        mmm = 10 ** i
        results.append(seq(mmm))
        if i != 0 and abs(results[i] - results[i - 1]) < 0.001:
            return round(results[i], 2)
        i += 1


def compute_derivative(f: Callable, x_0: float) -> float:
    """Compute and return the derivative of function f at point x_0."""
    dx = 1
    def alpha(x0):
        return (f(x0 + dx) - f(x0)) / dx
    prev_alpha = alpha(x_0) + 100
    while True:
        if abs(alpha(x_0) - prev_alpha) <= 0.001:
            break
        prev_alpha = alpha(x_0)
        dx *= 0.1
    return round(alpha(x_0), 2)


def get_tangent(f: Callable, x_0: float) -> str:
    """
    Compute and return the tangent line to function f at point x_0.
    """
    # Calculate the derivative and the value of the function at x_0
    derivative_at_x0 = compute_derivative(f, x_0)
    y_0 = f(x_0)
    # Calculate the slope and y-intercept of the tangent line
    slope = round(derivative_at_x0, 2)
    y_intercept = round(y_0 - derivative_at_x0 * x_0, 2)
    # Construct the string representation of the tangent line equation
    if slope == 0:
        return str(y_intercept)
    if slope == 1:
        slope_str = ""
    else:
        slope_str = str(slope)
    # Handle negative slope and y-intercept properly
    if slope_str.startswith("-"):
        slope_str = "- " + slope_str[1:]
    if y_intercept < 0:
        y_intercept_str = f" - {abs(y_intercept)}"
    else:
        y_intercept_str = f" + {y_intercept}" if slope_str else f"{y_intercept}"
    return f"{slope_str} * x{y_intercept_str}"


def get_root(f: Callable, a: float, b: float) -> float:
    """Compute and return the root of the function f in the interval (a, b)."""
    eps = 0.001
    res = 0
    while abs(a - b) > eps:
        res = (a + b) / 2
        if res == 0:
            break
        kof1 = f(a)
        kof2 = f(res)
        if kof1 * kof2 < 0:
            b = res
        else:
            a = res
    return round(res, 2)

#chat gpt can change code for tasks like calculus pretty quick, but is not really good in improving the code,
#since the functions either became more comlicated or didn't change
