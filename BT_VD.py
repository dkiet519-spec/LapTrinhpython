import math
a = float(input("Nhap chieu dai: "))
b = float(input("Nhap chieu rong: "))
c = float(input("Nhap chieu cao: "))
n = int(input("Nhap Số lượng số lẻ cần hiển thị : "))
dem=0
i = 1
while dem < n:
    if i % 2 != 0:
        print(i)
        dem += 1# dem này sẽ đếm số lượng số lẻ đã hiển thị, khi dem ko phải lẻ thì dừng
    i += 1# i này sẽ chạy qua từng số 
Schunhat = a*b
Vchunhat = Schunhat*c# tính thể tích hình chữ nhật
print ("Dien tich hinh chu nhat = ",Schunhat)
print ("The tich hinh chu nhat = ",Vchunhat)

