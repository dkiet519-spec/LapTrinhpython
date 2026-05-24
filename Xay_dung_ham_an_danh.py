import math
#Nhập thư viện math có sẵn trong Python. Dùng để gọi các hàm toán học như math.gcd() (ước chung lớn nhất) và math.sqrt() (căn bậc hai).

# a) Số thân thiện: gcd(n, số đảo ngược của n) = 1
so_than_thien = lambda n: math.gcd(n, int(str(n)[::-1])) == 1
#lambda :tạo hàm nhanh nhận tham số n
#int() trong trường hợp này để chuyển các  phần chuyển số thành số
# str(n)[::-1] : đảo ngược chuỗi biểu diễn số n
# math.gcd() : tính ước chung lớn nhất của n và số đảo ngược của n, nếu kết quả là 1 thì n là số thân thiện.
#== 1 là cho 2 số là số thân thiện


# b) Số chính phương
so_chinh_phuong = lambda n: int(math.sqrt(n)) ** 2 == n
#math .sqrt(n) : tính căn bậc hai của n
#int trong trường hợp này để lấy phần nguyên của căn bậc hai
#** 2 để kiểm tra xem bình phương của phần nguyên có bằng n hay không, nếu bằng thì n là số chính phương.

# c) Số đồng nhất: các chữ số đều giống nhau
so_dong_nhat_tatca = lambda n: all(ch == str(n)[0] for ch in str(n))
so_dong_nhat_mot_vai = lambda n: not any(ch != str(n)[0] for ch in str(n))
#str(n) : chuyển số n thành chuỗi để có thể duyệt qua từng chữ số
#all  :kiểm tra xem tất cả các chữ số có giống nhau hay không bằng cách so sánh mỗi chữ số với chữ số đầu tiên (str(n)[0]).
#any : kiểm tra xem có bất kỳ chữ số nào khác với chữ số đầu tiên hay không, nếu có thì n không phải là số đồng nhất.

# d) Số hoàn thiện: tổng ước không kể chính nó bằng n
so_hoan_thien = lambda n: n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) == n
#range(1, n // 2 + 1) : tạo dãy số từ 1 đến n // 2 + 1 để kiểm tra các ước của n (không cần kiểm tra đến n vì n không phải là ước của chính nó)
#n % i == 0 : kiểm tra xem i có phải là ước của n hay không


# e) Số phong phú:Số phong phú là số có tổng ước (không kể chính nó) lớn hơn bản thân nó (tổng ước không kể chính nó lớn hơn n)
so_phong_phu = lambda n: n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) > n
#ương tự số hoàn thiện, nhưng điều kiện cuối là > n thay vì == n.

 # f) Số tăng dần: chữ số từ trái sang phải không giảm
so_tang_dan = lambda n: all(str(n)[i] <= str(n)[i + 1] for i in range(len(str(n)) - 1))
#range(len(str(n)) - 1) : tạo dãy số từ 0 đến len(str(n)) - 2 để duyệt qua các cặp chữ số liền kề
#str(n)[i] <= str(n)[i + 1] : kiểm tra xem chữ số tại vị trí i có nhỏ hơn hoặc bằng chữ số tại vị trí i + 1 hay không, nếu tất cả các cặp chữ số đều thỏa
#all() : nếu tất cả các cặp chữ số đều thỏa

# g) Số Armstrong
so_armstrong = lambda n: sum(int(ch) ** len(str(n)) for ch in str(n)) == n
#len(str(n)) : đếm số chữ số của n
#int(ch) ** len(str(n)) : nâng từng chữ số lên lũy thừa bằng số chữ số của n



# h) Số nguyên tố
so_nguyen_to = lambda n: n > 1 and not any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1))
#range(2, int(math.sqrt(n)) + 1) : chỉ cần kiểm tra đến √n, vì nếu có ước > √n thì ước còn lại < √n đã được kiểm tra rồ
#any(n%i == 0 for i in range(2, int(math.sqrt(n)) + 1)) : kiểm tra xem n có chia hết cho bất kỳ số nào từ 2 đến √n hay không, nếu có thì n không phải là số nguyên tố.
#not any(...) : nếu không có số nào chia hết cho n, tức là n là số nguyên tố.


# i) Số Palindrome
so_palindrome = lambda n: str(n) == str(n)[::-1]
#Nếu chuỗi gốc == chuỗi đảo ngược → số đọc xuôi bằng đọc ngược → palindrome
#str(n)[::-1] : đảo ngược chuỗi biểu diễn số n

# j) Số nguyên tố Palindrome
so_nguyen_to_palindrome = lambda n: so_nguyen_to(n) and so_palindrome(n)
#Kết hợp hai hàm đã định nghĩa bên trên bằng and.n phải thỏa cả hai điều kiện: vừa là số nguyên tố, vừa là palindrome.

# k) Số lộc phát: chỉ chứa số 6 hoặc 8
so_loc_phat_all = lambda n: all(ch in "68" for ch in str(n))
so_loc_phat_dem = lambda n: str(n).count("6") + str(n).count("8") == len(str(n))
#Cách 1 (all): kiểm tra mọi chữ số đều nằm trong tập {"6", "8"}.
#Cách 2 (count): đếm số lượng chữ số 6 và 8, nếu tổng bằng độ dài của chuỗi thì n chỉ chứa 6 và 8.
#Hai cách cho kết quả giống nhau.

# l) Số lộc phát Palindrome
so_loc_phat_palindrome = lambda n: so_loc_phat_all(n) and so_palindrome(n)
#Kết hợp: phải vừa là số lộc phát (chỉ chứa 6 và 8), vừa là palindrome (đọc xuôi = đọc ngược).

#----------------------------------------
# IN KẾT QUẢ TỪ 1 ĐẾN 1 TRIỆU


print("Nhập một số nguyên dương N (1 <= N <= 1,000,000): ")
N = int(input())
#range(1, N+1) → duyệt từ 1 đến N (bao gồm N).
#[i for i in ... if ...] → list comprehension: tạo danh sách các số thỏa điều kiện.
#Mỗi dòng print dưới đây làm tương tự với hàm kiểm tra tương ứng.

print("a) Số thân thiện:")
print([i for i in range(1, N + 1) if so_than_thien(i)])

print("\nb) Số chính phương:")
print([i for i in range(1, N + 1) if so_chinh_phuong(i)])

print("\nc) Số đồng nhất:")
print([i for i in range(1, N + 1) if so_dong_nhat_tatca(i)])

print("\nd) Số hoàn thiện:")
print([i for i in range(1, N + 1) if so_hoan_thien(i)])

print("\ne) Số phong phú:")
print([i for i in range(1, N + 1) if so_phong_phu(i)])


print("\nf) Số tăng dần:")
print([i for i in range(1, N + 1) if so_tang_dan(i)])

print("\ng) Số Armstrong:")
print([i for i in range(1, N + 1) if so_armstrong(i)])

print("\nh) Số nguyên tố:")
print([i for i in range(1, N + 1) if so_nguyen_to(i)])

print("\ni) Số Palindrome:")
print([i for i in range(1, N + 1) if so_palindrome(i)])

print("\nj) Số nguyên tố Palindrome:")
print([i for i in range(1, N + 1) if so_nguyen_to_palindrome(i)])

print("\nk) Số lộc phát:")
print([i for i in range(1, N + 1) if so_loc_phat_all(i)])

print("\nl) Số lộc phát Palindrome:")
print([i for i in range(1, N + 1) if so_loc_phat_palindrome(i)])

