import re
from classes import Weight, Volume, Temp

global input_value, input_type


def menu():
    print("""\n\n             - Menu -
            Categories:
            
    Weight - Volume - Temperature
    
    Enter Quit to exit the program""")
    category_type = input("Please select the measurement category: ").lower()
    if category_type == "quit":
        exit()
    elif category_type == "weight":
        weight()
    elif category_type == "volume":
        volume()
    elif category_type == "temperature":
        temperature()
    else:
        print("""\n\nIncorrect spelling or measurement category.
Please make sure to enter a category that is on the provided list.""")
        menu()


def weight():
    global input_value, input_type
    weights_value = False
    while not weights_value:
        try:
            print("""\n  Kilograms (Kg) - Grams (g) - Pounds (lbs)""")
            input_type = input("Please choose the weight type you wish to convert: ").lower()
            weights = re.search("^kilograms$|^kg$|^grams$|^g$|^pounds$|^lbs$", input_type)
            if weights:
                weights_value = True
        except ValueError:
            print("""\n\nIncorrect spelling or measurement type.
            Please make sure to enter a measurement that is on the provided list.\n\n""")
    if input_type == "kg":
        input_type = "kilograms"
    elif input_type == "g":
        input_type = "grams"
    elif input_type == "lbs":
        input_type = "pounds"
    float_value = False
    while not float_value:
        try:
            input_value = float(input(f"\nPlease enter how many {input_type} you wish to convert: "))
            if input_value > 0:
                output = Weight(input_value, input_value, input_value, input_value, input_value, input_value)
                if input_type == "kilograms":
                    print(f"""{input_value}Kg is equal to:
{str(round(output.kg_pounds, 2))}lbs
{str(round(output.kg_grams, 2))}g """)
                elif input_type == "grams":
                    print(f"""{input_value}g is equal to:
{str(round(output.g_pounds, 2))}lbs
{str(round(output.g_kilograms, 2))}kg""")
                else:
                    print(f"""{input_value}lbs is equal to:
{str(round(output.lbs_kilograms, 2))}kg
{str(round(output.lbs_grams, 2))}g""")
                float_value = True
            else:
                print("\n\nThat's not a number greater than 0, try again please")
        except ValueError:
            print("\n\nThat's not a number, try again please")


def volume():
    global input_value, input_type
    weights_value = False
    while not weights_value:
        try:
            print("""\nLitres (l) - Millilitres (ml) - Fluid Ounces (fl oz)""")
            input_type = input("Please choose the weight type you wish to convert: ").lower()
            volumes = re.search("^litres$|^l$|^mililitres$|^ml$|^fluid ounces$|^fl oz$", input_type)
            if volumes:
                weights_value = True
        except ValueError:
            print("""\n\nIncorrect spelling or measurement type.
Please make sure to enter a measurement that is on the provided list.\n\n""")
    if input_type == "l":
        input_type = "litres"
    elif input_type == "ml":
        input_type = "millilitres"
    elif input_type == "fl oz":
        input_type = "fluid ounces"
    float_value = False
    while not float_value:
        try:
            input_value = float(input(f"\nPlease enter how many {input_type} you wish to convert: "))
            if input_value > 0:
                output = Volume(input_value, input_value, input_value, input_value, input_value, input_value)
                if input_type == "litres":
                    print(f"""{input_value}L is equal to:
{str(round(output.l_millilitres, 2))}ml
{str(round(output.l_fluid_ounces, 2))}fl oz""")
                elif input_type == "millilitres":
                    print(f"""{input_value}ml is equal to:
{str(round(output.ml_litres, 2))}L
{str(round(output.ml_fluid_ounces, 2))}fl oz""")
                elif input_type == "fluid ounces":
                    print(f"""{input_value}fl oz is equal to:
{str(round(output.fl_oz_millilitres, 2))}ml
{str(round(output.fl_oz_litres, 2))}l""")
                float_value = True
            else:
                print("That's not a number greater than 0, try again please")
        except ValueError:
            print("That's not a number, try again please")


def temperature():
    global input_value, input_type
    weights_value = False
    while not weights_value:
        try:
            print("""\n    Celsius (C) - Fahrenheit (F) - Kelvin (K)""")
            input_type = input("Please choose the weight type you wish to convert: ").lower()
            temperatures = re.search("^celsius$|^c$|^fahrenheit$|^f$|^kelvin$|^k$", input_type)
            if temperatures:
                weights_value = True
        except ValueError:
            print("""\n\nIncorrect spelling or measurement type.
Please make sure to enter a measurement that is on the provided list.\n\n""")
    if input_type == "c":
        input_type = "celsius"
    elif input_type == "f":
        input_type = "fahrenheit"
    elif input_type == "k":
        input_type = "kelvin"
    float_value = False
    while not float_value:
        try:
            input_value = float(input(f"\nPlease enter how many {input_type} you wish to convert: "))
            if input_value > 0:
                output = Temp(input_value, input_value, input_value, input_value, input_value, input_value)
                if input_type == "celsius":
                    print(f"""{input_value}C is equal to:
{str(round(output.c_fahrenheit, 2))}F
{str(round(output.c_kelvin, 2))}K""")
                elif input_type == "fahrenheit":
                    print(f"""{input_value}F is equal to:
{str(round(output.f_celsius, 2))}C
{str(round(output.f_kelvin, 2))}K""")
                elif input_type == "kelvin":
                    print(f"""{input_value}K is equal to:
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
    end_input = input("""\nEnter quit to exit the program.
or press any key to go back to the menu...""").lower()
    if end_input == "quit":
        exit()
