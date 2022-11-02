import random
import time
computer_number = random.randint(1, 100)
continue_game=True
guesses=[]
start_time = time.time()

while (continue_game):
        user_guess = int(input("kaadu skaitli, tavuprat, dators izvelejies?"))
        guesses.append(user_guess)


        if user_guess == computer_number:
            print("you win!")
            continue_game = False
        elif user_guess <computer_number:
            print("Lielaaks")
        elif user_guess>computer_number:
            print("Mazaaks")
        else:
            print("notika kluuda")
            
print("game over!")
print(guesses)

#jaapreekina videejaa starpiba starp minejumiem
sum_of_difference = 0
for n in guesses:
    sum_of_difference += abs(n-computer_number)
average = sum_of_difference / len(guesses)
print(f"videjaa starpiba ir {average}")

#jaapreekina laika starpiibu
print("tu speeleeji %s sekundes" % (time.time() -start_time))
