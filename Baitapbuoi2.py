# x = int(input("Nhập năm: "))
# y = int(input("Nhập tháng: "))


# if y in [1,3,5,7,8,10,12]:
#     print("Tháng có 31 ngày")

# elif y in [4,6,9,11]:
#     print("Tháng có 30 ngày")

# elif y == 2:
#     if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
#         print("Tháng có 29 ngày")
#     else:
#         print("Tháng có 28 ngày")
# else:
#     print("Tháng không hợp lệ")

# bai2
# x = int(input("Nhap vao so lương : "))
# if x == 15e6 :
#     thue = x * 30/100
#     print (" Thuế thu là: ", thue )
# elif x >=7e6 and x <= 15e6 :
#     thue = x * 20/100
#     print (" Thuế thu là: ", thue )
# else :
#     thue = x * 10/100
#     print (" Thuế thu là: ", thue )
# if x== 15e6:
#     print (" Lương thật của người đó là :", x-thue)
# elif x >=7e6 and x <= 15e6 :
#      print (" Lương thật của người đó là :", x-thue)
# else :
#      print (" Lương thật của người đó là :", x-thue)
#bai3
# n = int(input("Nhập n: "))
# dem = 0       
# tong = 0    
# tam = n      

# while tam > 0:
#     chu_so = tam % 10  
#     cs = tam % 10
#     print (cs)  
#     tong += chu_so       
#     dem += 1             
#     tam = tam // 10   
# print("Số lượng chữ số của", n, "là:", dem)
# print("Tổng các chữ số của", n, "là:", tong)
# bai4

# n = int(input("Nhập vào số xu : "))
# chai = n//28 # nhiệm vụ của bạn là xác định với N xu cho trước,
# vo = chai
# while vo >= 3 :    
#     doi = vo //3
#     chai += doi
#     vo = vo%3 + doi 
# print ("Số chai bia mua được không tính đổi vỏ là là: ",chai)