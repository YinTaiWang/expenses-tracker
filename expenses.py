# 檔案名稱
def file_name():
    file_name = input("File name: ")
    file_name = f'{file_name}.csv'
    return file_name

# 讀取檔案
def read_file(filename):
    products = []
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
    products = []
    while True:
        work = input('Create/Open a file:')
        if work == "create":
            new_file_name = file_name()
            create_file(new_file_name)
            new_products = user_input(products)
            write_file(new_file_name, new_products)
            break
        elif work == "open":
            while True:
                old_file_name = file_name()
                if os.path.isfile(old_file_name):
                    read_file(old_file_name)
                    new_products = user_input(products)
                    write_file(old_file_name, new_products)
                    break       
                else:
                    print("Can't find the file. Or please delete the file extension.")
            break
        else:
            print('Please input create/open.')

main()