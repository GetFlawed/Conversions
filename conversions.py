import re
from classes import Weights, Volumes, Temps
global input_value


def menu():
    print("""
    Menu
       
    Weight - (Kilograms (Kg), Grams (g), Pounds (lbs))
    Volume - (Litres (l), Millilitres (ml), Fluid Ounces (fl oz))
    Temperature - (Celsius (C), Fahrenheit (F), Kelvin (K))
    
    Enter Quit to exit the program
    """)
    input_type = input("\nPlease select which measurement you wish to enter: ")
    if input_type.lower() == "quit":
        exit()
    x = re.search("^kilograms$|^kg$|^grams$|^g$|^pounds$|^lbs$", input_type.lower())
    y = re.search("^litres$|^l$|^mililitres$|^ml$|^fluid ounces$|^fl oz$", input_type.lower())
    z = re.search("^celsius$|^c$|^fahrenheit$|^f$|^kelvin$|^k$", input_type.lower())

    if x:
        weight(input_type.lower())
    elif y:
        volume(input_type.lower())
    elif z:
        temperature(input_type.lower())
    else:
        print("Incorrect spelling or measurement type.")
        print("Please make sure to enter a measurement that is on the provided list")
        menu()


def weight(input_type):
    global input_value
    float_value = False
    if input_type == "kg" or input_type == "kilograms":
        while not float_value:
            try:
                input_value = float(input("\nPlease enter how many Kilograms you wish to convert: "))
                if input_value > 0:
                    output = Weights(input_value, input_value, input_value, input_value, input_value, input_value)
                    print(f"""
                    {input_value}Kg is equal to:
                    {str(round(output.kg_pounds, 2))}lbs
                    {str(round(output.kg_grams, 2))}g""")
                    float_value = True
                else:
                    print("That's not a number greater than 0, try again please")
            except ValueError:
                print("That's not a number, try again please")

    elif input_type == "g" or input_type == "grams":
        while not float_value:
            try:
                input_value = float(input("\nPlease enter how many Grams you wish to convert: "))
                if input_value > 0:
                    output = Weights(input_value, input_value, input_value, input_value, input_value, input_value)
                    print(f"""
                    {input_value}g is equal to:
                    {str(round(output.g_pounds, 2))}lbs
                    {str(round(output.g_kilograms, 2))}kg""")
                    float_value = True
                else:
                    print("That's not a number greater than 0, try again please")
            except ValueError:
                print("That's not a number, try again please")
    else:
        while not float_value:
            try:
                input_value = float(input("\nPlease enter how many Pounds you wish to convert: "))
                if input_value > 0:
                    output = Weights(input_value, input_value, input_value, input_value, input_value, input_value)
                    print(f"""
                    {input_value}lbs is equal to:
                    {str(round(output.lbs_kilograms, 2))}kg
                    {str(round(output.lbs_grams, 2))}g""")
                    float_value = True
                else:
                    print("That's not a number greater than 0, try again please")
            except ValueError:
                print("That's not a number, try again please")


def volume(input_type):
    global input_value
    float_value = False
    if input_type == "l" or input_type == "litres":
        while not float_value:
            try:
                input_value = float(input("\nPlease enter how many Litres you wish to convert: "))
                if input_value > 0:
                    output = Volumes(input_value, input_value, input_value, input_value, input_value, input_value)
                    print(f"""
                    {input_value}L is equal to:
                    {str(round(output.l_millilitres, 2))}ml
                    {str(round(output.l_fluid_ounces, 2))}fl oz""")
                    float_value = True
                else:
                    print("That's not a number greater than 0, try again please")
            except ValueError:
                print("That's not a number, try again please")
    elif input_type == "ml" or input_type == "millilitres":
        while not float_value:
            try:
                input_value = float(input("\nPlease enter how many Millilitres you wish to convert: "))
                if input_value > 0:
                    output = Volumes(input_value, input_value, input_value, input_value, input_value, input_value)
                    print(f"""
                    {input_value}ml is equal to:
                    {str(round(output.ml_litres, 2))}L
                    {str(round(output.ml_fluid_ounces, 2))}fl oz""")
                    float_value = True
                else:
                    print("That's not a number greater than 0, try again please")
            except ValueError:
                print("That's not a number, try again please")
    else:
        while not float_value:
            try:
                input_value = float(input("\nPlease enter how many Fluid Ounces you wish to convert: "))
                if input_value > 0:
                    output = Volumes(input_value, input_value, input_value, input_value, input_value, input_value)
                    print(f"""
                    {input_value}fl oz is equal to:
                    {str(round(output.fl_oz_millilitres, 2))}ml
                    {str(round(output.fl_oz_litres, 2))}l""")
                    float_value = True
                else:
                    print("That's not a number greater than 0, try again please")
            except ValueError:
                print("That's not a number, try again please")


def temperature(input_type):
    global input_value
    float_value = False
    if input_type == "c" or input_type == "celsius":
        while not float_value:
            try:
                input_value = float(input("\nPlease enter how many Celsius you wish to convert: "))
                if input_value > 0:
                    output = Temps(input_value, input_value, input_value, input_value, input_value, input_value)
                    print(f"""
                    {input_value}C is equal to:
                    {str(round(output.c_fahrenheit, 2))}F
                    {str(round(output.c_kelvin, 2))}K""")
                    float_value = True
                else:
                    print("That's not a number greater than 0, try again please")
            except ValueError:
                print("That's not a number, try again please")
    elif input_type == "f" or input_type == "fahrenheit":
        while not float_value:
            try:
                input_value = float(input("\nPlease enter how many Fahrenheit you wish to convert: "))
                if input_value > 0:
                    output = Temps(input_value, input_value, input_value, input_value, input_value, input_value)
                    print(f"""
                    {input_value}F is equal to:
                    {str(round(output.f_celsius, 2))}C
                    {str(round(output.f_kelvin, 2))}K""")
                    float_value = True
                else:
                    print("That's not a number greater than 0, try again please")
            except ValueError:
                print("That's not a number, try again please")
    else:
        while not float_value:
            try:
                input_value = float(input("\nPlease enter how many Kelvin you wish to convert: "))
                if input_value > 0:
                    output = Temps(input_value, input_value, input_value, input_value, input_value, input_value)
                    print(f"""
                    {input_value}K is equal to:
                    {str(round(output.k_celsius, 2))}C
                    {str(round(output.k_fahrenheit, 2))}F""")
                    float_value = True
                else:
                    print("That's not a number greater than 0, try again please")
            except ValueError:
                print("That's not a number, try again please")


loop = True
while loop:
    menu()
    input("\nPress any key to go back to the menu...")
