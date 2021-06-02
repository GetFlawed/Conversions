class Weight:
    def __init__(self, kg_pounds, kg_grams, g_kilograms, g_pounds, lbs_kilograms, lbs_grams):
        self.kg_pounds = kg_pounds * 2.205
        self.kg_grams = kg_grams * 1000
        self.g_kilograms = g_kilograms / 1000
        self.g_pounds = g_pounds / 454
        self.lbs_kilograms = lbs_kilograms / 2.205
        self.lbs_grams = lbs_grams * 454


class Volume:
    def __init__(self, l_millilitres, l_fluid_ounces, ml_litres, ml_fluid_ounces, fl_oz_litres, fl_oz_millilitres):
        self.l_millilitres = l_millilitres * 1000
        self.l_fluid_ounces = l_fluid_ounces * 35.195
        self.ml_litres = ml_litres / 1000
        self.ml_fluid_ounces = ml_fluid_ounces / 28.413
        self.fl_oz_litres = fl_oz_litres / 35.195
        self.fl_oz_millilitres = fl_oz_millilitres * 28.413


class Temp:
    def __init__(self, c_fahrenheit, c_kelvin, f_celsius, f_kelvin, k_fahrenheit, k_celsius):
        self.c_fahrenheit = (c_fahrenheit * (9 / 5)) + 32
        self.c_kelvin = c_kelvin + 273.15
        self.f_celsius = ((f_celsius - 32) * (5 / 9))
        self.f_kelvin = ((f_kelvin - 32) * (5 / 9)) + 273.15
        self.k_fahrenheit = ((k_fahrenheit - 273.15) * (9 / 5)) + 32
        self.k_celsius = k_celsius - 273.15
