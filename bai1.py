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
