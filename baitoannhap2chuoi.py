from collections import Counter
chuoi1 = input("Nhập chuỗi thứ nhất: ")
chuoi2 = input("Nhập chuỗi thứ hai: ")

demchuoi1 = Counter(chuoi1)#dem số lần xuất hiện của mỗi ký tự trong chuỗi 1
demchuoi2 = Counter(chuoi2)

# câu a in ra số lượng có các ký tự chung
diemchung = demchuoi1 & demchuoi2#tìm các ký tự chung giữa hai chuỗi
print("Các ký tự chung giữa hai chuỗi:", diemchung)
#1
#diemchung  nó sẽ từ dãy đã đặt điểm chung đó và lấy trực tiếp ở phần đếm chuổi 1 2
#Counter({'ký tự ': số_lần_xuất_hiện}) vd Counter({'l': 1, 'o': 1})
#2
#diemchung.keys() nó sẽ trả về các ký tự chung giữa hai chuỗi vd dict_keys(['l', 'o'])
#3
#set(diemchung.keys()) nó sẽ trả về một tập hợp các ký tự chung giữa hai chuỗi vd {'l', 'o'}--khác biệt là ko có dict_keys  

#câu b in ra các ký tự chỉ xuất hiện ở 1 chuổi (in ra số)
chico1 = set(demchuoi1.keys()) - set(diemchung.keys())#tìm các ký tự chỉ xuất hiện trong chuỗi 1
chico2 = set(demchuoi2.keys()) - set(diemchung.keys())#tìm các ký tự chỉ xuất hiện trong chuỗi 2
print("Các ký tự chỉ xuất hiện trong chuỗi thứ nhất:", len(chico1))
print("Các ký tự chỉ xuất hiện trong chuỗi thứ hai:", len(chico2))

#câu c in ra các ký tự chỉ xuất hiện ở 1 chuổi (in ra chữ)
print ("Các ký tự chỉ xuất hiện trong chuỗi thứ nhất:", set(chico1.keys()))
print ("Các ký tự chỉ xuất hiện trong chuỗi thứ hai:", set(chico2.keys()))