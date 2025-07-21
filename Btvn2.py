n = int(input("Nhập vào số xu : "))
chai = n//28 # nhiệm vụ của bạn là xác định với N xu cho trước,
vo = chai
while vo >= 3 :    
    doi = vo //3
    chai += doi
    vo = vo%3 + doi 
print ("Số chai bia mua được không tính đổi vỏ là là: ",chai)