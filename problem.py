# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other

def test_distinct(data):
    if len(data) == len(set(data)):

        return True

    else:
        return False

print(test_distinct( [1, 3, 4, 6]))
print(test_distinct ([2, 3, 3, 7, 8]))
#Write a Python function to find the first duplicate element in a sequence of numbers

def find_first_duplicate(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return num
        seen.add(num)
    return None  # Return None if no duplicates found

# Example usage:
if __name__ == "__main__":
    numbers = [3, 5, 2, 4, 5, 1, 2]
    result = find_first_duplicate(numbers)
    if result is not None:
        print(f"First duplicate element is: {result}")
    else:
        print("No duplicate elements found.")


#Write a Python program that removes and prints every third number from a list of numbers until the list is empty.Integer programming software

def remove_every_third(numbers):
    index = 0
    while numbers:
        index = (index + 2) % len(numbers)  # move to every third element
        removed = numbers.pop(index)
        print(f"Removed: {removed} | Remaining list: {numbers}")

if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    print(f"Original list: {numbers}")
    remove_every_third(numbers)
#Write a Python program to remove every nth element from a list until the list is empty, where n is input by the user.
def remove_every_nth(numbers,n):
    index = 0
    while numbers :
        index = (index + n - 1)% len(numbers)
        removed = numbers.pop(index)
        print(f"Removed :{removed} | Remaing list : {numbers}")
if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    print(f"Original list{numbers}")
    try:
        n = int(input("Enter the value of n (to remove every nth element): "))
        if n <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            remove_every_nth(numbers, n)
    except ValueError:
        print("Invalid input! Please enter an integer.")

# Write a Python program to make combinations of 3 digits.

import itertools

# Digits from 0 to 9
print(f"numbar combinations : ")
digits = list(range(10))

# Generate all combinations of 3 different digits
combinations = list(itertools.combinations(digits, 3))

# Print the combinations
for combo in combinations:
    print(combo)

print(f"\nTotal combinations: {len(combinations)}")


#Write a Python program that prints long text, converts it to a list, and prints all the words and the frequency of each word.

string_words = "python is great .  i love python .python is human readeble language. "
word_list = string_words.split()

word_freq = [word_list.count(n) for n in word_list]
print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(word_list)))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))
