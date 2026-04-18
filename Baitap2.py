while True:
    print ("==Menu chon bài toán bạn muốn==")
    print ("1. so luong chan va so le")
    print ("2. tong so luong so chan va so le")
    print ("3. tich so chan va so le")
    print ("6. Thoat")
    
    chosse = int(input("Nhap lua chon cua ban: "))
    if chosse == 1:
        n = int (input("Nhap luong so: "))
        chan= 0
        le = 0
        i = 1
        while n > 0:
            chuso = n % 10
            if chuso % 2 == 0:
                chan += 1   
            else:
                le += 1
            n //= 10
        print("So luong so chan la: ", chan)
        print("So luong so le la: ", le)        
        
    elif chosse == 2:
        n = int (input("Nhap luong so: "))
        chuso = n
        tong = 0
        while n > 0:
            chuso = n % 10
            if chuso % 2 == 0:
                tong = tong + ( chuso % 10)   
                chuso //= 10
        print("Tong so luong so chan va so le la: ", tong)

