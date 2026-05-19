# Định nghĩa một hàm để kiểm tra xem một số có phải là số strobogrammatic hay không
#strobogrammat là các số có hình dạng giống nhau khi được lật ngược lại, ví dụ như 69, 88, 818, v.v. Các cặp số strobogrammatic bao gồm: (0, 0), (1, 1), (6, 9), và (8, 8).
from numpy import put


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
# --- Kiểm tra ---
a = int(input("Nhập một số: "))
if la_so_strobogrammatic(a):
    print(f"{a} là số strobogrammatic.")
else:
    print(f"{a} không phải là số strobogrammatic.")