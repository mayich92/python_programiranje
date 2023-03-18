first_name = "Marko"
surname = "Marić"
year_of_birth = 1992
birth_country = "Hrvatska"
emplyment_status = "employed full time"
weight = 80
gender = "m"
print(first_name, surname, weight)
full_name= first_name + " " + surname
print(full_name)
 
a = 2
b = 5
P = a * b 

print(a , b ,P)

electricity_price = 0.982    # kn za 1 kwH
device_power = 1.3    # kW
daily_usage = 2    # h
DAYS_IN_MONTH = 30 
TAX = 1.25

monthly_consumption = DAYS_IN_MONTH * daily_usage * device_power
monthly_bill = monthly_consumption * electricity_price
monthly_bill_with_tax = monthly_bill * TAX
# print(monthly_consumption, monthly_bill,monthly_bill_with_tax,birth_country)
print("Mjesečni račun za struju s porezom:", monthly_bill_with_tax, "kn")

