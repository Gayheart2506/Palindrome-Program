print("THIS PROGRAM DETERMINES IF A WORD IS PALINDROME OR NOT \n")
print("*************** WELCOME TO THE PALINDROME CHECKER *************** \n")
continue_check = True

while continue_check:
    word1 = input("Enter a word you think is palindrome : ").upper()
    reverse_of_word = word1[::-1]
    if word1 == reverse_of_word:
        print("The word is palindrome")
        print("GAME COMPLETED !!")
        continue_check = False
    else:
        print("The word is not palindrome")
