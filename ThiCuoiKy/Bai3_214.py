import math

# g) Kiểm tra số chính phương
chinh_phuong = lambda n: n >= 0 and int(math.sqrt(n)) ** 2 == n
n = int(input("Nhập n: "))
print("Là số chính phương:", chinh_phuong(n))

# i) Kiểm tra 3 cạnh có tạo thành tam giác không, và loại tam giác


