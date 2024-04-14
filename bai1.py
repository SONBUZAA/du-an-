def KhoiTao():
    my_list = [2, 4, 6, 8, 10]
    return my_list

def HienThi(my_list):
    print("Giá trị của list:", my_list)

def Tong(my_list):
    total = sum(my_list)
    print("Tổng các phần tử trong list:", total)

def TimMaxMin(my_list):
    max_value = max(my_list)
    min_value = min(my_list)
    print("Phần tử lớn nhất trong list:", max_value)
    print("Phần tử nhỏ nhất trong list:", min_value)

def TimKiem(my_list, x):
    count_x = my_list.count(x)
    print(f"Số {x} xuất hiện {count_x} lần trong list.")

def main():
    my_list = KhoiTao()
    HienThi(my_list)
    Tong(my_list)
    TimMaxMin(my_list)
    
    x = int(input("Nhập số nguyên x: "))
    TimKiem(my_list, x)

if __name__ == "__main__":
    main()
