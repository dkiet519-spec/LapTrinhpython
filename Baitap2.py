n = int (input("Nhap luong so: "))
chan= 0
le = 0
i = 1
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        chan += 1   
    else:
        le += 1
    n //= 10
print("So luong so chan la: ", chan)
print("So luong so le la: ", le)
