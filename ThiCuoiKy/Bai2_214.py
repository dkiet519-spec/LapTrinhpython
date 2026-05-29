#kiểm tra đây có phải là số nguyên tố hay không
def songuyento(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("nhập số nguyên dương n");
n =int(input());


if songuyento(n):
    print("là số nguyên tố")
else:
    print("không phải số nguyên tố")

#liệt kê ước số là số nguyên tố hay không
uocsolasonguyento = []
for i in range(2, n + 1):
    if n % i == 0 and songuyento(i):
        uocsolasonguyento.append(i)

print("Ước số của n là số nguyên tố:", uocsolasonguyento)