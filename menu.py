import math
ADDITION_PROBLEM = 1
HARD_ADDITION_PROBLEM = 2
DIVISION_PROBLEM = 3
HARD_DIVISION_PROBLEM = 4
MULTIPLICATION_PROBLEM = 5
HARD_MULTIPLICATION_PROBLEM = 6
CALCULUS_PROBLEM = 7
QUIT_CHOICE = 8

def main():
    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        try:
            choice = int(input('Enter your choice:'))
        except ValueError:
            invalid_display()
            continue
        if choice == ADDITION_PROBLEM:
            return handle_choice_addition_problem()
        elif choice == HARD_ADDITION_PROBLEM:
            return handle_choice_hard_addition_problem()
        elif choice == DIVISION_PROBLEM:
            return handle_choice_division_problem()
        elif choice == HARD_DIVISION_PROBLEM:
            return handle_choice_hard_division_problem()
        elif choice == MULTIPLICATION_PROBLEM:
            return handle_choice_multiplication_problem()
        elif choice == HARD_MULTIPLICATION_PROBLEM:
            return handle_choice_hard_multiplication_problem()
        elif choice == CALCULUS_PROBLEM:
            return handle_choice_calculus_equation()
        elif choice == QUIT_CHOICE:
            print('┌------------------------┐')
            print('|    Quitting Program... |')
            print('└------------------------┘')
            print('__________________________')
        else:
            print('┌--------------------------------------┐')
            print("| You didn't make a correct selection! |")
            print('└--------------------------------------┘')
            print('________________________________________')
                
def Correct_Display():
    print('┌------------------------┐')
    print('|        CORRECT!        |')
    print('└------------------------┘')
    print('__________________________')
    
def Incorrect_Display():
    print('┌------------------------┐')
    print('|       INCORRECT!       |')
    print('└------------------------┘')
    print('__________________________')
    
def invalid_display():
    print('┌------------------------┐')
    print('|     INVALID CHOICE!    |')
    print('└------------------------┘')
    print('__________________________')
    
def handle_choice_addition_problem():
    print('What is 10 + 8?')
    add_problem = 0
    try:
        add_problem = int(input('Enter your answer: '))
    except ValueError:
        invalid_display()
        return main()
    if add_problem == 18:
        Correct_Display()
    elif add_problem != 18:
        Incorrect_Display()
    return main()
        
def handle_choice_hard_addition_problem():
    print('What is 284.3 + 324.8: ')
    hard_add_problem = 0.0
    try:
        hard_add_problem = float(input('Enter your answer: '))
    except ValueError:
        invalid_display()
        return main()
    if hard_add_problem == 609.1:
        Correct_Display()
    elif hard_add_problem != 609.1:
        Incorrect_Display()
    return main()
        
def handle_choice_division_problem():
    print('What is 10 / 2?')
    div_problem = 0
    try:
        div_problem = int(input('Enter your answer: '))
    except ValueError:
        invalid_display()
        return main()
    if div_problem == 5:
        Correct_Display()
    elif div_problem != 5:
        Incorrect_Display()
    return main()

def handle_choice_hard_division_problem():
    print('What is 17 / 40')
    hard_div_problem = 0.0
    try:
        hard_div_problem = float(input('Enter your answer: '))
    except ValueError:
        invalid_display()
        return main()
    if hard_div_problem == 0.425:
        Correct_Display()
    elif hard_div_problem != 0.425:
        Incorrect_Display()
    return main()
    
def handle_choice_multiplication_problem():
    print('What is 5 x 10')
    mult_problem = 0
    try:
        mult_problem = int(input('Enter your answer: '))
    except ValueError:
        invalid_display()
    if mult_problem == 50:
        Correct_Display()
    elif mult_problem != 50:
        Incorrect_Display()
    return main()

def handle_choice_hard_multiplication_problem():
    print('What is 2.5 x 3.45, to the third decimal place')
    hard_mult_problem = 0.0
    try:
        hard_mult_problem = float(input('Enter your answer: '))
    except ValueError:
        invalid_display()
        return main()
    if hard_mult_problem == 8.625:
        Correct_Display()
    elif hard_mult_problem != 8.625:
        Incorrect_Display()
    return main()
        
def handle_choice_calculus_equation():
    print('What is the derivative of 4x^3')
    calc_problem = ''
    try:
        calc_problem = str(input('Enter your answer: '))
    except ValueError:
        invalid_display()
        return main()
    if calc_problem == '12x^2':
        Correct_Display()
    elif calc_problem != '12x^2':
        Incorrect_Display()
    return main()
        
def display_menu():
    print('┌------------------------┐')
    print('|        MATH TEST       |')
    print('└------------------------┘')
    print('1) Solve a addition problem')
    print('2) solve a hard addition problem')
    print('3) Solve a division problem')
    print('4) Solve a hard division problem')
    print('5) Solve a multiplication problem')
    print('6) Solve a hard multiplication problem')
    print('7) Solve a calculus equation')
    print('8) Quit')

main()