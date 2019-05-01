def is_palindrome(word):
    for i in range(len(word)):
        if word[i] != word[-i - 1]:
            return False
    return True

with open("palindromic.txt", "r") as f:
    for line in f:
        line = line.strip().replace(' ', '')
        if is_palindrome(line):
            print(line + " is a palindrome")
        else:
            print(line + " is not a palindrome")
