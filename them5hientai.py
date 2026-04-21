from datetime import datetime, timedelta
#datetime.timedelta để thêm 5 giây vào thời gian hiện tại
t1 = datetime.now()
t2 = timedelta( seconds = 5)
t3 = t1 + t2
print("Thời gian hiện tại là:", t1)
print("Thời gian sau khi thêm 5 giây là:", t3)

