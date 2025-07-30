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
