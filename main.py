import random
#list of countries for givng hint
country = ['Nepal','India','USA','England','Spain','Italy','Japan',
        'Australia','Israel','Qatar','Saudi Arabia','Malaysia',
        'Ivory Coast','United Arab Emirates','Nigeria',' Ghana',
        'Ethopia','Yemen','Algeria','Jordan','Andorra','Turkey']
#list of capital cities of corresponding countries
capital = ['Kathmandu','New Delhi','Washington DC','London','Madrid',
        'Rome','Tokyo','Canberra','Jerusalem','Doha','Riyadh','Kuala Lumpur',
        'Yamoussoukro','Abu Dhabi','Abuja','Accra','Addis Ababa',
        'Aden','Algeris','Amman','Andorra la Vella','Ankara']

print("Welcome to the 'Hint and Guess' Game : \n")
print("Rules for the Game:\n")
print("1. Initially hint will be displayed to you as capital city of xyz country.\n")
print("2. You have to enter a guess based on the hint above.")
print("3. Next time, hint will be displayed as letters in the correct guess which was correct in previous input.\n")


while True:
    # get a random index number to be choosen by computer out of capital cities
    choice_for_giving_hint_byc = random.randint(0,len(capital)-1)

    hint = 'Hint: Capital City of {}'.format(country[choice_for_giving_hint_byc])
    #display the hint 
    print(hint)
    #get the correct guess from the capital list using index
    correct_guess = capital[choice_for_giving_hint_byc].lower()
    #Get the guess from user
    guess_by_user = input('Enter your guess using above hint:\n')
    # make each letters to lower case of the guess
    guess_by_user = guess_by_user.lower()
    chance = 1
    while(guess_by_user != correct_guess):
    
        #list with all 0's to track user has got correct character or not
        temp = list()
        for i in range(len(correct_guess)):
            temp.append(0)
        # get the length of smaller string out of correct and guessed string
        if len(correct_guess) >= len(guess_by_user):
            smaller_string_len = len(guess_by_user)
        else:
            smaller_string_len = len(correct_guess)
        #assign 1 to temp[i] for which guessed character is correct
        for j in range(smaller_string_len):
            if correct_guess[j] == guess_by_user[j]:
                temp[j] = 1
        # string for new hint
        new_hint = str()
        #where there is space , corresponding temp will be 2
        """
        temp[i] = 0 -> user didn't guess that character
        temp[i] = 1 -> user guessed that character
        temp[i] = 2 -> there is a space
        """
        for x in range(len(correct_guess)):
            if correct_guess[x] == ' ':
                temp[x] = 2
        for k in range(len(correct_guess)):
            if temp[k] == 1:
                if k == 0:
                    new_hint += correct_guess[k].capitalize()
                    continue
                new_hint += correct_guess[k]
            elif temp[k] == 0:
                new_hint += '_'
            else:
                new_hint += ' '
        chance += 1
        print(new_hint)
        guess_by_user = input('Enter your guess using above hint:\n')
        guess_by_user = guess_by_user.lower()

    print('You guessed the right word i.e.{}'.format(capital[choice_for_giving_hint_byc].capitalize()))
    if chance == 1:
        chance_or_chances = 'chance'
    else:
        chance_or_chances = 'chances'
    print('You took {} {} to guess the word'.format(chance,chance_or_chances))
    continue_or_exit = int(input('Enter 1 to continue or 0 to exit: '))

    if continue_or_exit == 0:
        break