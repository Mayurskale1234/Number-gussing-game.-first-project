import random

#importing random, your device will will make a number, which u should guess

num = random.randrange(1,50)
guess = int(input("Please guess a number: "))

#Let's make a conditon, wheather the guessed number is right or wrong.

while guess!=num:
    if guess < num:
        print("You gussed too lower....please guess higher.")
        guess = int(input("\nPlease guess the number again number: "))
    elif guess > num:
        print("You gussed too higher....please guess lower.")
        guess = int(input("\nPlease guess the number again number: "))
   
print("Congoo....you guessed correctly.")
        
        
    
