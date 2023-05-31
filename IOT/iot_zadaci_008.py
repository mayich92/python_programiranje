# Napisati funkciju koja rekurzivno zbraja sve numeričke elemente višestruko (nepoznato koliko) ugniježđene liste.
# Primjer rada:
# lst = [[1,2], [3,4, [5, 6]], 7, 8.9]
# print(sum_nested(lst))    # vraća rezultat 36.9

def sum_nested(lst):
    total = 0

    for item in lst:
        if isinstance(item, list):
            total += sum_nested(item)
        elif isinstance(item, (int, float)):
            total += item

    return total


lst = [[1, 2], [3, 4, [5, 6]], 7, 8.9]
print(sum_nested(lst))  # Output: 36.9
