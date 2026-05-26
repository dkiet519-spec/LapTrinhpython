while True:
    print("Tổ chức và xây dựng các hàm")
    print("1. nhập 2 số nguyên a và b cách nhau bởi dấu phẩy , in ra bảng cửu chương từ a đến b (a<b) or từ b đến a (b<a)")
    print("2. kiểm tra n có phải số nguyên tố không")
    print("3.liêt kê các số nguyên tố lớn hơn n")
    print("4. Đếm các số nguyên tố lớn hơn n")
    print("5. liệt kê các ước số của n là các số nguyên tố")
    print("0. Thoát")
    
    choice = input("Vui lòng chọn một tùy chọn: ")
    
    if choice == '1':
       a = int(input("Nhập số nguyên a: "))
       b = int(input("Nhập số nguyên b: "))
       if a < b:
            for i in range(a, b + 1):
                    print(f"Bảng cửu chương của {i}:")
                    for j in range(1, 11):
                         print(f"{i} x {j} = {i * j}")
                    print()
       else:
            for i in range(b, a + 1):
                print(f"Bảng cửu chương của {i}:")
                for j in range(1, 11):
                     print(f"{i} x {j} = {i * j}")
                print()
                #print() là để tạo một dòng trống giữa các bảng cửu chương để dễ đọc hơn
        
             
    elif choice == '2':
        n = int(input ("nhập số nguyên n: "))
        if n < 2:
            print(f"{n} không phải là số nguyên tố.")
        else:
            la_so = True
            for i in range(2, int(n**0.5) + 1):#chỉ cần kiểm tra đến √n, vì nếu n có ước > √n thì ước còn lại < √n đã được kiểm tra rồi (√ là **0.5) 
                if n % i == 0:
                    la_so = False
                    break
                
            if la_so:
                print(f"{n} là số nguyên tố.")
            else:
                print(f"{n} không phải là số nguyên tố.")
                
    elif choice == '3':
        n = int(input("Nhập số nguyên n: "))
        print(f"Các số nguyên tố lớn hơn {n} là:")
        for i in range(n + 1, n + 50): #liệt kê 50 số nguyên tố tiếp theo sau n
            #n+1 để bắt đầu từ số ngay sau n, n+50 để giới hạn phạm vi tìm kiếm (có thể điều chỉnh nếu muốn tìm nhiều hơn hoặc ít hơn)
            if i < 2:
                continue
            la_so = True
            for j in range(2, int(i**0.5) + 1):
                #kiểm tra xem i có phải là số nguyên tố hay không bằng cách kiểm tra xem i có chia hết cho bất kỳ số nào từ 2 đến √i hay không
                if i % j == 0:
                    la_so = False
                    break
            if la_so:
                print(i)
    
    elif choice == '4':
        n = int(input("Nhập số nguyên n: "))
        dem = 0
        for i in range(n + 1, n + 50): #đếm số nguyên tố trong phạm vi từ n+1 đến n+50
            if i < 2:
                continue
            la_so = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    la_so = False
                    break
            if la_so:
                dem += 1
        print(f"Số lượng số nguyên tố lớn hơn {n} là: {dem}")
        
        
        
    elif choice == '5':
        n = int(input("Nhập số nguyên n: "))
        print(f"Các ước số của {n} là các số nguyên tố:")
        for i in range(2, n + 1):#kiểm tra tất cả các số từ 2 đến n để tìm ước số của n, vì 1 không phải là ước số nguyên tố và n cũng không cần kiểm tra vì nó không phải là ước số của chính nó
            if n % i == 0:
                la_so = True
                for j in range(2, int(i**0.5) + 1):
                    if i % j == 0:
                        la_so = False
                        break
                if la_so:
                    print(i)

    elif choice == '0':
        print("Cảm ơn bạn đã sử dụng chương trình. Hẹn gặp lại!")
        break
        
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
    