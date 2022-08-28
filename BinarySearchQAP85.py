# Asking user for a sequence and a searching number in it to display its order in a sorted sequence;
# Sort sequence

sequence = list(map(int, input("Please, enter your sequence with space: ").split()))
sequence.sort()

any_number = int(input("Please, enter a number you interested in your sequence: "))

# Set a variables for the function "BinarySearch"
low = 0
middle = len(sequence) // 2
high = len(sequence) - 1

# Defing the function binary_search
def binary_search(sequence, any_number):
    low = 0
    middle = len(sequence) // 2
    high = len(sequence) - 1

    while sequence[middle] != any_number and low <= high:
        if any_number > sequence[middle]:
            low = middle + 1
        else:
            high = middle - 1
        middle = (low + high) // 2

# Cheking is interested number in a sorted list of sequence
    if low > high:
        print("No value")
    else:
        print(f"The position of chosen number in a sorted sequence is {middle}")

result = binary_search(sequence, any_number)
print(result)
