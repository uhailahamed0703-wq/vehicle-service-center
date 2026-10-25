
vehicles = [
    "B1001ABC",
    "B2045DEF",
    "B1234XYZ",
    "D5678GHI",
    "F9012JKL"
]

search_number = "B1234XYZ"

for i in range(len(vehicles)):
    if vehicles[i] == search_number:
        print("Vehicle found at index:", i)
        break
else:
    print("Vehicle not found")
