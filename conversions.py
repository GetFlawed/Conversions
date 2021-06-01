import re


def menu():
    print("""
    Menu
    
    Weight - (Kilograms (Kg), Grams (g), Pounds (lbs))
    Volume - (Litres (l), Millilitres (ml), Fluid Ounces (fl oz))
    Temperature - (Celsius (C), Fahrenheit (F), Kelvin (K))
    """)
    input_type = input("\nPlease select which measurement you wish to enter: ")
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
    if input_type == "kg" or input_type == "kilograms":
        input_value = float(input("\nPlease enter how many Kilograms you wish to convert: "))
    elif input_type == "g" or input_type == "grams":
        input_value = float(input("\nPlease enter how many Grams you wish to convert: "))
    else:
        input_value = float(input("\nPlease enter how many Pounds you wish to convert: "))

    output_value = 0
    while output_value == 0:
        output_type = input("\nPlease enter what measurement type to convert to: ")
        x = re.search("^kilograms$|^kg$", output_type.lower())
        y = re.search("^grams$|^g$", output_type.lower())
        z = re.search("^pounds$|^lbs$", output_type.lower())

        if x:
            if input_type == "grams" or input_type == "g":
                output_value = input_value / 1000
                print(f"\n {str(input_value)}g = {str(round(output_value, 2))}Kg.")
            elif input_type == "pounds" or input_type == "lbs":
                output_value = input_value / 2.205
                print(f"\n {str(input_value)}lbs = {str(round(output_value, 2))}Kg.")
            else:
                print("Error, can not convert to the same measurement type.")
        elif y:
            if input_type == "kilograms" or input_type == "kg":
                output_value = input_value * 1000
                print(f"\n {str(input_value)}Kg = {str(round(output_value, 2))}g.")
            elif input_type == "pounds" or input_type == "lbs":
                output_value = input_value * 454
                print(f"\n {str(input_value)}lbs = {str(round(output_value, 2))}g.")
            else:
                print("Error, can not convert to the same measurement type.")
        elif z:
            if input_type == "grams" or input_type == "g":
                output_value = input_value / 454
                print(f"\n {str(input_value)}g = {str(round(output_value, 2))}lbs.")
            elif input_type == "kilograms" or input_type == "kg":
                output_value = input_value * 2.205
                print(f"\n {str(input_value)}Kg = {str(round(output_value, 2))}lbs.")
            else:
                print("Error, can not convert to the same measurement type.")
        else:
            print("Incorrect spelling or measurement type. Please try again.")


def volume(input_type):
    if input_type == "l" or input_type == "litres":
        input_value = float(input("\nPlease enter how many Litres you wish to convert: "))
    elif input_type == "ml" or input_type == "millilitres":
        input_value = float(input("\nPlease enter how many Millilitres you wish to convert: "))
    else:
        input_value = float(input("\nPlease enter how many Fluid Ounces you wish to convert: "))

    output_value = 0
    while output_value == 0:
        output_type = input("\nPlease enter what measurement type to convert to: ")
        x = re.search("^litres$|^l$", output_type.lower())
        y = re.search("^millilitres$|^ml$", output_type.lower())
        z = re.search("^fluid ounces$|^fl oz$", output_type.lower())

        if x:
            if input_type == "millilitres" or input_type == "ml":
                output_value = input_value * 1000
                print(f"\n {str(input_value)}ml = {str(round(output_value, 2))}L.")
            elif input_type == "fluid ounces" or input_type == "fl oz":
                output_value = input_value * 35.195
                print(f"\n {str(input_value)}fl oz = {str(round(output_value, 2))}L.")
            else:
                print("Error, can not convert to the same measurement type.")
        elif y:
            if input_type == "litres" or input_type == "l":
                output_value = input_value / 1000
                print(f"\n {str(input_value)}L = {str(round(output_value, 2))}ml.")
            elif input_type == "fluid ounces" or input_type == "fl oz":
                output_value = input_value / 28.413
                print(f"\n {str(input_value)}fl oz = {str(round(output_value, 2))}ml.")
            else:
                print("Error, can not convert to the same measurement type.")
        elif z:
            if input_type == "litres" or input_type == "l":
                output_value = input_value / 35.195
                print(f"\n {str(input_value)}L = {str(round(output_value, 2))}fl oz.")
            elif input_type == "millilitres" or input_type == "ml":
                output_value = input_value * 28.413
                print(f"\n {str(input_value)}ml = {str(round(output_value, 2))}fl oz.")
            else:
                print("Error, can not convert to the same measurement type.")
        else:
            print("Incorrect spelling or measurement type. Please try again.")


def temperature(input_type):
    if input_type == "c" or input_type == "celsius":
        input_value = float(input("\nPlease enter how many Celsius you wish to convert: "))
    elif input_type == "f" or input_type == "fahrenheit":
        input_value = float(input("\nPlease enter how many Fahrenheit you wish to convert: "))
    else:
        input_value = float(input("\nPlease enter how many Kelvin you wish to convert: "))

    output_value = 0
    while output_value == 0:
        output_type = input("\nPlease enter what measurement type to convert to: ")
        x = re.search("^celsius$|^c$", output_type.lower())
        y = re.search("^fahrenheit$|^f$", output_type.lower())
        z = re.search("^kelvin$|^k$", output_type.lower())

        if x:
            if input_type == "fahrenheit" or input_type == "f":
                output_value = ((input_value - 32) * (5 / 9))
                print(f"\n {str(input_value)}F = {str(round(output_value, 2))}C.")
            elif input_type == "kelvin" or input_type == "k":
                output_value = input_value - 273.15
                print(f"\n {str(input_value)}K = {str(round(output_value, 2))}C.")
            else:
                print("Error, can not convert to the same measurement type.")
        elif y:
            if input_type == "celsius" or input_type == "c":
                output_value = ((input_value * (9 / 5)) + 32)
                print(f"\n {str(input_value)}C = {str(round(output_value, 2))}F.")
            elif input_type == "kelvin" or input_type == "k":
                output_value = ((input_value - 273.15) * (9 / 5)) + 32
                print(f"\n {str(input_value)}K = {str(round(output_value, 2))}F.")
            else:
                print("Error, can not convert to the same measurement type.")
        elif z:
            if input_type == "celsius" or input_type == "c":
                output_value = input_value + 273.15
                print(f"\n {str(input_value)}C = {str(round(output_value, 2))}K.")
            elif input_type == "fahrenheit" or input_type == "f":
                output_value = ((input_value - 32) * (5 / 9)) + 273.15
                print(f"\n {str(input_value)}F = {str(round(output_value, 2))}K.")
            else:
                print("Error, can not convert to the same measurement type.")
        else:
            print("Incorrect spelling or measurement type. Please try again.")


menu()
input("\nPress Enter to continue...")
menu()
