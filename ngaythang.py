from datetime import datetime #, timedelta
homnay = datetime.now()
print ("năm :", homnay.year)
print ("tháng hiện tại bằng chữ :", homnay.strftime("%B"))  
print ("tuần hiện tại là tuần thứ mấy trong năm :", homnay.strftime("%W")) 
print ("tuần hiên tại là tuần thứ mấy trong tháng :", homnay.strftime("%U"))
print ("ngày hiện tại là ngày thứ mấy trong năm :", homnay.strftime("%j"))
print ("ngày dương lịch hiện tại là ngày :", homnay.strftime("%d"))
print ("thứ của ngày hiện tại :", homnay.strftime("%A"))
print ("Giờ Phút Giây hiện tại :", homnay.strftime("%H:%M:%S"))

Day1= input("nhap ngay 1 (dd/mm/yyyy):")
D1 = datetime.strptime(Day1, "%d/%m/%Y")
Day2= input("nhap ngay 2 (dd/mm/yyyy):")
D2 = datetime.strptime(Day2, "%d/%m/%Y")
 
so_ngay_giua_hai_ngay = abs((D2 - D1).days)
#trị tuyệt đối abs(), .days để lấy khoản số của hai ngày để thành số nguyên, nếu không có .days thì sẽ trả về số ngày kèm theo giờ phút giây
print("Số ngày giữa hai ngày là:", so_ngay_giua_hai_ngay)

#chuyển ngày tháng năm và thời gian chuẩn 
s="Sep 18 2019 2:43PM"
DT = datetime.strptime(s, "%b %d %Y %I:%M%p")
print("Ngày tháng năm và thời gian chuẩn là:", DT)

# #datetime.timedelta để thêm 5 giây vào thời gian hiện tại
# t1 = datetime.now()
# t2 = timedelta( seconds = 5)
# t3 = t1 + t2
# print("Thời gian hiện tại là:", t1)
# print("Thời gian sau khi thêm 5 giây là:", t3)



