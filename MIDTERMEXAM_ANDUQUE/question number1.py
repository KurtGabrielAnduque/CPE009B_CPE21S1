def main():

    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp
    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32
    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15


    class FarhrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return  (self._temp - 32) * (5/9)

    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15



    tempInCelsius = float(input("Enter the temperature in Celsius: "))
    convert = CelsiusToKelvin(tempInCelsius)
    print(str(convert.conversion()) + " Kelvin")
    convert = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")


    print("\n")

    print("Farhrenheit to Celsius")

    tempInFarhrenheit = float(input("Enter the temperature in Fahrenheit: "))
    Fconvert = FarhrenheitToCelsius(tempInFarhrenheit)
    print(str(Fconvert.conversion()) + " Celsius")

    print("\n")

    print("Kelvin to Celsius")


    tempInKelvin = float(input("Enter the temperature in Kelvin: "))
    Kconvert = KelvinToCelsius(tempInKelvin)
    print(str(Kconvert.conversion()) + " Celsius")



main()