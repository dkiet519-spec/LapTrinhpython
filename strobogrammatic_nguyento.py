
#định nghĩa một hàm để kiểm tra xem một số có phải là số strobogrammatic hay không
def la_so_strobogrammatic(n):
    if n == 0:
        return True
    if n == 1:
        return n in strobogrammatic
    chuoi_n = str(n)
    left, right = 0, len(chuoi_n) - 1
    while left <= right:
        if chuoi_n[left] not in strobogrammatic or chuoi_n[right] not in strobogrammatic:
            return False
        if strobogrammatic[chuoi_n[left]] != chuoi_n[right]:
            return False
        left += 1
        right -= 1
    return True
strobogrammatic = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

#định nghĩa một hàm để kiểm tra xem một số strobogrammatic có phải là số nguyên tố hay không
def so_nguyen_to_strobogrammatic(n):
   if la_so_strobogrammatic(n):
       if n < 2:
           return False
       for i in range(2, int(n**0.5) + 1):
           if n % i == 0:
               return False
       return True
   
#điều kiện để in ra các số strobogrammatic nhỏ hơn 1000000
in_ra_so_nho_hon_1000000 = (1000000)
for i in range(in_ra_so_nho_hon_1000000):
    if so_nguyen_to_strobogrammatic(i):
        print(f"\n{i}")

