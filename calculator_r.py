from pathlib import Path

"""
Features 1 arithmetic operation : + ; - ; * ; /
Between 2 numbers
The numbers are integers or floating numbers
Computes and displays the results

History text file to record operations
Program can read, write in and reset history
"""

def enter_value() :
    """
    Entering a numeric value : integer or floating number
    Not enabling entering another type value
    """
    number = input("Please enter a number :\n")
    try :
        number = number.replace(",", ".")
        number = float(number)
        return number
    except ValueError:
        print("Input error")

def enter_symbol():
    """
    Entering a symbol for computing : '+', '-', '*', '/'
    """
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
        
        # displays result with a formatted string
        line = f"Result : {first} {symbol} {second} = {result}\n"
        print(line)
        # formatted result is stored in history file history.txt
        write_history(line)

    # Errors & exceptions handling
    except ZeroDivisionError :
        print("Dividing by zero : forbidden")

    except ArithmeticError :
        print("Calculating is impossible")

    except ValueError:
        print("Input error")
    
    except AttributeError:
        print("Error")

def write_history(line):

    try :
        history_f = Path("./history.txt")

        # if history.txt text already exists in same directory
        if history_f.is_file():
            with open("history.txt", "a") as history_f:
                history_f.write(line)

        else :
            # if history.txt text doesn't already exists
            with open("history.txt", "w") as history_f :
                history_f.write(line)

    except (FileNotFoundError, NameError, PermissionError, IsADirectoryError, IOError, UnicodeDecodeError, UnicodeEncodeError, OSError, OverflowError) as error :
        print("Error while writing")

    except Exception :
        print("Error while writing")

def read_history():

    try :
        print("\nCalculator history :\n")

        history_f = Path("./history.txt")
        if history_f.is_file():
            with open("history.txt", "r") as history_f :
                print(history_f.read())
            print()
        else :
            print("Empty history\n")

    except (FileNotFoundError, NameError, PermissionError, IsADirectoryError, IOError, UnicodeDecodeError, UnicodeEncodeError, OSError, OverflowError) as error :
        print("Error while reading")

    except Exception :
        print("Error while reading")

def reset_history():

    try:
        history_f = Path("./history.txt")
        with open("history.txt", "w") as history_f :
            history_f.write("")
        print("History reset\n")

    except (FileNotFoundError, NameError, PermissionError, IsADirectoryError, IOError, UnicodeDecodeError, UnicodeEncodeError, OSError, OverflowError) as error :
        print("Error while writing")

    except Exception :
        print("Error while writing")

def program_run():
    try :
        fonctions = menu()
        if fonctions == "2":
            read_history()
            program_run()
        elif fonctions == "3":
            reset_history()
            program_run()
        elif fonctions == "4":
            return
        elif fonctions == "1":
            while True:
                calculate()

    except KeyboardInterrupt :
        program_run()

def menu():
    print("Calculator menu\nWhat is your choice ?")
    print("Choice 1 : using the calculator")
    print("Choice 2 : displaying history")
    print("Choice 3 : resetting history")
    print("Choice 4 : quit")
    menu = input()
    while menu not in ("1", "2", "3", "4"):
        print("Sorry I didn't understand")
        print("Choice 1 : using the calculator")
        print("Choice 2 : displaying history")
        print("Choice 3 : resetting history")
        print("Choice 4 : quit")
        menu = input()
    return menu

def main():
    program_run()

main()