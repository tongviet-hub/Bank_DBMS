import os
import psycopg2

# ✅ Lấy đường dẫn tuyệt đối đến thư mục chứa file Python hiện tại
base_dir = os.path.dirname(os.path.abspath(__file__))
sql_folder = os.path.join(base_dir, "data")  # 👉 Đảm bảo đúng thư mục chứa file .sql

# Kết nối đến PostgreSQL
conn = psycopg2.connect(
    dbname='Bank',         # 🔁 Đổi thành tên database của bạn
    user='postgres',       # 🔁 Username
    password='hntd1cd@',   # 🔁 Password
    host='localhost',      # 🔁 Địa chỉ host
    port='5432'            # 🔁 Port mặc định
)
cursor = conn.cursor()

# Danh sách file SQL, sắp xếp theo tên để đảm bảo thứ tự chạy
sql_files = sorted([f for f in os.listdir(sql_folder) if f.endswith(".sql")])

for file_name in sql_files:
    file_path = os.path.join(sql_folder, file_name)
    print(f"🔄 Đang chạy file: {file_name}")

    with open(file_path, 'r', encoding='utf-8') as file:
        sql_script = file.read()
        try:
            cursor.execute(sql_script)
            conn.commit()
            print(f"✅ Đã chạy xong: {file_name}")
        except Exception as e:
            print(f"❌ Lỗi khi chạy {file_name}: {e}")
            conn.rollback()

# Đóng kết nối
cursor.close()
conn.close()
print("🏁 Đã hoàn tất chạy tất cả file SQL!")
