# from sqlalchemy.orm import Session
# from database import SessionLocal
# from models import Chi_nhanh

# db: Session = SessionLocal()
# chi_nhanhs = [
#     Chi_nhanh(Name="Chi nhánh Hà Nội", Dia_chi="123 Trần Duy Hưng, Hà Nội", Phone="0241234567"),
#     Chi_nhanh(Name="Chi nhánh Hồ Chí Minh", Dia_chi="456 Nguyễn Huệ, Quận 1, HCM", Phone="0289876543"),
#     Chi_nhanh(Name="Chi nhánh Đà Nẵng", Dia_chi="789 Lê Duẩn, Đà Nẵng", Phone="0236123456"),
#     Chi_nhanh(Name="Chi nhánh Hải Phòng", Dia_chi="321 Tô Hiệu, Hải Phòng", Phone="0225123456"),
#     Chi_nhanh(Name="Chi nhánh Cần Thơ", Dia_chi="654 30/4, Ninh Kiều, Cần Thơ", Phone="0292387654"),
#     Chi_nhanh(Name="Chi nhánh Nha Trang", Dia_chi="987 Trần Phú, Nha Trang", Phone="0258384756"),
#     Chi_nhanh(Name="Chi nhánh Huế", Dia_chi="159 Hùng Vương, TP. Huế", Phone="0234389123"),
#     Chi_nhanh(Name="Chi nhánh Biên Hòa", Dia_chi="753 Đồng Khởi, Biên Hòa", Phone="0251892345"),
#     Chi_nhanh(Name="Chi nhánh Vũng Tàu", Dia_chi="852 Trần Hưng Đạo, Vũng Tàu", Phone="0254356678"),
#     Chi_nhanh(Name="Chi nhánh Buôn Ma Thuột", Dia_chi="951 Lê Duẩn, TP. Buôn Ma Thuột", Phone="0262354789")
# ]
# try:
#     for chi_nhanh in chi_nhanhs:
#         db.add(chi_nhanh)  # Thêm từng chi nhánh vào session
#     db.commit()  # Lưu thay đổi vào cơ sở dữ liệu
#     print("✅ Dữ liệu chi nhánh đã được thêm thành công!")
# except Exception as e:
#     db.rollback()  # Hoàn tác nếu có lỗi
#     print(f"❌ Lỗi khi thêm dữ liệu: {e}")
# finally:
#     db.close()  # Đóng kết nối