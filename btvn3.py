bài1
# Nhập số lượng phần tử
N = int(input("Nhập số lượng phần tử N: "))

# Nhập list N phần tử
lst = []
for i in range(N):
    num = int(input(f"Nhập phần tử thứ {i + 1}: "))
    lst.append(num)

# Nhập số X và đếm số lần xuất hiện
X = int(input("Nhập số X: "))
count_X = lst.count(X)
print(f"Số {X} xuất hiện {count_X} lần trong list.")

# Thay thế phần tử từ vị trí 2 -> 7 (tức index 1 -> 6)
if len(lst) >= 7:
    lst[1:7] = [8, 5, 4, 0, 1, 3]
else:
    print("List không đủ 7 phần tử để thay thế.")
print("List sau khi thay thế:", lst)

# Tìm số lớn nhất và nhỏ nhất
max_val = max(lst)
min_val = min(lst)
print(f"Số lớn nhất trong list là: {max_val}")
print(f"Số nhỏ nhất trong list là: {min_val}")

# Nhập số Y và chèn vào đầu list
Y = int(input("Nhập số Y: "))
lst.insert(0, Y)
print("List sau khi chèn Y vào đầu:", lst)

# Kiểm tra thứ tự sắp xếp
if lst == sorted(lst):
    print("TĂNG")
elif lst == sorted(lst, reverse=True):
    print("GIẢM")
else:
    print("NO")




Bài2
# Nhập số phần tử k
k = int(input("Nhập số phần tử của list a (k): "))

# Nhập list a gồm k phần tử
a = []
for i in range(k):
    x = int(input(f"Nhập phần tử thứ {i + 1}: "))
    a.append(x)

# Nhập số dòng và số cột của ma trận
n = int(input("Nhập số dòng n của ma trận: "))
m = int(input("Nhập số cột m của ma trận: "))

# Kiểm tra có đủ phần tử để tạo ma trận không
if n * m > k:
    print("NO")
else:
    X = []  # ma trận kết quả
    index = 0
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[index])
            index += 1
        X.append(row)

    # In ma trận
    print("Ma trận X là:")
    for row in X:
        print(row)



bài3
# Nhập 2 chuỗi s1, s2
s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")

# In ra chuỗi s1 đảo ngược
print("Chuỗi s1 đảo ngược:", s1[::-1])

# Nhập 2 số nguyên a, b
a = int(input("Nhập a (1 <= a < b <= len(s2)): "))
b = int(input("Nhập b: "))

# Kiểm tra điều kiện
if 1 <= a < b <= len(s2):
    # Đảo ngược đoạn từ s2[a-1] đến s2[b-1] (do index bắt đầu từ 0)
    s2_modified = s2[:a-1] + s2[a-1:b][::-1] + s2[b:]
    print("Chuỗi s2 sau khi đảo đoạn từ vị trí a đến b:", s2_modified)
else:
    print("Giá trị a, b không hợp lệ!")

# Tạo chuỗi s3 là s1 sau khi xóa các kí tự ở vị trí chẵn (tính từ 0)
s3 = ''.join(s1[i] for i in range(len(s1)) if i % 2 != 0)
print("Chuỗi s1 sau khi xóa các kí tự ở vị trí chẵn (s3):", s3)

# Tạo chuỗi s4 là đan xen các ký tự của s1 và s2
s4 = ''
min_len = min(len(s1), len(s2))
for i in range(min_len):
    s4 += s1[i] + s2[i]
# Nối phần dư nếu s1 hoặc s2 dài hơn
s4 += s1[min_len:] + s2[min_len:]
print("Chuỗi s4 (đan xen):", s4)



bài4
# Nhập chuỗi họ tên từ bàn phím
name = input("Nhập họ tên: ")

# Xóa khoảng trắng thừa và tách thành các từ
parts = name.strip().lower().split()

# Viết hoa chữ cái đầu mỗi từ
normalized_parts = [word.capitalize() for word in parts]

# Nối lại thành chuỗi họ tên hoàn chỉnh
normalized_name = ' '.join(normalized_parts)

# In kết quả
print("Họ tên sau khi chuẩn hóa:", normalized_name)
