import itertools

def find_missing(lst):
    return sorted(set(range(lst[0], lst[-1])) - set(lst))

lst = [1, 2, 4, 6, 7, 9, 10]
print("The original list: ", lst)
print("The missing elements: ", find_missing(lst))
