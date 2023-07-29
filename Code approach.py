def code_approach(num):
    for i in range(num):
        for j in range(i + 1):
            print(chr(ord("a") + j), end=" ")
        print()

code_approach(5)
