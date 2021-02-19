#!/usr/bin/env python3
import math

while True:
    typeofProblem = input("What would sort of equation do you need help with? (-list to list my commands) ").lower()
    if typeofProblem == "-list":
        print('  "aos" will solve for the area of symmetry and vertex given a standard quadratic equation \n "factored form to standard form" will convert any quadratic equation in factored form, to be in standard format (x + 2) (x + 2) -->> x^2 + 4x + 4 \n "missing quadratic values" will solve for to missing quadratic values, (x2 and k) given x1. \n "solving quartic equations" will solve the x values for equations in this format ax^4 + bx^2 + c, given the variables a, b, and c. \n vertex to standard form allows you to convert from vertex form to standard form.  y = a(x – h)2 + k -->> y = ax^2 + bx + c')
    if typeofProblem != "-list":
        break

def solving_quartic_equations():
    a = float(input("What is the value of a?  (ax² + bx +c) "))
    b = float(input("What is the value of b?  (ax² + bx +c) "))
    c = float(input("what is the value of c?  (ax² + bx +c) "))
    discriminant = (b ** 2) - (4 *a * c)
    positive_solution_set = (-b + math.sqrt(discriminant)) / (2*a)
    negative_solution_set = (-b - math.sqrt(discriminant)) / (2*a)
    sqrt_pos = math.sqrt(positive_solution_set)
    sqrt_neg = math.sqrt(negative_solution_set)

    print(f"-{sqrt_pos} , {sqrt_pos} , -{sqrt_neg} , {sqrt_neg} are your solutions.")

def missing_quadratic_values():
    x1 = int(input("What is the given X value? (x1) "))
    a  = int(input("What is the value of a (ax² + bx +c)? (defaults to 1) ") or 1)
    b  = int(input("What is the value of b (ax² + bx +c)? "))
    x2 = -b / a + -x1
    print(f"{str(x1)} + x2 = {str(-b /a )}")
    print(f"x2 = {str(x2)} ")
    print(f"{x1} * {x2} = k")
    print(f"k = {str(x1 * x2)}")
def factored_form_to_standard_form():
    a = int(input("What is value outside of the parenthesis? "))
    val1 = int(input("Value excluding x in first parenthesis pair? "))
    val2 = int(input("Value excluding x in second parenthesis pair? "))
    val3 = val1 + val2
    val4 = val1 * val2
    print(f"{a}x² + " + str(a*val3) + "x" , a*val4)
def aos_and_coords():
    a = float(input("What is the value of a?  (ax² + bx +c) "))
    b = float(input("What is the value of b?  (ax² + bx +c) "))
    c = float(input("what is the value of c?  (ax² + bx +c) "))
    x  = -b / (2 * a)
    y = a * x ** 2 + b * x + c
    print(f" AOS is {x}")
    print("coordinates are" ,  x , y)



# --- -----------------------------------------------------------Dictonary Database for linking input strings with functions---------------------------------------------------------------------------------
database ={"aos":aos_and_coords, "factored form to standard form":factored_form_to_standard_form , "missing quadratic values":missing_quadratic_values,  "solving quartic equations":solving_quartic_equations

}
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
typeofProblem = database[typeofProblem]
typeofProblem()


