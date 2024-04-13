# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
def sort_array(lst):
    sorted_odds = sorted([n for n in lst if n % 2])
    new_list = []
    for i, n in enumerate(lst):
        if n % 2:
            new_list.append(sorted_odds.pop(0))
        else:
            new_list.append(n)
    return list(new_list)
