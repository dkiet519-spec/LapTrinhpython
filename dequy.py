# def tongcacchuso(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + tongcacchuso(n // 10) #n = 123 = 3 + tongcacchuso(12) = 3 + 2 + tongcacchuso(1) = 3 + 2 + 1 + tongcacchuso(0) = 3 + 2 + 1 + 0 = 6
# n = int(input("Nhập một số nguyên: "))
# print("Tổng các chữ số của", n, "là:", tongcacchuso(n))

# def  tinhgiaithua(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * tinhgiaithua(n - 1) #n! = n × (n-1)!
# n = int(input("Nhập một số nguyên dương: "))
# print("Giai thừa của", n, "là:", tinhgiaithua(n))

# def tinhmu(n,x):
#     if n == 0:
#         return 1
#     else:
#         return x * tinhmu(n - 1,x) #x^n = x × x^(n-1) 
#     #luy_thua(2,3)
# # = 2 * luy_thua(2,2)
# # = 2 * (2 * luy_thua(2,1))
# # = 2 * 2 * (2 * luy_thua(2,0))
# # = 2 * 2 * 2 * 1
# # = 8
# n = int(input("Nhập số mũ n: "))
# x = int(input("Nhập cơ số x: "))
# print(x, "lũy thừa", n, "là:", tinhmu(n,x))

def uocso(a,b):
    if b == 0:
        
        return a
    else:
        return uocso(b, a % b)
a = 12
b = 8
print("Ước số chung của", a, "và", b, "là:", uocso(a, b))