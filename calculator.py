# my calculator program


print("welcome to my calculator!")
print("==========================")

n1 = float(input("enter first number: "))
n2 = float(input("enter second number: "))

print()
print("what do you want to do?")
print("1 = add")
print("2 = subtract")
print("3 = multiply")
print("4 = divide")

ch = input("pick 1, 2, 3 or 4: ")

if ch == '1':
    ans = n1 + n2
    print("answer =", ans)

elif ch == '2':
    ans = n1 - n2
    print("answer =", ans)

elif ch == '3':
    ans = n1 * n2
    print("answer =", ans)

elif ch == '4':
    if n2 == 0:
        print("cant divide by zero!!")
    else:
        ans = n1 / n2
        print("answer =", ans)

else:
    print("thats not a valid option try again")
 