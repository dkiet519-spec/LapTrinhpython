def show(a) :
    a = int(input("nhap so: "))
    inra=a
    show(inra)
    
def cong(b) :
    return b +15
b = int(input("nhap so: "))
print (cong(b))    