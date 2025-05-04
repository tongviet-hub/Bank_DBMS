from sqlalchemy.orm import Session
from models import Khach_hang,Thao_tac
from schemas import KhachHangCreate,ThaoTacCreate
from fastapi import HTTPException
from datetime import datetime

# def create_khach_hang(db: Session, khach_hang: KhachHangCreate):
#     try:
#         # Chuyển đổi dữ liệu từ schema
#         khach_hang_data = khach_hang.dict()

#         # Kiểm tra và chuyển đổi ngày sinh nếu cần
#         if isinstance(khach_hang_data.get("ngay_sinh"), str):
#             try:
#                 khach_hang_data["ngay_sinh"] = datetime.strptime(khach_hang_data["ngay_sinh"], "%Y-%m-%d").date()
#             except ValueError:
#                 raise HTTPException(status_code=400, detail="Ngày sinh không đúng định dạng (YYYY-MM-DD)")

#         # Tạo đối tượng Khach_hang
#         db_khach_hang = Khach_hang(**khach_hang_data)
#         db.add(db_khach_hang)
#         db.commit()
#         db.refresh(db_khach_hang)
#         return db_khach_hang

#     except Exception as e:
#         db.rollback()  # Rollback nếu có lỗi
#         print("💥 Lỗi khi thêm khách hàng vào database:", e)
#         raise HTTPException(status_code=500, detail=f"Lỗi server: {str(e)}")

def create_thao_tac(db: Session, thao_tac: ThaoTacCreate):
    db_thao_tac = Thao_tac(Ten_thao_tac=thao_tac.Ten_thao_tac)
    db.add(db_thao_tac)
    db.commit()
    db.refresh(db_thao_tac)
    return db_thao_tac

def create_khach_hang(db: Session, khach_hang: KhachHangCreate):
    db_khach_hang = Khach_hang(**khach_hang.dict())
    db.add(db_khach_hang)
    db.commit()
    db.refresh(db_khach_hang)
    return db_khach_hang

def get_khach_hang(db: Session, khach_hang_id: int):
    db_khach_hang = db.query(Khach_hang).filter(Khach_hang.id == khach_hang_id).first()
    if db_khach_hang is None:
        raise HTTPException(status_code=404, detail="Khách hàng không tồn tại")
    return db_khach_hang

def delete_thao_tac(db: Session, thao_tac_id: int):
    db_thao_tac = db.query(Thao_tac).filter(Thao_tac.id == thao_tac_id).first()
    if db_thao_tac is None:
        raise HTTPException(status_code=404, detail="Thao tác không tồn tại")
    db.delete(db_thao_tac)
    db.commit()
    return {"message": "Thao tác đã được xóa thành công"}