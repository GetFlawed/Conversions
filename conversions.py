# Global Variables
weight_array = {"kilograms", "kg", "grams", "g", "pounds", "lbs"}
volume_array = {"litres", "l", "millilitres", "ml", "fluid ounces", "fl oz"}
temperature_array = {"celsius", "c", "fahrenheit", "f"}


def menu():
    print("""
    Menu
    
    Weight - (Kilograms (Kg), Grams (g), Pounds (lbs))
    Volume - (Litres (l), Millilitres (ml), Fluid Ounces (fl oz))
    Temperature - (Celsius (C), Fahrenheit (F))
    """)
    input_type = input("\nPlease select which measurement you wish to enter: ")
    if input_type.lower() in weight_array:
        weight(input_type)
    elif input_type.lower() in volume_array:
        volume(input_type)
    elif input_type.lower() in temperature_array:
        temperature(input_type)
    else:
        print("Incorrect spelling or measurement type.")
        print("Please make sure to enter a measurement that is on the provided list")
        menu()


def weight(input_type):
    weight_convert_array = weight_array
    if input_type.lower() == "kg" or input_type.lower() == "kilograms":
        input_value = float(input("\nPlease enter how many Kilograms you wish to convert: "))
        weight_convert_array.remove("kilograms")
        weight_convert_array.remove("kg")
    elif input_type.lower() == "g" or input_type.lower() == "grams":
        input_value = float(input("\nPlease enter how many Grams you wish to convert: "))
        weight_convert_array.remove("grams")
        weight_convert_array.remove("g")
    else:
        input_value = float(input("\nPlease enter how many Pounds you wish to convert: "))
        weight_convert_array.remove("pounds")
        weight_convert_array.remove("lbs")

    loop = 1
    while loop == 1:
        output_type = input("\nPlease enter what measurement type to convert to: ")
        if output_type.lower() in weight_convert_array:
            if input_type == "kg" or input_type == "kilograms":
                if output_type.lower() == "grams" or output_type.lower() == "g":
                    output_value = input_value / 1000
                    print(f"\n {str(input_value)}Kg = {str(round(output_value, 2))}g.")
                    loop = 0
                else:
                    output_value = input_value * 2.205
                    print(f"\n {str(input_value)}Kg = {str(round(output_value, 2))}lbs.")
                    loop = 0
            elif input_type == "g" or input_type == "grams":
                if output_type.lower() == "kilograms" or output_type.lower() == "kg":
                    output_value = input_value * 1000
                    print(f"\n {str(input_value)}g = {str(round(output_value, 2))}lbs.")
                    loop = 0
                else:
                    output_value = input_value / 454
                    print(f"\n {str(input_value)}g = {str(round(output_value, 2))}lbs.")
                    loop = 0
            else:
                if output_type.lower() == "kg" or output_type.lower() == "kilograms":
                    output_value = input_value / 2.205
                    print(f"\n {str(input_value)}lbs = {str(round(output_value, 2))}Kg.")
                    loop = 0
                else:
                    output_value = input_value * 454
                    print(f"\n {str(input_value)}lbs = {str(round(output_value, 2))}g.")
                    loop = 0
        else:
            print("Incorrect spelling or measurement type. Please try again.")


def volume(input_type):
    volume_convert_array = volume_array
    if input_type.lower() == "l" or input_type.lower() == "litres":
        input_value = float(input("\nPlease enter how many Litres you wish to convert: "))
        volume_convert_array.remove("litres")
        volume_convert_array.remove("l")
    elif input_type.lower() == "ml" or input_type.lower() == "millilitres":
        input_value = float(input("\nPlease enter how many Millilitres you wish to convert: "))
        volume_convert_array.remove("millilitres")
        volume_convert_array.remove("ml")
    else:
        input_value = float(input("\nPlease enter how many Fluid Ounces you wish to convert: "))
        volume_convert_array.remove("fluid ounces")
        volume_convert_array.remove("fl oz")

    loop = 1
    while loop == 1:
        output_type = input("\nPlease enter what measurement type to convert to: ")
        if output_type.lower() in volume_convert_array:
            if input_type == "l" or input_type == "litres":
                if output_type.lower() == "millilitres" or output_type.lower() == "ml":
                    output_value = input_value * 1000
                    print(f"\n {str(input_value)}L = {str(round(output_value, 2))}ml.")
                    loop = 0
                else:
                    output_value = input_value * 35.195
                    print(f"\n {str(input_value)}L = {str(round(output_value, 2))}fl oz.")
                    loop = 0
            elif input_type == "millilitres" or input_type == "ml":
                if output_type.lower() == "litres" or output_type.lower() == "l":
                    output_value = input_value / 1000
                    print(f"\n {str(input_value)}ml = {str(round(output_value, 2))}L.")
                    loop = 0
                else:
                    output_value = input_value / 28.413
                    print(f"\n {str(input_value)}ml = {str(round(output_value, 2))}fl oz.")
                    loop = 0
            else:
                if output_type.lower() == "l" or output_type.lower() == "litres":
                    output_value = input_value / 35.195
                    print(f"\n {str(input_value)}fl oz = {str(round(output_value, 2))}L.")
                    loop = 0
                else:
                    output_value = input_value * 28.413
                    print(f"\n {str(input_value)}fl oz = {str(round(output_value, 2))}ml.")
                    loop = 0
        else:
            print("Incorrect spelling or measurement type. Please try again.")


def temperature(input_type):
    temp_convert_array = temperature_array
    if input_type.lower() == "c" or input_type.lower() == "celsius":
        input_value = float(input("\nPlease enter how many Celsius you wish to convert: "))
        temp_convert_array.remove("celsius")
        temp_convert_array.remove("c")
    else:
        input_value = float(input("\nPlease enter how many Fahrenheit you wish to convert: "))
        temp_convert_array.remove("fahrenheit")
        temp_convert_array.remove("f")

    loop = 1
    while loop == 1:
        output_type = input("\nPlease enter what measurement type to convert to: ")
        if output_type.lower() in temp_convert_array:
            if input_type == "c" or input_type == "celsius":
                output_value = ((input_value * (9/5)) + 32)
                print(f"\n {str(input_value)}C = {str(round(output_value, 2))}F.")
                loop = 0
            else:
                output_value = ((input_value - 32) * (9/5))
                print(f"\n {str(input_value)}F = {str(round(output_value, 2))}C.")
                loop = 0
        else:
            print("Incorrect spelling or measurement type. Please try again.")


menu()
input("\nPress Enter to continue...")
menu()
