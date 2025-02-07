TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("electricity bill estimator")
choice_of_tariff = input("Which tariff? 11 or 31: ")

if choice_of_tariff == "11":
    price_per_kwh = TARIFF_11
else:
    price_per_kwh = TARIFF_31

daily_use_kWh = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days:"))


estimated_bill = price_per_kwh * daily_use_kWh * billing_days
print(f"Estimated bill: $ {estimated_bill:.2f}")