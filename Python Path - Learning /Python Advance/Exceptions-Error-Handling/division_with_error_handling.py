def example1():
    for i in range(3):
        try:
            x = int(input("Enter a number: "))
            y = int(input("Enter another number: "))
            print(x, '/', y, '=', x / y)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Error: Please enter valid integers.")

def example2(L):
    print("\n\nExample 2")
    sumOfPairs = []
    try:
        for i in range(len(L) - 1):  # Avoid IndexError by stopping at len(L) - 1
            sumOfPairs.append(L[i] + L[i + 1])
        print("sumOfPairs =", sumOfPairs)
    except TypeError:
        print("Error: List contains non-numeric values.")

def printUpperFile(fileName):
    try:
        with open(fileName, "r") as file:  # Use 'with' to ensure file is closed
            for line in file:
                print(line.upper())
    except FileNotFoundError:
        print(f"Error: File '{fileName}' not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading the file: {e}")

def main():
    example1()
    L = [10, 3, 5, 6, 9, 3]
    example2(L)
    example2([10, 3, 5, 6, "NA", 3])  # This will trigger a TypeError
    # example3([10, 3, 5, 6])  # Uncomment and implement example3 if needed

    printUpperFile("doesNotExistYest.txt")  # This will trigger FileNotFoundError
    printUpperFile("./Dessssktop/misspelled.txt")  # This will also trigger FileNotFoundError

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Exception raised during main(): {e}")




