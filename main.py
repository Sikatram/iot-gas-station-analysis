from methods import Methods
from print_methods import PrintMethods

print("\n\nReport for Mobil Downtown Devices\n")
PrintMethods.printLine()
Methods.greaterThanASecond('data/mobil_downtown.csv')
PrintMethods.printLine()
Methods.greaterThanThirtySeconds('data/mobil_downtown.csv')
PrintMethods.printLine()
Methods.greaterThanAMinute('data/mobil_downtown.csv')
PrintMethods.printLine()
Methods.greaterThanFifteenMinutes('data/mobil_downtown.csv')

PrintMethods.printNextSection()

print("Report for Mobil Outskirt Devices\n")
PrintMethods.printLine()
Methods.greaterThanASecond('data/mobil_outskirts.csv')
PrintMethods.printLine()
Methods.greaterThanThirtySeconds('data/mobil_outskirts.csv')
PrintMethods.printLine()
Methods.greaterThanAMinute('data/mobil_outskirts.csv')
PrintMethods.printLine()
Methods.greaterThanFifteenMinutes('data/mobil_outskirts.csv')

PrintMethods.printNextSection()

print("Report for Varso Outskirt Devices\n")
PrintMethods.printLine()
Methods.greaterThanASecond('data/varso_gas.csv')
PrintMethods.printLine()
Methods.greaterThanThirtySeconds('data/varso_gas.csv')
PrintMethods.printLine()
Methods.greaterThanAMinute('data/varso_gas.csv')
PrintMethods.printLine()
Methods.greaterThanFifteenMinutes('data/varso_gas.csv')

PrintMethods.printNextSection()
print("\nprogram complete")
