from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError  # Import lỗi chuyên trị cho SQLAlchemy

# Thông tin kết nối
database_url = "postgresql://postgres:hntd1cd%40@localhost:5432/Quizzapplication"

# Tạo engine kết nối
engine = create_engine(database_url)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        db_version = result.fetchone()
        print(f"✅ Connected to: {db_version[0]}")
except SQLAlchemyError as e:
    print("❌ False")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
