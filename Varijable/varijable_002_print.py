consumption_per_km = 5.3 / 100    # litara / km  
fuel_price = 9.56    # kn / litri
days_in_month = 28
distance = 20    # km 

daily_consumption = consumption_per_km * distance * 2
daily_bill = daily_consumption * fuel_price
monthly_bill = daily_bill * days_in_month
# print(monthly_bill)

C = 10_000    # kn
t = 15    # godina 
p = 2.5 / 100 
# p = 0.025
k = C * p * t
print("Vaš prinos je: ", k)