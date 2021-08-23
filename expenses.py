import os
products = []

# 檔案名稱
def file_n():
    file_n = input("File name: ")
    file_n = file_n + ".csv"
    return file_n

# 讀取檔案
def read_file(filename):
    with open(filename, "r") as f:
        for line in f:
            if "My Expenses Tracker" or "Products" and "Price" in line:
                continue
            name, price = line.strip().split(",")
            products.append([name, price])
    return products

# 建立初始檔案
def create_file(filename):
    print("Create a new file")
    with open(filename, "w") as f:
        f.write("My Expenses Tracker" + "\n")
        f.write("Products" + "," + "Price" + "\n")

# 使用者新增項目
def user_input(products):
    print("Type 'q' to exit")
    while True:
        name = input("Products: ")
        if name == "q":
            break
        price = input("Price: ")
        products.append([name, price])
    print("Save file!")
    return products

# 寫入檔案
def write_file(filename, products):
    with open(filename, "a") as f:
        for p in products:
            f.write(p[0] + "," + p[1] + "\n")

def main():
    import os
    while True:
        work = input('Create/Open a file:')
        if work == "create":
            file_n = file_n()
            create_file(file_n)
            products = user_input(products)
            write_file(file_n, products)
            break
        elif work == "open":
            while True:
                n = file_n()
                if os.path.isfile(n):
                    read_file(n)
                    products = user_input(products)
                    write_file(n, products)
                    break       
                else:
                    print("Can't find the file. Or please delete the file extension.")
            break
        else:
            print('Please input create/open.')

main()