"""
consumption_per_km = input("Input consumption per km: ")    # litara / km
consumption_per_km = float(consumption_per_km)
consumption_per_km /= 100

fuel_price = input("What is the fuel price? ")    # kn / litri
fuel_price = float(fuel_price)

days_in_month = input("How many days in a month are you going to work? ")
days_in_month = int(days_in_month)

distance = input("What is your distance to work? ")    # km
distance = float(distance)

daily_consumption = consumption_per_km * distance * 2
daily_bill = daily_consumption * fuel_price
monthly_bill = daily_bill * days_in_month
print("Based on your distance to work which is ", round(distance, 0), " and the ", days_in_month,
      " days of going to work, your monthly bill would be ", monthly_bill, " hrk")
"""
C = float(input("Unesite iznos glavnice: "))   # kn
t = int(input("Unesite broj godina: "))    # godina
p = float(input("Unesite godisnju kamatnu stopu: "))
p = p / 100
# p = 0.025
k = C * p * t
print("Vaš prinos je: ", k)

