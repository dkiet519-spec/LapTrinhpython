import math

# a) Trị tuyệt đối của n
tuyet_doi = lambda n: abs(n)
a = int(input("Nhập n: "))
print("Trị tuyệt đối:", tuyet_doi(a))

# b) Giá trị n + 15
cong15 = lambda n: n + 15
b = int(input("Nhập n: "))
print("n + 15 =", cong15(b))

# c) Tích của x và y
tich = lambda x, y: x * y
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
print("Tích x*y =", tich(x, y))

# d) Kiểm tra bội số của 13 hoặc 19
boi_so = lambda n: n % 13 == 0 or n % 19 == 0
n = int(input("Nhập n: "))
print("Là bội của 13 hoặc 19:", boi_so(n))

# e) Diện tích hình tròn
dien_tich_tron = lambda r: math.pi * r ** 2
r = float(input("Nhập bán kính r: "))
print("Diện tích hình tròn:", dien_tich_tron(r))

# f) Chu vi hình chữ nhật
chu_vi_hcn = lambda d, r: 2 * (d + r)
d = float(input("Nhập chiều dài d: "))
r = float(input("Nhập chiều rộng r: "))
print("Chu vi hình chữ nhật:", chu_vi_hcn(d, r))

# g) Kiểm tra số chính phương
chinh_phuong = lambda n: n >= 0 and int(math.sqrt(n)) ** 2 == n
n = int(input("Nhập n: "))
print("Là số chính phương:", chinh_phuong(n))

# h) Kiểm tra số nguyên tố
nguyen_to = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))
n = int(input("Nhập n: "))
print("Là số nguyên tố:", nguyen_to(n))

# i) Kiểm tra 3 cạnh có tạo thành tam giác không, và loại tam giác
