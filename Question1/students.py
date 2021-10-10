"""
file:           students.py
created:        06/10/2021 23:17
author:         ciaran mcdevitt
version:        v1.0.0
licensing:      (c) 2021 Ciaran McDevitt, LYIT
                available under the GNU Public License (GPL)
description:
credits:

"""
import time

if __name__ == '__main__':
    '''
    Main method of application
    
    Ask a student for their ID and use it retrieve student course information and grades. If an ID that's not 
     available ask the user to check their input. If the user enter 'X' then exit the program.

    Parameters:
    argument1 (tuple): l_numbers (tuple of student ID's)
    argument2 (list): modules (list of available subjects)
    argument3 (dict): java_oo_programming_grades (dictionary of ID's (key) and java grades (value))
    argument4 (dict): python_Scripting_grades (dictionary of ID's (key) and python grades (value))
    argument5 (list): module_grades (list of the grade dictionaries, so this solution can be programmed dynamically)
    '''

    l_numbers = ("L12345", "L54321")
    modules = ["java_oo_programming", "python_Scripting"]
    java_oo_programming_grades = {"L12345": 40, "L54321": 70}
    python_Scripting_grades = {"L12345": 69, "L54321": 58}
    module_grades = [java_oo_programming_grades, python_Scripting_grades]

    while True:
        student_number = input("\nPlease enter a student number:\t(enter x to exit)\n")
        student_number_upper = student_number.upper()
        if student_number_upper == "X":
            print("Goodbye!")
            time.sleep(5)
            quit()
        elif student_number in l_numbers or student_number.upper() in l_numbers:
            print("-- Module --------------- Grade ------")
            for i, module in enumerate(modules):
                print(f"-{module:<22}    -{module_grades[i].get(student_number_upper)}")
        else:
            print("Please check that you have entered a valid student ID")
