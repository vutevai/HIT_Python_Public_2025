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
