import random

rand_number = random.randint(0, 40)
num_of_guess = 1
while True:
    
    user_number = int(input())

    if user_number == rand_number:
        print("πππππβCongratulationβπππππ")
        break

    elif user_number < rand_number:
        print("π Go Up β«")

    elif user_number > rand_number:
        print("π Go Down β¬")
    num_of_guess += 1

print("Number of your guesses is:", num_of_guess)
print("End of game, Come back soonπ")

