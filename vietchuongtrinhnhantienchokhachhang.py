a = int(input("Nhập số tiền hàng cần phải trả: "))
b = int(input("Nhập số tiền khách hàng đưa: "))

if a > b:
    print("Số tiền khách hàng đưa không đủ!")
else:
    tien_thua = b - a
    print(f"Số tiền thừa cần trả lại khách hàng: {tien_thua}đ")
    if a == b:
        print("Khách hàng đã trả đủ tiền, không cần trả lại!") 
    else:
        if  a < b:
            print("Khách hàng đã trả thừa tiền, cần trả lại!")

