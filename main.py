is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are a tall female")
else:
    print("You are a short female")

#comparisons

def max_num(num1, num2, num3):
    if num1 >=  num2 and num2 >= num3:
        return num1
    if num2 >= num1 and num2 >= num3:
        return num2
    if num3 >= num1 and num3 >= num2:
        return num3
    else:
        print("WTF u siked my programme")

num1 = int(input("Type your first number"))
num2 = int(input("Type your second number"))
num3 = int(input("Type your third number"))

print(str(max_num(num1, num2, num3)) + " is the highest number")