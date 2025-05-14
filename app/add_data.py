

import os 
from sqlalchemy import create_engine, text
from database import SessionLocal, engine

data_folder = "data"

for filename in os.listdir(data_folder):
    if filename.endswith(".py"):
        file_path = os.path.join(data_folder, filename)
        print(f"Đang thực thi {filename}...")
        with open(file_path, "r") as file:
            sql_script = file.read()
    else:
        print(f"Skipped {filename}")
        
    try:
        with engine.connect() as connection:
            connection.execute(text(sql_script))
            print(f"✅ Đã thực thi {filename} thành công.")
        print(f"✅ Đã thực thi {filename} thành công.")
    except Exception as e:
        print(f"❌ Lỗi khi thực thi {filename}: {e}")