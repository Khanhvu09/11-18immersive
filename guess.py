import random 
print "I am thinking of a number 1 through 10. "
secret_number = random.randint(1, 10);
print secret_number
guess = 0;
number_of_guesses = 5;
while (guess != secret_number):
    if (number_of_guesses == 0):
        print "You ran out of guesses."
        break
    print "You have " + str(number_of_guesses) + " guesses left."
    number_of_guesses = number_of_guesses - 1;
    guess = int(raw_input("What is the secret number? "));
    if (secret_number == guess):
        print "Yes, you win"
    else:
        print "Nope, try again"
      
       
 
        
