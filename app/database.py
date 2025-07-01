from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError  # Bắt lỗi

# 🔐 Kết nối đến PostgreSQL
database_url = "postgresql://postgres:hntd1cd%40@localhost:5432/Bank"

# 🛠️ Tạo engine
engine = create_engine(database_url)

# 🔍 Kiểm tra kết nối (tuỳ chọn, có thể bỏ nếu không cần debug)
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        db_version = result.fetchone()
        print(f"✅ Connected to: {db_version[0]}")
except SQLAlchemyError as e:
    print("❌ Kết nối thất bại:", str(e))

# ⚙️ Tạo session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 📦 Base dùng để khai báo model
Base = declarative_base()
