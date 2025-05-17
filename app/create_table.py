from database import engine
from models import Base
import models  # Import này quan trọng để đảm bảo tất cả models được load

def init_db():
    try:
        # Xóa tất cả bảng cũ
        Base.metadata.drop_all(bind=engine)
        print("✅ Đã xóa bảng cũ thành công!")
        
        # Tạo lại bảng mới
        Base.metadata.create_all(bind=engine)
        print("✅ Đã tạo bảng mới thành công!")
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")

if __name__ == "__main__":
    init_db() 