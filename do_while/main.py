n = 0
while True:
    n = n + 1
    print(f"Is {n} odd or even?")
    if n<=10:
        if n%2 == 0:
            print(f"{n} is even.")
        else:
            print(f"{n} is odd.")
    else:
        break
