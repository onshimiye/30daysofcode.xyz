def guess(tries, target):
    n = 0
    while tries >= 1:
        n = int(input("Enter your guess"))

        if n > target:
            print("Guessed number greater than the target")
        else:
            print("Guessed number less than the target")

        tries -= 1

    return abs(target - n)
