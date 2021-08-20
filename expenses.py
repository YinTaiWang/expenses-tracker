import os
products = []

if os.path.isfile("expenses.csv"):
	# 讀取舊檔案
	with open("expenses.csv", "r") as f:
		for line in f:
			if "My Expenses Tracker" or "Products" and "Price" in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
else:
	print("Create a new file")
	# 初始建立檔案
	with open("expenses.csv", "w") as f:
		f.write("My Expenses Tracker" + '\n')
		f.write("Products" + "," + "Price" + "\n")


# 使用者新增項目
print("Type 'q' to exit")
while True:
	name = input("Products: ")
	if name == "q":
		break
	price = input("Price: ")
	products.append([name, price])
print("Save file!")
with open("expenses.csv", "a") as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')