dal = 27
attempts = 5
while attempts > 0:
    guess = int(input("guess a number from 1 to 50:"))
    attempts = attempts - 1
    if guess == dal:
        print("You guessed it right! 🎉")
        break
    diff = abs(dal - guess)
    if diff < 10:
        print("You are very close 🔥")
    elif diff < 20:
        print("You are close 🌡️")
    elif diff < 30:
        print("You are far away 🥶")
    else:
        print("You are very far away 🧊")
    print(f"remaining_attempts = ")
    for i in range(attempts):
        print("❤️", end =" ")
    
