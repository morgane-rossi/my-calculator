"""
Features 1 arithmetic operation : + ; - ; * ; /
Between 2 numbers
The numbers are integers or floating numbers
"""

def enter_value() :
    number = input("Please enter a number :\n")
    try :
        number = number.replace(",", ".")
        number = float(number)
        return number
    except ValueError:
        print("Input error")

def enter_symbol():
    symbol = -1
    while symbol not in ("+", "-", "*", "/"):
        print("Please enter a symbol : + ; - ; * : /")
        symbol = input()
        if symbol not in ("+", "-", "*", "/"):
            print("Unknown symbol, please retry")
    return symbol

def calculate():
    result = -1
    try :
        first = enter_value()
        symbol = enter_symbol()
        second = enter_value()
        if first == None or symbol == None or second == None :
            raise ValueError("Input error")

        if symbol == "+":
            result = first + second
        elif symbol == "-":
            result = first - second
        elif symbol == "*":
            result = first * second
        elif symbol == "/":
            result = first / second
        if result.is_integer():
            result = int(result)
        else :
            result = f"{result:.3f}"
        print(f"Result : {first} {symbol} {second} = {result}")

    except ZeroDivisionError :
        print("Dividing by zero : forbidden")

    except ArithmeticError :
        print("Impossible calculation")

    except ValueError:
        print("Input error")
    
    except AttributeError:
        print("Error")

def history():
    # voir toutes les opérations arithmétiques effectuées par l'utilisateur
    # possibilité d’effacer  cet  historique
    # possibilité de réinitialiser cet  historique
    pass


def program_run():
    try :
        fonctions = menu()

        while True :
            if fonctions == "1":
                calculate()
            elif fonctions == "2":
                history()
            elif fonctions == "3":
                return

    except KeyboardInterrupt :
        program_run()

def menu():
    print("Calculator menu\nWhat is your choice ?")
    print("Choice 1 : using the calculator")
    print("Choice 2 : displaying histor")
    print("Choice 3 : quit")
    menu = input()
    while menu not in ("1", "2", "3"):
        print("Sorry I didn't understand")
        print("Choice 1 : using the calculator")
        print("Choice 2 : displaying histor")
        print("Choice 3 : quit")
        menu = input()
    return menu

def main():
    program_run()

main()