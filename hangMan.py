
#This holds all the words the user can guess
secreatWord = ("earsplitting")
#This will tell us which letters the suer gussed
lettersGussed = ""

#The number of tries the user have before they loses
failure_count = 6

if message == "Y":
    while failure_count > 0:
        guess = input("\nEnter a letter: ")

        #This will check of the user input is in the secreatWord
        if guess in secreatWord: 
            print("The letter is in secreatWord") #This will happen if the user gussed correct
        else: 
            failure_count -= 1
            print(f"Sorry there is not {guess} in the secreat word. You have {failure_count} left") #This will happen of the user guessed incorrect

        #If the letter the user guessed is correct the letter will be added of the lettersGussed list
        lettersGussed = lettersGussed + guess
        wrong_letter_count = 0
        for letter in secreatWord:
            if letter in lettersGussed:
                print(f"{letter}", end = "")
            else: 
                print("_", end = "")
                wrong_letter_count += 1

        #This will execuate if the user gussed the word correctly
        if wrong_letter_count == 0:
            print(f"\nCongredulation you have {secreatWord} the word correctly")
            break

    else: 
        print("\nSorry you ran out of tries.")

message = input("Do you want to play again (Y/N): ")
if message == "Y":
    failure_count()