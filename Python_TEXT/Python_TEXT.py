#Python_TEXT

import math


def main():
    n = eval(input("Input:"))
    for i in range(n):
        print("This program finds the real solutions to a quadratic.\n")
        try:
            a, b, c = eval(input("Please enter the coefficients (a, b, c): \n"))
            discRoot = math.sqrt(b * b - 4 * a * c)
            root1 = (-b + discRoot) / (2 * a)
            root2 = (-b + discRoot) / (2 * a)
            print("\nThe soultions are:  ", root1, root2)
        except ValueError as excObj:
            if str(excObj) == "math domain error":
                print("No Real Roots.")
            else:
                print("You didn't give me the right number of coefficients.")
        except NameError:
            print("\nYou didn't enter three numbers.")
        except TypeError:
            print("\nYour inputs were not all numbers.")
        except SyntaxError:
            print("\nYour input was not in the correct from.Missing comma?")
        except:
            print("\nSomething went wrong,Sorry!")

main()