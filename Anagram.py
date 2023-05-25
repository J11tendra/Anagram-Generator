#Importing the module:
from opening_file import open_file

#Defining the path of file:
word = open_file('D:/Python_work/text_files/All_Words.txt')


#Flag to control the flow of input:
active = True


#Getting the user input:
while active:
    print("\n\n\t\t||---------------------------------------------------||")
    print("Hit 'q' to quit.")
    user = input("Enter A Word:")
    user = user.strip().lower()

    if user == "q":
        active = False

    elif len(user) <= 2:
        print("Please enter a word with letters more than 2.")

    else:
        anagram = []
        user = sorted(user)
        #Checking the anagram:
        def sort_word():
            '''Sorting the word from the list'''
            for x in word:
                y = x.lower()
                y = sorted(y)
                if y == user:
                    anagram.append(x)
            return anagram

        #Calling the Function:
        ana = sort_word()
        print(f'We have found {len(ana)} anagrams: {ana}')