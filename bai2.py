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
