"""
Features 1 arithmetic operation : + ; - ; * ; /
Between 2 numbers
The numbers are integers or floating numbers
"""

def enter_value() :
    number = input("veuillez rentrer un nombre :\n")
    try :
        number = float(number)
        return number
    except ValueError:
        print("erreur de saisie")

def enter_symbol():
    symbol = -1
    while symbol not in ("+", "-", "*", "/"):
        print("veuillez choisir une opération : + ; - ; * : /")
        symbol = input()
        if symbol not in ("+", "-", "*", "/"):
            print("opération non conforme, veuillez recommencer")
    return symbol

def calculate():
    result = -1
    try :
        first = enter_value()
        symbol = enter_symbol()
        second = enter_value()
        if first == None or symbol == None or second == None :
            raise ValueError("erreur de saisie")

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
        print(f"résultat de {first} {symbol} {second} = {result}")

    except ArithmeticError :
        print("Impossible de diviser par zéro")

    except ValueError:
        print("erreur saisie")

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
    print("Menu de la calculatrice.\nQue voulez-vous faire ?")
    print("Tapez 1 pour utiliser la calculatrice")
    print("Tapez 2 pour afficher l'historique")
    print("Tapez 3 pour quitter")
    menu = input()
    while menu not in ("1", "2", "3"):
        print("Je n'ai pas compris votre choix.")
        print("Tapez 1 pour utiliser la calculatrice")
        print("Tapez 2 pour afficher l'historique")
        print("Tapez 3 pour quitter")
        menu = input()    
    return menu

def main():
    program_run()

main()