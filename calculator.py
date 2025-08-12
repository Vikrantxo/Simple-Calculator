# A simple calculator
print("Welcome :-)")
try:
    num1 = float(input("Enter first number:  "))
    num2 = float(input("Enter second number:  "))
except ValueError:
    print("Expected Value Error")
    exit()  # Exit if input is invalid

op = input(
    "Press following for:\n A or a = Addition\n S or s = Subtraction\n M or m = Multiplication\n D or d = Division\n op = "
)
match op:
    case "A" | "a":
        ans = num1 + num2
        print("Answer = ", ans)
    case "S" | "s":
        ans = num1 - num2
        print("Answer = ", ans)
    case "M" | "m":
        ans = num1 * num2
        print("Answer = ", ans)
    case "D" | "d":
        if num2 != 0:
            ans = num1 / num2
            print("Answer = ", ans)
        else:
            print("This operation can't be done")
    case _:
        print("Choose a correct operation")

print("Thank You for using this calculator")
