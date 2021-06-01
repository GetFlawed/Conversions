def menu():
    print("""
    Menu
    
    Weight - (Kilograms (Kg), Grams (g), Pounds (lbs))
    Volume - (Litres (l), Millilitres (ml), Fluid Ounces (fl oz))
    Temperature - (Celsius (C), Fahrenheit (F))
    """)
    input_type = input("\nPlease select which measurement you wish to enter: ")
    weight_array = ("kilograms", "kg", "grams", "g", "pounds", "lbs", "weight")
    if input_type.lower() in weight_array:
        weight(input_type)
    elif input_type.lower() == "litres" or "l" or "millilitres" or "ml" or "fluid ounces" or "fl oz" or "volume":
        volume(input_type)
    elif input_type.lower() == "celsius" or "c" or "fahrenheit" or "f" or "temperature":
        temperature(input_type)
    else:
        print("Incorrect spelling or measurement type.")
        print("Please make sure to enter a measurement that is on the provided list")
        menu()


def weight(input_type):
    input_value = input("\nPlease enter how many Kg you wish to convert: ")


def volume(input_type):
    print("test2")


def temperature(input_type):
    print("test3")


menu()
