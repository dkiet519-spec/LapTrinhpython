# sdt = input("Nhập chuỗi số điện thoại: ")

# cacsobithiueu = []

# for i in range(10):
#      if str(i) not in sdt:
#         cacsobithiueu.append(str(i))
# print("số điện thoại đã nhập:", sdt)
# print("Các số bị thiếu trong chuỗi số điện thoại:", cacsobithiueu)
 
daykitu = input("nhâp chuỗi ký tự: ")

cackytu = daykitu.split() #tách chuỗi thành các ký tự riêng biệt và lưu vào một danh sách
ketqua = None

cactudagap = []#các từ bị lặp lại

for cactu in cackytu:    
    if cactu in cactudagap: #nếu từ đã xuất hiện trong danh sách các từ bị lặp lại thì bỏ qua
      ketqua = cactu
      break
    cactudagap.append(cactu) #nếu từ chưa xuất hiện trong danh sách các từ bị lặp lại thì thêm vào danh sách
print("Chuỗi ký tự đã nhập:", ketqua)