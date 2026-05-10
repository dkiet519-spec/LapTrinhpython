try:
    a=open("D:\\python\\LapTrinhpython\\Thuyền và biển.txt","r", encoding="utf-8")
    result=a.read()
    print(result)
    print("\nĐọc file thành công")
finally:
    a.close()
    