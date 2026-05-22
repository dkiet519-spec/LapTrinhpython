import math

# a) Số thân thiện: gcd(n, số đảo ngược của n) = 1
so_than_thien = lambda n: math.gcd(n, int(str(n)[::-1])) == 1

# b) Số chính phương
so_chinh_phuong = lambda n: int(math.sqrt(n)) ** 2 == n

# c) Số đồng nhất: các chữ số đều giống nhau
so_dong_nhat_all = lambda n: all(ch == str(n)[0] for ch in str(n))
so_dong_nhat_any = lambda n: not any(ch != str(n)[0] for ch in str(n))

# d) Số hoàn thiện: tổng ước không kể chính nó bằng n
so_hoan_thien = lambda n: n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) == n

# e) Số phong phú: tổng ước không kể chính nó lớn hơn n
so_phong_phu = lambda n: n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) > n



# ==========================
# IN KẾT QUẢ TỪ 1 ĐẾN 1 TRIỆU
# ==========================

print("Nhập một số nguyên dương N (1 <= N <= 1,000,000): ")
N = int(input())

print("a) Số thân thiện:")
print([i for i in range(1, N + 1) if so_than_thien(i)])

print("\nb) Số chính phương:")
print([i for i in range(1, N + 1) if so_chinh_phuong(i)])

print("\nc) Số đồng nhất:")
print([i for i in range(1, N + 1) if so_dong_nhat_all(i)])

print("\nd) Số hoàn thiện:")
print([i for i in range(1, N + 1) if so_hoan_thien(i)])

print("\ne) Số phong phú:")
print([i for i in range(1, N + 1) if so_phong_phu(i)])

