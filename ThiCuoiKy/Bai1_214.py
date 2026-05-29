dai = float(input("Nhập chiều dài hình chữ nhật: "))
rong = float(input("Nhập chiều rộng hình chữ nhật: "))
cao = float(input("Nhập chiều cao hình chữ nhật: "))
so_luong_le = int(input("Số lượng lẻ: "))
#kiểm tra chiều dài
if dai >= 2.134:
    print(dai)
else:
    print("bạn phải nhập đúng số liệu")
    exit()

#kiểm tra chiều rộng
if rong >= 3.4567:
    print(rong)
else:
    print("bạn phải nhập đúng số liệu")
    exit()

#kiểm tra chiều cao
if cao >= 4.1:
    print(cao)
else:
    print("bạn nhập sai. bạn phải nhập đúng số liệu")
    exit()

#đếm các số lượng lẻ
dem = 0
i = 1
while dem < so_luong_le:
    if i % 2 != 0:
        print(i)
        dem += 1
    i += 1

#tính diện tích đấy và thể tích hình khối
S_chunhat = dai * rong
V_chunhat = S_chunhat * cao

#trả về kết quả
print("Diện tích hình chữ nhật:", S_chunhat)  # thêm dòng này
print("Thể tích hình chữ nhật:", V_chunhat)   # thêm dòng này