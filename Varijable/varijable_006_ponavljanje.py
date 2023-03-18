'''
consumption_per_km = input("Unesite Vašu potrošnju litara na 100 km: ")   # 5.3 / 100    # litara / km
consumption_per_km = float(consumption_per_km)
consumption_per_km /= 100
#consumption_per_km = consumption_per_km / 100
print(consumption_per_km)

fuel_price = input("Unesite cijenu goriva po litri: ")
fuel_price = float(fuel_price)

days_in_month = input("Unesite broj dana: ")
days_in_month = int(days_in_month)

distance = float(input("Unesite udaljenost do lokacije: "))
#distance = float(distance)


daily_consumption = consumption_per_km * distance * 2
daily_bill = daily_consumption * fuel_price
monthly_bill = daily_bill * days_in_month
#print(monthly_bill)


print("Potrošnja po litri: ", consumption_per_km)
print("Cijena goriva po litri: ", fuel_price)
print("Broj radnih dana u mjesecu: ", days_in_month)
print("Udaljenost do lokacije: ", distance)
print("-"*50)
print("Ukupni mjesečni trošak: ", round(monthly_bill, 2))
'''

'''
C = 10_000    # kn
t = 15    # godina
p = 2.5 / 100
'''
C = float(input("Unesite iznos glavnice: "))
p = float(input("Unesite godišnju kamatnu stopu u postotcima: "))
p = p/100
t = int(input("Unesite broj godina: "))


k = C * p * t
print("-"*50)
print("Vaš prinos je: ", k)



