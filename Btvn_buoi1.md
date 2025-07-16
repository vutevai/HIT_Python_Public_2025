Bai1:
Python là ngôn ngữ thông dịch, không phải ngôn ngữ biên dịch:
Khi chạy chương trình Python, máy tính đọc và thực hiện từng dòng lệnh một, chứ không dịch toàn bộ chương trình thành ngôn ngữ máy trước như C hoặc C++.
Python dùng một trình thông dịch để chạy chương trình, giống như người phiên dịch đọc từng câu rồi dịch luôn, không dịch sẵn cả bài.

Bai 2:
Các kiểu dữ liệu trong python:
kiểu dữ liệu	mô tả	        ví dụ
int	            số nguyên	   -5,10,0
float	        số thực	         3.14
str	            chuỗi kí tự	    "hello"
bool	        đúng/sai	   true,false
list	        danh sách      [1,2,3]
tuple	        bộ giá trị cố định	(1,2)
dict	       key-value	{"name":"Vũ","age":"19"}
set	            tập hợp	    {1,2,3}

Các Toán tử trong Python:hihihhihih
Toán tử số học
toán tử	ý nghĩa	ví dụ
+	cộng	a+b=2
-	trừ	a-b=1
*	nhân	a*b=10
/	chia	a/b=2.5
//	chia lấy nguyên	a//b=2
%	chia lấy dư	a%b=0
**	lũy thừa	a**b=25
Toán tử so sánh:>,<,>=,<=,!=,==
Toán tử logic: and,or,not
Mệnh đề điều kiện và vòng lặp:

Mệnh đề điều kiện(if,else if,else)
x = 10
if x > 0:
print("Số dương")
elif x == 0:
print("Số không")
else:
print("Số âm")
Vòng lặp:
For(lặp qua danh sách)
for i in [1, 2, 3]:
print(i)
While(lặp đến khi điều kiện sai)
i = 1
while i <= 3:
print(i)
i += 1
Kiểu dữ liệu True và False:

True và False là hai giá trị của kiểu dữ liệu boolean (bool).
Dùng để kiểm tra điều kiện trong if, while, v.v.
vd
a = 5
b = 10
print(a < b)  # Kết quả: True