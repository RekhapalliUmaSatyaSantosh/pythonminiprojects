# while True:
#     print("\n=== UNIT CONVERTER ===")
#     print("1. Length (meters, feet, inches, kilometers, miles)")
#     print("2. Weight (grams, kilograms, pounds, ounces)")
#     print("3. Temperature (Celsius, Fahrenheit, Kelvin)")
#     print("4. Exit")
#     choice = input("Enter your Choice: ")
#     if choice == '1':
#         print("\n=== Length Converter ===")
#         print("1. Meters → Feet")
#         print("2. Feet → Meters")
#         print("3. Kilometers → Miles")
#         print("4. Miles → Kilometers")
#         print("5. Inches → Centimeters")
#         print("6. Centimeters → Inches")
#         choose = input("Choose (1-6): ")
#         if choose == '1':
#             value = float(input("Enter value in meters: "))
#             result = value * 3.28084
#             print(f"\n{value} meters = {result:.2f} feet")    
#         elif choose == '2':
#             value = float(input("Enter value in feet: "))
#             result = value / 3.28084
#             print(f"\n{value} feet = {result:.2f} meters")
#         elif choose == '3':
#             value = float(input("Enter value in kilometers: "))
#             result = value * 0.621371
#             print(f"\n{value} kilometers = {result:.2f} miles")
#         elif choose == '4':
#             value = float(input("Enter value in miles: "))
#             result = value / 0.621371
#             print(f"\n{value} miles = {result:.2f} kilometers")
#         elif choose == '5':
#             value = float(input("Enter value in inches: "))
#             result = value * 2.54
#             print(f"\n{value} inches = {result:.2f} centimeters")
#         elif choose == '6':
#             value = float(input("Enter value in centimeters: "))
#             result = value / 2.54
#             print(f"\n{value} centimeters = {result:.2f} inches")
#         else:
#             print("Invalid choice!")
#     elif choice == '2':
#         print("\n=== Weight Converter ===")
#         print("1. Kilograms → Pounds")
#         print("2. Pounds → Kilograms")
#         print("3. Grams → Ounces")
#         print("4. Ounces → Grams")
#         print("5. Kilograms → Grams")
#         print("6. Grams → Kilograms")
#         choose = input("Choose (1-6): ")
#         if choose == '1':
#             value = float(input("Enter value in kilograms: "))
#             result = value * 2.20462
#             print(f"\n{value} kilograms = {result:.2f} pounds")
#         elif choose == '2':
#             value = float(input("Enter value in pounds: "))
#             result = value / 2.20462
#             print(f"\n{value} pounds = {result:.2f} kilograms")
#         elif choose == '3':
#             value = float(input("Enter value in grams: "))
#             result = value / 28.3495
#             print(f"\n{value} grams = {result:.2f} ounces")
#         elif choose == '4':
#             value = float(input("Enter value in ounces: "))
#             result = value * 28.3495
#             print(f"\n{value} ounces = {result:.2f} grams")
#         elif choose == '5':
#             value = float(input("Enter value in kilograms: "))
#             result = value * 1000
#             print(f"\n{value} kilograms = {result:.2f} grams")
#         elif choose == '6':
#             value = float(input("Enter value in grams: "))
#             result = value / 1000
#             print(f"\n{value} grams = {result:.2f} kilograms")
#         else:
#             print("Invalid choice!")
#     elif choice == '3':
#         print("\n=== Temperature Converter ===")
#         print("1. Celsius → Fahrenheit")
#         print("2. Fahrenheit → Celsius")
#         print("3. Celsius → Kelvin")
#         print("4. Kelvin → Celsius")
#         print("5. Fahrenheit → Kelvin")
#         print("6. Kelvin → Fahrenheit")
#         choose = input("Choose (1-6): ")
#         if choose == '1':
#             value = float(input("Enter temperature in Celsius: "))
#             result = (value * 9/5) + 32
#             print(f"\n{value}°C = {result:.2f}°F") 
#         elif choose == '2':
#             value = float(input("Enter temperature in Fahrenheit: "))
#             result = (value - 32) * 5/9
#             print(f"\n{value}°F = {result:.2f}°C") 
#         elif choose == '3':
#             value = float(input("Enter temperature in Celsius: "))
#             result = value + 273.15
#             print(f"\n{value}°C = {result:.2f} K")  
#         elif choose == '4':
#             value = float(input("Enter temperature in Kelvin: "))
#             result = value - 273.15
#             print(f"\n{value} K = {result:.2f}°C")    
#         elif choose == '5':
#             value = float(input("Enter temperature in Fahrenheit: "))
#             celsius = (value - 32) * 5/9
#             result = celsius + 273.15
#             print(f"\n{value}°F = {result:.2f} K")      
#         elif choose == '6':
#             value = float(input("Enter temperature in Kelvin: "))
#             celsius = value - 273.15
#             result = (celsius * 9/5) + 32
#             print(f"\n{value} K = {result:.2f}°F")       
#         else:
#             print("Invalid choice!")
#     elif choice == '4':
#         print("\nThanks for using Unit Converter! Goodbye!")
#     else:
#         print("Invalid choice! Please select 1, 2, 3, or 4")
#     again = input("\nDo another conversion? (y/n): ").lower()
#     if again != 'y':
#         print("Thanks for using Unit Converter!")
#         break

class UnitConverter:

    def main_menu(self):
        print("\n" + "=" * 45)
        print("              UNIT CONVERTER")
        print("=" * 45)
        print("1. Length Converter")
        print("2. Weight Converter")
        print("3. Temperature Converter")
        print("4. Exit")
        print("=" * 45)

    def length_menu(self):
        print("\n" + "-" * 45)
        print("             LENGTH CONVERTER")
        print("-" * 45)
        print("1. Meters      → Feet")
        print("2. Feet        → Meters")
        print("3. Kilometers  → Miles")
        print("4. Miles       → Kilometers")
        print("5. Inches      → Centimeters")
        print("6. Centimeters → Inches")
        print("-" * 45)

    def weight_menu(self):
        print("\n" + "-" * 45)
        print("             WEIGHT CONVERTER")
        print("-" * 45)
        print("1. Kilograms → Pounds")
        print("2. Pounds    → Kilograms")
        print("3. Grams     → Ounces")
        print("4. Ounces    → Grams")
        print("5. Kilograms → Grams")
        print("6. Grams     → Kilograms")
        print("-" * 45)

    def temperature_menu(self):
        print("\n" + "-" * 45)
        print("          TEMPERATURE CONVERTER")
        print("-" * 45)
        print("1. Celsius    → Fahrenheit")
        print("2. Fahrenheit → Celsius")
        print("3. Celsius    → Kelvin")
        print("4. Kelvin     → Celsius")
        print("5. Fahrenheit → Kelvin")
        print("6. Kelvin     → Fahrenheit")
        print("-" * 45)

    def length_converter(self):
        self.length_menu()
        choice = input("Choose (1-6): ")

        value = float(input("Enter value: "))

        if choice == '1':
            result = value * 3.28084
            print(f"\n✓ {value} meters = {result:.2f} feet")
        elif choice == '2':
            result = value / 3.28084
            print(f"\n✓ {value} feet = {result:.2f} meters")
        elif choice == '3':
            result = value * 0.621371
            print(f"\n✓ {value} kilometers = {result:.2f} miles")
        elif choice == '4':
            result = value / 0.621371
            print(f"\n✓ {value} miles = {result:.2f} kilometers")
        elif choice == '5':
            result = value * 2.54
            print(f"\n✓ {value} inches = {result:.2f} centimeters")
        elif choice == '6':
            result = value / 2.54
            print(f"\n✓ {value} centimeters = {result:.2f} inches")
        else:
            print("❌ Invalid choice!")

    def weight_converter(self):
        self.weight_menu()
        choice = input("Choose (1-6): ")

        value = float(input("Enter value: "))

        if choice == '1':
            result = value * 2.20462
            print(f"\n✓ {value} kilograms = {result:.2f} pounds")
        elif choice == '2':
            result = value / 2.20462
            print(f"\n✓ {value} pounds = {result:.2f} kilograms")
        elif choice == '3':
            result = value / 28.3495
            print(f"\n✓ {value} grams = {result:.2f} ounces")
        elif choice == '4':
            result = value * 28.3495
            print(f"\n✓ {value} ounces = {result:.2f} grams")
        elif choice == '5':
            result = value * 1000
            print(f"\n✓ {value} kilograms = {result:.2f} grams")
        elif choice == '6':
            result = value / 1000
            print(f"\n✓ {value} grams = {result:.2f} kilograms")
        else:
            print("❌ Invalid choice!")

    def temperature_converter(self):
        self.temperature_menu()
        choice = input("Choose (1-6): ")

        value = float(input("Enter temperature: "))

        if choice == '1':
            result = (value * 9 / 5) + 32
            print(f"\n✓ {value}°C = {result:.2f}°F")
        elif choice == '2':
            result = (value - 32) * 5 / 9
            print(f"\n✓ {value}°F = {result:.2f}°C")
        elif choice == '3':
            result = value + 273.15
            print(f"\n✓ {value}°C = {result:.2f} K")
        elif choice == '4':
            result = value - 273.15
            print(f"\n✓ {value} K = {result:.2f}°C")
        elif choice == '5':
            celsius = (value - 32) * 5 / 9
            result = celsius + 273.15
            print(f"\n✓ {value}°F = {result:.2f} K")
        elif choice == '6':
            celsius = value - 273.15
            result = (celsius * 9 / 5) + 32
            print(f"\n✓ {value} K = {result:.2f}°F")
        else:
            print("❌ Invalid choice!")

    def run(self):
        while True:
            self.main_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.length_converter()
            elif choice == '2':
                self.weight_converter()
            elif choice == '3':
                self.temperature_converter()
            elif choice == '4':
                print("\nThanks for using Unit Converter!")
                break
            else:
                print("❌ Invalid choice!")

            again = input("\nDo another conversion? (y/n): ").lower()
            if again != 'y':
                print("\nThanks for using Unit Converter!")
                break


obj = UnitConverter()
obj.run()
