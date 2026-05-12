menhgia = [1,2,5,10,20,50,100,200,500]
def demtien(menhgia, tien):# def dùng trong trường hợp bên ngoài code muốn gọi lại
    print(f"----------------SỐ TIỀN {tien}được đổi thành----------")
    tong  = 0
    for i in reversed(menhgia):
        sotien = tien // i
        tien = tien % i
        tong += sotien 
        print (f"số tờ {i} là: {sotien}")#f giúp đưa dữ liệu vào cho đẹp không cần phải phẩy
    print("tổng số tờ cần đổi:", tong)    
    return tong

tien = int(input("Nhập số tiền: "))
print("Mệnh giá có sẵn:", menhgia)
demtien(menhgia, tien)



