
# def cong(b) :
#     return b +15

# b = int(input("nhap so: "))
# print (cong(b))    

# def show(a):
#     return a 
# a = input("nhap chuoi: ")
# print(show(a))

def nhan(x,y):
    return x * y
x = int(input("nhap so x: "))
y = int(input("nhap so y: "))
print(nhan(x,y))
   
   
   # f) Số tăng dần: chữ số từ trái sang phải không giảm
so_tang_dan = lambda n: all(str(n)[i] <= str(n)[i + 1] for i in range(len(str(n)) - 1))

# g) Số Armstrong
so_armstrong = lambda n: sum(int(ch) ** len(str(n)) for ch in str(n)) == n

# h) Số nguyên tố
so_nguyen_to = lambda n: n > 1 and not any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1))

# i) Số Palindrome
so_palindrome = lambda n: str(n) == str(n)[::-1]

# j) Số nguyên tố Palindrome
so_nguyen_to_palindrome = lambda n: so_nguyen_to(n) and so_palindrome(n)

# k) Số lộc phát: chỉ chứa số 6 hoặc 8
so_loc_phat_all = lambda n: all(ch in "68" for ch in str(n))
so_loc_phat_dem = lambda n: str(n).count("6") + str(n).count("8") == len(str(n))

# l) Số lộc phát Palindrome
so_loc_phat_palindrome = lambda n: so_loc_phat_all(n) and so_palindrome(n)


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