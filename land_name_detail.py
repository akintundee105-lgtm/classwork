plot_size = float(input("Enter plot size in square meters: "))
price_per_sqm = float(input("Enter price per square meter: "))
location_type = input("Enter location type(Urban, Suburban, Rural): ")

total_price = plot_size * price_per_sqm
if location_type == "Urban":
   total_price = total_price + (total_price * 0.15)
elif location_type == "Suburban":
     total_price = total_price + (total_price * 0.10)
elif location_type == "Rural":
     total_price = total_price
else:
    print("Invalid location_type entered.")

if total_price > 70000000:
   approval_status = "Requires Governor's Approval"
elif total_price > 40000000:
     approval_status = "Requires Governor's Approval"
else:
    approval_status = "Approved by local"

print("\n Land Detail Name:")
print("Total Price: Naira", total_price)
print("Location Type:", location_type)
print("Plot Size:", plot_size)
print("Price Per sqm: Naira", price_per_sqm)