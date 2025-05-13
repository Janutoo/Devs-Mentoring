
print("Alfabet normalny")
for char in range(ord('a'), ord('z') + 1):
    print(chr(char), end=' ')


print("\nAlfabet odwrocony:")
for char in range(ord('Z'), ord('A') - 1, -1):
    print(chr(char), end=' ')
