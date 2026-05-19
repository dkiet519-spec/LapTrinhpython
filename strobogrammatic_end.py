def la_so_strobogrammatic(n):
    # if n == 0:
    #     return True
    # if n == 1:
    #     return n in strobogrammatic
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
strobogrammatic = {"0": "0", "1": "1", "2": "2","5": "5", "6": "9", "8": "8", "9": "6"}
#điều kiện để in ra các số strobogrammatic nhỏ hơn 1000000
def so_nguyen_to_strobogrammatic(n):
   if la_so_strobogrammatic(n):
       if n < 2:
           return False
       for i in range(2, int(n**0.5) + 1):
           if n % i == 0:
               return False
       return True
   
def dao_180(n):   
    chuoi_n = str(n)
    dao_chuoi = ""
    for i in range(len(chuoi_n)-1, -1, -1):
        if chuoi_n[i] in strobogrammatic:
            dao_chuoi += strobogrammatic[chuoi_n[i]]
        else:
            return None
    return dao_chuoi
     
for i in range(1000000):
    if la_so_strobogrammatic(i):
       continue
    if so_nguyen_to_strobogrammatic(i):
        continue
    dao_so= dao_180(i)
    if dao_so is not None and so_nguyen_to_strobogrammatic(int(dao_so)):
        print(f"\n{i}") 
        
   
   