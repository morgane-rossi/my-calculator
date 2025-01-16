#User
def enter_number():
    while True :
        try :    
            input_number1 = input("Enter the first number: ")
            input_number1 = input_number1.replace(',','.')
            number1 = float(input_number1)

            operator = input("Enter your operator: ")
            if operator not in ['+', '-', '*', '/']:
                print("Invalid operator. Please enter one of +, -, *, or /.")
                continue

            input_number2 = input("Enter the second number: ")
            input_number2 = input_number2.replace(',','.')
            number2 = float(input_number2)

            return number1,operator,number2
        except ValueError :
            print("Please enter valid numeric values")
            continue
    
#calculate function
def calculate(number1,operator,number2):
    while True : 
        try :
            if operator == "+":
                return number1 + number2
            elif operator == "-":
                return number1 - number2
            elif operator == "/":
                if number2 == 0:
                    return None
                return number1 / number2
            elif operator == "x" or operator == "*":
                return number1 * number2
        except ValueError :
            print("make an effort please")
            return None


#Main
number1,operator,number2 = enter_number()
result = calculate(number1,operator,number2)

try:
    if isinstance(result, int) or result.is_integer():
            print(f"{int(result)}")
    else:
            print(f"{result:.2f}")
except AttributeError :
    print("make an effort please")
except ValueError : 
    print("make an effort please")



