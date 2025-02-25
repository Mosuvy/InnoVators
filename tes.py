# tes = "woi"
# print(tes)

# print([x**2 for x in [1, 2, 3, 4, 5]])

# array = [1,2,3,4,5]
# for angka in array:
#     print(angka ** 2)



# for angka in array:
#     if angka % 2 == 0:
#         print("genap")
#     else: 
#         print("ganjil")



# list_array = [[1,2,3], [2,3,4], [3,4,5]]
# hasil = [sum(sublist) for sublist in list_array]
# print(hasil)



# Input = [800, 600, 400, 200]
# Compared_input = {500, 200, 400}

# for i, angka in enumerate(Input):
#     Input[i] = 1 if angka in Compared_input else 0

# print(Input)



# Input = [
#     {'nama': 'Budi', 'gaji': 5000},
#     {'nama': 'Dwi', 'gaji': 8000},
#     {'nama': 'Joko', 'gaji': 6000}
# ]

# total_salary = sum(item['gaji'] for item in Input)

# highest_salary = max(Input, key=lambda x: x['gaji'])['nama']

# Output = {
#     "highest_salary": highest_salary,
#     "total_salary": total_salary
# }

# print(Output)



# input_data = {
#     "Indoramet": {
#         "Ayam": 30000,
#         "Sayur": 15000,
#         "Buah": 20000,
#         "Ikan": 22000
#     },
#     "Alfaramet": {
#         "Ayam": 25000,
#         "Sayur": 12000,
#         "Buah": 30000,
#         "Ikan": 25000
#     }
# }
# items_to_buy = {
#     "Ayam": 2,
#     "Sayur": 1,
#     "Ikan": 1
# }

# cheapest_prices = {}
# for item in items_to_buy:
#     harga_indoramet = input_data["Indoramet"].get(item, float('inf'))
#     harga_alfaramet = input_data["Alfaramet"].get(item, float('inf'))
#     cheapest_prices[item] = min(harga_indoramet, harga_alfaramet)

# total_cost = sum(cheapest_prices[item] * items_to_buy[item] for item in items_to_buy)

# print("Output =", total_cost)
# print("\nRincian:")
# for item in items_to_buy:
#     print(f"{item} : {items_to_buy[item]} * {cheapest_prices[item]} = {items_to_buy[item] * cheapest_prices[item]}")



x = float(input("Masukkan Angka Pertama: "))
y = float(input("Masukkan Angka Kedua: "))  
op = input("Masukkan Operator (+, -, /, *): ")

# if op == "+":
#     print(f"Hasil dari {x} + {y} = {x + y}")
# elif op == "-":
#     print(f"Hasil dari {x} - {y} = {x - y}")
# elif op == "*":
#     print(f"Hasil dari {x} * {y} = {x * y}")
# elif op == "/":
#     if y != 0:
#         print(f"Hasil dari {x} / {y} = {x / y}")
#     else:
#         print("Error: Pembagian dengan nol tidak diperbolehkan!")
# else:
#     print("Operator tidak valid! Gunakan +, -, *, atau /.")
    
# versi lambda
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Error: Pembagian dengan nol tidak diperbolehkan!"
}

if op in operations:
    hasil = operations[op](x, y)
    print(f"Hasil dari {x} {op} {y} = {hasil}")
else:
    print("Operator tidak valid! Gunakan +, -, *, atau /.")
    