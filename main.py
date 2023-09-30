# 1
try:
    number = input()
    summa = int(number[0]) + int(number[3])
    subtraction = int(number[1]) - int(number[2])
    if summa == subtraction:
        print(f"YES")
    else:
        print("NO")

except ValueError:
    print("it's not a number")

# 2
try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Access is allowed")
    else:
        print("Access is denied")
except ValueError:
    print("it's not a number")


# 3
try:
    first = input()
    second = input()
    third = input()
    if int(second) - int(first) == int(third) - int(second):
        print("YES")
    else:
        print("NO")

except ValueError:
    print("it's not a number")

# 4
try:
    col_r1 = int(input())
    row_r1 = int(input())
    col_r2 = int(input())
    row_r2 = int(input())

    if col_r1 == col_r2 or row_r1 == row_r2:
        print("YES")
    else:
        print("NO")
except ValueError:
    print("it's not a number")

# 5
try:
    col_k1 = int(input())
    row_k1 = int(input())
    col_k2 = int(input())
    row_k2 = int(input())

    if abs(col_k1 - col_k2) <= 1 and abs(row_k1 - row_k2) <= 1:
        print("YES")
    else:
        print("NO")
except ValueError:
    print("it's not a number")

# 6
try:
    f = input()
    s = input()
    t = input()
    summa1 = int(f) + int(s) + int(t)
    average = summa1/3
    print(average)
except ValueError:
    print("it's not a number")

# 7
try:
    num = int(input())

    if num == 2:
        print(28)
    elif num == 4 or num == 6 or num == 9 or num == 11:
        print(30)
    else:
        print(31)
except ValueError:
    print("it's not a number")


# 8
try:
    weigh = int(input("Enter your weigh: "))
    if weigh <= 60:
        print("Light weight – up to 60 kg.")
    elif weigh == 61 or weigh <= 64:
        print("First welterweight – up to 64 kg.")
    elif weigh == 65 or weigh <= 69:
        print("Welterweight – up to 69 kg.")
    else:
        print("You can't")

except ValueError:
    print("It's not a number")


# 9
try:
    password = input()
    password_check = input()
    if password == password_check:
        print("Password accepted")
    else:
        print("Password not accepted")
except ValueError:
    print("It's not a number")

# 10
try:
    write_number = int(input("Enter your number: "))
    if write_number % 2 == 0:
        print("Even value")
    else:
        print("Odd value")
except ValueError:
    print("It's not a number")

# 11
try:
    f_number = input()
    s_number = input()
    small_number = 0
    if f_number > s_number:
        small_number = s_number
    else:
        small_number = f_number

    print(small_number)
except ValueError:
    print("It's not a number")


# 12
try:
    age_of_user = int(input("Enter your age: "))
    if age_of_user <= 13:
        print("up to 13 inclusive-childhood")
    elif age_of_user == 14 or age_of_user <= 24:
        print("from 14 to 24 – youth")
    elif age_of_user == 25 or age_of_user <= 59:
        print("from 25 to 59 – maturity")
    elif age_of_user == 60 or age_of_user <= 100:
        print("from 60 – old age")
    else:
        print("You are not alive")

except ValueError:
    print("It's not a number")

# 13
try:
    a = int(input())
    b = int(input())
    c = int(input())

    if a == b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Versatile")
except ValueError:
    print("It's not a number")
