dayso = []
while True:
    n = int(input("nhập một số nguyên dương: "))
    dayso.append(n) 
    nhapthem = input("Bạn có muốn nhập thêm số không? (y/n): ")
    if nhapthem.upper() != 'Y':
        break
print ("Dãy số bạn đã nhập là: ", dayso)

daysoduong = [x for x in dayso if x > 0] #lọc ra các số dương trong dãy số

daysoam = [x for x in dayso if x < 0] #lọc ra các số âm trong dãy số

tongduong = sum(daysoduong) #tính tổng các số dương
print("Tổng các số dương là: ", tongduong)
tongam = sum(daysoam) #tính tổng các số âm
print("Tổng các số âm là: ", tongam)

lonnhat = max(dayso) #tìm số lớn nhất trong dãy số
print("Số lớn nhất là: ", lonnhat)
nhonhat = min(dayso) #tìm số nhỏ nhất trong dãy số
print("Số nhỏ nhất là: ", nhonhat)