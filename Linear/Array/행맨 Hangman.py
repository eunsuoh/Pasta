question = list(input("Enter the word to guess: ").strip().lower())
lst = ["_"] * len(question)

print("Here is the word")
print(" ".join(lst))

num_of_try = 10

while True:
    char = input("Guess a character: ").strip().lower()
    if len(char) != 1 or not char.isalpha():
        print("Please enter a single alphabetical character.")
        continue

    i = 0
    for elem in question:
        if elem == char:
            lst[i] = char
        i += 1

    print(" ".join(lst))

    if "_" not in lst:
        print("You won!")
        break

    num_of_try -= 1
    if num_of_try < 1:
        print("You lost! The word was:", "".join(question))
        break

    print(f"Tries left: {num_of_try}")
