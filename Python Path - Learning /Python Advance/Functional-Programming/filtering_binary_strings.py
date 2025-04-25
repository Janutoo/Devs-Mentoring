lines = ['10000101011', '111111', '01010101010010', '011001100001', '001010101011']

no_adjacent_ones = list(filter(lambda x: x.count('11') == 0, lines))
result = len(no_adjacent_ones)

print(f"Liczba ciągów bez dwóch sąsiadujących '1': {result}")

